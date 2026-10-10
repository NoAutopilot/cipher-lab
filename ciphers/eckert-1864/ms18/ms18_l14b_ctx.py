#!/usr/bin/env python3
"""L14-B: context windows around the phrase hits of ms18_l14b_print.py (volume, nearest preceding date heading, 700 chars)."""
import gzip, os, re, sys
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
def win(vol, pat, n=1, w=650):
    t = re.sub(r'\s+', ' ', gzip.open(f'{D}/{vol}_djvu.txt.gz', 'rt', errors='ignore').read())
    for m in list(re.finditer(pat, t, flags=re.I))[:n]:
        print(f'--- {vol} /{pat}/ @{m.start()}\n', t[max(0, m.start()-w):m.end()+w], '\n')
for a in sys.argv[1:]:
    v, p = a.split('::', 1); win(v, p)
