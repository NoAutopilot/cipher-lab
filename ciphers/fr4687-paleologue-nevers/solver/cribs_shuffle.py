#!/usr/bin/env python3
"""Unit-shuffle null for the 'suofratel' crib test (A2-PAL2, 3 Oct 2026; NOTES.md step of that date).

A2-PAL's crib test (cribs_repeat.py target) gave 'suofratel' on the anchor 17 9 6 10 20 4 y 3 18 a margin of +0.657/unit
over the best of 11 wrong cribs. Confound left open: the margin may come from the anchor units plus the language model
alone (the crib agreeing with the solver's own optimum), not from Italian context around it. Null: keep both anchor
occurrences in place, permute every other unit of the segmented target across all non-anchor positions (unit counts and
passage lengths unchanged, order destroyed), and run the identical test -- same 12 cribs, same restarts, iterations,
seed and scoring as cribs_repeat.py target. The statistic (suofratel margin over best other) depends on the context the
shuffle destroys, so the null can differ from the target (CLAUDE.md rule 3).

  python3 cribs_shuffle.py MODEL_ALL.npz --shuffle K [--restarts 6 --iters 150000]   (K = -1: real target, same settings)
"""
import argparse
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from seg_homophonic import LM, Problem, parse_design, read_cipher, segment  # noqa: E402
from cribs import ANCHOR  # noqa: E402
from cribs_repeat import WRONG, run  # noqa: E402


def shuffled_passages(passages, k):
    flat = [u for p in passages for u in p]
    keep = set()
    for i in range(len(flat) - 8):
        if flat[i:i + 9] == ANCHOR:
            keep |= set(range(i, i + 9))
    free = [i for i in range(len(flat)) if i not in keep]
    vals = [flat[i] for i in free]
    np.random.default_rng(7000 + k).shuffle(vals)
    for i, v in zip(free, vals):
        flat[i] = v
    out, pos = [], 0
    for p in passages:
        out.append(flat[pos:pos + len(p)])
        pos += len(p)
    return out, len(keep) // 9


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model')
    ap.add_argument('--shuffle', type=int, required=True)
    ap.add_argument('--iters', type=int, default=150000)
    ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--procs', type=int, default=4)
    a = ap.parse_args()
    lm = LM(a.model, 3.0)
    P, ym = parse_design('12:letter')
    pas = segment(read_cipher(os.path.join(HERE, 'signs_full.txt')), P, ym)[0]
    sp, nanc = shuffled_passages(pas, a.shuffle) if a.shuffle >= 0 else (pas, 2)  # -1: the real target, unshuffled
    prob = Problem(sp)
    print(f'shuffle {a.shuffle}: {prob.n} units, anchor kept at {nanc} occurrences', flush=True)
    res = run(prob, lm, 11, ANCHOR, ['suofratel'] + WRONG, a, f'SHUFFLE {a.shuffle}')
    others = {w: s for w, s in res.items() if w != 'suofratel'}
    bw = max(others, key=others.get)
    print(f'SHUFFLE {a.shuffle}: suofratel {res["suofratel"]:.3f} margin {res["suofratel"] - others[bw]:+.3f} '
          f'over {bw}', flush=True)


if __name__ == '__main__':
    main()
