"""B1 companion 2: is the particle->x10 alignment specific to a trailing ZERO (padding) or does the whole decade
10v..10v+9 follow n(v) (any trailing digit a null)?  Null: redraw every 3-digit book value (100-999) keeping
the hundreds-block profile and the multiset of units digits (units digits permuted among the redrawn values),
2,000 draws; report corr(n(v), n(10v)) and corr(n(v), n(10v+1..9)) with percentiles, lag-1 autocorrelation of
n(v), and the vocabulary size under each collapse rule."""
import random, sys
from collections import Counter
sys.path.insert(0, '.')
from padding_test import target_tokens
toks = target_tokens(); c = Counter(toks)
def corr(xs, ys):
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); sxx = sum((x-mx)**2 for x in xs); syy = sum((y-my)**2 for y in ys)
    return sxy / (sxx*syy) ** 0.5 if sxx and syy else 0.0
V = list(range(10, 100))
def stats(t):
    cc = Counter(t)
    a = corr([cc[v] for v in V], [cc[10*v] for v in V])
    b = corr([cc[v] for v in V], [sum(cc[10*v+u] for u in range(1, 10)) for v in V])
    d = corr([cc[v] for v in V], [sum(cc[10*v+u] for u in range(0, 10)) for v in V])
    return a, b, d
print("lag-1 autocorrelation of n(v), v=10..99:", round(corr([c[v] for v in V[:-1]], [c[v] for v in V[1:]]), 3))
t0 = stats(toks)
print(f"target: corr zero-form {t0[0]:.3f}, nonzero-forms {t0[1]:.3f}, whole decade {t0[2]:.3f}")
rng = random.Random(3)
three = [v for v in toks if 100 <= v < 1000]; others = [v for v in toks if not (100 <= v < 1000)]
dist = sorted(set(three)); mult = [c[v] for v in dist]
units = [v % 10 for v in dist]; hund = [v // 100 for v in dist]
draws = []
import os
for _ in range(int(os.environ.get("DRAWS", "2000"))):
    # permute units digits WITHIN each hundreds block, then assign each (block, units) group its decades by
    # sampling without replacement from the 10 decades (deadlock-free; a global permutation could put more than
    # 10 equal units digits into one block, which is what hung the first version of this script)
    us = units[:]
    for hb in set(hund):
        idx = [i for i, h in enumerate(hund) if h == hb]
        sub = [us[i] for i in idx]; rng.shuffle(sub)
        for i, u in zip(idx, sub): us[i] = u
    groups = {}
    for i, (h, u) in enumerate(zip(hund, us)): groups.setdefault((h, u), []).append(i)
    vals = [0] * len(dist)
    for (h, u), idx in groups.items():
        decs = rng.sample(range(10), len(idx))
        for i, d in zip(idx, decs): vals[i] = 100*h + 10*d + u
    t = others[:]
    for v, m in zip(vals, mult): t += [v]*m
    draws.append(stats(t))
for k, name in enumerate(("zero-form", "nonzero-forms", "whole decade")):
    arr = sorted(d[k] for d in draws)
    print(f"{name:14s} target {t0[k]:.3f}  null mean {sum(arr)/len(arr):.3f}  p95 {arr[int(.95*len(arr))]:.3f}  p99 {arr[int(.99*len(arr))]:.3f}  pct {100*sum(1 for a in arr if a < t0[k])/len(arr):.1f}")
# vocabulary under collapse rules
def strip0(v):
    while v % 10 == 0 and v >= 10: v //= 10
    return v
def stripany(v):
    return v // 10 if v >= 100 else v
for name, f in (("as transcribed", lambda v: v), ("strip trailing zeros", strip0), ("strip one trailing digit from every value >= 100", stripany)):
    cc = Counter(f(v) for v in toks)
    print(f"{name:50s} distinct {len(cc):3d} singletons {sum(1 for n in cc.values() if n == 1):3d} max count {max(cc.values())}")
