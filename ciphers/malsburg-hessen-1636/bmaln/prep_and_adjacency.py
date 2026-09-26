"""bMALN (26 Sept 2026): numeric-only pool (values 0-99) for block_homophonic, and the direct block test:
under a contiguous-block table, values v and v+1 (same block) encode the same letter, so their bigram-context
profiles (left+right neighbour counts) should be closer than those of random value pairs. Control: the same
statistic under random relabelings of the 100 values (permutation of labels on the same data), so the
adjacency structure is destroyed while every count is kept -- this control can differ from the target."""
import csv, math, random, sys
from collections import Counter, defaultdict
rows = list(csv.DictReader(open('pool/pooled.tsv'), delimiter='\t'))
msgs = defaultdict(list); drop_hi = drop_non = 0
for r in rows:
    s = r['sign']
    if s.isdigit():
        v = int(s)
        if v <= 99: msgs[r['line']].append(v)
        else: drop_hi += 1
    else: drop_non += 1
keep = sum(len(m) for m in msgs.values())
with open('bmaln/pool_numeric_0_99.tsv', 'w') as f:
    f.write('line\tposition\tsign\n')
    for ln, m in msgs.items():
        for i, v in enumerate(m, 1): f.write(f'{ln}\t{i}\t{v}\n')
print(f'kept {keep} tokens in {len(msgs)} lines, K={len({v for m in msgs.values() for v in m})}; dropped >=100: {drop_hi}, non-numeric: {drop_non}')

def ctx(label):
    c = defaultdict(Counter)
    for m in msgs.values():
        L = [label[v] for v in m]
        for i, x in enumerate(L):
            if i > 0: c[x]['L%d' % L[i-1]] += 1
            if i + 1 < len(L): c[x]['R%d' % L[i+1]] += 1
    return c
def cos(a, b):
    num = sum(a[k]*b[k] for k in a if k in b)
    da = math.sqrt(sum(x*x for x in a.values())); db = math.sqrt(sum(x*x for x in b.values()))
    return num/(da*db) if da and db else None
cnt = Counter(v for m in msgs.values() for v in m)
def stat(label, minc=5):
    c = ctx(label); inv = {label[v]: v for v in label}
    vals = []
    for v in range(99):
        a, b = label[v], label[v+1]
        if cnt[v] >= minc and cnt[v+1] >= minc:
            x = cos(c[a], c[b]);
            if x is not None: vals.append(x)
    return sum(vals)/len(vals), len(vals)
ident = {v: v for v in range(100)}
real, n = stat(ident)
# random-pair baseline within the real data: mean cosine over all pairs of values with count>=5
c = ctx(ident); ok = [v for v in range(100) if cnt[v] >= 5]
allp = [cos(c[a], c[b]) for i, a in enumerate(ok) for b in ok[i+1:]]
print(f'adjacent-pair context cosine (v,v+1, both count>=5): {real:.4f} over {n} pairs; all-pair mean {sum(allp)/len(allp):.4f}')
rng = random.Random(1); null = []
for _ in range(1000):
    p = list(range(100)); rng.shuffle(p); lab = {v: p[v] for v in range(100)}
    # permute labels: data value v becomes p[v]; adjacency now asks about original values whose labels are adjacent
    inv = {p[v]: v for v in range(100)}
    vals = []
    for x in range(99):
        a, b = inv[x], inv[x+1]
        if cnt[a] >= 5 and cnt[b] >= 5:
            y = cos(c[a], c[b])
            if y is not None: vals.append(y)
    null.append(sum(vals)/len(vals))
null.sort()
print(f'label-permutation control (1000): mean {sum(null)/len(null):.4f}, p95 {null[949]:.4f}, p99 {null[989]:.4f}; real rank p = {sum(x >= real for x in null)/1000:.3f}')
# same statistic at gaps 2..5 (block widths): within-block pairs at distance d
for d in (2, 3, 4, 5):
    vals = [cos(c[v], c[v+d]) for v in range(100-d) if cnt[v] >= 5 and cnt[v+d] >= 5]
    print(f'  distance {d}: mean {sum(vals)/len(vals):.4f} over {len(vals)}')
