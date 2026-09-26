"""Power check for the adjacency-cosine block test (rule 3: the test must be able to see a block design at this N):
synthetic width-w block ciphers of German (composed_enhg) at the pool's N and line lengths, value drawn within a
block in proportion to the pool's own value counts; same statistic, same label-permutation null."""
import csv, math, random, re, sys
from collections import Counter, defaultdict
sys.path.insert(0, '../../tools')
rows = list(csv.DictReader(open('bmaln/pool_numeric_0_99.tsv'), delimiter='\t'))
lines = defaultdict(list)
for r in rows: lines[r['line']].append(int(r['sign']))
lens = [len(m) for m in lines.values()]; N = sum(lens)
pcnt = Counter(v for m in lines.values() for v in m)
text = re.sub('[^a-z]', '', open('../../tools/data/de16/composed_enhg.txt', encoding='utf-8', errors='ignore').read().lower())
def cos(a, b):
    num = sum(a[k]*b[k] for k in a if k in b); da = math.sqrt(sum(x*x for x in a.values())); db = math.sqrt(sum(x*x for x in b.values()))
    return num/(da*db) if da and db else None
def stats(msgs):
    cnt = Counter(v for m in msgs for v in m); c = defaultdict(Counter)
    for L in msgs:
        for i, x in enumerate(L):
            if i: c[x]['L%d' % L[i-1]] += 1
            if i+1 < len(L): c[x]['R%d' % L[i+1]] += 1
    def adj(inv):
        vals = [cos(c[inv[x]], c[inv[x+1]]) for x in range(99) if cnt[inv[x]] >= 5 and cnt[inv[x+1]] >= 5]
        vals = [v for v in vals if v is not None]; return sum(vals)/len(vals)
    real = adj(list(range(100))); rng = random.Random(1); null = []
    for _ in range(300):
        p = list(range(100)); rng.shuffle(p); null.append(adj(p))
    null.sort(); return real, null[284]
for w in (3, 4, 5):
    for seed in (1, 2, 3):
        rng = random.Random(seed); st = rng.randrange(len(text) - N - 10); pt = text[st:st+N]
        nb = math.ceil(100 / w); letters = [ch for ch, _ in Counter(text).most_common()]
        order = letters[:nb] + [rng.choice(letters) for _ in range(max(0, nb-len(letters)))]; rng.shuffle(order)
        vals_of = defaultdict(list)
        for v in range(100): vals_of[order[v // w]].append(v)
        msgs = []; i = 0
        for L in lens:
            m = []
            for ch in pt[i:i+L]:
                vs = vals_of.get(ch) or list(range(100))
                m.append(rng.choices(vs, weights=[pcnt[v]+0.5 for v in vs])[0])
            msgs.append(m); i += L
        real, p95 = stats(msgs)
        print(f'width {w} seed {seed}: adjacent cosine {real:.4f} vs label-permutation p95 {p95:.4f} -> {"DETECTED" if real > p95 else "missed"}')
