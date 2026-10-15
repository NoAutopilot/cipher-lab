#!/usr/bin/env python3
"""CL1161-S7 gate scoring per PREREG-CL1161-S7.md. python3 s7/s7_score.py (from the target folder)."""
import csv, itertools, os
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: {r[0]: r[1] for r in csv.reader(open(os.path.join(H, f)), delimiter='\t') if r and r[0].startswith('W')}
def agree(p, q):
    """best one-to-one group matching on windows both mark non-NONE; returns (agreed, n_both)."""
    ws = [w for w in p if p[w] != 'NONE' and q.get(w, 'NONE') != 'NONE']
    gp, gq = sorted({p[w] for w in ws}), sorted({q[w] for w in ws})
    best = 0
    for perm in itertools.permutations(gq, min(len(gp), len(gq))) if len(gq) >= len(gp) else []:
        best = max(best, sum(1 for w in ws if dict(zip(gp, perm)).get(p[w]) == q[w]))
    for perm in itertools.permutations(gp, len(gq)) if len(gp) > len(gq) else []:
        best = max(best, sum(1 for w in ws if dict(zip(gq, perm)).get(q[w]) == p[w]))
    return best, len(ws)
truth = {r[1]: r[4] for r in csv.reader(open(os.path.join(H, 'windows_key.tsv')), delimiter='\t') if r[0] == 'plant'}
groups = lambda p: {g: sum(1 for v in p.values() if v == g) for g in set(p.values()) if g != 'NONE'}
power = {}
for x in 'AB':
    p = rd(f'pass_plant_{x}.tsv'); a, n = agree(p, truth)   # NONE counts as wrong: score over 12
    power[x] = len(groups(p)) >= 2 and a >= 10
    print(f'POWER pass {x}: groups {groups(p)}, matches true q/qb on {a}/12 -> {"PASS" if power[x] else "FAIL"}')
for s in ('S', '7'):
    A, B = rd(f'pass_{s}_A.tsv'), rd(f'pass_{s}_B.tsv'); a, n = agree(A, B)
    big = lambda p: sum(1 for v in groups(p).values() if v >= 3)
    two = big(A) >= 2 and big(B) >= 2 and a >= 10 and n >= 9
    one = all(sum(1 for v in groups(p).values() if v > 1) <= 1 and sorted(groups(p).values())[:-1] in ([], [1]) for p in (A, B))
    one = one and all(power.values())
    v = 'TWO SHAPES' if two else 'ONE SHAPE' if one else 'UNDECIDED'
    print(f'{s}: groups A {groups(A)} B {groups(B)}; partitions agree {a}/{n} -> {v}')
