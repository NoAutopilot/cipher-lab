#!/usr/bin/env python3
"""H45 (29 Sept 2026): is base+mark compositional? Table: for the 21 bases that carry a mark on some id
(glyphs/base_mark.tsv, 16 mark classes), token counts from the settled inventory (inventory_settled.tsv) of every
(base, mark) id including the unmarked base (mark 'none'). Statistic: G = 2 * sum O ln(O/E) against the independence
table E (base marginal x mark marginal / N) over the observed cells, divided by N (G/N; lower = more product-like,
i.e. base and mark chosen independently, as consonant sign and vowel mark would be). Null (can differ): 10,000
re-assignments of the target's own id counts to its ids at random (same set of (base, mark) pairs, same count
multiset, frequencies no longer tied to base or mark) -- a holistic inventory whose frequencies are arbitrary per id.
z < 0 (target more product-like than the null) supports composition. Power: a planted abugida from fr19 prose
syllables (base = onset consonants, mark = vowel nucleus, the commonest nucleus written unmarked; restricted to the
same number of bases and marks by frequency), scored the same way against its own count-shuffle null. Writes
h45_base_mark.json."""
import os, json, random, collections, math, sys, re
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); sys.path.insert(0, here)
import csv
bm = {r['sign']: (r['base'], r['mark']) for r in csv.DictReader(open(os.path.join(root, 'glyphs/base_mark.tsv')), delimiter='\t')}
cnt = {r['sign']: int(r['count']) for r in csv.DictReader(open(os.path.join(root, 'inventory_settled.tsv')), delimiter='\t')}
marked_bases = {b for s, (b, m) in bm.items() if m != 'none'}
cells = {bm[s]: cnt.get(s, 0) for s in bm if bm[s][0] in marked_bases and cnt.get(s, 0) > 0}
def gN(cells):
    N = sum(cells.values()); B = collections.Counter(); M = collections.Counter()
    for (b, m), c in cells.items(): B[b] += c; M[m] += c
    return 2 * sum(c * math.log(c * N / (B[b] * M[m])) for (b, m), c in cells.items() if c) / N
def test(cells, rng, T=10000):
    obs = gN(cells); keys = list(cells); vals = list(cells.values()); null = []
    for _ in range(T):
        rng.shuffle(vals); null.append(gN(dict(zip(keys, vals))))
    m = sum(null) / T; sd = (sum((x - m) ** 2 for x in null) / T) ** 0.5
    return dict(G_per_N=round(obs, 4), null_mean=round(m, 4), null_lo=round(sorted(null)[250], 4), null_hi=round(sorted(null)[9749], 4),
                z=round((obs - m) / sd, 2), p_le=sum(x <= obs for x in null) / T, cells=len(cells), N=sum(cells.values()))
rng = random.Random(45); out = dict(target=test(cells, rng))
out['target']['bases'] = len(marked_bases); out['target']['marks'] = len({m for (b, m) in cells})
print('target', out['target'])
import h3_unit_profile as h3
W = h3.corpus_words(); syl = [s for w in W[:200000] for s in h3.syll(w)]
def split(s):
    m = re.match(r'^([^aeiouy]*)([aeiouy]+)', s); return (m.group(1) or 'V', m.group(2)) if m else (s, 'none')
pairs = collections.Counter(split(s) for s in syl)
nuc = collections.Counter(); ons = collections.Counter()
for (o, n), c in pairs.items(): nuc[n] += c; ons[o] += c
top_n = [n for n, _ in nuc.most_common(out['target']['marks'])]; top_o = [o for o, _ in ons.most_common(out['target']['bases'])]
common = top_n[0]
Nt = out['target']['N']; total = sum(c for (o, n), c in pairs.items() if o in top_o and n in top_n)
ab = collections.Counter()
for (o, n), c in pairs.items():
    if o in top_o and n in top_n: ab[(o, 'none' if n == common else n)] += c
scale = Nt / total; ab = {k: max(0, round(v * scale)) for k, v in ab.items()}; ab = {k: v for k, v in ab.items() if v}
out['planted_abugida'] = test(ab, rng); print('abugida', out['planted_abugida'])
json.dump(out, open(os.path.join(root, 'h45_base_mark.json'), 'w'), indent=1)
