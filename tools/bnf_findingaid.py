#!/usr/bin/env python3
"""Fetch a BnF manuscript volume's finding aid (archivesetmanuscrits.bnf.fr) and list its items as TSV.

One row per catalogued item: folio, item number, cipher flag ("chiffre" in the item text), decipherment flag
("déchiffr"), and the item text.  Built for the BNF-FOCUS lane (7 Oct 2026, BNF-VALUE.md part 2): comparing the
catalogue's own "avec chiffre" marks against the leaves this project has read finds cipher letters the record
does not flag (BnF fr.3251 no.11 f.21, no.14 f.27) and leaves whose decipherment the record does not mention.

Route (plain curl, no browser, descriptive UA, 2 s between requests -- CLAUDE.md access playbook):
  1. POST resultatRechercheSimple.html with TEXTE_LIBRE_INPUT="<cote>" (the search is fuzzy: it matches any
     record containing the number), then keep only the result whose title starts "<cote> ." exactly;
  2. GET https://archivesetmanuscrits.bnf.fr/ark:/12148/<ark> (the whole dépouillement is in page 1's HTML).

Scope (Usage 8a):
  catches  a volume whose notice lists items as "Fol. N • no. Lettre ..." (Français, Clairambault, Dupuy,
           Mélanges de Colbert, Espagnol, ...): every item, flagged or not;
  does NOT a volume catalogued only at volume level (no "Fol." lines): it prints 0 items and says so, never
  catch    "no cipher" -- an absent item list is not a negative.

--pile (MQS-BNFPILE, 9 Oct 2026; offline, scores saved notices, one row per volume):
  catches  an unread pile: cipher items catalogued with no name, date or place ("Pièce en chiffre."), the way the
           57 Mary Stuart letters sat in fr.2988 (Lasry, Biermann, Tomokiyo 2023, Cryptologia 47/2 pp.101-109);
           counts key sheets apart, drops deciphered items, takes volume-level prior work from the notice's own
           Présentation / Bibliographie, flags the clear-neighbour trap (M41), digitised yes/no/unknown (M42), and
           asks tools/prior_work.py check 3 (cached Tomokiyo, DECODE listing, solver caches) per cipher item.
  does NOT rank a volume whose cipher items are all named/dated/deciphered (fr.4715: 40 of 44 deciphered), count
           a key sheet ("Table de chiffrement", "Clef d'un chiffre") as a bare item, or call a volume-level notice
           with no item list a negative: it is class image-triage.
  est_signs = n_bare x median folio gap x 650: calibrated on ONE point, fr.2988 itself (26 x 4 x 650 = 67,600 vs the
           paper's ~68,000), the development volume; it is an estimate, not a measurement.
  Per-item exclusion goes through prior_work.py (check_portals), not a second path; --prior FILE (TSV: shelfmark,
  folio, status, source) is only an override for statuses no cache holds.  Known gap in prior_work check 3 seen on
  9 Oct 2026: its classifier reads the Tomokiyo line "f.2 and f.9 ... not deciphered yet" as KNOWN and f.1 "broken by
  Torbjorn Andersson" as CONTEXT; --pile applies a stated wording guard on top (negation words void a KNOWN,
  "broken/deciphered/solved by" makes a CONTEXT KNOWN), see item_status().
  --permute N (with --pile; MQS-BNF-S2A, 9 Oct 2026): across-volume permutation null for the pile statistic. Pools
           every item of the given notices, permutes item texts across volumes N times (per-volume item counts kept,
           seed 20261009) and reports the real max `bare` in one volume beside the null's p50/p95/max.
  catches  a pile that is a real concentration in one volume (fr.2988: 26 vs a null p95 of a few);
  does NOT pass a set whose bare items are spread thin across volumes (test: an even spread ties its own null), and a
           within-volume order shuffle is not offered (it cannot change `bare`: rule 3, a control that cannot vary).
  --prior-work (with --pile; MQS-BNF-S3, 9 Oct 2026; disk only): two per-item checks --pile did not call.
  (1) own work across the repository: top-level *.md and items.tsv of every ciphers/<slug>/ folder and ciphers/_triage/*.md,
      matched with tools/shelfmark.py match() == 'exact' (folio bound to the volume, never the folio alone; a line naming
      no volume counts only inside a folder whose slug carries the volume, never in _triage). Skipped: RESTRICTED.md
      folders, any 'restricted' path, ciphers/debosnys-1883. A hit marks the item ours (columns ours_items, ours_slugs)
      and takes it out of open_bare/open_named, as a KNOWN does. A range notice (fr.3974-3995: items carry no volume) gets
      ours? in ours_range and keeps its open counts.
  (2) prior_work.py check 3a (active edition, MQS-SCOUT): a LEAD on any item sets contact_first; counts and class unchanged.
  catches  a pile item a folder of ours already names (fr.2988 f.1: ciphers/_triage/bnf-fr2988-f1-fr20506-f146.md);
           fr.2988 contact_first (the Mary Stuart - Castelnau edition).
  does NOT mark fr.29880 f.18, fr.3040 f.19, fr.3041 f.18 against a line 'BnF fr.3040 f.18r', or read a RESTRICTED.md
           folder or debosnys-1883 (tools/tests/test_bnf_findingaid_prior.py). Not a DONE: prior_work.py check 1 stays per-slug.
           Controls (PREREG-MQS-BNF-S3.md): K1 volume recall, N1 folio shift +37, N2 volume swap; shelf grade on its row.
  --census PHRASE ... --out DIR: one quoted POST per phrase, total + facets + first-page ids (never pages further).
  --local-search IR TERM and --branch-pdf ARK: routes read from /js/pagePresentationIr.js (status in --help).

Usage:
  python3 tools/bnf_findingaid.py --pile NOTICE.html [...] [--prior FILE] [--tsv OUT]
  python3 tools/bnf_findingaid.py --census "pièce en chiffre" "dépêches chiffrées" --out DIR
  python3 tools/bnf_findingaid.py --cote "Français 3251" --save-html DIR      # search + fetch + TSV to stdout
  python3 tools/bnf_findingaid.py --ark cc49712p --save-html DIR             # skip the search
  python3 tools/bnf_findingaid.py --html saved.html                          # offline parse only
"""
import argparse, html as H, os, re, subprocess, sys, time, urllib.parse

