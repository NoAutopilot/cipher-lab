#!/usr/bin/env python3
"""name_candidates.py -- propose people or places for a whole-name nomenclature code from its decoded contexts.

MQS-NAMES, LANE MQS (account 4), 9 Oct 2026. The "brother-in-law" step of Lasry, Biermann and Tomokiyo 2023 (p.122,
p.103): one symbol stands in "l'arrivee prochaine de [K] mon beau-frere", 20 Jan 1580, Mary writing, so K is a living
brother-in-law expected in England -- the Duke of Anjou. This tool PROPOSES and never decides: a candidate becomes a
reading only after `decode_key.py --try` tests it at every occurrence and a verifier grades it. It never writes key.tsv,
names.tsv or any reading (an offline test hashes key.tsv before and after).

  python3 tools/name_candidates.py ciphers/<t> --code CODE [--config decode.json ...] [--contexts CTX.tsv ...]
      --sender NAME|QID --recipient NAME|QID --date YYYY-MM-DD [--lang fr|de] [--index FILE|MANIFEST.tsv ...]
      [--pool FROZEN.tsv] [--freeze-pool OUT.tsv] [--wikidata] [--offline] [--mask-letters L1,L2]
      [--truth 'alias|alias'] [--top 10] [--nulls 200] [--out ciphers/<t>/candidates_<code>.tsv]
  python3 tools/name_candidates.py --find-controls [--min 8]     # scan ciphers/* for known-answer name-code sets

Steps (brief .claude/briefs/runs/2026-10-09-acct3-mqs-names.md):
 1. Contexts: every occurrence of CODE in decode_key's graded tokens (`graded_recs`), +-W tokens rendered as decoded
    text (NULLs dropped, unknown codes as <code>, the tested code ALWAYS as <CODE>, its key value never read; the ciphertext's
    gloss and notes columns are never read), or rows of a --contexts TSV (letter, date, line, left, right).
 2. Cues from tools/data/name_cues_<lang>.tsv (kinship, possessive, title/office, gender, place and person frames).
 3. Pool, built and frozen BEFORE scoring (--freeze-pool, sha256 printed): KEY-OFFICES.tsv correspondents, --index edition
    text (the promoted H41 surname extraction plus titled phrases and recurrent capitalised names), and Wikidata
    (--wikidata: kin of sender and recipient to depth 2 incl. siblings-in-law, their positions with dates, their places).
    Never from the tested code's own names.tsv/key.tsv row; never from a masked letter's printed text (--mask-letters).
 4. Score: relation match, alive at date, office at date, gender agreement, place/person frame, co-mention in the
    (unmasked) edition text near the date, consistency over ALL contexts, already-assigned penalty.
 5. Nulls: (i) context null -- the scorer gets the contexts of random other codes of matched occurrence count
    (--nulls draws); the true/top candidate's score and rank under real vs null contexts; (ii) decoy null (promoted from
    NEVBIR-NAMES' random-word null) -- random words of the candidates' lengths from the index text enter the pool as
    decoys with a random pool entry's type; the share of draws in which a decoy outranks the true/top candidate.
 6. Output TSV: rank, candidate, source, features, score, grade (M at most; I when only inferred), evidence.

What earlier runs taught (rule 3's third-attempt clause: this is a different instrument, not a re-try):
 - A2-LVN4 (2 Oct 2026, ciphers/lodewijk-van-nassau-1573-74/replies/reply_fit.py): names from Orange's printed replies
   matched as stems against unread codes' contexts; known answer 0 hits, 1 wrong -- every wrong proposal came from ONE
   generic passage, and a reply names whatever it happens to discuss. Here: no reply text; cues are relation, office
   and alive-at-date features of the code's OWN contexts, and a candidate must fit all contexts (one passage cannot carry it).
 - A2-GRA6 (3 Oct 2026, ciphers/fr2980-gramont/f84_names_test.py): a same-sender clear letter's topic did not match; the
   letter-shuffle null reproduced short words (p99 tied the true score); a boundary-fit statistic favoured T-/-A edges.
   Here: no topic letter; the null shuffles CONTEXTS between codes, never letters inside a name, so an identity shuffle
   cannot tie it, and no statistic looks at a name's letters at all, so an edge-letter bias cannot drive it.
 - BIRAGO-NUM2 (2 Oct 2026, LEDGER.md 1648-1649): 12 pre-registered cribs, power control weak. Here: power is
   measured by subsampling to the target's own count (control (a), n=1 class).
 - NEVBIR-NAMES (3 Oct 2026, ciphers/nevers-birago-fr3251-1572/harvest/names/match_names.py): random words of the same
   lengths fit most gaps -- promoted here as the decoy null.
 - Mercy H41 (28 Sept 2026, ciphers/espagnol142-mercy-1648/h41/names.py + fit.py): a list built from an edition BEFORE
   scoring; its surname extraction is promoted into the --index pool step (h41_surnames below); its letter-by-letter
   fit lives in tools/crib_list_fit.py -- route any partly SPELLED window there; this tool is for whole-name codes.

Usage 8a scope (each backed by an offline test in tools/tests/test_name_candidates.py):
 - catches: a kin cue at the date ("mon beau-frere" 1580-01-20 ranks Anjou and Henry III above the dead Charles IX);
   a candidate dead at the date (Anjou below Henry III at 1585); a candidate that fits one context and contradicts another.
 - must NOT block: a code with no cue word still returns a co-mention/recurrence ranking flagged "no relation cue",
   never an empty list; a pool built with and without the tested code's names.tsv row, and with and without the masked
   letters' edition passages, is identical (and so is every feature value) -- the no-leak tests.
"""
import argparse, csv, glob, hashlib, json, math, os, random, re, sys, time, unicodedata
import urllib.parse, urllib.request
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

UA = 'cipher-lab research script (+https://github.com/NoAutopilot/cipher-lab)'
WD_ENDPOINT = 'https://query.wikidata.org/sparql'
WD_CACHE = os.path.join(ROOT, 'sources', 'wikidata', '2026-10-09')
WD_MAX = 60
POOL_COLS = ['id', 'label', 'aliases', 'type', 'relations', 'titles', 'born', 'died', 'offices', 'gender', 'source']
NOCUE = 'no relation cue'


# ------------------------------------------------------------------ text helpers

