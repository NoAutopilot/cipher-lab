#!/usr/bin/env python3
"""H47 (29 Sept 2026): are the O-family (O, O-TILDE, O-DASH2, O-DASHBELOW, ...) and X-family (X, X-DASH, X-BAR,
X-DOT, X-O, X-BAR-CC) members homophone variants of one unit each? For every pair of ids with >= 5 settled tokens,
the Jensen-Shannon divergence (bits) between their neighbour distributions (left and right neighbours pooled, as a
bag). Reference sets at the same counts: (a) 'unrelated' pairs -- every pair of ids >= 5 tokens not in the same
family; (b) planted variants -- the tokens of a frequent id (X, PCT, Y-CURL, CIRC-O) split at random into two pseudo-
ids of the family pair's sizes, JSD between the halves (what true variants of one unit look like at these counts).
A family pair whose JSD sits with (b) and below (a) is variant-like. Settled lines, punctuation and clear spans
dropped. Writes h47_families.json."""
import os, json, random, collections, math, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
sys.path.insert(0, here); from settled_lines import settled_lines
import csv
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
lines = [l for l in ([s for s in v if s not in PUNCT] for v in settled_lines(root, 'c', drop_clear=True).values()) if len(l) >= 2]
bm = {r['sign']: r['base'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/base_mark.tsv')), delimiter='\t')}
fam = lambda s: bm.get(s, s)
occ = collections.defaultdict(list)
for li, l in enumerate(lines):
    for i, s in enumerate(l): occ[s].append((li, i))
def nb(positions):
    c = collections.Counter()
    for li, i in positions:
        l = lines[li]
        if i > 0: c['L:' + l[i - 1]] += 1
        if i + 1 < len(l): c['R:' + l[i + 1]] += 1
    return c
def jsd(a, b):
    na, nb_ = sum(a.values()), sum(b.values()); out = 0
    for k in set(a) | set(b):
        p = a[k] / na; q = b[k] / nb_; m = (p + q) / 2
        if p: out += 0.5 * p * math.log2(p / m)
        if q: out += 0.5 * q * math.log2(q / m)
    return out
ids = [s for s in occ if len(occ[s]) >= 5]
pairs_same = [(a, b) for i, a in enumerate(ids) for b in ids[i + 1:] if fam(a) == fam(b) and fam(a) in ('O', 'X')]
pairs_unrel = [(a, b) for i, a in enumerate(ids) for b in ids[i + 1:] if fam(a) != fam(b)]
unrel = sorted(jsd(nb(occ[a]), nb(occ[b])) for a, b in pairs_unrel)
rng = random.Random(47); res = dict(unrelated=dict(n=len(unrel), median=round(unrel[len(unrel) // 2], 3), p10=round(unrel[len(unrel) // 10], 3)), family={})
for a, b in pairs_same:
    na, nbn = len(occ[a]), len(occ[b]); obs = jsd(nb(occ[a]), nb(occ[b]))
    planted = []
    for src in ('X', 'PCT', 'Y-CURL', 'CIRC-O'):
        pos = occ[src]
        if len(pos) < na + nbn: continue
        for _ in range(200):
            s = rng.sample(pos, na + nbn); planted.append(jsd(nb(s[:na]), nb(s[na:])))
    planted.sort()
    if not planted:
        res['family'][f'{a}|{b}'] = dict(sizes=[na, nbn], jsd=round(obs, 3), note='no source id large enough for a planted split'); print(a, b, res['family'][f'{a}|{b}']); continue
    # matched-count unrelated: same sizes drawn from two different unrelated ids
    mu = []
    for _ in range(400):
        x, y = rng.sample(pairs_unrel, 1)[0]
        if len(occ[x]) >= na and len(occ[y]) >= nbn: mu.append(jsd(nb(rng.sample(occ[x], na)), nb(rng.sample(occ[y], nbn))))
    mu.sort()
    res['family'][f'{a}|{b}'] = dict(sizes=[na, nbn], jsd=round(obs, 3), planted_median=round(planted[len(planted) // 2], 3), planted_p975=round(planted[int(0.975 * len(planted))], 3),
                                    unrelated_matched_median=round(mu[len(mu) // 2], 3) if mu else None, unrelated_matched_p025=round(mu[int(0.025 * len(mu))], 3) if mu else None,
                                    variant_like=obs <= planted[int(0.975 * len(planted))] and (not mu or obs < mu[int(0.025 * len(mu))]))
    print(a, b, res['family'][f'{a}|{b}'])
print('unrelated', res['unrelated']); json.dump(res, open(os.path.join(root, 'h47_families.json'), 'w'), indent=1)
