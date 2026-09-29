#!/usr/bin/env python3
"""Test R follow-up (29 Sept 2026): the null for the target's scan maximum made from the TARGET ITSELF -- c2 shuffled
within lines (every count and line kept), then the same 61-reading scan. Usage: reread_null.py SEED N OUT."""
import sys, json, random
src = open('reread.py').read().split("res = {}")[0]; g = {}; exec(src, g)
seed, n, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]; rng = random.Random(seed); g['rng'].seed(seed + 1)
rows = []
for i in range(n):
    q = [rng.sample(l, len(l)) for l in g['escape'].t2]; b, s, _ = g['scan'](q); rows.append((b, s))
json.dump(rows, open(out, 'w'))