BASE = 'https://archivesetmanuscrits.bnf.fr/'
UA = 'cipher-lab research script (contact via repository)'


def curl(args):
    r = subprocess.run(['curl', '-sS', '-A', UA, '--max-time', '60'] + args, capture_output=True)
    if r.returncode:
        sys.exit('curl failed: %s' % r.stderr.decode(errors='ignore')[:200])
    return r.stdout.decode('utf-8', errors='ignore')


def _match(s, cote):
    for m in re.finditer(r'href="[^"]*ark:/12148/(cc[0-9a-z]+)(?:/[a-z0-9]+)?"[^>]*>(.*?)</a>', s, re.S):
        t = H.unescape(' '.join(re.sub(r'<[^>]+>', '', m.group(2)).split()))
        if t.startswith(cote + ' .') or t.startswith(cote + '.'):
            return m.group(1), t
    return None, None


def find_ark(cote):
    """POST the simple search (keeping the session cookie); if the exact title is not on the default first page of
    20, ask the same result list again at 100 per page (BNF-FOCUS, 8 Oct 2026: fr.3413, 3635-3641, 4687-4712 were
    missed on page 1)."""
    import tempfile
    jar = tempfile.NamedTemporaryFile(prefix='bnfjar', delete=False).name
    try:
        s = curl(['-c', jar, '-b', jar, '-X', 'POST', '--data-urlencode', 'TEXTE_LIBRE_INPUT=' + cote,
                  '-d', 'DOC_NUMERISE_INPUT_RADIO=all_docs&NUMERO_DEPARTEMENT_INPUT=', BASE + 'resultatRechercheSimple.html'])
        ark, t = _match(s, cote)
        if ark:
            return ark, t
        time.sleep(2)
        s = curl(['-c', jar, '-b', jar, BASE + 'resultatRechercheSimple.html?pageEnCours=1&nbResultParPage=100'])
        return _match(s, cote)
    finally:
        os.unlink(jar)


def to_text(s):
    s = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', s)
    s = re.sub(r'(?i)<br\s*/?>|</(p|div|li|tr|h\d)>', '\n', s)
    s = H.unescape(re.sub(r'<[^>]+>', ' ', s))
    return [' '.join(l.split()) for l in s.split('\n') if l.strip()]


