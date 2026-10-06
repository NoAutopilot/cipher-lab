#!/usr/bin/env python3
"""R9-WVOX scorer: shape concordance between three sign inventories, same-letter count vs a within-key label permutation.

Usage: python3 score.py concordance.tsv [--draws 10000] [--seed 1564]
concordance.tsv columns: a_id  b_id  confidence(high|medium|low)  (ids: f.23 code, B## for 1069, C## for 174)
Only high+medium pairs are scored (pre-registered in ../PREREG-R9-WVOX.md).
"""
import random, sys, argparse, collections
ap = argparse.ArgumentParser(); ap.add_argument('conc'); ap.add_argument('--draws', type=int, default=10000)
ap.add_argument('--seed', type=int, default=1564); a = ap.parse_args()
S = '../../willem-van-hessen-1567/siblings/'
def tsv(p):
    return [l.rstrip('\n').split('\t') for l in open(p) if l.strip() and not l.startswith('#')][1:]
# f.23: letter only where pass A and pass B keys agree (gloss-derived); else unlabelled
ka = {r[0]: r[1] for r in tsv('../r9align/key_passA.tsv')}; kb = {r[0]: r[1] for r in tsv('../r9align/key_passB.tsv')}
lab = {'A': {c: ka[c] for c in ka if c in kb and ka[c] == kb[c] and not c.startswith('?')}}
lab['B'] = {f'B{i:02d}': ('NULL' if r[1] == 'o' else r[1]) for i, r in enumerate(tsv(S + 'key_1069.tsv'), 1)}
lab['C'] = {f'C{i:02d}': r[1] for i, r in enumerate([r for r in tsv(S + 'key_174_nomenclator.tsv') if r[0] == 'alphabet'], 1)}
fam = lambda x: 'B' if x[:1] == 'B' and x[1:].isdigit() else 'C' if x[:1] == 'C' and x[1:].isdigit() else 'A'
pairs = collections.defaultdict(list)
for r in tsv(a.conc):
    if r[2].strip().lower() not in ('high', 'medium'): continue
    x, y = r[0].strip(), r[1].strip(); fx, fy = fam(x), fam(y)
    if fx > fy: x, y, fx, fy = y, x, fy, fx
    if x in lab[fx] and y in lab[fy]: pairs[fx + fy].append((x, y))
def stat(L, P): return sum(L[fx][x] == L[fy][y] for x, y in P for fx, fy in [(fam(x), fam(y))])
rng = random.Random(a.seed)
print('labelled signs: f23 %d (of pass-agreed codes), 1069 %d, 174 %d' % tuple(len(lab[k]) for k in 'ABC'))
for key in ('AB', 'AC', 'BC'):
    P = pairs[key]; real = stat(lab, P); draws = []
    for _ in range(a.draws):
        L = {}
        for k in 'ABC':
            ks = list(lab[k]); vs = [lab[k][c] for c in ks]; rng.shuffle(vs); L[k] = dict(zip(ks, vs))
        draws.append(stat(L, P))
    draws.sort(); p95 = draws[int(0.95 * len(draws))]; mean = sum(draws) / len(draws)
    p = sum(d >= real for d in draws) / len(draws)
    name = {'AB': 'f23 vs 1069', 'AC': 'f23 vs 174', 'BC': '1069 vs 174'}[key]
    print(f'{name}: scored pairs {len(P)}, same-letter real {real}, perm mean {mean:.2f} p95 {p95} max {draws[-1]} p {p:.4f} -> {"PASS" if real > p95 else "FAIL/tie"}')
    for x, y in P: print(f'   {x}={lab[fam(x)][x]}  {y}={lab[fam(y)][y]}  {"SAME" if lab[fam(x)][x]==lab[fam(y)][y] else ""}')
