#!/usr/bin/env python3
"""FT4o (account-4, 3 Oct 2026): locate what the f.206 pin 722 = ti forces in f.213 (pre-registered, PREREG-FT4o.md).

Model: gate_pair.Scorer.consistent (exact coverage of the f.214r slip, MAXLEN 12, every free repeated code one chunk),
pins 22 de / 501 et / 722 ti (pooled_gate3.PINS present in f.213), group 73 already dropped (FT4m's edit 1).
Scan (edit 2, one per run): for each remaining group index i, (D) drop i (zero letters) and (R) release i (rename the
occurrence to a unique free code: a misread digit, a polyvalent use or a code outside the key, 1..12 letters).
A run is FIT / NOFIT / TIMEOUT (--limit s). Output: one row per (i, edit).
Known-answer control (--control): the f.206 passage, which fits all ten pins, gets one injected error (a group
overwritten with a copy of another code in the passage, seeded); kept only if the injection makes it inconsistent;
the same R and D scans are run; reported: is the injected index in the FIT set, and the FIT-set size.
  python3 ft4o_scan.py [--limit 6] [--lo 0 --hi 83]
  python3 ft4o_scan.py --control --seed 1 --n 3
"""
import argparse, os, random, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
import pooled_gate3 as pg
T = pg.T


def run(sc, A, pins, lim):
    r = sc.consistent(A, pins, time.time() + lim)
    return 'TIMEOUT' if r is None else ('FIT' if r else 'NOFIT')


def scan(sc, A, pins, lim, lo, hi, out):
    for i in range(lo, min(hi, len(A))):
        for e in 'DR':
            B = A[:i] + A[i + 1:] if e == 'D' else A[:i] + [f'R{i}'] + A[i + 1:]
            p = {k: v for k, v in pins.items() if k in B}
            t0 = time.time()
            r = run(sc, B, p, lim)
            out(f'{i}\t{A[i]}\t{e}\t{r}\t{time.time()-t0:.1f}')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=float, default=6)
    ap.add_argument('--lo', type=int, default=0)
    ap.add_argument('--hi', type=int, default=999)
    ap.add_argument('--control', action='store_true')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--n', type=int, default=3)
    a = ap.parse_args()
    pr = lambda s: print(s, flush=True)
    if not a.control:
        c, s, m = pg.PAIR3['f213']
        A, t = g.load(os.path.join(T, c), os.path.join(T, s))
        A = [x for i, x in enumerate(A) if i != 73]
        pins = {k: v for k, v in pg.PINS.items() if k in A and k in ('22', '501', '722')}
        sc = g.Scorer(t, m)
        pr(f'# f213 minus g73: {len(A)} groups, {len(t)} letters, pins {pins}; base {run(sc, A, pins, 60)}')
        pr('# idx(after drop 73; idx>=73 is original idx+1)\tcode\tedit\tresult\tsec')
        scan(sc, A, pins, a.limit, a.lo, a.hi, pr)
        return
    c, s, m = pg.FILES[0]
    A0, t = g.load(os.path.join(T, c), os.path.join(T, s))
    pins = {k: v for k, v in pg.PINS.items() if k in A0}
    sc = g.Scorer(t, m)
    rng = random.Random(a.seed)
    pr(f'# control f206: {len(A0)} groups, pins {sorted(pins)}; base {run(sc, A0, pins, 60)}')
    done = 0
    while done < a.n:
        i, j = rng.randrange(len(A0)), rng.randrange(len(A0))
        if A0[i] == A0[j]:
            continue
        A = A0[:i] + [A0[j]] + A0[i + 1:]
        p = {k: v for k, v in pins.items() if k in A}
        if run(sc, A, p, 30) != 'NOFIT':
            pr(f'# injection {i}<-{A0[j]} skipped (still fits or timed out)')
            continue
        rows = []
        scan(sc, A, p, a.limit, 0, len(A), rows.append)
        fits = sorted({int(r.split('\t')[0]) for r in rows if r.split('\t')[3] == 'FIT'})
        to = sum(1 for r in rows if r.split('\t')[3] == 'TIMEOUT')
        pr(f'injection {done}: idx {i} ({A0[i]} -> {A0[j]}): FIT idx {fits}; injected in set {i in fits}; set size {len(fits)}; timeouts {to}')
        done += 1


if __name__ == '__main__':
    main()
