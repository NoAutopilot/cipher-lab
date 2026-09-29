#!/usr/bin/env python3
"""H46 (29 Sept 2026): the neighbours of X. On the settled lines (punctuation and clear spans dropped), the entropy of
the sign just left of X and just right of X (X-X pairs counted as X), against (a) 10,000 within-line shuffles (a sign
placed freely has near-shuffle context entropy; a unit bound into words has lower) and (b) the same statistic for
frequency-matched non-X ids (the eight next most frequent ids, each against its own shuffle null, reported as z).
Entropy is plug-in in bits over the neighbour tokens; since it is biased by count, every comparison is against the
same id's own shuffle. Writes h46_x_context.json."""
import os, json, random, collections, math, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
lines = [l for l in ([s for s in v if s not in PUNCT] for v in settled_lines(root, 'c', drop_clear=True).values()) if len(l) >= 2]
def H(c):
    n = sum(c.values()); return -sum(v / n * math.log2(v / n) for v in c.values()) if n else 0
def ctx(ls, t):
    L = collections.Counter(); R = collections.Counter()
    for l in ls:
        for i, s in enumerate(l):
            if s != t: continue
            if i > 0: L[l[i - 1]] += 1
            if i + 1 < len(l): R[l[i + 1]] += 1
    return H(L), H(R)
def test(t, rng, T):
    obs = ctx(lines, t); null = []
    for _ in range(T):
        sh = []
        for l in lines: c = l[:]; rng.shuffle(c); sh.append(c)
        null.append(ctx(sh, t))
    r = {}
    for k, name in enumerate(('left', 'right')):
        v = [x[k] for x in null]; m = sum(v) / T; sd = (sum((x - m) ** 2 for x in v) / T) ** 0.5
        r[name] = dict(obs=round(obs[k], 3), null_mean=round(m, 3), z=round((obs[k] - m) / sd, 2) if sd else 0, p_le=sum(x <= obs[k] for x in v) / T)
    return r
rng = random.Random(46); cnt = collections.Counter(s for l in lines for s in l)
out = dict(X=test('X', rng, 10000)); print('X', cnt['X'], out['X'])
for t, c in cnt.most_common(9)[1:]:
    out[t] = test(t, rng, 2000); print(t, c, out[t])
json.dump(out, open(os.path.join(root, 'h46_x_context.json'), 'w'), indent=1)
