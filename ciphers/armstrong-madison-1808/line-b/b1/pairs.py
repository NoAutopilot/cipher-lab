"""B1 companion: the (v, 10v) pair table, a count-correlation statistic with the same redraw null, and the
next-token class of v vs 10v (does the padded form keep the unpadded form's context?)."""
import random, sys
from collections import Counter
sys.path.insert(0, '.')
from padding_test import target_tokens, null_draws, stat
toks = target_tokens(); c = Counter(toks); present = set(c)
print("v  n(v)  n(10v)  n(100v)")
for v in sorted(x for x in present if x < 100):
    print(f"{v:3d} {c[v]:3d} {c[10*v]:5d} {c[100*v]:6d}")
# correlation statistic over v = 10..99
def corr(toks):
    c = Counter(toks)
    xs = [c[v] for v in range(10, 100)]; ys = [c[10*v] for v in range(10, 100)]
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    sxy = sum((x-mx)*(y-my) for x, y in zip(xs, ys)); sxx = sum((x-mx)**2 for x in xs); syy = sum((y-my)**2 for y in ys)
    return sxy / (sxx*syy) ** 0.5
rng = random.Random(5)
r = corr(toks)
# reuse null_draws machinery: rebuild draws of token lists
import padding_test as pt
def null_corr(weighted, draws=3000):
    cc = Counter(toks); x0 = sorted(v for v in cc if v >= 100 and v % 10 == 0)
    others = [v for v in toks if not (v >= 100 and v % 10 == 0)]
    pool = list(range(100, 1901, 10))
    hb = Counter(v // 100 for v in toks if v >= 100)
    w = [hb.get(p // 100, 0) + 0.25 for p in pool] if weighted else [1.0]*len(pool)
    mult = [cc[v] for v in x0]; out = []
    for _ in range(draws):
        avail = pool[:]; aw = w[:]; chosen = []
        for _ in x0:
            i = rng.choices(range(len(avail)), weights=aw)[0]; chosen.append(avail.pop(i)); aw.pop(i)
        t = others[:]
        for v, m in zip(chosen, mult): t += [v]*m
        out.append(corr(t))
    return out
for wname, weighted in (("uniform", False), ("hundreds-weighted", True)):
    nd = sorted(null_corr(weighted))
    p95 = nd[int(0.95*len(nd))]; p99 = nd[int(0.99*len(nd))]
    print(f"count-correlation n(v) vs n(10v), v=10..99: target {r:.3f}; {wname} null mean {sum(nd)/len(nd):.3f} p95 {p95:.3f} p99 {p99:.3f} percentile {100*sum(1 for a in nd if a < r)/len(nd):.1f}")
# contexts
seq = []
for line in open('../../ciphertext.txt'):
    if line.startswith('#'): continue
    for t in line.split():
        seq.append(int(t) if t.isdigit() else ('*' if t.startswith('*') else t))
def ctx(v):
    nxt = Counter(); prv = Counter()
    for i, t in enumerate(seq):
        if t == v:
            n = seq[i+1] if i+1 < len(seq) else None; p = seq[i-1] if i > 0 else None
            nxt['part' if isinstance(n, int) and n < 100 else 'book' if isinstance(n, int) else 'mark/none'] += 1
            prv['part' if isinstance(p, int) and p < 100 else 'book' if isinstance(p, int) else 'mark/none'] += 1
    return dict(prv), dict(nxt)
print("\ncontexts (prev class, next class):")
for v in (17, 170, 18, 180, 76, 760, 14, 140, 11, 110, 16, 160, 74, 740, 12, 120, 38, 380):
    print(v, c[v], ctx(v))
