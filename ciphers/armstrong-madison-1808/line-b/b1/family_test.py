"""B1 companion 3: decade-family parse vs row parse.
Decade parse: 2-digit xy is a head; 3-digit xyz and 4-digit 1xyz belong to family xy (prefix 1, suffix z).
Row parse (a printed 100-row form): value = 100*column + row, so v aligns with 100h + v (same last two digits).
For each parse: corr(n(head v), n(members of v)) over v = 10..99, with the redraw null of decade_test.py
(3-digit AND 4-digit values redrawn within their hundreds block, units permuted within block); then the family
census under the decade parse."""
import os, random, sys
from collections import Counter, defaultdict
sys.path.insert(0, '.')
from padding_test import target_tokens
toks = target_tokens(); c = Counter(toks)
def corr(xs, ys):
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); sxx = sum((x-mx)**2 for x in xs); syy = sum((y-my)**2 for y in ys)
    return sxy / (sxx*syy) ** 0.5 if sxx and syy else 0.0
V = list(range(10, 100))
def fam3(cc, v): return sum(cc[10*v+u] for u in range(10))            # 3-digit members
def fam4(cc, v): return sum(cc[1000+10*v+u] for u in range(10))       # 4-digit members (prefix 1)
def row(cc, v): return sum(cc[100*h+v] for h in range(1, 19))         # same last two digits
def stats(t):
    cc = Counter(t); heads = [cc[v] for v in V]
    return (corr(heads, [fam3(cc, v) for v in V]), corr(heads, [fam4(cc, v) for v in V]),
            corr(heads, [fam3(cc, v)+fam4(cc, v) for v in V]), corr(heads, [row(cc, v) for v in V]),
            corr([fam3(cc, v) for v in V], [fam4(cc, v) for v in V]))
names = ("head~3-digit family", "head~4-digit family (1xyz)", "head~both", "head~same-row (100h+v)", "3-digit family~4-digit family")
t0 = stats(toks)
rng = random.Random(9)
big = [v for v in toks if v >= 100]; others = [v for v in toks if v < 100]
dist = sorted(set(big)); mult = [c[v] for v in dist]; units = [v % 10 for v in dist]; hund = [v // 100 for v in dist]
draws = []
for _ in range(int(os.environ.get("DRAWS", "2000"))):
    us = units[:]
    for hb in set(hund):
        idx = [i for i, h in enumerate(hund) if h == hb]; sub = [us[i] for i in idx]; rng.shuffle(sub)
        for i, u in zip(idx, sub): us[i] = u
    groups = defaultdict(list)
    for i, (h, u) in enumerate(zip(hund, us)): groups[(h, u)].append(i)
    vals = [0]*len(dist)
    for (h, u), idx in groups.items():
        for i, d in zip(idx, rng.sample(range(10), len(idx))): vals[i] = 100*h + 10*d + u
    t = others[:]
    for v, m in zip(vals, mult): t += [v]*m
    draws.append(stats(t))
print("statistic                          target  null_mean  p95    p99    percentile")
for k, name in enumerate(names):
    arr = sorted(d[k] for d in draws)
    print(f"{name:34s} {t0[k]:6.3f} {sum(arr)/len(arr):9.3f} {arr[int(.95*len(arr))]:6.3f} {arr[int(.99*len(arr))]:6.3f} {100*sum(1 for a in arr if a < t0[k])/len(arr):9.1f}")
# family census under the decade parse
def parse(v):
    if v < 10: return ('digit', v, None, None)
    if v < 100: return ('head', v, 0, None)
    if v < 1000: return ('fam', v // 10, 0, v % 10)
    return ('fam', (v - 1000) // 10, 1, v % 10)
fam = defaultdict(Counter); heads = Counter()
for v in toks:
    kind, r, p, z = parse(v)
    if kind == 'digit': fam['digits'][v] += 1
    elif kind == 'head': heads[r] += 1; fam[r][('head',)] += 1
    else: fam[r][(p, z)] += 1
roots = [r for r in fam if r != 'digits']
print(f"\nfamilies (2-digit roots 10-99) in use: {len(roots)} of 90; tokens in families {sum(sum(fam[r].values()) for r in roots)}; single-digit tokens {sum(fam['digits'].values())}")
print(f"roots occurring as a bare head: {sum(1 for r in roots if ('head',) in fam[r])}; roots with >=2 distinct forms: {sum(1 for r in roots if len(fam[r])>=2)}; roots with only one token: {sum(1 for r in roots if sum(fam[r].values())==1)}")
sizes = Counter(sum(fam[r].values()) for r in roots)
print("tokens per root (size: n roots):", sorted(sizes.items()))
z = Counter(); z1 = Counter()
for r in roots:
    for k, n in fam[r].items():
        if k != ('head',): (z if k[0]==0 else z1)[k[1]] += n
print("suffix digit profile, 3-digit tier:", sorted(z.items()), " 4-digit tier:", sorted(z1.items()))
print("\nrichest families (root: forms):")
for r in sorted(roots, key=lambda r: -sum(fam[r].values()))[:20]:
    forms = ", ".join(("%d" % r if k == ('head',) else "%s%d%d" % ("1" if k[0] else "", r, k[1])) + "x%d" % n for k, n in sorted(fam[r].items(), key=lambda kv: (kv[0] != ('head',), kv[0])))
    print(f"  {r:2d} ({sum(fam[r].values())}): {forms}")
