#!/usr/bin/env python3
"""FT4aa (account-4, 3 Oct 2026): two-release scan on the f.206 joint conflicts (PREREG-FT4aa.md, pushed before any run).
Pair A = F206 + F216V, pair B = F206 + f.266r S1. Release = rename a code in the F206 block only. FT4x/FT4z exact CP-SAT
unchanged (ft4x_pool.solve_exact, ft4z_pool blocks/join), C pins 22/66/581, 722 and 121 free (primary), MAXLEN 12, 30 s.
  python3 ft4aa_scan.py --ctrl s|g --pair A|B     (40 draws, seed 3, partner perturbed, Pool(4))
  python3 ft4aa_scan.py --real [--pin121]
"""
import argparse, itertools, os, random, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
from ft4x_pool import solve_exact, PINS, LIMIT
import ft4z_pool as fz

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTNER = {'A': 'F216V', 'B': 'S1'}


def lab(r):
    return 'unresolved' if r is None else ('fit' if r else 'nofit')


def shared(A, t2):
    return sorted((set(A) & set(t2)) - set(PINS), key=int)


def solve_rel(A, ta, t2, x2, rel, pins):
    A2 = [t if t not in rel else 'R' + t for t in A]
    toks, text = fz.join([(A2, ta), (t2, x2)])
    return solve_exact(toks, text, pins, LIMIT)


def draw_stat(job):
    A, ta, t2, x2 = job
    sh = shared(A, t2)
    if solve_rel(A, ta, t2, x2, set(sh), PINS) is False:
        return 'neg(release-all nofit)'
    for k in (0, 1, 2):
        for rel in itertools.combinations(sh, k):
            r = solve_rel(A, ta, t2, x2, set(rel), PINS)
            if r is not False:
                return f'POS {k} {rel} {lab(r)}'
    return 'neg(specific)'


def f216v_words():
    w = []
    for l in open(os.path.join(T, 'slip_f217r.txt'), encoding='utf-8'):
        if not l.startswith('#'):
            w += [x for x in (g.letters(y) for y in l.split()) if x]
    return w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--pair', choices=['A', 'B'])
    ap.add_argument('--real', action='store_true')
    ap.add_argument('--pin121', action='store_true')
    a = ap.parse_args()
    B, sw = fz.blocks()
    A, ta = B['F206']
    if a.ctrl:
        t2, x2 = B[PARTNER[a.pair]]
        words = sw if a.pair == 'B' else f216v_words()
        assert ''.join(words) == x2, 'partner words do not rebuild the partner text'
        rng = random.Random(3)
        jobs = []
        for _ in range(40):
            if a.ctrl == 's':
                w = words[:]; rng.shuffle(w); jobs.append((A, ta, t2, ''.join(w)))
            else:
                t = t2[:]; rng.shuffle(t); jobs.append((A, ta, t, x2))
        with Pool(4) as pool:
            res = pool.map(draw_stat, jobs)
        for i, r in enumerate(res):
            print(f'draw {a.pair} {a.ctrl} {i} {r}')
        hi = sum(r.startswith('POS') for r in res)
        print(f'CONTROL pair {a.pair} ({a.ctrl}): positives {hi}/40 share {hi/40:.3f}')
        return
    pins = dict(PINS, **({'121': 's'} if a.pin121 else {}))
    for p in ('A', 'B'):
        t2, x2 = B[PARTNER[p]]
        sh = [c for c in shared(A, t2) if c not in pins]
        print(f'REAL pair {p} pins {sorted(pins)} shared {sh}', flush=True)
        print(f'  0-release: {lab(solve_rel(A, ta, t2, x2, set(), pins))}', flush=True)
        singles, unres = [], []
        for c in sh:
            r = solve_rel(A, ta, t2, x2, {c}, pins)
            if r is not False:
                singles.append(c)
            if r is None:
                unres.append((c,))
        pairs = []
        for c1, c2 in itertools.combinations(sh, 2):
            if c1 in singles or c2 in singles:
                continue
            r = solve_rel(A, ta, t2, x2, {c1, c2}, pins)
            if r is not False:
                pairs.append((c1, c2, lab(r)))
            if r is None:
                unres.append((c1, c2))
        minimal = [(c,) for c in singles] + [(c1, c2) for c1, c2, _ in pairs]
        print(f'  single restoring {singles}; pair restoring (no single inside) {pairs}', flush=True)
        print(f'  MINIMAL <=2 restoring {minimal} count {len(minimal)}; unresolved {unres}', flush=True)


if __name__ == '__main__':
    sys.exit(main())
