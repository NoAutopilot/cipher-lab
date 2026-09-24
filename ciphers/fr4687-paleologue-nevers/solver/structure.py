#!/usr/bin/env python3
"""Structure tests on signs.txt (24 Sept 2026): is 1 (and 2) a prefix sign? Shuffle null, 20000 permutations
of the real signs over the real line lengths. Prints observed statistics and permutation p-values."""
import random
from collections import Counter
L = [l.rstrip("\n").split("\t")[1] for l in open("signs.txt") if not l.startswith("#")]

def stats(lines):
    s = Counter()
    for v in lines:
        for i, c in enumerate(v):
            nxt = v[i + 1] if i + 1 < len(v) else "$"
            prv = v[i - 1] if i else "^"
            if c in "12" and nxt in "y$":
                s[c + "_final_or_before_y"] += 1
            if c == "0" and prv != "2":
                s["0_not_after_2"] += 1
            if c in "78" and prv != "1":
                s[c + "_not_after_1"] += 1
    return s

obs = stats(L)
keys = ["1_final_or_before_y", "2_final_or_before_y", "0_not_after_2", "7_not_after_1", "8_not_after_1"]
allsig = [c for v in L for c in v]
rnd = random.Random(7)
le = {k: 0 for k in keys}
mean = Counter()
N = 20000
for _ in range(N):
    rnd.shuffle(allsig)
    out, i = [], 0
    for v in L:
        out.append("".join(allsig[i:i + len(v)])); i += len(v)
    s = stats(out)
    for k in keys:
        mean[k] += s[k] / N
        le[k] += s[k] <= obs[k]
for k in keys:
    print(f"{k}\tobserved {obs[k]}\tshuffle mean {mean[k]:.1f}\tp(<=obs) {le[k] / N:.5f}")
