#!/usr/bin/env python3
"""GLY-11106 (8 Oct 2026): known-answer check of the WVO 11106 atlas. On boxes that atlas/map_tx.py matched 1:1 and
firmly to a position both readers agreed on, purity = share of boxes carrying their cluster's majority label; the null
is the same statistic with the labels permuted among those boxes (seeded, 2000 draws), which keeps cluster sizes and the
label distribution and so can differ from the target. Per look-alike pair (the tx/focus.tsv classes): boxes of the two
labels only, pair purity vs its own permutation null. Descriptive, no gate. Writes atlas/purity.tsv."""
import csv, random
from collections import Counter, defaultdict
from pathlib import Path
here = Path(__file__).resolve().parent
cl = {r['id']: r['cluster'] for r in csv.DictReader(open(here / 'clusters.tsv'), delimiter='\t') if r['kind'] == 'sign'}
bm = [r for r in csv.DictReader(open(here / 'boxmap.tsv'), delimiter='\t') if r['firm'] == '1' and r['agree'] == '1' and r['kind'] == 'cipher']
def purity(pairs):
    pairs = list(pairs)
    g = defaultdict(Counter)
    for c, l in pairs: g[c][l] += 1
    return sum(max(v.values()) for v in g.values()) / max(1, len(pairs))
def test(rows, n=2000, seed=11106):
    cs, ls = [cl[r['sid']] for r in rows], [r['label'] for r in rows]
    real = purity(zip(cs, ls)); rnd = random.Random(seed); null = []
    for _ in range(n): l2 = ls[:]; rnd.shuffle(l2); null.append(purity(zip(cs, l2)))
    null.sort(); return real, sum(null) / n, null[int(.95 * n)], sum(x >= real for x in null) / n
out = [('scope', 'n', 'purity', 'null_mean', 'null_p95', 'p')]
r = test(bm); out.append(('all firm+agreed', len(bm), *r))
for a, b in [('d', 'dd'), ('y', 'yx'), ('s', 'S'), ('g', 'G'), ('g', 'q'), ('g', '9'), ('z', '2'), ('s', '5'), ('n', 'u'), ('g', 'y')]:
    rows = [x for x in bm if x['label'] in (a, b)]
    k = Counter(x['label'] for x in rows)
    if k[a] and k[b]: out.append((f'{a}/{b} ({k[a]}/{k[b]})', len(rows), *test(rows)))
    else: out.append((f'{a}/{b} ({k[a]}/{k[b]})', len(rows), '', '', '', ''))
with open(here / 'purity.tsv', 'w') as o:
    for row in out: o.write('\t'.join(f'{v:.3f}' if isinstance(v, float) else str(v) for v in row) + '\n')
print(open(here / 'purity.tsv').read())
