#!/usr/bin/env python3
"""Crib test anchored on 'suofratel' with a matched repeat control (A2-PAL, 3 Oct 2026; NOTES.md step of that date).

Follow-up named in NOTES "Full text: extras reconciled and solver rerun": crib tests anchored on `suofratel` with 6
restarts and a matched control whose TRUE crib sits on a repeat. The 24 Sept method control (cribs.py) took its true
crib from a window that occurs once; the target's anchor (17 9 6 10 20 4 y 3 18) occurs twice, so fixing it constrains
two places at once. Here the control is built the same way as the target looks: held-out Italian (control_heldout.txt,
never seen by it16_train), 540 letters, a random homophonic key over the 1x/2x + y-letter inventory, the target's line
lengths, 10 % sign noise -- and a 9-letter window of its own plaintext planted a second time ~110 letters later with
the SAME 9 units (a scribe repeating a phrase with the same homophones), both copies protected from noise (the
target's anchor is observed intact twice by definition). The true crib is that window; the wrong cribs are cribs.py's
20 candidates cut to 11 (WRONG) for the box, plus 'suofratel' as a wrong crib in the control.

Statistic (pre-registered in NOTES.md before the control ran): per candidate, best constrained score/unit over 6
restarts; margin = true-crib score minus best wrong-crib score. Control passes on a seed when the true crib ranks
first with margin >= 0.30/unit; the control gate is met when it passes on >= 2 of 3 seeds. The target runs only if
the gate is met, and 'suofratel' reads only if it ranks first with margin >= 0.30/unit over every other candidate.
The control's margin can differ from the target's (it depends on the cipher text, not on a manipulation orthogonal
to it), so the comparison is a test (CLAUDE.md rule 3).

  python3 cribs_repeat.py control MODEL_TRAIN.npz --seed 1 [--restarts 6 --iters 150000]
  python3 cribs_repeat.py target MODEL_ALL.npz [--restarts 6 --iters 150000]
"""
import argparse
import os
import sys
from collections import Counter

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
from italian_ngram import ALPHA  # noqa: E402
from seg_homophonic import LM, Problem, parse_design, read_cipher, segment  # noqa: E402
from cribs import ANCHOR, anneal_fixed, fix_for  # noqa: E402

GAP = 110  # letters between the two copies (target: f8_left_L1 pos 36 and f8_L3 pos 3, a few lines apart)


def make_repeat_control(plain, n, lens, rng, noise):
    P, ym = parse_design('12:letter')
    text = ''.join(l.replace('#', '') for l in plain)
    st = int(rng.integers(0, len(text) - n))
    pt = list(text[st:st + n])
    singles = [d for d in '0123456789' if d not in P] + ['y']
    units = singles + [p + d for p in sorted(P) for d in '0123456789']
    letters = [c for c, _ in Counter(''.join(pt)).most_common()]
    assign, pool = {}, units[:]
    rng.shuffle(pool)
    for k, u in enumerate(pool):
        assign.setdefault(letters[k % len(letters)] if k < len(letters) else
                          letters[int(rng.integers(0, min(8, len(letters))))], []).append(u)
    uct = [assign[c][int(rng.integers(len(assign[c])))] for c in pt]
    # the copied window has 9 distinct units, like the target's anchor
    while True:
        i = int(rng.integers(100, n - GAP - 20))
        if len(set(uct[i:i + 9])) == 9:
            break
    j = i + GAP
    pt[j:j + 9] = pt[i:i + 9]
    uct[j:j + 9] = uct[i:i + 9]
    pt = ''.join(pt)
    prot = set(range(i - 1, i + 9)) | set(range(j - 1, j + 9))  # one unit before each copy too (parse boundary)
    raw, cur, cprot, k = [], [], [], 0
    for ui, u in enumerate(uct):
        for ch in u:
            cur.append(ch)
            cprot.append(ui in prot)
        if len(cur) >= lens[k % len(lens)]:
            raw.append((cur, cprot))
            cur, cprot, k = [], [], k + 1
    if cur:
        raw.append((cur, cprot))
    lines = []
    for k, (sg, pr) in enumerate(raw):
        out = []
        for c, p in zip(sg, pr):
            if p:
                out.append(c)
                continue
            r = rng.random()
            if r < noise / 3:
                continue
            if r < 2 * noise / 3 and c in '49':
                c = '9' if c == '4' else '4'
            out.append(c)
            if rng.random() < noise / 3:
                out.append(str(rng.integers(0, 10)))
        lines.append((f'c{k // 6}_L{k}', ''.join(out)))
    return lines, pt, uct[i:i + 9], pt[i:i + 9]


