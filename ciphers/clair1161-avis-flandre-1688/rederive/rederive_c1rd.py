#!/usr/bin/env python3
"""NEAR3-C1RD (4 Oct 2026): independent rule-7 re-derivation for clair1161-avis-flandre-1688.
Reads ciphertext.tsv + key.tsv only. Clear words ([PLAIN:..]) and '/' are not cipher tokens (spec).
Output: rederive_c1rd.txt, one line per cipher token: line pos sign value grade  ('?' = unkeyed, grade U).
Grade: key row's grade (S/C); M when transcription conf is M; U when unkeyed."""
import csv, os, sys
here = os.path.dirname(os.path.abspath(__file__)); d = os.path.dirname(here)
key = {r['sign']: r for r in csv.DictReader(open(f'{d}/key.tsv'), delimiter='\t')}
out = []
for r in csv.DictReader(open(f'{d}/ciphertext.tsv'), delimiter='\t'):
    s = r['sign']
    if s == '/' or s.startswith('[PLAIN:'):
        continue
    k = key.get(s)
    if k is None:
        v, g = '?', 'U'
    else:
        v, g = k['value'], k['grade']
        if r['conf'] != 'H':
            g = 'M'
    out.append(f"{r['line']}\t{r['pos']}\t{s}\t{v}\t{g}")
open(f'{here}/rederive_c1rd.txt', 'w').write('\n'.join(out) + '\n')
from collections import Counter
print(len(out), dict(Counter(l.split('\t')[4] for l in out)))
