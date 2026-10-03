#!/usr/bin/env python3
"""Solver-optimum crib null on other windows of the real target (A2-PAL3, 3 Oct 2026; NOTES.md step of that date).

A2-PAL's crib test gave 'suofratel' on the anchor 17 9 6 10 20 4 y 3 18 a margin of +0.657/unit over the best of 11
wrong cribs; A2-PAL2's unit-shuffle null (p95 +0.207) did not reject it, but left one confound open: the unconstrained
solver already reads the anchor as '..saofrat..', so any crib that matches the solver's own optimum on this sequentially
structured text may beat the 11 wrong cribs by as much. Null (pre-registered here, committed before the windows ran):
1. one unconstrained solve of the real target (6 restarts x 30k iters, seed 11, it16_all model);
2. eligible windows: 9 consecutive units inside one passage, 9 distinct unit types (like the anchor), not overlapping
   either anchor occurrence; any window whose 9 units recur elsewhere is taken first (repeats first), then single
   windows at evenly spaced positions, 15 windows in all;
3. each window's crib = the unconstrained solve's 9 letters there; the identical test of cribs_repeat.py target
   (that crib + the same 11 WRONG cribs, 6 restarts x 30k iters, seed 11, constrained score per unit);
4. statistic = window crib score minus best wrong crib. The anchor's +0.657 (A2-PAL2, same 6 x 30k setting) survives
   only if it stands above the p95 of the 15 window margins; otherwise the crib test cannot tell 'suofratel' from
   the solver's own optimum, and the candidate gets no support from it.
The window margins depend on the target's own context at each window, so they can differ from the anchor's (rule 3).

  python3 cribs_window.py MODEL_ALL.npz --list            (unconstrained solve, writes runs_window/windows.tsv)
  python3 cribs_window.py MODEL_ALL.npz --window K        (crib test on window K of windows.tsv)
"""
import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from italian_ngram import ALPHA  # noqa: E402
from seg_homophonic import LM, Problem, parse_design, read_cipher, segment  # noqa: E402
from cribs import ANCHOR, anneal_fixed  # noqa: E402
from cribs_repeat import WRONG, run  # noqa: E402

NWIN = 15
TSV = os.path.join(HERE, 'runs_window', 'windows.tsv')


def windows(pas, key, prob):
    anc = set()
    for pi, p in enumerate(pas):
        for i in range(len(p) - 8):
            if p[i:i + 9] == ANCHOR:
                anc |= {(pi, i + k) for k in range(9)}
    seen, wins = {}, []
    for pi, p in enumerate(pas):
        for i in range(len(p) - 8):
            w = p[i:i + 9]
            seen.setdefault(tuple(w), []).append((pi, i))
            if len(set(w)) == 9 and not any((pi, i + k) in anc for k in range(9)):
                wins.append((pi, i, w))
    rep = [x for x in wins if len(seen[tuple(x[2])]) > 1]
    single = [x for x in wins if len(seen[tuple(x[2])]) == 1]
    need = NWIN - len(rep)
    idx = np.linspace(0, len(single) - 1, need).round().astype(int) if need > 0 else []
    pick = [(x, 'repeat') for x in rep][:NWIN] + [(single[j], 'single') for j in idx]
    out = []
    for (pi, i, w), kind in pick:
        crib = ''.join(ALPHA[key[prob.tid[u]]] for u in w)
        out.append((pi, i, ' '.join(w), crib, kind))
    return out, len(wins), len(rep)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--window')
    ap.add_argument('--iters', type=int, default=30000)
    ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--procs', type=int, default=4)
    a = ap.parse_args()
    lm = LM(a.model, 3.0)
    P, ym = parse_design('12:letter')
    pas = segment(read_cipher(os.path.join(HERE, 'signs_full.txt')), P, ym)[0]
    prob = Problem(pas)
    if a.list:
        key, sc = anneal_fixed(prob, lm, np.random.default_rng(11), {}, a.iters, a.restarts)
        anc = ''.join(ALPHA[key[prob.tid[u]]] for u in ANCHOR)
        wins, ne, nr = windows(pas, key, prob)
        print(f'unconstrained {sc / prob.n:.3f}/unit over {prob.n} units; anchor reads {anc!r}; '
              f'{ne} eligible windows, {nr} on repeats', flush=True)
        with open(TSV, 'w') as f:
            f.write('k\tpassage\tpos\tunits\tcrib\tkind\n')
            f.write(f'A\t-\t-\t{" ".join(ANCHOR)}\t{anc}\tanchor-solver-optimum\n')
            for k, w in enumerate(wins):
                f.write(f'{k}\t' + '\t'.join(map(str, w)) + '\n')
        print(open(TSV).read(), flush=True)
        return
    rows = [l.rstrip('\n').split('\t') for l in open(TSV)][1:]
    r = [x for x in rows if x[0] == a.window][0]
    units, crib = r[3].split(), r[4]
    res = run(prob, lm, 11, units, [crib] + [w for w in WRONG if w != crib], a, f'WINDOW {a.window}')
    others = {w: s for w, s in res.items() if w != crib}
    bw = max(others, key=others.get)
    print(f'WINDOW {a.window}: crib {crib} {res[crib]:.3f} margin {res[crib] - others[bw]:+.3f} over {bw}', flush=True)


if __name__ == '__main__':
    main()
