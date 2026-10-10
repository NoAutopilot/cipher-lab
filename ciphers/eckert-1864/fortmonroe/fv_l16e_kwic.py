#!/usr/bin/env python3
"""FV-L16e KWIC with nearest running-head page numbers: fv_l16e_kwic.py VOL 'word word ...' [width] [max]"""
import gzip, re, sys
v, phrase = sys.argv[1], sys.argv[2]
w = int(sys.argv[3]) if len(sys.argv) > 3 else 600
mx = int(sys.argv[4]) if len(sys.argv) > 4 else 4
t = gzip.open(f'sources/ia-fulltext/print-check/{v}_djvu.txt.gz', 'rt', errors='ignore').read()
pat = r'\W+'.join(map(re.escape, phrase.split()))
for m in list(re.finditer(pat, t, re.I))[:mx]:
    before = t[:m.start()]
    heads = re.findall(r'\n\s*(\d{1,4})\s+[A-Z][A-Z .,]{8,}\n|\n[A-Z][A-Z .,;]{8,}\s(\d{1,4})\s*\n', before[-40000:])
    pg = [a or b for a, b in heads][-2:]
    print(f'## {v} | {phrase} | running heads before: {pg}')
    print(re.sub(r'\n\s*\n+', '\n', t[max(0, m.start()-w):m.end()+w])); print()