def fold(w):
    """Spelling-tolerant fold for matching names across languages and periods (not a scoring statistic)."""
    w = unicodedata.normalize('NFKD', (w or '').lower())
    w = ''.join(c for c in w if not unicodedata.combining(c)).replace('ß', 'ss')
    w = re.sub('[^a-z]', '', w)
    for a, b in (('ck', 'k'), ('ph', 'f'), ('th', 't'), ('y', 'i'), ('j', 'i'), ('v', 'u'), ('w', 'u'), ('c', 'k'),
                 ('z', 's'), ('dt', 't')):
        w = w.replace(a, b)
    return re.sub(r'(.)\1+', r'\1', w)


def words(s):
    return [x for x in re.split(r"[^\w<>']+", (s or '').lower().replace("'", "' ")) if x]


def alias_match(a, b):
    """Two names agree: equal folds, or one fold a prefix of the other with at least 5 letters (Frankreich/France no)."""
    fa, fb = fold(a), fold(b)
    if not fa or not fb:
        return False
    if fa == fb:
        return True
    s, l = sorted((fa, fb), key=len)
    return len(s) >= 5 and l.startswith(s)


def cand_names(c):
    return [c['label']] + [a for a in c.get('aliases', '').split('|') if a]


def sha256(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def year(d):
    m = re.match(r'-?\d{1,4}', d or '')
    return int(m.group(0)) if m else None


def date_key(d):
    """YYYY[-MM[-DD]] -> comparable tuple; None if unknown."""
    m = re.match(r'(-?\d{1,4})(?:-(\d\d))?(?:-(\d\d))?', d or '')
    if not m:
        return None
    return (int(m.group(1)), int(m.group(2) or 0), int(m.group(3) or 0))


# ------------------------------------------------------------------ cues

def load_cues(lang, path=None):
    """Cue TSV: cue, class, value, weight[, corpus_count, ...]. '#' lines are the header naming the general source."""
    path = path or os.path.join(ROOT, 'tools', 'data', f'name_cues_{lang}.tsv')
    cues = []
    for l in open(path, encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        p = l.rstrip('\n').split('\t')
        if p[0] == 'cue':
            continue
        cues.append(dict(cue=p[0].lower(), cls=p[1], value=p[2], weight=float(p[3] or 1)))
    return cues


def cue_hits(ctx, cues, span=3):
    """Cues found within `span` words of the code (left words nearest first, right words nearest first)."""
    L, R = words(ctx['left'])[::-1][:span], words(ctx['right'])[:span]
    hits = []
    for c in cues:
        toks = c['cue'].split()
        n = len(toks)
        for side, ws in (('L', L), ('R', R)):
            seq = ws[::-1] if side == 'L' else ws
            for i in range(len(seq) - n + 1):
                if seq[i:i + n] == toks:
                    dist = (len(seq) - i - n) if side == 'L' else i
                    hits.append(dict(c, side=side, dist=dist, at=i, n=n))
    # a cue inside a longer cue at the same place ('frere' inside 'beau frere') is dropped
    return [h for h in hits if not any(o is not h and o['side'] == h['side'] and o['n'] > h['n']
                                       and o['at'] <= h['at'] and h['at'] + h['n'] <= o['at'] + o['n'] for o in hits)]


# ------------------------------------------------------------------ contexts

def letter_of(name):
    m = re.search(r'(\d{4,})', os.path.basename(name))
    return m.group(1) if m else os.path.splitext(os.path.basename(name))[0]


def render(r, code):
    """One decoded token as context text; the tested code is always <CODE> and its key value is never read."""
    if r['kind'] == 'clear':
        return ' ' + r['value'] + ' '
    if r['kind'] != 'sign':
        return ''
    if r['sign'] == code:
        return f' <{code}> '
    v = r.get('value')
    if r.get('null'):
        return ''
    if v in (None, '', '?') or r.get('grade') == 'U':
        return f' <{r["sign"]}> '
    v = v.lstrip('=')
    return (' ' + v + ' ') if len(v) >= 2 else v


def contexts_from_config(target, cfg_path, code, width=8, all_codes=False):
    """Occurrences of `code` (or of every code, all_codes=True: {code: [ctx]}) in each job of a decode config."""
    import decode_key
    cfg = json.load(open(cfg_path))
    tdir = target if os.path.isabs(target) else os.path.join(ROOT, target)
    if cfg.get('target'):
        tdir = os.path.join(ROOT, cfg['target'])
    out = defaultdict(list)
    for job in cfg['jobs']:
        try:
            recs, ct = decode_key.graded_recs(tdir, job)
        except (OSError, KeyError, ValueError) as e:
            print(f'name_candidates: skip job {job.get("ciphertext")}: {e}', file=sys.stderr)
            continue
        signs = [r for r in recs if r['kind'] in ('sign', 'clear')]
        letter = job.get('letter') or letter_of(ct)
        for i, r in enumerate(signs):
            if r['kind'] != 'sign' or (not all_codes and r['sign'] != code):
                continue
            c = r['sign']
            left = ''.join(render(x, c) for x in signs[max(0, i - width):i])
            right = ''.join(render(x, c) for x in signs[i + 1:i + 1 + width])
            out[c].append(dict(letter=letter, date=job.get('date', ''), line=r['line'], pos=r['pos'],
                               left=re.sub(r'\s+', ' ', left).strip(), right=re.sub(r'\s+', ' ', right).strip(),
                               source=os.path.relpath(os.path.join(tdir, ct), ROOT)))
    return out if all_codes else out.get(code, [])


def contexts_from_tsv(path, code=None):
    rows = []
    for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'):
        if code is not None and r.get('code', code) != code:
            continue
        rows.append(dict(letter=r.get('letter', ''), date=r.get('date', ''), line=r.get('line', ''),
                         pos=r.get('pos', ''), left=r.get('left', ''), right=r.get('right', ''), source=path,
                         code=r.get('code', code)))
    return rows


def contexts_from_mdblocks(folder, all_codes=True, width=8, items=None):
    """Contexts of every code word in an md-blocks folder (tools/holder_export.py's MdBlocks loader, read-only):
    neighbours rendered by their meanings (H/C/S/M), unread ones as <word>; {code word: [ctx]}."""
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location('holder_export', os.path.join(HERE, 'holder_export.py'))
    md = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(md)
    mb = md.MdBlocks(Path(folder if os.path.isabs(folder) else os.path.join(ROOT, folder)))
    out = defaultdict(list)
    for iid in mb.items:
        if items is not None and iid not in items:
            continue
        toks = [t for t in mb.tokens(iid) if t[4] in ('word', 'as-written', 'numeral', 'time')]
        for i, (_, w, meaning, g, kind) in enumerate(toks):
            if kind != 'word':
                continue
            def rd(t):
                if t[1] == w:
                    return f'<{w}>'
                return t[2] if t[3] in ('H', 'C', 'S', 'M') and t[2] else f'<{t[1]}>'
            left = ' '.join(rd(t) for t in toks[max(0, i - width):i])
            right = ' '.join(rd(t) for t in toks[i + 1:i + 1 + width])
            out[w].append(dict(letter=iid, date='', line=iid, pos=i, left=re.sub(r'\(.*?\)', '', left),
                               right=re.sub(r'\(.*?\)', '', right), source=mb.items[iid]['cipher_file']))
    return out


# ------------------------------------------------------------------ index (edition text) pool step

def h41_surnames(text, min_count=2):
    """Promoted from ciphers/espagnol142-mercy-1648/h41/names.py (Mercy H41, 28 Sept 2026): the word after
    von / v. / Graf(en) / Freiherr(n) / Herr(n) / Oberst / Kanzler, or a capitalised word with a possessive 's, seen
    at least twice. Returns {surname: count} (unfolded; H41's own alphabet fold is target-specific and stays there)."""
    c = Counter()
    for m in re.finditer(r"\b(?:von|v\.|Graf|Grafen|Freiherr|Freiherrn|Herr|Herrn|Oberst|Kanzler)\s+([A-ZÄÖÜ][a-zäöüß]{4,14})\b", text):
        c[m.group(1)] += 1
    for m in re.finditer(r"\b([A-ZÄÖÜ][a-zäöüß]{4,14})'s\b", text):
        c[m.group(1)] += 1
    return {w: n for w, n in c.items() if n >= min_count}


TITLE_RE = (r"\b((?:le |la |der |die |dem |den |des |du )?(?:{titles})\s+(?:de |d'|von |van |zu |of |du |des )"
            r"(?:la |le )?[A-ZÄÖÜÉ][\w'éèàäöü]{{2,20}})")


def titled_phrases(text, title_words):
    pat = TITLE_RE.format(titles='|'.join(sorted({re.escape(t) for t in title_words}, key=len, reverse=True)))
    c = Counter()
    for m in re.finditer(pat, text, flags=re.I):
        p = re.sub(r'^(le|la|der|die|dem|den|des|du) ', '', m.group(1), flags=re.I)
        c[p] += 1
    return c


def proper_names(text, min_count=2, stop=None):
    """Recurrent capitalised words not at a sentence start (places and surnames)."""
    c = Counter()
    for m in re.finditer(r"(?<![.!?:;]\s)(?<!^)(?<=[\s,(])([A-ZÄÖÜÉ][a-zäöüéèàß]{3,16})\b", text):
        w = m.group(1)
        if stop and w.lower() in stop:
            continue
        c[w] += 1
    return {w: n for w, n in c.items() if n >= min_count}


def load_index(specs, mask):
    """--index FILE or MANIFEST.tsv (path, letters, date[, lang]). A file whose letters meet the mask, or whose name is a
    folder decipherment_/plaintext_/reading_ file of a masked letter, is excluded. Returns (kept, masked) lists of
    dict(path, letters, date, text)."""
    entries = []
    for s in specs or []:
        if s.endswith('.tsv') and open(s, encoding='utf-8').readline().startswith('path'):
            base = os.path.dirname(s)
            for r in csv.DictReader(open(s, encoding='utf-8'), delimiter='\t'):
                p = r['path'] if os.path.isabs(r['path']) else os.path.join(ROOT, r['path'])
                if not os.path.exists(p):
                    p = os.path.join(base, r['path'])
                entries.append(dict(path=p, letters={x for x in re.split(r'[,; ]+', r.get('letters', '')) if x},
                                    date=r.get('date', '')))
        else:
            entries.append(dict(path=s, letters={letter_of(s)} if re.search(r'\d{4,}', os.path.basename(s)) else set(),
                                date=''))
    kept, masked = [], []
    for e in entries:
        bn = os.path.basename(e['path'])
        own = re.match(r'(decipherment|plaintext|reading)_', bn) and letter_of(bn) in mask
        (masked if (e['letters'] & mask or own) else kept).append(e)
    for e in kept:
        t = open(e['path'], encoding='utf-8', errors='replace').read()
        if e['path'].endswith(('.html', '.htm')):
            t = re.sub(r'<[^>]+>', ' ', t)
        e['text'] = t
    return kept, masked


# ------------------------------------------------------------------ Wikidata (query.wikidata.org only, cached)

class Wikidata:
    def __init__(self, offline=False, cache=WD_CACHE, limit=WD_MAX):
        self.offline, self.cache, self.limit, self.n, self.stopped = offline, cache, limit, 0, None
        self.manifest_path = os.path.join(cache, 'manifest.json')

    def _manifest(self):
        return json.load(open(self.manifest_path)) if os.path.exists(self.manifest_path) else []

    def sparql(self, q, label):
        h = hashlib.sha1(q.encode()).hexdigest()[:16]
        f = os.path.join(self.cache, f'{label}_{h}.json')
        if os.path.exists(f):
            return json.load(open(f))
        if self.offline or self.stopped:
            print(f'name_candidates: wikidata {label} not cached ({"offline" if self.offline else self.stopped})',
                  file=sys.stderr)
            return None
        if self.n >= self.limit:
            self.stopped = f'request cap {self.limit} reached'
            return None
        if self.n:
            time.sleep(1.5)
        self.n += 1
        url = WD_ENDPOINT + '?' + urllib.parse.urlencode({'query': q, 'format': 'json'})
        req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/sparql-results+json'})
        t0 = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                body, status = r.read(), r.status
        except Exception as e:  # 403, 429, timeout: stop the host, finish from cache
            status = getattr(e, 'code', 'error')
            self.stopped = f'HTTP {status}'
            self._log(dict(url=url, status=status, bytes=0, time=t0, file=None, label=label))
            print(f'name_candidates: wikidata stopped ({self.stopped}); finishing from cache and indexes', file=sys.stderr)
            return None
        os.makedirs(self.cache, exist_ok=True)
        open(f, 'wb').write(body)
        self._log(dict(url=url, status=status, bytes=len(body), time=t0, file=os.path.basename(f), label=label))
        return json.loads(body)

    def _log(self, row):
        os.makedirs(self.cache, exist_ok=True)
        m = self._manifest()
        m.append(row)
        json.dump(m, open(self.manifest_path, 'w'), indent=1)


def wd_resolve(wd, name):
    if re.fullmatch(r'Q\d+', name or ''):
        return name
    q = ('SELECT ?p WHERE { VALUES ?n { "%s"@en "%s"@fr "%s"@de "%s"@nl } ?p rdfs:label ?n ; wdt:P31 wd:Q5 . } LIMIT 3'
         % ((name.replace('"', ''),) * 4))
    res = wd.sparql(q, 'resolve')
    b = (res or {}).get('results', {}).get('bindings', [])
    return b[0]['p']['value'].rsplit('/', 1)[1] if b else None


KIN_PATHS = [
    ('parent', 'wdt:P22|wdt:P25'), ('child', 'wdt:P40'), ('sibling', 'wdt:P3373'), ('spouse', 'wdt:P26'),
    ('sibling_in_law', 'wdt:P26/wdt:P3373'), ('sibling_in_law', 'wdt:P3373/wdt:P26'),
    ('uncle_aunt', '(wdt:P22|wdt:P25)/wdt:P3373'), ('nephew_niece', 'wdt:P3373/wdt:P40'),
    ('grandparent', '(wdt:P22|wdt:P25)/(wdt:P22|wdt:P25)'), ('grandchild', 'wdt:P40/wdt:P40'),
    ('parent_in_law', 'wdt:P26/(wdt:P22|wdt:P25)'), ('child_in_law', 'wdt:P40/wdt:P26'),
    ('cousin', '(wdt:P22|wdt:P25)/wdt:P3373/wdt:P40'),
]


def wd_kin(wd, ego, role):
    """Kin of ego to depth 2 (cousins at 3), with life dates, gender, labels; one request."""
    unions = ' UNION '.join('{ wd:%s %s ?p . BIND("%s" AS ?rel) }' % (ego, path, rel) for rel, path in KIN_PATHS)
    q = ('SELECT ?p ?rel ?b ?d ?g ?len ?lfr ?lde ?lnl WHERE { %s FILTER(?p != wd:%s) '
         'OPTIONAL { ?p wdt:P569 ?b } OPTIONAL { ?p wdt:P570 ?d } OPTIONAL { ?p wdt:P21 ?g } '
         'OPTIONAL { ?p rdfs:label ?len FILTER(lang(?len)="en") } OPTIONAL { ?p rdfs:label ?lfr FILTER(lang(?lfr)="fr") } '
         'OPTIONAL { ?p rdfs:label ?lde FILTER(lang(?lde)="de") } OPTIONAL { ?p rdfs:label ?lnl FILTER(lang(?lnl)="nl") } }'
         % (unions, ego))
    return wd.sparql(q, f'kin_{role}_{ego}')


def wd_details(wd, qids, label):
    """Positions (with start/end) and places (birth, death, citizenship, residence) of the pool persons; one request."""
    if not qids:
        return None
    vals = ' '.join('wd:' + q for q in sorted(qids))
    q = ('SELECT ?p ?kind ?x ?s ?e ?xen ?xfr ?xde ?xnl WHERE { VALUES ?p { %s } '
         '{ ?p p:P39 ?st . ?st ps:P39 ?x . OPTIONAL { ?st pq:P580 ?s } OPTIONAL { ?st pq:P582 ?e } BIND("office" AS ?kind) } '
         'UNION { ?p wdt:P97 ?x . BIND("office" AS ?kind) } '
         'UNION { ?p wdt:P19|wdt:P20|wdt:P551 ?x . BIND("place" AS ?kind) } '
         'UNION { ?p wdt:P27 ?x . BIND("place" AS ?kind) } '
         'OPTIONAL { ?x rdfs:label ?xen FILTER(lang(?xen)="en") } OPTIONAL { ?x rdfs:label ?xfr FILTER(lang(?xfr)="fr") } '
         'OPTIONAL { ?x rdfs:label ?xde FILTER(lang(?xde)="de") } OPTIONAL { ?x rdfs:label ?xnl FILTER(lang(?xnl)="nl") } }'
         % vals)
    return wd.sparql(q, label)


def _v(b, k):
    return b[k]['value'] if k in b else ''


def _qid(u):
    return u.rsplit('/', 1)[1] if u else ''


def pool_from_wikidata(wd, egos):
    """egos: {'sender': QID, 'recipient': QID}. Returns candidate dicts (persons, their offices, their places)."""
    persons = {}
    for role, ego in egos.items():
        if not ego:
            continue
        res = wd_kin(wd, ego, role)
        for b in (res or {}).get('results', {}).get('bindings', []):
            q = _qid(_v(b, 'p'))
            c = persons.setdefault(q, dict(id=q, label='', aliases=set(), type='person', relations=set(), titles=set(),
                                           born='', died='', offices=set(), gender='', source='wikidata:' + q))
            labs = [_v(b, k) for k in ('len', 'lfr', 'lde', 'lnl') if _v(b, k)]
            if labs and not c['label']:
                c['label'] = labs[0]
            c['aliases'].update(labs)
            c['relations'].add(f'{role}:{_v(b, "rel")}')
            c['born'] = c['born'] or _v(b, 'b')[:10].lstrip('+')
            c['died'] = c['died'] or _v(b, 'd')[:10].lstrip('+')
            g = _qid(_v(b, 'g'))
            c['gender'] = c['gender'] or {'Q6581097': 'm', 'Q6581072': 'f'}.get(g, '')
    places = {}
    det = wd_details(wd, set(persons), 'details_' + '_'.join(v for v in egos.values() if v))
    for b in (det or {}).get('results', {}).get('bindings', []):
        p, x = _qid(_v(b, 'p')), _qid(_v(b, 'x'))
        labs = [_v(b, k) for k in ('xen', 'xfr', 'xde', 'xnl') if _v(b, k)]
        if not labs or p not in persons:
            continue
        if _v(b, 'kind') == 'office':
            persons[p]['offices'].add(f'{labs[0]}@{_v(b, "s")[:10].lstrip("+")}/{_v(b, "e")[:10].lstrip("+")}')
            persons[p]['aliases'].update(labs[:1])
        else:
            c = places.setdefault(x, dict(id=x, label=labs[0], aliases=set(), type='place', relations=set(),
                                          titles=set(), born='', died='', offices=set(), gender='',
                                          source='wikidata:' + x))
            c['aliases'].update(labs)
    return list(persons.values()) + list(places.values())


# ------------------------------------------------------------------ pool

def norm_cand(c):
    d = dict(c)
    for k in ('aliases', 'relations', 'titles', 'offices'):
        v = d.get(k, '')
        d[k] = '|'.join(sorted(v)) if isinstance(v, (set, list, tuple)) else (v or '')
    for k in POOL_COLS:
        d.setdefault(k, '')
    return {k: d[k] for k in POOL_COLS}


def title_classes(text, cues):
    """Title classes a label or office string carries, from the cue file's title rows plus English office words."""
    t = ' ' + ' '.join(words(text)) + ' '
    out = set()
    for c in cues:
        if c['cls'] == 'title' and (' ' + c['cue'] + ' ') in t:
            out.add(c['value'])
    for w, v in EN_TITLES.items():
        if (' ' + w + ' ') in t:
            out.add(v)
    return out


# General English office vocabulary for Wikidata labels (not a control's values; a fixed list of ranks).
EN_TITLES = {'king': 'king', 'queen': 'queen', 'emperor': 'emperor', 'empress': 'emperor', 'duke': 'duke',
             'duchess': 'duke', 'count': 'count', 'countess': 'count', 'prince': 'prince', 'princess': 'prince',
             'elector': 'elector', 'landgrave': 'landgrave', 'margrave': 'margrave', 'palatine': 'palatine',
             'bishop': 'bishop', 'archbishop': 'bishop', 'cardinal': 'cardinal', 'pope': 'pope', 'stadtholder':
             'governor', 'governor': 'governor', 'regent': 'governor', 'ambassador': 'ambassador', 'chancellor':
             'chancellor', 'admiral': 'admiral', 'baron': 'baron', 'lord': 'lord', 'marquis': 'marquis'}


def build_pool(egos, wd, index_kept, cues, key_offices=True, lang=None):
    cands = []
    if wd is not None:
        cands += pool_from_wikidata(wd, egos)
    title_words = [c['cue'] for c in cues if c['cls'] == 'title']
    stop = {c['cue'] for c in cues} | STOP_COMMON
    for e in index_kept:
        t = e['text']
        for p, n in titled_phrases(t, title_words).items():
            cands.append(dict(id='index:' + fold(p), label=p, type='person', titles=title_classes(p, cues),
                              source='index:' + os.path.relpath(e['path'], ROOT)))
        for w, n in list(h41_surnames(t).items()) + list(proper_names(t, stop=stop).items()):
            cands.append(dict(id='index:' + fold(w), label=w, type='', source='index:' + os.path.relpath(e['path'], ROOT)))
    if key_offices:
        p = os.path.join(ROOT, 'KEY-OFFICES.tsv')
        if os.path.exists(p):
            for r in csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'):
                for nm in re.split(r';\s*', r.get('correspondents', '')):
                    nm = re.sub(r'\(.*?\)', '', nm).strip()
                    if 3 <= len(nm) <= 60:
                        cands.append(dict(id='keyoffices:' + fold(nm), label=nm, type='person',
                                          titles=title_classes(nm, cues), source='KEY-OFFICES.tsv'))
    # merge by fold of label; Wikidata entries absorb index entries with a matching alias
    merged, by_fold = [], {}
    for c in cands:
        c = dict(c)
        for k in ('aliases', 'relations', 'titles', 'offices'):
            v = c.get(k, set())
            c[k] = set(v.split('|')) - {''} if isinstance(v, str) else set(v)
        keys = {fold(x) for x in [c['label']] + list(c['aliases']) if fold(x)}
        hit = next((by_fold[k] for k in keys if k in by_fold), None)
        if hit is None:
            merged.append(c)
            for k in keys:
                by_fold[k] = c
            continue
        for k in ('aliases', 'relations', 'titles', 'offices'):
            hit[k] |= c[k]
        hit['aliases'].add(c['label'])
        hit['aliases'].discard(hit['label'])
        for k in ('born', 'died', 'gender'):
            hit[k] = hit.get(k) or c.get(k, '')
        hit['type'] = hit.get('type') or c.get('type', '')
        if c['source'] not in hit['source'].split(';'):
            hit['source'] = (hit['source'] + ';' + c['source'])[:300]
        for k in keys:
            by_fold.setdefault(k, hit)
    for c in merged:
        if not c['titles']:
            c['titles'] = title_classes(' '.join([c['label']] + sorted(c['aliases']) + sorted(c['offices'])), cues)
    rows = sorted((norm_cand(c) for c in merged if fold(c['label'])), key=lambda r: (r['type'], r['id']))
    return rows


STOP_COMMON = set('''monsieur monseigneur madame majeste majesté seigneur sire dieu messieurs excellence altesse
lettre lettres herr herrn gott euer eure ewer ewre item datum nota postscript''' .split())


def write_pool(rows, path):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\t'.join(POOL_COLS) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[k]).replace('\t', ' ').replace('\n', ' ') for k in POOL_COLS) + '\n')
    return sha256(path)


def read_pool(path):
    return [dict((k, r.get(k, '') or '') for k in POOL_COLS) for r in csv.DictReader(open(path, encoding='utf-8'),
                                                                                    delimiter='\t')]


# ------------------------------------------------------------------ scoring

def alive_at(c, d):
    if c['type'] != 'person' or not d:
        return 0.0, ''
    b, x = date_key(c['born']), date_key(c['died'])
    if x and x < d:
        return -3.0, f'died {c["died"]}'
    if b and b > d:
        return -3.0, f'born {c["born"]}'
    return (0.5, 'alive') if (b or x) else (0.0, 'life dates unknown')


def office_spans(c):
    out = []
    for o in c['offices'].split('|'):
        if not o:
            continue
        nm, _, span = o.partition('@')
        s, _, e = span.partition('/')
        out.append((nm, date_key(s), date_key(e)))
    return out


def comention_counts(pool, index_kept, d):
    """Weighted mentions of each candidate's names in the unmasked edition text (weights by date proximity)."""
    out = {}
    folded = []
    for e in index_kept:
        y = year(e.get('date', ''))
        w = 1.0 if (d is None or y is None or abs(y - d[0]) <= 1) else (0.5 if abs(y - d[0]) <= 3 else 0.2)
        folded.append((w, Counter(fold(x) for x in re.findall(r"[A-Za-zÀ-ÿ]{3,}", e['text']))))
    for c in pool:
        names = {fold(n) for n in cand_names(c) if len(fold(n)) >= 4}
        names |= {fold(n.split()[-1]) for n in cand_names(c) if ' ' in n and len(fold(n.split()[-1])) >= 5}
        out[c['id']] = sum(w * sum(cnt[n] for n in names) for w, cnt in folded)
    return out


def score_context(c, hits, d):
    """Per-context feature values for candidate c given the cue hits of one context."""
    f = dict(relation=0.0, office=0.0, gender=0.0, frame=0.0)
    ev = []
    rels = c['relations'].split('|') if c['relations'] else []
    titles = set(c['titles'].split('|')) - {''}
    poss = [h['value'] for h in hits if h['cls'] == 'poss']
    kin_pos, kin_neg = 0.0, 0.0
    for h in hits:
        if h['cls'] == 'kin':
            want, _, wg = h['value'].partition('/')
            whose = poss or ['sender', 'recipient']
            ok = [r for r in rels if r.split(':')[1] == want and r.split(':')[0] in whose
                  and not (wg and c['gender'] and c['gender'] != wg)]
            if ok:
                kin_pos = max(kin_pos, 2.0 * h['weight'])
                ev.append(f'kin {h["cue"]}->{ok[0]}')
            elif c['type'] == 'person':
                kin_neg = min(kin_neg, -1.0 if not rels else -0.5)
            elif c['type'] == 'place':
                kin_neg = min(kin_neg, -1.0)
        elif h['cls'] == 'title':
            if h['value'] in titles:
                held = [o for o in office_spans(c) if h['value'] in title_classes(o[0], [])
                        and (o[1] is None or o[1] <= d) and (o[2] is None or d is None or o[2] >= d)]
                f['office'] = max(f['office'], (1.5 if held else 1.0) * h['weight'])
                ev.append(f'title {h["cue"]}' + (' held at date' if held else ''))
        elif h['cls'] == 'gender':
            if c['gender'] and c['gender'] != h['value'] and c['type'] == 'person':
                f['gender'] = -1.0
            elif c['gender'] == h['value']:
                f['gender'] = max(f['gender'], 0.5)
        elif h['cls'] in ('place', 'person'):
            if not c['type']:
                continue
            f['frame'] += (1.0 if c['type'] == h['cls'] else -1.0) * h['weight'] / (1 + h['dist'])
    f['relation'] = kin_pos if kin_pos > 0 else kin_neg
    f['frame'] = max(-2.0, min(2.0, f['frame']))
    return f, ev


def score_pool(pool, ctxs, cues, d, comention, assigned, nocue_flag=True):
    hits_per = [cue_hits(x, cues) for x in ctxs]
    any_cue = any(h for hs in hits_per for h in hs if h['cls'] in ('kin', 'title', 'place', 'person'))
    out = []
    for c in pool:
        per = [score_context(c, hs, d) for hs in hits_per]
        ctx_vals = [sum(f.values()) for f, _ in per]
        mean_ctx = sum(ctx_vals) / len(ctx_vals) if ctx_vals else 0.0
        contra = sum(1 for v in ctx_vals if v < 0) if any(v > 0 for v in ctx_vals) else 0
        a, aev = alive_at(c, d)
        cm = math.log1p(comention.get(c['id'], 0.0))
        pen = -1.5 if any(alias_match(n, v) for n in cand_names(c) for v in assigned) else 0.0
        feats = dict(context=round(mean_ctx, 3), contradictions=contra, alive=a, comention=round(cm, 3),
                     assigned=pen)
        sc = mean_ctx - 0.75 * contra + a + 0.5 * cm + pen
        ev = sorted({e for _, es in per for e in es})
        if aev:
            ev.append(aev)
        if not any_cue and nocue_flag:
            ev.append(NOCUE)
        out.append(dict(c, score=round(sc, 4), feats=feats, evidence='; '.join(ev),
                        fit=f'{sum(1 for v in ctx_vals if v > 0)}/{len(ctx_vals)}'))
    out.sort(key=lambda r: (-r['score'], r['label']))
    return out, any_cue


def truth_rank(ranked, truth):
    if not truth:
        return None
    al = [t for t in truth.split('|') if t]
    for i, r in enumerate(ranked):
        if any(alias_match(n, t) for n in cand_names(r) for t in al):
            return i + 1, r
    return None


def assigned_values(target, code):
    """Values assigned to OTHER codes (names.tsv, key*.tsv) -- a penalty feature, never a pool source."""
    vals = set()
    for p in glob.glob(os.path.join(target, 'names.tsv')) + glob.glob(os.path.join(target, 'key*.tsv')):
        for l in open(p, encoding='utf-8', errors='replace'):
            q = l.rstrip('\n').split('\t')
            if len(q) >= 2 and q[0] != code and q[0] != 'code' and not q[0].startswith('#'):
                v = q[1].split('(')[0].strip()
                if len(fold(v)) >= 4 and v not in ('NULL',):
                    vals.add(v)
    return vals


# ------------------------------------------------------------------ nulls

def context_null(pool, ctxs_by_code, code, n, cues, d, comention, assigned, truth, draws, seed):
    """Re-score on the contexts of random other codes with a matched occurrence count."""
    rng = random.Random(seed)
    others = [c for c, xs in ctxs_by_code.items() if c != code and len(xs) >= max(1, n)]
    if not others:
        return None
    scores, ranks = [], []
    top_label = None
    for _ in range(draws):
        oc = rng.choice(others)
        xs = rng.sample(ctxs_by_code[oc], max(1, n))
        ranked, _ = score_pool(pool, xs, cues, d, comention, assigned, nocue_flag=False)
        if truth:
            tr = truth_rank(ranked, truth)
            if tr:
                ranks.append(tr[0]); scores.append(tr[1]['score'])
        else:
            scores.append(ranked[0]['score'])
    scores.sort()
    p95 = scores[int(0.95 * (len(scores) - 1))] if scores else None
    return dict(draws=draws, p95_score=p95, median_rank=(sorted(ranks)[len(ranks) // 2] if ranks else None),
                top5_share=(sum(1 for r in ranks if r <= 5) / len(ranks) if ranks else None))


def decoy_null(pool, ctxs, cues, d, comention, assigned, index_kept, ref_score, draws, seed):
    """Promoted from NEVBIR-NAMES (match_names.py, 3 Oct 2026): random words of the pool's name lengths enter as decoys."""
    rng = random.Random(seed + 1)
    vocab = sorted({w for e in index_kept for w in re.findall(r"[A-Za-zÀ-ÿ]{4,16}", e['text'])})
    if not vocab or ref_score is None:
        return None
    lens = [len(c['label']) for c in pool] or [6]
    by_len = defaultdict(list)
    for w in vocab:
        by_len[len(w)].append(w)
    beat = 0
    for _ in range(draws):
        L = rng.choice(lens)
        opts = by_len.get(L) or vocab
        w = rng.choice(opts)
        typ = rng.choice(pool)['type'] if pool else ''
        dec = norm_cand(dict(id='decoy:' + w, label=w, type=typ, source='decoy'))
        cm = dict(comention)
        cm.update(comention_counts([dec], index_kept, d))
        ranked, _ = score_pool([dec], ctxs, cues, d, cm, assigned, nocue_flag=False)
        if ranked[0]['score'] > ref_score:
            beat += 1
    return dict(draws=draws, decoy_beat_share=beat / draws)


# ------------------------------------------------------------------ find-controls

def find_controls(min_codes=8, use_mdblocks=True):
    """Scan ciphers/* for sets of >= min_codes distinct H/C-graded whole-name codes (person/place) in decoded context.
    Sources: names.tsv, key*.tsv (multi-letter values, grade H/C, value capitalised or multiword or in a names file),
    reading_tokens*.tsv (multi-letter H/C values next to other decoded tokens), and md-blocks folders through
    tools/holder_export.py's loader (read-only import). Returns rows (folder, codes, n_codes, sources)."""
    rows = []
    md = None
    if use_mdblocks:
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location('holder_export', os.path.join(HERE, 'holder_export.py'))
            md = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(md)
        except Exception as e:  # pragma: no cover
            print(f'name_candidates: md-blocks loader unavailable ({e}); scope excludes md-blocks folders',
                  file=sys.stderr)
            md = None
    for folder in sorted(glob.glob(os.path.join(ROOT, 'ciphers', '*'))):
        if not os.path.isdir(folder):
            continue
        codes, srcs = {}, set()
        for p in glob.glob(os.path.join(folder, 'names.tsv')):
            for r in csv.reader(open(p, encoding='utf-8', errors='replace'), delimiter='\t'):
                if len(r) > 6 and r[6] in ('H', 'C') and len(fold(r[1])) >= 3 and r[1] != 'NULL':
                    codes[r[0]] = r[1]; srcs.add('names.tsv')
        for p in glob.glob(os.path.join(folder, 'reading_*tokens*.tsv')):
            try:
                rd = list(csv.DictReader(open(p, encoding='utf-8', errors='replace'), delimiter='\t'))
            except Exception:
                continue
            for r in rd:
                v, g, s = (r.get('value') or ''), (r.get('grade') or ''), (r.get('sign') or '')
                if g in ('H', 'C') and NAMEISH(v) and s and not s.startswith('='):
                    codes.setdefault(s, v.lstrip('=')); srcs.add(os.path.basename(p))
        if md is not None and glob.glob(os.path.join(folder, 'reading*.md')):
            try:
                from pathlib import Path
                mb = md.MdBlocks(Path(folder))
                for iid in mb.items:
                    for _, w, meaning, g, kind in mb.tokens(iid):
                        if kind == 'word' and g in ('H', 'C') and NAMEISH(meaning):
                            codes.setdefault(w, meaning); srcs.add('md-blocks')
            except Exception as e:
                print(f'name_candidates: md-blocks {os.path.basename(folder)} unreadable ({e})', file=sys.stderr)
        if len(codes) >= min_codes:
            rows.append(dict(folder=os.path.relpath(folder, ROOT), n_codes=len(codes),
                             codes=';'.join(f'{k}={v}' for k, v in sorted(codes.items())[:40]), sources=','.join(sorted(srcs))))
    return rows


def NAMEISH(v):
    v = (v or '').lstrip('=')
    return len(v) >= 4 and (v[:1].isupper() or ' ' in v)


# ------------------------------------------------------------------ main

def run(a):
    target = a.target if os.path.isabs(a.target) else os.path.join(ROOT, a.target)
    code = a.code
    cues = load_cues(a.lang, a.cues)
    mask = {x for m in (a.mask_letters or []) for x in re.split(r'[,; ]+', m) if x}
    d = date_key(a.date)
    # contexts (all codes, for the context null)
    by_code = defaultdict(list)
    for cfg in a.config or []:
        for c, xs in contexts_from_config(target, cfg, code, a.width, all_codes=True).items():
            by_code[c] += xs
    for p in a.contexts or []:
        for x in contexts_from_tsv(p):
            by_code[x.get('code') or code].append(x)
    if a.mdblocks:
        for c, xs in contexts_from_mdblocks(target, width=a.width).items():
            by_code[c] += xs
    ctxs = by_code.get(code, [])
    if a.subsample:
        ctxs = random.Random(a.seed).sample(ctxs, min(a.subsample, len(ctxs)))
    index_kept, index_masked = load_index(a.index, mask)
    # pool, frozen before scoring
    if a.pool:
        pool = read_pool(a.pool)
        pool_sha = sha256(a.pool)
    else:
        wd = Wikidata(offline=a.offline) if a.wikidata else None
        egos = {}
        if wd:
            egos = {'sender': wd_resolve(wd, a.sender), 'recipient': wd_resolve(wd, a.recipient)}
        pool = build_pool(egos, wd, index_kept, cues, lang=a.lang)
        out = a.freeze_pool or os.path.join(ROOT, 'tools', 'tests', f'_pool_{code}.tsv')
        pool_sha = write_pool(pool, out)
        print(f'pool frozen: {os.path.relpath(out, ROOT)} {len(pool)} candidates sha256 {pool_sha}', file=sys.stderr)
        if wd:
            print(f'wikidata requests this run: {wd.n}' + (f' (stopped: {wd.stopped})' if wd.stopped else ''),
                  file=sys.stderr)
        if a.freeze_only:
            return dict(pool_sha=pool_sha, pool=len(pool))
    comention = comention_counts(pool, index_kept, d)
    assigned = assigned_values(target, code)
    ranked, any_cue = score_pool(pool, ctxs, cues, d, comention, assigned)
    tr = truth_rank(ranked, a.truth)
    coverage = None
    if a.truth:
        al = [t for t in a.truth.split('|') if t]
        coverage = any(alias_match(n, t) for c in pool for n in cand_names(c) for t in al)
    ref = tr[1]['score'] if tr else (ranked[0]['score'] if ranked else None)
    cnull = context_null(pool, by_code, code, len(ctxs), cues, d, comention, assigned, a.truth, a.nulls, a.seed) \
        if a.nulls else None
    dnull = decoy_null(pool, ctxs, cues, d, comention, assigned, index_kept, ref, a.nulls, a.seed) if a.nulls else None
    summary = dict(code=code, n_contexts=len(ctxs), pool=len(pool), pool_sha256=pool_sha, any_cue=any_cue,
                   masked_index=[os.path.relpath(e['path'], ROOT) for e in index_masked],
                   coverage=coverage, truth_rank=(tr[0] if tr else None), truth_score=(tr[1]['score'] if tr else None),
                   truth_label=(tr[1]['label'] if tr else None), top=[r['label'] for r in ranked[:a.top]],
                   context_null=cnull, decoy_null=dnull,
                   beats_null_p95=(None if not (tr and cnull and cnull['p95_score'] is not None)
                                   else tr[1]['score'] > cnull['p95_score']))
    if a.out:
        os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(f'# name_candidates.py {code}: proposals only (grade M at most); test with decode_key.py --try; '
                    f'pool sha256 {pool_sha}; contexts {len(ctxs)}{"" if any_cue else "; " + NOCUE}\n')
            f.write('rank\tcandidate\tsource\ttype\tcontext\tcontradictions\talive\tcomention\tassigned\tfit\tscore\t'
                    'grade\tevidence\n')
            for i, r in enumerate(ranked[:a.top]):
                ft = r['feats']
                grade = 'M' if (ft['context'] > 0) else 'I'
                f.write('\t'.join(str(x) for x in (i + 1, r['label'], r['source'], r['type'], ft['context'],
                                                    ft['contradictions'], ft['alive'], ft['comention'], ft['assigned'],
                                                    r['fit'], r['score'], grade, r['evidence'])) + '\n')
    return dict(summary=summary, ranked=ranked, contexts=ctxs)


def parser():
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('target', nargs='?')
    ap.add_argument('--code')
    ap.add_argument('--config', action='append', help='decode.json (repeatable); contexts from decode_key.graded_recs')
    ap.add_argument('--contexts', action='append', help='TSV: code, letter, date, line, left, right (repeatable)')
    ap.add_argument('--mdblocks', action='store_true', help='contexts from the folder\'s md-blocks readings')
    ap.add_argument('--sender', default='')
    ap.add_argument('--recipient', default='')
    ap.add_argument('--date', default='')
    ap.add_argument('--place', default='')
    ap.add_argument('--lang', default='fr')
    ap.add_argument('--cues', help='cue TSV (default tools/data/name_cues_<lang>.tsv)')
    ap.add_argument('--index', action='append', help='edition text file or manifest TSV (path, letters, date)')
    ap.add_argument('--pool', help='read a frozen pool TSV (no pool building)')
    ap.add_argument('--freeze-pool', help='write the built pool here and print its sha256')
    ap.add_argument('--freeze-only', action='store_true', help='build and freeze the pool, then stop (no scoring)')
    ap.add_argument('--wikidata', action='store_true', help='add Wikidata kin/offices/places (query.wikidata.org, cached)')
    ap.add_argument('--offline', action='store_true', help='Wikidata from the cache only')
    ap.add_argument('--mask-letters', action='append', help='letters whose printed text never enters (comma list)')
    ap.add_argument('--truth', help="known-answer aliases 'a|b' (controls only): report coverage and rank")
    ap.add_argument('--subsample', type=int, help='use only N random contexts (power check at the target count)')
    ap.add_argument('--width', type=int, default=8)
    ap.add_argument('--top', type=int, default=10)
    ap.add_argument('--nulls', type=int, default=200)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out')
    ap.add_argument('--json', action='store_true', help='print the summary as JSON')
    ap.add_argument('--find-controls', action='store_true')
    ap.add_argument('--min', type=int, default=8)
    return ap


def main(argv=None):
    ap = parser()
    a = ap.parse_args(argv)
    if a.find_controls:
        rows = find_controls(a.min)
        print('folder\tn_codes\tsources\tcodes')
        for r in rows:
            print(f'{r["folder"]}\t{r["n_codes"]}\t{r["sources"]}\t{r["codes"]}')
        return 0
    if not (a.target and a.code):
        ap.error('target and --code are required (or --find-controls)')
    res = run(a)
    if a.freeze_only:
        print(json.dumps(res))
        return 0
    s = res['summary']
    if a.json:
        print(json.dumps(s, ensure_ascii=False))
    else:
        print(f'code {s["code"]}: {s["n_contexts"]} contexts, pool {s["pool"]} (sha256 {s["pool_sha256"][:12]}), '
              f'{"cues found" if s["any_cue"] else NOCUE}')
        for i, r in enumerate(res['ranked'][:a.top]):
            print(f'  {i + 1:>2} {r["score"]:>7.3f} {r["label"][:40]:<40} {r["type"]:<6} fit {r["fit"]} {r["evidence"][:80]}')
        if a.truth:
            print(f'  truth: coverage {s["coverage"]}, rank {s["truth_rank"]}, score {s["truth_score"]}, '
                  f'context-null p95 {s["context_null"] and s["context_null"]["p95_score"]}, beats p95 {s["beats_null_p95"]}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
