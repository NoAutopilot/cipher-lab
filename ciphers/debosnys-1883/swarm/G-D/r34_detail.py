#!/usr/bin/env python3
"""Test R follow-up: component breakdown of the target's best readings, 1,000 within-line shuffles each."""
import random, json
src = open('reread.py').read().split("res = {}")[0]; g = {}; exec(src, g)
rd = g['readings'](g['escape'].t2); rng = random.Random(9); out = {}
for k in ('R33', 'R34', 'R35', 'R17', 'columns'):
    z = g['dcore'].zstats(rd[k], rng, 1000); out[k] = {s: z[s] for s in ('mi1', 'bg2', 'rep3', 'dbl', 'mi2', 'bgmax')}
    print(k, {s: (z[s]['obs'], z[s]['z']) for s in ('mi1', 'bg2', 'rep3', 'dbl', 'mi2', 'bgmax')}, flush=True)
json.dump(out, open('r34_detail.json', 'w'), indent=1)
