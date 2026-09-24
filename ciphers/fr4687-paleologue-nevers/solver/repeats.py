#!/usr/bin/env python3
"""Repeat test on the full text (24 Sept 2026): repeated unit n-grams under the 1x/2x design, target vs
sign-shuffle nulls vs matched synthetic controls (make_control from tools/seg_homophonic.py, same line lengths,
units 540, noise 0 / 0.10). Italian enciphered with ~30 unit types keeps many repeated trigrams and 4-grams
(che, per, della, ...); a code or non-letter design, or heavy noise, loses them.
  python3 repeats.py > runs_full/repeats.txt
"""
import os
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
from seg_homophonic import make_control, parse_design, read_cipher, segment, shuffled  # noqa: E402


def rep(lines, n):
    P, ym = parse_design('12:letter')
    passages, _ = segment(lines, P, ym)
    c = Counter()
    for p in passages:
        for i in range(len(p) - n + 1):
            c[tuple(p[i:i + n])] += 1
    return sum(v for v in c.values() if v > 1), sum(1 for v in c.values() if v > 1)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    tgt = read_cipher(os.path.join(here, 'signs_full.txt'))
    plain = [l.strip() for l in open(os.path.join(here, 'control_heldout.txt')) if l.strip()]
    lens = [len(s) for _, s in tgt]
    print('n\ttarget(occ,types)\tshuffle mean occ (20)\tcontrol n0 mean occ (10)\tcontrol n0.10 mean occ (10)')
    for n in (3, 4, 5):
        t = rep(tgt, n)
        rng = np.random.default_rng(7)
        sh = [rep(shuffled(tgt, rng), n)[0] for _ in range(20)]
        cs = {}
        for noise in (0.0, 0.10):
            v = []
            for s in range(10):
                r = np.random.default_rng(2000 + s)
                lines, _, _ = make_control(plain, 540, '12:letter', lens, r, noise, 0.066)
                v.append(rep(lines, n)[0])
            cs[noise] = v
        print(f'{n}\t{t[0]},{t[1]}\t{np.mean(sh):.1f} (sd {np.std(sh):.1f})\t{np.mean(cs[0.0]):.1f} '
              f'(min {min(cs[0.0])})\t{np.mean(cs[0.10]):.1f} (min {min(cs[0.10])})')


if __name__ == '__main__':
    main()
