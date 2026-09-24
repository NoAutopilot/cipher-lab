#!/usr/bin/env python3
"""Write matched control ciphers (units 540, the target's line lengths, design 1x/2x y letter) at a given noise, for
calibrating the target's score per unit and unit-null z (24 Sept 2026).  python3 calib_dump.py NOISE SEED OUT"""
import os
import sys

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
from seg_homophonic import make_control, read_cipher  # noqa: E402

here = os.path.dirname(os.path.abspath(__file__))
noise, seed, out = float(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
plain = [l.strip() for l in open(os.path.join(here, 'control_heldout.txt')) if l.strip()]
lens = [len(s) for _, s in read_cipher(os.path.join(here, 'signs_full.txt'))]
lines, pt, _ = make_control(plain, 540, '12:letter', lens, np.random.default_rng(seed), noise, 0.066)
with open(out, 'w') as f:
    f.write(f'# synthetic control, seed {seed}, noise {noise}; plaintext: {pt}\n')
    for lid, s in lines:
        f.write(f'{lid}\t{s}\n')
