#!/usr/bin/env python3
"""FT4x post hoc 3 (NOT registered): f.252r group 1 read as its flagged alternative 233 instead of 253; where 213/248/369 sit in S1."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4x_pool as P
import ft4v_pair as fv
B, _ = P.blocks()
s1t, s1x = B['S1']
gt, gw = fv.load('primary'); gx = ''.join(gw)
print('233 in S1:', s1t.count('233'), '; S1 positions 369/213/248:', [(c, [i for i, t in enumerate(s1t) if t == c]) for c in ('369', '213', '248')])
t = ['233' if x == '253' else x for x in gt]
print('alt 233: J', P.J(P.pooled([B['S1']], t, gx) + (None,)))
for c in ('213', '248', '369'):
    t2 = [x + 'x' if x == c else x for x in t]
    print(f'alt 233 + drop {c}: J', P.J(P.pooled([B['S1']], t2, gx) + (None,)))
