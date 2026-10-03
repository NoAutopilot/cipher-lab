#!/usr/bin/env python3
"""FT4h copy of f249_diag.py for the f.213/f.214r pair. FT4e (account-4, 3 Oct 2026) diagnostic, NOT a gate: is the f.249r-v / f.250 pair, as transcribed, fittable at all
under the exact-coverage + repeated-code-consistency model of gate_pair.py? Run after the registered gate_pair.py run
returned H = 0. (1) consistency with the f.206 pins, (2) with no pins, (3) for each repeated code, the same no-pin test
with that one code's occurrences made distinct (which single code's consistency the infeasibility rests on).
  python3 f249_diag.py   (about 2-3 minutes, 4 processes)
"""
import os, sys, time
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A, t = g.load(os.path.join(T, 'ciphertext_f213.txt'), os.path.join(T, 'slip_f214r.txt'))


def job(c):
    B, k = [], 0
    for x in A:
        if x == c:
            B.append(f'{x}_{k}'); k += 1
        else:
            B.append(x)
    t0 = time.time()
    return c, g.Scorer(t, 12).consistent(B, {}, time.time() + 40), round(time.time() - t0, 1)


if __name__ == '__main__':
    sc = g.Scorer(t, 12)
    pm = {c: v for c, v in g.PINS.items() if c in A}
    print('all pins present', pm, '-> consistent:', sc.consistent(A, pm, time.time() + 60))
    print('no pins -> consistent:', sc.consistent(A, {}, time.time() + 60), '(True / False proved / None timed out)')
    rep = [c for c, n in Counter(A).items() if n > 1]
    with Pool(4) as p:
        for c, r, s in sorted(p.map(job, rep), key=lambda z: int(z[0])):
            print(f'  {c} x{Counter(A)[c]} made distinct -> {r} ({s} s)')
