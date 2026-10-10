#!/usr/bin/env python3
"""AUD2-LEDGER16-3 (10 Oct 2026): KWIC over cached IA djvu texts (sources/ia-fulltext/print-check) for the second audit of eckert-1864
E558 E564 E569 E574. Usage: aud2_l16_3_print.py ID[,ID] 'regex' [width]. Prints each hit with a window and the nearest running-head page
number before it. A miss is a search result under these words, not a statement about print (rule 10)."""
import gzip, re, sys, os
D = 'sources/ia-fulltext/print-check'
ids, pat = sys.argv[1].split(','), re.compile(sys.argv[2], re.I | re.S)
w = int(sys.argv[3]) if len(sys.argv) > 3 else 300
for i in ids:
    p = os.path.join(D, i + '_djvu.txt.gz')
    if not os.path.exists(p): print(i, 'NOT ON DISK'); continue
    t = gzip.open(p, 'rt', errors='replace').read()
    hits = list(pat.finditer(t))
    print(f'== {i}: {len(hits)} hits')
    for m in hits[:40]:
        pre = t[max(0, m.start() - 6000):m.start()]
        pg = re.findall(r'\n\s*(\d{2,4})\s+[A-Z][A-Z .,]{4,}\n|\n[A-Z][A-Z .,]{4,}\s+(\d{2,4})\s*\n', pre)
        pg = [a or b for a, b in pg][-1:] or ['?']
        print(f'  [p~{pg[0]}]', ' '.join(t[max(0, m.start() - w):m.end() + w].split()))
