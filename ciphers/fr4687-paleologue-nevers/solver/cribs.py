#!/usr/bin/env python3
"""Crib test on the full text (24 Sept 2026), design 1x/2x with y a letter.

Anchor: the 9-unit run 17 9 6 10 20 4 y 3 18 (signs 1796102049y318 minus the leading 1: f8_left_L1 pos 36-48 and
f8_L3 pos 3-15, the only long repeat in the text; NOTES.md). Each candidate plaintext fixes those units' letters;
the rest of the key is annealed as in tools/seg_homophonic.py (same model, guard, iterations) and the score per
unit is compared with the unconstrained solve. A crib that conflicts (one unit, two letters) is rejected.

Control of the method: the same test on a matched synthetic control (make_control, 540 units, noise 0.10, the
target's line lengths), with the true plaintext of a 9-unit window as the right crib and the same wrong
candidates. The method is informative only if the right crib beats the wrong ones there.

  python3 cribs.py MODEL.npz [--iters 150000] [--restarts 4] > runs_full/cribs.txt
"""
import argparse
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
from italian_ngram import ALPHA, IDX  # noqa: E402
from seg_homophonic import LM, NL, Problem, make_control, parse_design, read_cipher, segment  # noqa: E402

ANCHOR = ['17', '9', '6', '10', '20', '4', 'y', '3', '18']
CANDS = ['cardinale', 'lcardinal', 'francesco', 'guglielmo', 'monsignor', 'suamaesta', 'ilducadis', 'monferrat',
         'disauoiae', 'lacorteet', 'cheilrede']
# 9-letter windows of 'nostro/vostro/suo fratello': the unconstrained solve reads the anchor as '..oesaofrat..'
# both times, and the clear line after f8_left_L4 is 'il cardinale nostro fratello'
for ph in ('nostrofratello', 'vostrofratello', 'suofratello'):
    CANDS += [ph[i:i + 9] for i in range(len(ph) - 8) if ph[i:i + 9] not in CANDS]


def anneal_fixed(prob, lm, rng, fixed, iters, restarts, t0=60.0):
    T = len(prob.types)
    free = [t for t in range(T) if t not in fixed]
    best_key, best = None, -1e18
    for r in range(restarts):
        key = rng.choice(NL, size=T, p=lm.p1).astype(np.int64)
        for t, c in fixed.items():
            key[t] = c
        cur = lm.score_passages(prob.text(key))
        for it in range(iters):
            temp = t0 * (1 - it / iters) + 1e-3
            t = free[rng.integers(len(free))]
            old = key[t]
            key[t] = rng.integers(NL)
            if key[t] == old:
                continue
            s = lm.score_passages(prob.text(key))
            if s >= cur or rng.random() < np.exp((s - cur) / temp):
                cur = s
            else:
                key[t] = old
        improved = True
        while improved:
            improved = False
            for t in free:
                old, bl, bs = key[t], key[t], cur
                for c in range(NL):
                    if c == old:
                        continue
                    key[t] = c
                    s = lm.score_passages(prob.text(key))
                    if s > bs + 1e-6:
                        bl, bs = c, s
                key[t] = bl
                if bl != old:
                    cur, improved = bs, True
        if cur > best:
            best, best_key = cur, key.copy()
    return best_key, best


def fix_for(prob, units, word):
    fixed = {}
    for u, ch in zip(units, word):
        if ch not in IDX:
            return None
        t, c = prob.tid[u], IDX[ch]
        if fixed.get(t, c) != c:
            return None
        fixed[t] = c
    return fixed


def run(prob, lm, rng, units, cands, a, label, truth=None):
    _, free = anneal_fixed(prob, lm, rng, {}, a.iters, a.restarts)
    print(f'{label}: unconstrained score/unit {free / prob.n:.3f}', flush=True)
    for w in cands:
        fx = fix_for(prob, units, w)
        if fx is None:
            print(f'  {w}\tconflict (one unit, two letters)', flush=True)
            continue
        key, sc = anneal_fixed(prob, lm, rng, fx, a.iters, a.restarts)
        txt = ''.join(ALPHA[c] for c in prob.text(key)[0])[:80]
        tag = ' (TRUE)' if w == truth else ''
        print(f'  {w}{tag}\t{sc / prob.n:.3f}\tdelta {(sc - free) / prob.n:+.3f}\t{txt}', flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('model')
    ap.add_argument('--iters', type=int, default=150000)
    ap.add_argument('--restarts', type=int, default=4)
    ap.add_argument('--part', choices=['target', 'control', 'both'], default='both')
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    lm = LM(a.model, 3.0)
    P, ym = parse_design('12:letter')
    tgt = read_cipher(os.path.join(here, 'signs_full.txt'))
    rng = np.random.default_rng(11)
    cands = [w for w in CANDS if len(w) == 9 and w.isalpha()]
    if a.part in ('control', 'both'):
        plain = [l.strip() for l in open(os.path.join(here, 'control_heldout.txt')) if l.strip()]
        lines, pt, assign = make_control(plain, 540, '12:letter', [len(s) for _, s in tgt],
                                         np.random.default_rng(3000), 0.10, 0.066)
        cp = Problem(segment(lines, P, ym)[0])
        # right crib: the plaintext under a window of 9 distinct units (like the anchor) of the clean stream that
        # survives intact in the noisy one
        clean, _, _ = make_control(plain, 540, '12:letter', [len(s) for _, s in tgt],
                                   np.random.default_rng(3000), 0.0, 0.066)
        cu = [u for p in segment(clean, P, ym)[0] for u in p]
        nu = [u for p in cp_seqs(cp) for u in p]
        win = None
        for i in range(100, len(cu) - 9):
            w = cu[i:i + 9]
            if len(set(w)) == 9 and any(nu[j:j + 9] == w for j in range(max(0, i - 40), min(len(nu) - 9, i + 40))):
                win = (w, pt[i:i + 9])
                break
        cp_units, truth = win
        run(cp, lm, rng, cp_units, [truth] + cands, a, f'CONTROL (noise 0.10, window {".".join(cp_units)})', truth)
    if a.part in ('target', 'both'):
        tp = Problem(segment(tgt, P, ym)[0])
        run(tp, lm, rng, ANCHOR, cands, a, 'TARGET')


def cp_seqs(prob):
    return [[prob.types[t] for t in s] for s in prob.seqs]


if __name__ == '__main__':
    main()
