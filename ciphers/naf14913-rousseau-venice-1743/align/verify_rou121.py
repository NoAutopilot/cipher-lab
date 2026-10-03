#!/usr/bin/env python3
"""VERIFY-ROU121 (account-4 verifier, 3 Oct 2026): independent re-check of FT4z's key row 121 = s.
Imports FT4z's own blocks and FT4x's solve_exact unchanged.
  python3 verify_rou121.py --repro          REAL F216V+S1 J and 121 feasible set (as FT4z), per-block 121 feasible sets
  python3 verify_rou121.py --ctrl s|g       controls, seed 11, n 80 (FT4z used seed 3, n 40)
  python3 verify_rou121.py --power          planted 121 value (ons, qx) in the real pool: does the readout recover it uniquely?
  python3 verify_rou121.py --witness        other 121 carriers: exact and one-edit fit with 121 = s / ons / free
"""
import argparse, inspect, os, random, sys
from multiprocessing import Pool
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4s_seg as fs, ft4u_seg as fu, ft4t_seg as ftt, ft4v_pair as fv, one_edit_seg as oes
import ft4x_pool as fx
from ft4x_pool import solve_exact, PINS, LIMIT
import ft4z_pool as fz

# solution-returning copy of solve_exact (power plant needs the 121 chunk positions)
_src = inspect.getsource(fs.solve_pins).replace('def solve_pins(toks, text, pins, limit, force=None):',
                                                'def solve_sol(toks, text, pins, limit, force=None):')
_src = _src.replace('m.Add(sum(edv) <= 1)', 'm.Add(sum(edv) == 0)')
assert _src.count('        return True') == 1
_src = _src.replace('        return True', '        return {i: (s.Value(a[i]), s.Value(ln[i])) for i in R}')
_ns = dict(fs.__dict__); exec(_src, _ns); solve_sol = _ns['solve_sol']


def lab(r):
    return 'unresolved' if r is None else ('fit' if r else 'nofit')


def feasible(toks, text, code, carriers, solver=solve_exact, pins=PINS):
    cand = sorted({x[p:p + l] for x in carriers[:1] for l in range(1, fs.MAXLEN + 1) for p in range(len(x) - l + 1)
                   if all(x[p:p + l] in y for y in carriers)}, key=lambda s: (len(s), s))
    feas, unres = [], []
    for v in cand:
        r = solver(toks, text, dict(pins, **{code: v}), LIMIT)
        if r:
            feas.append(v)
        elif r is None:
            unres.append(v)
    return len(cand), feas, unres


def J(job):
    return solve_exact(job[0], job[1], PINS, LIMIT)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repro', action='store_true'); ap.add_argument('--power', action='store_true')
    ap.add_argument('--witness', action='store_true'); ap.add_argument('--ctrl', choices=['s', 'g'])
    ap.add_argument('--seed', type=int, default=11); ap.add_argument('--n', type=int, default=80)
    a = ap.parse_args()
    B, sw = fz.blocks()
    real = [B['F216V'], B['S1']]
    toks, text = fz.join(real)
    if a.repro:
        print(f'REAL F216V+S1 J {lab(J((toks, text)))}')
        n, f, u = feasible(toks, text, '121', [x for t, x in real])
        print(f'pooled 121: candidates {n} feasible {f} unresolved {u}')
        for k in ('F216V', 'S1'):
            t, x = B[k]
            n, f, u = feasible(t, x, '121', [x])
            print(f'{k} alone 121: candidates {n} feasible {len(f)} {f[:40]} unresolved {len(u)}')
        return
    if a.ctrl:
        rng = random.Random(a.seed)
        st, sx = B['S1']
        jobs = []
        for _ in range(a.n):
            if a.ctrl == 's':
                w = sw[:]; rng.shuffle(w); jobs.append(fz.join([B['F216V'], (st, ''.join(w))]))
            else:
                t = st[:]; rng.shuffle(t); jobs.append(fz.join([B['F216V'], (t, sx)]))
        with Pool(4) as p:
            res = p.map(J, jobs)
        hi = sum(r is not False for r in res)
        print(f'CONTROL {a.ctrl} seed {a.seed} n {a.n}: fit {sum(r is True for r in res)} unresolved {sum(r is None for r in res)} '
              f'fit-or-unresolved {hi}/{a.n} share {hi/a.n:.3f}')
        return
    if a.power:
        sol = solve_sol(toks, text, PINS, LIMIT)
        pos = sorted({sol[i] for i, t in enumerate(toks) if t == '121'})
        print(f'real solution 121 spans {[(p, text[p:p+l]) for p, l in pos]}')
        for plant in ('ons', 'qx'):
            t2 = text
            for p, l in sorted(pos, reverse=True):
                t2 = t2[:p] + plant + t2[p + l:]
            parts = t2.split('|')
            n, f, u = feasible(toks, t2, '121', parts)
            print(f'PLANT 121={plant}: J {lab(J((toks, t2)))}; candidates {n} feasible {f} unresolved {u}; '
                  f'recovered {plant in f} unique {f == [plant]}')
        return
    if a.witness:
        se = fx.solve_exact
        W = {'F206': B['F206'][:2]}
        for k in ('f213', 'f249'):
            t, x, _ = oes.load(k); W[k] = (t, x)
        t, x, _ = ftt.segment(); W['f249-FT4t-seg'] = (t, x)
        t, x, _ = fu.segment('S2'); W['f266r-S2'] = (t, x)
        t, x, _ = fu.segment('S3'); W['f266r-S3'] = (t, x)
        gt, gw = fv.load('primary'); W['f252r'] = (gt, ''.join(gw))
        for k, (t, x) in W.items():
            row = [f'{k}: 121 x{t.count("121")} groups {len(t)} letters {len(x)}']
            for name, solver in (('exact', se), ('one-edit', fs.solve_pins)):
                r = {v: lab(solver(t, x, dict(PINS, **({'121': v} if v else {})), LIMIT)) for v in (None, 's', 'ons')}
                row.append(f'{name} free {r[None]} s {r["s"]} ons {r["ons"]}')
            print(' | '.join(row), flush=True)
        return


if __name__ == '__main__':
    sys.exit(main())
