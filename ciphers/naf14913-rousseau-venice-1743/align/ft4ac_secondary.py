#!/usr/bin/env python3
"""FT4ac unregistered secondary (diagnostic only, drives nothing): which single occurrence of 581 in f.206, freed alone
(the other 581 occurrences keep au), restores f.206's exact fit under each arm."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ft4z_pool as fz
from ft4x_pool import solve_exact, LIMIT
from ft4ac_scan import BASE, ARMS, lab
B, _ = fz.blocks()
A, ta = B['F206']
for arm, (c, v) in ARMS.items():
    pins = dict(BASE, **{c: v})
    for i, t in enumerate(A):
        if t == '581':
            a2 = A[:]; a2[i] = f'X581_{i}'
            print(f'SECONDARY arm {arm}: free 581 occurrence at group {i} alone -> {lab(solve_exact(a2, ta, pins, LIMIT))}')
