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

Usage:
  python3 tools/bnf_findingaid.py --cote "Français 3251" --save-html DIR      # search + fetch + TSV to stdout
  python3 tools/bnf_findingaid.py --ark cc49712p --save-html DIR             # skip the search
  python3 tools/bnf_findingaid.py --html saved.html                          # offline parse only
"""
import argparse, html as H, os, re, subprocess, sys, time

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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--cote')
    g.add_argument('--ark')
    g.add_argument('--html')
    ap.add_argument('--save-html', help='directory to keep the fetched notice (fetch once, read from disk after)')
    a = ap.parse_args()
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
