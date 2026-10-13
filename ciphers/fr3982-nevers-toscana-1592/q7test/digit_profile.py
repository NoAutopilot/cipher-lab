#!/usr/bin/env python3
"""BNF-Q7-TEST diagnostic (not pre-registered, not a gate): digit histogram of f.25 vs 100 synthetic no.62
encipherments (structural_control.py's generator, 0% error), and the leftover contexts of f.25's best parse."""
import random, collections, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from structural import load_codes, load_ct
from structural_control import windows, words_map
ct = load_ct().replace('?', ''); rng = random.Random(62)
syn = windows(rng, 100, len(ct), words_map())
tc = collections.Counter(ct)
print('digit target  synthetic mean [min-max] over 100')
for d in '0123456789':
    v = [s.count(d) for s in syn]
    print(f'{d}  {tc[d]:4d}  {sum(v)/len(v):6.1f} [{min(v)}-{max(v)}]')
codes = set(load_codes()); n = len(ct); best = [(0, None)]*(n+1)
for i in range(n-1, -1, -1):
    b = (best[i+1][0], None)
    for L in (1,2,3):
        if i+L <= n and ct[i:i+L] in codes and L+best[i+L][0] > b[0]: b = (L+best[i+L][0], L)
    best[i] = b
i = 0; left = collections.Counter(); ctx = []
while i < n:
    L = best[i][1]
    if L is None: left[ct[i]] += 1; ctx.append(ct[max(0,i-2):i+3]); i += 1
    else: i += L
print('leftover digits in best parse:', dict(left), 'total', sum(left.values()))
print('leftover contexts (2 before, 2 after):', ' '.join(ctx[:40]))
