#!/usr/bin/env python3
"""Control (b), WVO-1068-KEY: shape concordance of key_1068 against key_1069 (B) and f.23's gloss key (A), scored as in
R9-WVOX (../../../wvo-hessen-1564/r9wvox/score.py): S = high+medium concordant pairs whose two letters are equal; null =
letters permuted within each key over its labelled signs, 10000 draws. Prereg: PREREG-WVO1068-CONC.md.

Usage: python3 concord_1068.py [--conc concordance_1068.tsv] [--draws 10000] [--seed 1068]
"""
import argparse, collections, random
from pathlib import Path
HERE = Path(__file__).parent
R9 = HERE / '../../../wvo-hessen-1564'
ap = argparse.ArgumentParser(); ap.add_argument('--conc', default=str(HERE / 'concordance_1068.tsv'))
ap.add_argument('--draws', type=int, default=10000); ap.add_argument('--seed', type=int, default=1068); a = ap.parse_args()
def tsv(p):
    return [l.rstrip('\n').split('\t') for l in open(p, encoding='utf-8') if l.strip() and not l.startswith('#')][1:]
ka = {r[0]: r[1] for r in tsv(R9 / 'r9align/key_passA.tsv')}; kb = {r[0]: r[1] for r in tsv(R9 / 'r9align/key_passB.tsv')}
lab = {'A': {c: ka[c] for c in ka if c in kb and ka[c] == kb[c] and not c.startswith('?')}}
lab['B'] = {f'B{i:02d}': ('NULL' if r[1] == 'o' else r[1]) for i, r in enumerate(tsv(HERE / '../key_1069.tsv'), 1)}
lab['D'] = {f'D{i:02d}': r[1] for i, r in enumerate(tsv(HERE / '../key_1068.tsv'), 1) if r[1] != '?' and not r[1].startswith('^')}
shapes = [r[0] for r in tsv(HERE / 'k1068_shapes.tsv')]
assert len(shapes) == len(tsv(HERE / '../key_1068.tsv')), 'k1068_shapes.tsv out of step with key_1068.tsv'
fam = lambda x: 'D' if x[:1] == 'D' and x[1:].isdigit() else 'B' if x[:1] == 'B' and x[1:].isdigit() else 'A'
pairs = collections.defaultdict(list); listed = collections.Counter()
for r in tsv(a.conc):
    x, y = r[0].strip(), r[1].strip(); fy = fam(y); listed[fy] += 1
    if r[2].strip().lower() not in ('high', 'medium'): continue
    if x in lab['D'] and y in lab[fy]: pairs['D' + fy].append((x, y))
def stat(L, P): return sum(L['D'][x] == L[fam(y)][y] for x, y in P)
rng = random.Random(a.seed)
print('labelled signs: 1068 %d, 1069 %d, f23 %d' % (len(lab['D']), len(lab['B']), len(lab['A'])))
for key, name in (('DB', '1068 vs 1069'), ('DA', '1068 vs f.23')):
    P = pairs[key]; real = stat(lab, P); draws = []
    for _ in range(a.draws):
        L = {}
        for k in 'ABD':
            ks = list(lab[k]); vs = [lab[k][c] for c in ks]; rng.shuffle(vs); L[k] = dict(zip(ks, vs))
        draws.append(stat(L, P))
    draws.sort(); p95 = draws[int(0.95 * len(draws))]; mean = sum(draws) / len(draws)
    p = sum(d >= real for d in draws) / len(draws)
    deg = ' (degenerate null: non-test)' if p95 == draws[-1] == real else ''
    print(f'{name}: pairs listed {listed[key[1]]}, scored (high+medium, both labelled) {len(P)}, same-letter real {real} of {len(P)}, '
          f'perm mean {mean:.2f} p95 {p95} max {draws[-1]} p {p:.4f} -> {"PASS" if real > p95 else "FAIL/tie"}{deg}')
    for x, y in P: print(f'   {x}={lab["D"][x]}  {y}={lab[fam(y)][y]}  {"SAME" if lab["D"][x] == lab[fam(y)][y] else ""}')
