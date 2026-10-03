#!/usr/bin/env python3
"""FT4ac (account-4, 3 Oct 2026): single-release scan on f.206 alone (PREREG-FT4ac.md, pushed before any run).
Arms H-T (338 = tou) and H-C (534 = che), each with 121 = s and C pins 22/66/581. Release = every occurrence of the row
becomes an independent token. Exact CP-SAT = ft4x_pool.solve_exact unchanged.
  python3 ft4ac_scan.py --ctrl s|g --arm T|C    (40 draws, seed 3)
  python3 ft4ac_scan.py --ctrl p                 (planted known-answer, 40 draws, seed 3)
  python3 ft4ac_scan.py --real
"""
import argparse, os, random, sys
from collections import Counter
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_pair as g
import ft4z_pool as fz
from ft4x_pool import solve_exact, PINS, LIMIT

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = dict(PINS, **{'121': 's'})
ARMS = {'T': ('338', 'tou'), 'C': ('534', 'che')}
ROWS = ['22', '66', '581', '121', '279', '336', '501', '722']


def lab(r):
    return 'unresolved' if r is None else ('fit' if r else 'nofit')


def release(A, pins, rel, keep_rep=False):
    out, p = [], dict(pins)
    for i, t in enumerate(A):
        if t in rel:
            p.pop(t, None)
            out.append(t if keep_rep else f'X{t}_{i}')
        else:
            out.append(t)
    return out, p


def scan(job):
    A, ta, pins = job
    base = solve_exact(A, ta, pins, LIMIT)
    allr = solve_exact(*release(A, pins, set(ROWS))[:1], ta, release(A, pins, set(ROWS))[1], LIMIT)
    rest, unres = [], []
    for r in ROWS:
        if r not in A:
            continue
        a2, p2 = release(A, pins, {r})
        x = solve_exact(a2, ta, p2, LIMIT)
        if x is not False:
            rest.append(r)
        if x is None:
            unres.append(r)
    return base, allr, rest, unres


def words206():
    w = []
    for l in open(os.path.join(T, 'slip_f206r.txt'), encoding='utf-8'):
        if not l.startswith('#'):
            w += [x for x in (g.letters(y) for y in l.split()) if x]
    return w


def summ(res, X=None):
    out = []
    for i, (b, a, rest, un) in enumerate(res):
        fd = b is False and len(rest) == 1 and not un
        out.append(fd)
        print(f'  draw {i}: base {lab(b)} release-all {lab(a)} restoring {rest} unresolved {un}'
              + (f' planted {X[i]}' if X else '') + (' FALSE-DECISIVE' if fd and not X else ''))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ctrl', choices=['s', 'g', 'p'])
    ap.add_argument('--arm', choices=['T', 'C'])
    ap.add_argument('--real', action='store_true')
    a = ap.parse_args()
    B, _ = fz.blocks()
    A, ta = B['F206']
    rng = random.Random(3)
    if a.ctrl in ('s', 'g'):
        c, v = ARMS[a.arm]
        pins = dict(BASE, **{c: v})
        words = words206()
        assert ''.join(words) == ta, 'f.206 slip words do not rebuild the text'
        jobs = []
        for _ in range(40):
            if a.ctrl == 's':
                w = words[:]; rng.shuffle(w); jobs.append((A, ''.join(w), pins))
            else:
                t = A[:]; rng.shuffle(t); jobs.append((t, ta, pins))
        with Pool(4) as pool:
            res = pool.map(scan, jobs)
        fd = summ(res)
        ok = sum(r[1] is True for r in res)
        print(f'CONTROL arm {a.arm} ({a.ctrl}): false-decisive {sum(fd)}/40 share {sum(fd)/40:.3f}; '
              f'release-all fit {ok}/40; base fit {sum(r[0] is True for r in res)}/40')
        return
    if a.ctrl == 'p':
        assert solve_exact(A, ta, BASE, LIMIT) is True
        cnt = Counter(A)
        singles = [i for i, t in enumerate(A) if cnt[t] == 1 and t not in BASE]
        jobs, X, redraw = [], [], 0
        while len(jobs) < 40:
            i, x = rng.choice(singles), rng.choice(ROWS)
            a2 = A[:]; a2[i] = x
            if solve_exact(a2, ta, BASE, LIMIT) is not False:
                redraw += 1; continue
            jobs.append((a2, ta, BASE)); X.append(x)
        with Pool(4) as pool:
            res = pool.map(scan, jobs)
        summ(res, X)
        cont = sum(X[i] in r[2] for i, r in enumerate(res))
        uni = sum(r[2] == [X[i]] and not r[3] for i, r in enumerate(res))
        print(f'CONTROL (p) planted: contains-X {cont}/40 share {cont/40:.3f}; unique-located {uni}/40 share {uni/40:.3f}; '
              f'redrawn (planted still fit) {redraw}')
        return
    for arm, (c, v) in ARMS.items():
        pins = dict(BASE, **{c: v})
        b, al, rest, un = scan((A, ta, pins))
        print(f'REAL arm {arm} ({c}={v}): base {lab(b)} release-all {lab(al)} restoring {rest} unresolved {un}', flush=True)
        for r in rest:
            a2, p2 = release(A, pins, {r}, keep_rep=True)
            print(f'  descriptor {r}: unpin-only (repetition kept) {lab(solve_exact(a2, ta, p2, LIMIT))}', flush=True)


if __name__ == '__main__':
    sys.exit(main())