ITEM = re.compile(r'^(?:Fol\.\s*([0-9]+[rv]?(?:\s*-\s*[0-9]+[rv]?)?)\s*•\s*)?([0-9]+[a-z]?(?:\s*-\s*[0-9]+)?)\s+(\S.*)$')


def parse(s):
    rows, title = [], ''
    for line in to_text(s):
        if not title and re.match(r'^[A-ZÉ][\w\-éè\. ]+ [0-9]+.* • ', line):
            title = line
        m = ITEM.match(line)
        if not m or not m.group(1) and not line.startswith(m.group(2) + ' '):
            continue
        txt = m.group(3)
        if not re.search(r'(?i)lettre|pi[eè]ce|chiffr|copie|m[ée]moire|instruction|d[ée]p[eê]che|avis|minute', txt):
            continue
        rows.append(dict(folio=m.group(1) or '', no=m.group(2), chiffre='yes' if re.search(r'(?i)chiffr', txt) else '',
                         dechiffre='yes' if re.search(r'(?i)d[ée]s?chiffr', txt) else '', text=txt))
    # the notice prints the item list twice (dépouillement with folios, then an index without): keep the first
    seen, out = set(), []
    for r in rows:
        k = (r['no'], r['text'])
        if k not in seen:
            seen.add(k)
            out.append(r)
    return title, out

# ---------------------------------------------------------------------------------------------------------------
# --pile: score a saved notice for an unread cipher pile (MQS-BNFPILE, 9 Oct 2026).  Scope in the module docstring.
# ---------------------------------------------------------------------------------------------------------------
CIPHER = re.compile(r'(?i)\b(chiffr|cifra|cifre|ziffer)')
DECIPH = re.compile(r'(?i)d[ée]s?chiffr')
KEYSHEET = re.compile(r'(?i)\b(table|cl[ée]f|clef|alphabet)\b|chiffre pr[ée]c[ée]dent')
NAME = re.compile(r'[A-ZÉÈ]{4,}|«')
MONTHS = (r'janvier|f[ée]vrier|mars|avril|mai|juin|juillet|ao[uû]t|septembre|octobre|novembre|d[ée]cembre|'
          r'gennaio|febbraio|marzo|aprile|maggio|giugno|luglio|agosto|settembre|ottobre|dicembre|'
          r'enero|febrero|abril|mayo|junio|julio|septiembre|octubre|noviembre|diciembre|decembre|jung')
DATE = re.compile(r'1[4-8]\d\d|M\.\s?D|V\.\s?C|\b(?:%s)\b' % MONTHS, re.I)
FORMULA = {'pièce', 'pièces', 'lettre', 'lettres', 'chiffre', 'chiffres', 'copie', 'minute', 'mémoire', 'dépêche',
           'billet', 'instruction', 'avis', 'double', 'fragment', 'en', 'et', 'de', 'la', 'le', 'des', 'du'}
LANG = re.compile(r'(?i)\ben (italien|espagnol|latin|anglais|allemand|flamand|portugais|n[ée]erlandais)\b')
STOP_HEAD = {'Bibliographie', 'Présentation du contenu', "Présentation de l'IR", 'Versions numérisées :'}
PRIOR_VOL = re.compile(r'(?i)lasry|tomokiyo|bourdeau|desenclos|DECODE|d[ée]s?chiffr|lettres chiffr[ée]es de')
NEGATION = re.compile(r'(?i)not (yet )?deciphered|undeciphered|unsolved|unread|not been deciphered|pas (encore )?d[ée]chiffr')
POSITIVE = re.compile(r'(?i)\b(was broken by|broken by|deciphered by|decipherment by|solved by|was deciphered)\b')
GAP_CONST = 650
PILE_MIN = 5       # open bare items for class 'pile' (pre-registered; fr.2988 has 26, no other saved notice more than 3)


def _folio_num(f):
    m = re.match(r'\s*(\d+)', f or '')
    return int(m.group(1)) if m else None


