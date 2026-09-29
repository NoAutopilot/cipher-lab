#!/usr/bin/env python3
"""H34 (29 Sept 2026): long repeats. On the settled text (settled_lines, punctuation-class boxes dropped, lines
concatenated page by page), count the distinct n-grams occurring twice or more for n = 3, 4, 5+, and the total
number of positions they cover. Null (a): 1,000 within-line shuffles (kills word order inside a line, keeps each
line's multiset). Control (b): 200 samples of the H13 mixed design (h10_mixed.encode, q 0.3, fr19 prose) at the
target's N with pre-noise K matched as in H13 v2, then 10 pct noise of which half invents singleton types -- the
design that fits each cryptogram's single-sign profile (H13). A code or a syllabary that writes recurring words the
same way shows repeats beyond (a); beyond (b) means more phrase-level repetition than French prose under that design.
Lists every repeat of n >= 4 with its lines and whether a pictogram opens it. Writes h34_long_repeats.json."""
import os, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
import h3_unit_profile as h3, h10_mixed as h10, h13_newtype_noise as h13
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
def is_pict(s): return s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
raw = settled_lines(root, 'c')
lines = [(k, [s for s in v if s not in PUNCT]) for k, v in raw.items()]
def page(k): return {'c2a': 'c2', 'c2b': 'c2', 'c4a0': 'c4', 'c4a': 'c4', 'c4b': 'c4'}.get(k.split('_')[0], k.split('_')[0])
def repeats(seqs):
    r = {}
    for n in (3, 4, 5):
        c = collections.Counter()
        for s in seqs:
            for i in range(len(s) - n + 1): c[tuple(s[i:i + n])] += 1
        r[n] = sum(1 for v in c.values() if v >= 2)
    return r
def pages(ls):
    out = collections.OrderedDict()
    for k, l in ls: out.setdefault(page(k), []).extend(l)
    return list(out.values())
obs = repeats(pages(lines)); N = sum(len(l) for _, l in lines); K = len({s for _, l in lines for s in l})
print('target N', N, 'K', K, 'repeats', obs)
rng = random.Random(34); A = []
for _ in range(1000):
    sh = []
    for k, l in lines: c = l[:]; rng.shuffle(c); sh.append((k, c))
    A.append(repeats(pages(sh)))
W = h3.corpus_words(); Bs = []; p, f = 0.10, 0.5; K0 = max(10, int(K - round(p * f * N)))
while len(Bs) < 200:
    o = rng.randrange(len(W) - N); s = h10.encode(W[o:o + N], 0.3, K0, rng)[:N]
    if len(s) < N: continue
    Bs.append(repeats([h13.noise_new(s, p, f, rng)]))
def band(v, n):
    x = sorted(d[n] for d in v); return dict(lo=x[int(0.025 * len(x))], hi=x[int(0.975 * len(x)) - 1], median=x[len(x) // 2], p_ge=sum(y >= obs[n] for y in x) / len(x))
res = {n: dict(obs=obs[n], shuffle=band(A, n), mixed_design=band(Bs, n)) for n in (3, 4, 5)}
for n, d in res.items(): print(n, d)
# list the long repeats
seqs = pages(lines); lst = []
for n in (6, 5, 4):
    c = collections.defaultdict(list)
    for pi, s in enumerate(seqs):
        for i in range(len(s) - n + 1): c[tuple(s[i:i + n])].append((pi, i))
    for g, occ in c.items():
        if len(occ) >= 2 and not any(set(g) <= set(x['ngram']) and len(x['ngram']) > n for x in lst):
            lst.append(dict(ngram=list(g), n=n, occurrences=len(occ), pict_opens=is_pict(g[0]), where=occ))
for x in lst: print(x['n'], ' '.join(x['ngram']), x['occurrences'], x['where'])
json.dump(dict(N=N, K=K, stats=res, long_repeats=lst), open(os.path.join(root, 'h34_long_repeats.json'), 'w'), indent=1)
