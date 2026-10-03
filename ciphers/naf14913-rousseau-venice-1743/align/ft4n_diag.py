#!/usr/bin/env python3
"""FT4n post-hoc diagnostic (NOT part of the registered gate): is each passage of pooled_gate3 --pair3 f213 --drop 73
internally consistent with the pins (every repeated code one chunk within its passage), given a long time limit?
Separates 'real Hp 0 because the real search timed out' from 'real Hp 0 because a passage has no consistent fit'."""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
import pooled_gate3 as pg
T = pg.T
lim = float(sys.argv[1]) if len(sys.argv) > 1 else 300
for name, (c, s, m), drop in [('f206', pg.FILES[0], []), ('f216v', pg.FILES[1], []), ('f213-drop73', pg.PAIR3['f213'], [73]),
                              ('f213-full', pg.PAIR3['f213'], [])]:
    A, t = g.load(os.path.join(T, c), os.path.join(T, s))
    A = [x for i, x in enumerate(A) if i not in set(drop)]
    pins = {k: v for k, v in pg.PINS.items() if k in A}
    sc = g.Scorer(t, m)
    t0 = time.time()
    f = sc.feasible(A, pins)
    r = sc.consistent(A, pins, time.time() + lim)
    print(f'{name}: groups {len(A)} letters {len(t)} pins {sorted(pins)} feasible(pins) {f} consistent(pins) {r} ({time.time()-t0:.1f}s, limit {lim})', flush=True)