def classify_item(r):
    """-> 'clear' (not a cipher item), 'deciphered', 'keysheet', 'bare' or 'named'."""
    t = r['text']
    if not CIPHER.search(t):
        return 'clear'
    if DECIPH.search(t):
        return 'deciphered'
    if KEYSHEET.search(t):
        return 'keysheet'
    if NAME.search(t) or DATE.search(t) or re.search(r'(?i)en clair', t):      # 'en clair' = a mixed piece, not a bare cipher
        return 'named'
    toks = [w.strip('.,;:()') for w in t.split()]
    if any(w[:1].isupper() and w.lower() not in FORMULA for w in toks[1:]):     # a place-name proxy
        return 'named'
    return 'bare'


def volume_blocks(s):
    """Text lines under 'Présentation du contenu' and 'Bibliographie' (the notice's own volume-level statements)."""
    L, out = to_text(s), []
    for i, l in enumerate(L):
        if l in ('Présentation du contenu', 'Bibliographie'):
            for x in L[i + 1:i + 4]:
                if x in STOP_HEAD or len(x) < 6:
                    break
                out.append(x)
    return out


def digitised(s):
    t = ' '.join(to_text(s))
    if re.search(r'(?i)non num[ée]ris|n.est pas num[ée]ris|pas de version num[ée]ris', t):
        return 'no'
    if re.search(r'(?i)version num[ée]ris[ée]e de ce document|gallica\.bnf\.fr/ark', t) or 'Voir le document numérisé' in t:
        return 'yes'
    return 'unknown'


_PW = {}


def _pw_ctx(root):
    """A prior_work.py context for check 3 (its functions are called read-only; offline, working tree)."""
    if root not in _PW:
        import types
        sys.path.insert(0, os.path.join(root, 'tools'))
        import prior_work as pw
        a = types.SimpleNamespace(slug='bnf-pile', root=root, ref='WORKTREE', now=None, max_requests=0, reading=None,
                                  known_answer=None, strict=False, cache=None, clone=[], dry_run=True, json=False,
                                  me='', or_dir=[])
        ctx = pw.Ctx(a, pw.State(root, 'WORKTREE'))
        ctx.net = None
        _PW[root] = (pw, ctx)
    return _PW[root]


def item_status(rows):
    """prior_work check-3 rows -> ('known'|'open', evidence).  A KNOWN stays known unless its evidence says
    undeciphered; a CONTEXT row whose evidence says 'broken/deciphered by' counts as known (the wording guard)."""
    for r in rows:
        ev = r.get('evidence', '')
        if r['verdict'] in ('KNOWN', 'KNOWN-PART') and not NEGATION.search(ev):
            return 'known', ev
        if r['verdict'] == 'CONTEXT' and POSITIVE.search(ev) and not NEGATION.search(ev):
            return 'known', ev
    return 'open', ''


def portal_status(cote, folio, root):
    pw, ctx = _pw_ctx(root)
    it = pw.item_from_spec('shelfmark=BnF %s;folio=%s' % (cote, folio))
    return item_status(pw.check_portals(ctx, it, pw.item_unit(it)))


def title_cote(title):
    m = re.match(r'^(Français|Clairambault|Dupuy|Espagnol|[A-ZÉ][\w\-éè\. ]*?) ([0-9][\w\-]*)', title)
    if not m:
        return ''
    name = {'Français': 'fr.', 'Clairambault': 'Clair. ', 'Dupuy': 'Dupuy ', 'Espagnol': 'esp. '}.get(m.group(1), m.group(1) + ' ')
    return name + m.group(2)


