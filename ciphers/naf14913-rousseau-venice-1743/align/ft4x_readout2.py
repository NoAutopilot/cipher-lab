#!/usr/bin/env python3
"""FT4x post hoc 2 (NOT registered): drop 253 plus one more shared code; 253's exact-feasible chunks in S1 vs in f.252r."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4x_pool as P
import ft4v_pair as fv
B, _ = P.blocks()
s1 = [B['S1']]
gt, gw = fv.load('primary'); gx = ''.join(gw)
sh = sorted(set(gt) & set(B['S1'][0]))
for c in [x for x in sh if x != '253']:
    t = [x + 'x' if x in ('253', c) else x for x in gt]
    print(f'post hoc drop 253+{c}: J {P.J(P.pooled(s1, t, gx) + (None,))}', flush=True)
s1t, s1x = B['S1']
f_s1 = sorted({s1x[p:p + l] for l in range(1, 13) for p in range(len(s1x) - l + 1)
               if s1x[p:p + l] in gx and P.solve_exact(s1t, s1x, dict(P.PINS, **{'253': s1x[p:p + l]}), 30) is not False})
print('253 chunks feasible in S1 alone that are also gloss substrings:', f_s1)
f_g = sorted({gx[p:p + l] for l in range(1, 13) for p in range(len(gx) - l + 1)
              if P.solve_exact(gt, gx, dict(P.PINS, **{'253': gx[p:p + l]}), 30) is not False})
print('253 chunks feasible in f252r alone:', f_g)
