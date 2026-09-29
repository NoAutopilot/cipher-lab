#!/usr/bin/env python3
"""NULL held-out control: no language. Tokens drawn iid from the c2 sign-count curve (A: N 688; B: N 134, 10 pct fresh signs).
Tests whether a held-out percentile above 99.9 can come from sign-frequency / letter-frequency matching alone."""
import sys, os, random
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from plant import curve
seed, tag = int(sys.argv[1]), sys.argv[2]; rng = random.Random(seed); cv = curve('c2'); K = len(cv)
A = rng.choices(range(K), weights=cv, k=sum(cv)); B = rng.choices(range(K), weights=cv, k=134)
B = [K + rng.randrange(8) if rng.random() < 0.10 else x for x in B]
for nm, arr in (('hA', A), ('hB', B)):
    open(os.path.join(H, 'work', f'{nm}_{tag}.cip'), 'w').write(' '.join(map(str, arr)) + '\n')
    open(os.path.join(H, 'work', f'{nm}_{tag}.ans'), 'w').write('x' * len(arr) + '\n')