def score_volume(s, ark='', root=None, prior=None, portals=True, prior_work=False):
    title, rows = parse(s)
    cote = title_cote(title)
    for r in rows:
        r['kind'] = classify_item(r)
        r['f'] = _folio_num(r['folio']) or (1 if r['no'] == '1' else None)
    kinds = [r['kind'] for r in rows]
    n = {k: kinds.count(k) for k in ('clear', 'deciphered', 'keysheet', 'bare', 'named')}
    bare = [r for r in rows if r['kind'] == 'bare']
    bf_ = [r['f'] for r in bare if r['f'] is not None]
    gaps = sorted(b - a for a, b in zip(bf_, bf_[1:]) if b > a)
    gap = gaps[len(gaps) // 2] if gaps else 0
    pv = [b for b in volume_blocks(s) if PRIOR_VOL.search(b)]
    trap = False                       # clear-neighbour trap (M41)
    if len(bare) >= 2:
        idx = [i for i, r in enumerate(rows) if r['kind'] == 'bare']
        span = rows[idx[0]:idx[-1] + 1]
        clear = [r for r in span if r['kind'] == 'clear']
        years = [int(y) for r in clear for y in re.findall(r'\b(1[4-8]\d\d)\b', r['text'])]
        trap = bool(clear) and (any(LANG.search(r['text']) for r in clear) or
                                (len(years) >= 2 and max(years) - min(years) >= 10))
    ov = prior or {}
    open_items, ours, ours_q, slugs = [], 0, 0, set()
    is_range = len(range_vols(cote)) > 1
    for r in rows:
        if r['kind'] not in ('bare', 'named'):
            continue
        if prior_work and root and cote and r['f'] is not None:
            hit = own_hits(cote, r['f'], root)
            if hit:
                slugs.update(hit)
                if is_range:
                    ours_q += 1
                else:
                    ours += 1
                    continue                              # ours: out of the open counts, as a KNOWN
        st, key = 'open', (cote, r['f'])
        if key in ov:
            st = ov[key][0]
        elif r['kind'] == 'bare' and pv:
            st = 'known'                                  # the notice's own Présentation / Bibliographie
        elif portals and root and cote and r['f'] is not None:
            st = portal_status(cote, r['f'], root)[0]
        if st != 'known':
            open_items.append(r)
    open_bare = sum(1 for r in open_items if r['kind'] == 'bare')
    ncipher = n['bare'] + n['named'] + n['keysheet'] + n['deciphered']
    if not rows:
        cls = 'image-triage'
    elif not ncipher:
        cls = 'no-cipher-items'
    elif open_bare >= PILE_MIN:
        cls = 'pile'
    elif open_bare:
        cls = 'few-bare'
    elif open_items:
        cls = 'named-open'
    else:
        cls = 'excluded'
    return dict(cote=cote, title=title[:70], ark=ark, items=len(rows), cipher=ncipher, deciphered=n['deciphered'],
                keysheets=n['keysheet'], named=n['named'], bare=n['bare'], open_bare=open_bare,
                open_named=sum(1 for r in open_items if r['kind'] == 'named'), median_gap=gap,
                est_signs=len(bare) * gap * GAP_CONST, est_signs_open=open_bare * gap * GAP_CONST,
                neighbour_trap='yes' if trap else '', digitised=digitised(s), prior_work=' | '.join(pv)[:200], cls=cls,
                ours_items=ours, ours_range=ours_q, ours_slugs=' '.join(sorted(slugs))[:200],
                contact_first=(active_edition(cote, [r for r in rows if r['kind'] in ('bare', 'named')], root)
                               if prior_work and root and cote else ''))


SKIP_SLUGS = {'debosnys-1883'}
_OWN = {}


def own_index(root):
    """volume key -> [(slug, path:line, line, context_vols or None)] over ciphers/*/ top-level *.md + items.tsv (disk)."""
    if root in _OWN:
        return _OWN[root]
    sys.path.insert(0, os.path.join(root, 'tools'))
    import shelfmark as sm
    idx, base = {}, os.path.join(root, 'ciphers')
    for slug in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        d = os.path.join(base, slug)
        if (slug in SKIP_SLUGS or 'restricted' in slug.lower() or not os.path.isdir(d)
                or os.path.exists(os.path.join(d, 'RESTRICTED.md'))):
            continue
        fvols = set() if slug.startswith('_') else {v for v in sm.volume_keys(slug) if not v.startswith('hint:')}
        for fn in sorted(os.listdir(d)):
            if not (fn.endswith('.md') or fn == 'items.tsv') or 'restricted' in fn.lower():
                continue
            for i, line in enumerate(open(os.path.join(d, fn), errors='ignore'), 1):
                if not re.search(r'\d', line):
                    continue
                real = {v for v in sm.volume_keys(line) if not v.startswith('hint:')}
                keys, ctx = (real, None) if real else (fvols, fvols)
                for k in keys:
                    idx.setdefault(k, []).append((slug, '%s/%s:%d' % (slug, fn, i), line, ctx))
    _OWN[root] = (sm, idx)
    return _OWN[root]


def range_vols(cote):
    """'fr.3974-3995' -> ['fr.3974', ..., 'fr.3995'] (<= 200); a single cote -> [cote]."""
    m = re.match(r'^(.*?)(\d+)-(\d+)$', cote or '')
    if not m or int(m.group(3)) <= int(m.group(2)) or int(m.group(3)) - int(m.group(2)) > 200:
        return [cote]
    return ['%s%d' % (m.group(1), n) for n in range(int(m.group(2)), int(m.group(3)) + 1)]


def own_hits(cote, folio, root):
    """-> sorted slugs of ciphers/ folders naming this volume + folio exactly."""
    sm, idx = own_index(root)
    out = set()
    for v in range_vols(cote):
        u = sm.unit('BnF ' + v, str(folio))
        for k in u.vols:
            for slug, where, line, ctx in idx.get(k, []):
                if slug not in out and sm.match(u, line, context_vols=ctx) == 'exact':
                    out.add(slug)
    return sorted(out)


def active_edition(cote, rows, root):
    pw, ctx = _pw_ctx(root)
    for r in rows or [{'f': None}]:
        it = pw.item_from_spec('shelfmark=BnF %s' % cote + (';folio=%s' % r['f'] if r.get('f') else ''))
        hits = pw.check_active_edition(ctx, it, pw.item_unit(it))
        if hits:
            return hits[0]['route'] or 'active-edition'
    return ''


PILE_COLS = ['cote', 'ark', 'items', 'cipher', 'deciphered', 'keysheets', 'named', 'bare', 'open_bare', 'open_named',
             'median_gap', 'est_signs', 'est_signs_open', 'neighbour_trap', 'digitised', 'cls', 'prior_work']
PRIOR_COLS = ['ours_items', 'ours_range', 'ours_slugs', 'contact_first']


def read_prior(path):
    out = {}
    if path:
        for l in open(path, encoding='utf-8'):
            c = l.rstrip('\n').split('\t')
            if len(c) >= 3 and not c[0].startswith('#') and c[0] != 'shelfmark':
                out[(c[0], _folio_num(c[1]))] = (c[2], c[3] if len(c) > 3 else '')
    return out


def pile(paths, prior=None, tsv=None, root=None, portals=True, prior_work=False):
    root = root or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    ov, res = read_prior(prior), []
    cols = PILE_COLS + (PRIOR_COLS if prior_work else [])
    for p in paths:
        ark = re.match(r'(cc[0-9a-z]+)', os.path.basename(p))
        res.append(score_volume(open(p, errors='ignore').read(), ark.group(1) if ark else '', root, ov, portals, prior_work))
    res = list({r['ark'] or r['cote']: r for r in res}.values())       # one row per notice
    res.sort(key=lambda r: (-r['open_bare'], -r['bare'], r['cote']))
    lines = ['\t'.join(cols)] + ['\t'.join(str(r[c]) for c in cols) for r in res]
    if tsv:
        open(tsv, 'w').write('\n'.join(lines) + '\n')
    return res, lines


def permute_null(volumes, n=200, seed=20261009):
    """volumes: list of item-text lists, one per volume.  -> (real max bare, sorted null maxima).  Item kinds are a
    function of the text alone (classify_item), so permuting texts across volumes permutes kinds."""
    import random
    kinds = [[classify_item({'text': t}) == 'bare' for t in v] for v in volumes]
    real = max((sum(k) for k in kinds), default=0)
    pool = [b for k in kinds for b in k]
    sizes, rng, null = [len(k) for k in kinds], random.Random(seed), []
    for _ in range(n):
        rng.shuffle(pool)
        i, m = 0, 0
        for z in sizes:
            m, i = max(m, sum(pool[i:i + z])), i + z
        null.append(m)
    return real, sorted(null)


def permute_report(paths, n=200, seed=20261009):
    vols = [[r['text'] for r in parse(open(p, errors='ignore').read())[1]] for p in paths]
    real, null = permute_null([v for v in vols if v], n, seed)
    q = lambda f: null[min(len(null) - 1, int(f * len(null)))]
    return '# permute: volumes %d items %d | real max bare %d | null n=%d p50 %d p95 %d max %d | real > p95: %s' % (
        sum(1 for v in vols if v), sum(map(len, vols)), real, n, q(0.5), q(0.95), null[-1], 'yes' if real > q(0.95) else 'no')


# ---------------------------------------------------------------------------------------------------------------
# --census / --local-search / --branch-pdf (MQS-BNFPILE, 9 Oct 2026)
# ---------------------------------------------------------------------------------------------------------------
def curl_meta(args):
    """-> (http status, body, seconds, bytes); sys.exit only on a curl transport error."""
    t0 = time.time()
    r = subprocess.run(['curl', '-sS', '-A', UA, '--max-time', '60', '-w', '\n%{http_code}'] + args, capture_output=True)
    if r.returncode:
        sys.exit('curl failed: %s' % r.stderr.decode(errors='ignore')[:200])
    body, _, code = r.stdout.decode('utf-8', errors='ignore').rpartition('\n')
    return int(code or 0), body, round(time.time() - t0, 2), len(r.stdout)


def parse_results(s):
    """Total, facets (Départements / Dates / Noms as 'label (n)'), first-page finding-aid arks, Gallica links."""
    L = to_text(s)
    total = next((int(m.group(1).replace(' ', '')) for l in L for m in [re.match(r'^([\d\s]+) r[ée]sultats?$', l)] if m), None)
    if total is None and any(l.startswith('Aucun résultat') for l in L):
        total = 0
    facets, cur = {}, None
    for l in L:
        if l in ('Départements', 'Dates', 'Noms'):
            cur = l
            facets[cur] = []
        elif cur and re.search(r'\(\d+\)$', l):
            facets[cur].append(l)
        elif cur and not re.search(r'\(\d+\)$', l):
            cur = None
    arks = []
    for m in re.finditer(r'ark:/12148/(cc[0-9a-z]+)', s):
        if m.group(1) not in arks:
            arks.append(m.group(1))
    return dict(total=total, facets=facets, arks=arks, gallica=s.count('class="pictoGallica"'),
                challenge=bool(re.search(r'(?i)captcha|challenge|access denied|cloudflare', s[:3000])))


def census(phrases, outdir, gap=2.0):
    """One quoted POST per phrase; saves each response, appends census.tsv and manifest.json under OUTDIR.
    Stops at the first non-200 or challenge page (good-citizen rule); never pages beyond the first result page."""
    import json
    os.makedirs(os.path.join(outdir, 'html'), exist_ok=True)
    manifest, rows = [], []
    for i, ph in enumerate(phrases, 1):
        q = '"%s"' % ph.strip('"')
        code, body, secs, size = curl_meta(['-X', 'POST', '--data-urlencode', 'TEXTE_LIBRE_INPUT=' + q,
                                            '-d', 'DOC_NUMERISE_INPUT_RADIO=all_docs&NUMERO_DEPARTEMENT_INPUT=',
                                            BASE + 'resultatRechercheSimple.html'])
        fn = os.path.join(outdir, 'html', 'q%02d.html' % i)
        open(fn, 'w').write(body)
        manifest.append(dict(phrase=ph, url=BASE + 'resultatRechercheSimple.html', status=code, bytes=size, seconds=secs, file=fn))
        r = parse_results(body)
        rows.append([ph, str(r['total']), '; '.join('%s: %s' % (k, ', '.join(v)) for k, v in r['facets'].items()),
                     ' '.join(r['arks'][:20]), str(r['gallica'])])
        if code != 200 or r['challenge']:
            sys.stderr.write('STOP: HTTP %s / challenge=%s on %r\n' % (code, r['challenge'], ph))
            break
        time.sleep(gap)
    open(os.path.join(outdir, 'census.tsv'), 'w').write(
        'phrase\ttotal\tfacets\tfirst_page_arks\tgallica_links\n' + '\n'.join('\t'.join(x) for x in rows) + '\n')
    open(os.path.join(outdir, 'manifest.json'), 'w').write(json.dumps(manifest, ensure_ascii=False, indent=1))
    return rows


def local_search(ir, term):
    """Search inside ONE finding aid (route read from /js/pagePresentationIr.js).  IR is the finding-aid id seen in
    the notice's refreshCompInfo('FRBNFEAD000049442_d0e92') calls, i.e. FRBNFEAD000049442.  Confirmed on fr.2988
    (9 Oct 2026): 'chiffre' answers 'Nombre d'éléments trouvés : 29' in one response, no pagination."""
    code, body, _, _ = curl_meta([BASE + 'affichageDetailsComposants.html?eadCid=%s&typeIndex=TEXTE_LIBRE_LOCAL&val=%s'
                                  % (ir, urllib.parse.quote(term))])
    return code, to_text(body)


def branch_pdf(ark):
    """UNTESTED ROUTE: exportBranchePdf.html?arkId=ARK answered HTTP 500 on 9 Oct 2026 (cc49442s, one request); it
    probably needs a session or the browser's own parameters.  Kept so a later session can retry with them."""
    code, body, _, _ = curl_meta([BASE + 'exportBranchePdf.html?arkId=' + ark])
    return code, body[:300]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--pile', nargs='+', metavar='NOTICE.html', help='score saved notices for an unread cipher pile (offline)')
    g.add_argument('--census', nargs='+', metavar='PHRASE', help='count quoted catalogue phrases (needs --out DIR)')
    g.add_argument('--local-search', nargs=2, metavar=('IR', 'TERM'), help='search inside one finding aid')
    g.add_argument('--branch-pdf', metavar='ARK', help='UNTESTED ROUTE (HTTP 500 on 9 Oct 2026)')
    g.add_argument('--cote')
    g.add_argument('--ark')
    g.add_argument('--html')
    ap.add_argument('--prior', help='--pile: override TSV (shelfmark, folio, status, source) for statuses no cache holds')
    ap.add_argument('--out', help='--census: output directory (census.tsv, manifest.json, html/)')
    ap.add_argument('--tsv', help='--pile: write the per-volume table here')
    ap.add_argument('--permute', type=int, metavar='N', help='--pile: across-volume permutation null, N permutations')
    ap.add_argument('--prior-work', action='store_true', help='--pile: own work across ciphers/ (shelfmark exact) + active edition; disk only')
    ap.add_argument('--no-portals', action='store_true', help='--pile: skip the prior_work.py per-item check (fast)')
    ap.add_argument('--save-html', help='directory to keep the fetched notice (fetch once, read from disk after)')
    a = ap.parse_args()
    if a.census:
        if not a.out:
            ap.error('--census needs --out DIR')
        for r in census(a.census, a.out):
            print('\t'.join(r)[:300])
        return 0
    if a.local_search:
        code, lines = local_search(*a.local_search)
        print('# HTTP %s' % code)
        print('\n'.join(lines))
        return 0
    if a.branch_pdf:
        print(branch_pdf(a.branch_pdf))
        return 0
    if a.pile:
        res, lines = pile(a.pile, a.prior, a.tsv, portals=not a.no_portals, prior_work=a.prior_work)
        print('\n'.join(lines))
        if a.permute:
            print(permute_report(a.pile, a.permute))
        return 0
    ark = a.ark
    if a.html:
        s = open(a.html, errors='ignore').read()
    else:
        if a.cote:
            ark, t = find_ark(a.cote)
            if not ark:
                print('# no exact-title match for %r in the simple search' % a.cote)
                return 2
            time.sleep(2)
        cached = os.path.join(a.save_html, ark + '.html') if a.save_html else ''
        if cached and os.path.exists(cached):          # fetch once, read from disk after (one notice can cover
            s = open(cached, errors='ignore').read()   # a whole run of volumes, e.g. fr.3974-3995)
            a.save_html = None
        else:
            s = curl([BASE + 'ark:/12148/' + ark])
        if a.save_html:
            os.makedirs(a.save_html, exist_ok=True)
            open(os.path.join(a.save_html, ark + '.html'), 'w').write(s)
    title, rows = parse(s)
    print('# %s | ark:/12148/%s | %d items, %d flagged chiffre' % (title[:160], ark or '?', len(rows),
                                                                   sum(1 for r in rows if r['chiffre'])))
    if not rows:
        print('# no item list in this notice: not a negative')
    print('folio\tno\tchiffre\tdechiffre\ttext')
    for r in rows:
        print('\t'.join([r['folio'], r['no'], r['chiffre'], r['dechiffre'], r['text'][:300]]))
    return 0


if __name__ == '__main__':
    sys.exit(main())