WRONG = ['cardinale', 'francesco', 'guglielmo', 'monsignor', 'suamaesta', 'ilducadis', 'monferrat', 'lacorteet',
         'cheilrede', 'nostrofra', 'ostrofrat']  # cribs.py's set cut to 11 for the 45-min box (one 9-shift kept per phrase family)
_G = {}


def _one(w):
    prob, lm, units, a, seed = _G['args']
    fx = fix_for(prob, units, w)
    if fx is None:
        return w, None, ''
    key, sc = anneal_fixed(prob, lm, np.random.default_rng([seed, sum(map(ord, w))]), fx, a.iters, a.restarts)
    return w, sc / prob.n, ''.join(ALPHA[c] for c in prob.text(key)[0])[:80]


def run(prob, lm, seed, units, cands, a, label, truth=None):
    from multiprocessing import Pool
    _G['args'] = (prob, lm, units, a, seed)
    with Pool(a.procs) as pool:
        out = pool.map(_one, cands)
    print(f'{label}: {len(cands)} cribs, {a.restarts} restarts x {a.iters} iters each', flush=True)
    res = {}
    for w, sc, txt in out:
        if sc is None:
            print(f'  {w}\tconflict (one unit, two letters)', flush=True)
            continue
        res[w] = sc
        print(f'  {w}{" (TRUE)" if w == truth else ""}\t{sc:.3f}\t{txt}', flush=True)
    return res


def verdict(res, focus, label):
    others = {w: s for w, s in res.items() if w != focus}
    bw = max(others, key=others.get)
    margin = res[focus] - others[bw]
    rank = 1 + sum(1 for s in others.values() if s > res[focus])
    ok = rank == 1 and margin >= 0.30
    print(f'{label}: {focus} rank {rank}/{len(res)}, margin {margin:+.3f} over best other ({bw}) -> '
          f'{"PASS" if ok else "FAIL"} (gate: rank 1, margin >= 0.30)', flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('part', choices=['control', 'target'])
    ap.add_argument('model')
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--iters', type=int, default=150000)
    ap.add_argument('--restarts', type=int, default=6)
    ap.add_argument('--noise', type=float, default=0.10)
    ap.add_argument('--procs', type=int, default=4)
    a = ap.parse_args()
    lm = LM(a.model, 3.0)
    P, ym = parse_design('12:letter')
    tgt = read_cipher(os.path.join(HERE, 'signs_full.txt'))
    if a.part == 'control':
        plain = [l.strip() for l in open(os.path.join(HERE, 'control_heldout.txt')) if l.strip()]
        lines, pt, wunits, truth = make_repeat_control(plain, 540, [len(s) for _, s in tgt],
                                                       np.random.default_rng(5000 + a.seed), a.noise)
        prob = Problem(segment(lines, P, ym)[0])
        stream = [prob.types[t] for s in prob.seqs for t in s]
        hits = [k for k in range(len(stream) - 8) if stream[k:k + 9] == wunits]
        print(f'control seed {a.seed}: {sum(len(s) for _, s in lines)} signs, {prob.n} units, '
              f'{len(prob.types)} types; planted crib {truth!r} on units {".".join(wunits)} found at {hits}', flush=True)
        cands = [truth] + [w for w in WRONG + ['suofratel'] if w != truth]
        res = run(prob, lm, a.seed, wunits, cands, a, 'CONTROL', truth)
        verdict(res, truth, f'CONTROL seed {a.seed}')
    else:
        prob = Problem(segment(tgt, P, ym)[0])
        res = run(prob, lm, 11, ANCHOR, ['suofratel'] + WRONG, a, 'TARGET')
        verdict(res, 'suofratel', 'TARGET')


if __name__ == '__main__':
    main()
