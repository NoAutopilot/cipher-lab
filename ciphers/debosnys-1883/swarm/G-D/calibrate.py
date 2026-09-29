#!/usr/bin/env python3
"""Calibration set: n pairs per design at c1/c2 shape, features to calib.jsonl. Seeds are the calibration seeds only."""
import dcore, random, json, sys
n = int(sys.argv[1]); p = float(sys.argv[2]); xnull = float(sys.argv[3]); out = sys.argv[4]
t1, t2 = dcore.target('c1'), dcore.target('c2'); L1 = [len(l) for l in t1]; L2 = [len(l) for l in t2]
cv = dcore.curve_of(t1 + t2)
D = ['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'FR-SYLL', 'LA-HOMO', 'NULL-IID', 'NULL-HABIT', 'NULL-AVOID']
with open(out, 'w') as fo:
    for d in D:
        rng = random.Random(f'calib-{d}-{p}-{xnull}')
        for i in range(n):
            a, b = dcore.make_pair(d, L1, L2, cv, rng, p, xnull)
            fo.write(json.dumps(dict(design=d, p=p, xnull=xnull, f=dcore.features(a, b, rng))) + '\n')
        print(d, 'done', flush=True)
