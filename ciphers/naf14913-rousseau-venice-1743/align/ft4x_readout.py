#!/usr/bin/env python3
"""FT4x readouts after J_real nofit (PREREG-FT4x): (1) registered secondary: 'literal' and 'est' gloss texts, S1 + f.252r;
(2) post hoc, NOT registered: leave-one-shared-code-out (the f.252r token renamed so it no longer joins S1) and keep-one-only."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4x_pool as P
import ft4v_pair as fv
B, _ = P.blocks()
s1 = [B['S1']]
for which in ('primary', 'literal', 'est'):
    gt, gw = fv.load(which)
    print(f'secondary text {which}: J {P.J(P.pooled(s1, gt, "".join(gw)) + (None,))}', flush=True)
gt, gw = fv.load('primary'); gx = ''.join(gw)
sh = sorted(set(gt) & set(B['S1'][0]))
for c in sh:
    t = [x + 'x' if x == c else x for x in gt]
    print(f'post hoc drop {c}: J {P.J(P.pooled(s1, t, gx) + (None,))}', flush=True)
for c in sh:
    t = [x if x == c else x + 'x' for x in gt]
    print(f'post hoc only {c}: J {P.J(P.pooled(s1, t, gx) + (None,))}', flush=True)
