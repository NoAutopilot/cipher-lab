#!/usr/bin/env python3
"""H41 (29 Sept 2026): is there any sequential order in the settled text once X is removed? Statistic: adjacent-sign
mutual information within lines (plug-in, bits) and the number of bigram types seen twice or more, on the settled
lines minus punctuation-class boxes and minus X. Null: 10,000 within-line shuffles (5,000 for speed are enough for a
2.5-97.5 band; 10,000 used). Power: 100 samples of two H39 best-fitting designs (h38_homophonic_fit.py's sample(),
X-free by construction), each cut into lines of the target's own line lengths, scored the same way against 200 of
their own within-line shuffles: the design's z-score (observed minus shuffle mean, over shuffle sd) is what the test
can see at this N. Also the target WITH X, for comparison. Writes h41_sequential.json."""
import os, json, random, collections, sys, math
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
sys.argv = [sys.argv[0], '--drop-x'] + sys.argv[1:]
import h38_homophonic_fit as h38
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
raw = settled_lines(root, 'c')
def stat(lines):
    bg = collections.Counter(); L = collections.Counter(); R = collections.Counter()
    for l in lines:
        for a, b in zip(l, l[1:]): bg[(a, b)] += 1; L[a] += 1; R[b] += 1
    n = sum(bg.values()); mi = sum(c / n * math.log2(c * n / (L[a] * R[b])) for (a, b), c in bg.items())
    return mi, sum(1 for c in bg.values() if c >= 2)
def z(lines, trials, rng):
    obs = stat(lines); sh = []
    for _ in range(trials):
        s = []
        for l in lines: c = l[:]; rng.shuffle(c); s.append(c)
        sh.append(stat(s))
    out = {}
    for k, name in enumerate(('MI', 'bigram_types_2plus')):
        v = sorted(x[k] for x in sh); m = sum(v) / len(v); sd = (sum((x - m) ** 2 for x in v) / len(v)) ** 0.5
        out[name] = dict(obs=round(obs[k], 4), lo=round(v[int(0.025 * len(v))], 4), hi=round(v[int(0.975 * len(v)) - 1], 4), z=round((obs[k] - m) / sd, 2) if sd else 0, p_ge=sum(x >= obs[k] for x in v) / len(v))
    return out
rng = random.Random(41); res = {}
for label, dropx in (('noX', True), ('withX', False)):
    ls = [[s for s in v if s not in PUNCT and not (dropx and s == 'X')] for v in raw.values()]
    ls = [l for l in ls if len(l) >= 2]
    res[label] = z(ls, 10000, rng); print(label, res[label])
lens = [len(l) for l in ([s for s in v if s not in PUNCT and s != 'X'] for v in raw.values()) if len(l) >= 2]
for cond in ((0.3, 2, 6, True, 0.1, 61), (0.2, 2, 3, True, 0.2, 32)):
    q, h, c, zipf, p, K0 = cond
    samples = []
    while len(samples) < 100:
        o = rng.randrange(len(h38.W) - h38.N); seq = h38.h10.encode(h38.W[o:o + h38.N], q, K0, rng)[:h38.N]
        if len(seq) < h38.N: continue
        seq = h38.split(seq, h, c, zipf, rng); seq = h38.h13.noise_new(seq, p, 0.5, rng)
        ls = []; j = 0
        for n in lens: ls.append(seq[j:j + n]); j += n
        r = z(ls, 200, rng); samples.append(r)
    key = f'design_q{q}_h{h}_c{c}_{"zipf" if zipf else "eq"}_p{p}_K0{K0}'
    res[key] = {k: dict(z_median=sorted(x[k]['z'] for x in samples)[50], share_above_p975=sum(x[k]['p_ge'] <= 0.025 for x in samples) / 100) for k in ('MI', 'bigram_types_2plus')}
    print(key, res[key])
json.dump(res, open(os.path.join(root, 'h41_sequential.json'), 'w'), indent=1)
