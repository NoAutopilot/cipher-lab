#!/usr/bin/env python3
"""FV-MS18g (9 Oct 2026): letters-only phrase grep for E347, E349, E350 over the
cached print-check texts (sources/ia-fulltext/print-check/*.gz) plus OR djvu texts
fetched to a scratch dir (argv[1]). Prints file, phrase, and a context window."""
import gzip, glob, os, re, sys
PH = {
 'E347': ['profoundsecret', 'haveyourcarput', 'fredericktrain', 'refreshments', 'wgwood', 'monocacythisafternoon', 'meetyourcar'],
 'E349': ['relievecolonelcrane', 'colonelcrane', 'disbursingofficerareincompatible', 'appointedinspector', 'longcipherdispatch', 'orwaityourarrival', 'atbaltimoreorwait'],
 'E350': ['burnethouse', 'plantershouse', 'serviceablehorsesthereforissue', 'redwoodprice', 'countermandstheorders', 'pleasontonsandgrierson', 'brackett'],
}
def texts(scratch):
    for f in sorted(glob.glob('sources/ia-fulltext/print-check/*.gz')):
        yield f, gzip.open(f, 'rt', errors='replace').read()
    for f in sorted(glob.glob(os.path.join(scratch, '*.txt'))):
        yield f, open(f, errors='replace').read()
seen = set()
for f, t in texts(sys.argv[1]):
    base = os.path.basename(f).split('_djvu')[0].replace('.txt', '')
    if base in seen: continue
    seen.add(base)
    idx = [i for i, c in enumerate(t) if c.isalpha()]
    s = ''.join(t[i] for i in idx).lower()
    for e, phs in PH.items():
        for p in phs:
            for m in re.finditer(p, s):
                a = idx[m.start()]
                print(f"{e}\t{p}\t{base}\t{' '.join(t[max(0,a-160):a+220].split())}")
print('volumes', len(seen), file=sys.stderr)
