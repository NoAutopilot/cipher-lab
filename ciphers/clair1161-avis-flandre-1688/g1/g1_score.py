#!/usr/bin/env python3
"""C1161-G1 (15 Oct 2026): score blind passes D (group 1 fresh pass B) and E (fourth reader on f, dia) as PREREG g1/PREREG-C1161-G1.md.
  python3 g1/g1_score.py  -> g1/concordance_g1.tsv, summary on stdout"""
import csv, collections, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); X = os.path.join(T, 'exc')
def rd(p): return list(csv.DictReader(open(p), delimiter='\t'))
def col(a):
    a = (a or '').strip()
    return a if a.startswith(('nom:', 'null:')) or a in ('none', '') else a.split(':')[0]
def answers(P, g):
    ids = {r['id']: r['label'] for r in rd(os.path.join(X, f'ids_{P}.tsv'))}
    return {ids[r['id']]: r['sheet'] for r in rd(os.path.join(X, f'pass_{P}_g{g}.tsv'))}
key = {r['sign']: r['value'] for r in rd(os.path.join(T, 'key.tsv'))}
A1 = answers('A', 1); D = answers('D', 1); E = answers('E', 1)
A = {**answers('A', 3), **answers('A', 4)}; B = {**answers('B', 3), **answers('B', 4)}; C = answers('C', 1)
powD = col(D['qb']) == 'a'; powE = col(E['sd']) == 'g' and col(E['y']) == 'r'
print('POWER D', 'PASS' if powD else 'FAIL', D['qb'], '| POWER E', 'PASS' if powE else 'FAIL', E['sd'], E['y'])
out = []
for l in 'd psi rot s th tri'.split():
    a, d = col(A1[l]), col(D[l])
    if not powD: v, his = 'NON-TEST (power)', ''
    elif a == d and a not in ('none', ''): v, his = 'MAPPED', a
    elif 'none' in (a, d): v, his = 'NO MATCH', ''
    else: v, his = 'UNDECIDED', ''
    out.append((l, A1[l], D[l], '', '', v, his))
for l in ('f', 'dia'):
    votes = [col(x[l]) for x in (A, B, C, E) if l in x]
    c = collections.Counter(v for v in votes if v not in ('none', ''))
    top = c.most_common(2)
    if powE and top and top[0][1] >= 2 and (len(top) == 1 or top[1][1] < top[0][1]): v, his = f'FINAL ({top[0][1]} of 4)', top[0][0]
    else: v, his = 'UNDECIDED', ''
    out.append((l, A[l], E[l], B[l], C.get(l, ''), v, his))
with open(os.path.join(H, 'concordance_g1.tsv'), 'w') as f:
    f.write('label\tpassA\tpassD_or_E\tpassB\tpassC\tverdict\this_value_blind\tours_value\tconcordance\n')
    for l, a, d, b, c, v, his in out:
        his_l = his.replace('u/v', 'u')
        conc = '' if not his else ('agree' if his_l == key.get(l) else 'disagree')
        f.write(f'{l}\t{a}\t{d}\t{b}\t{c}\t{v}\t{his}\t{key.get(l, "")}\t{conc}\n')
        print(l, v, his, 'ours', key.get(l), conc)
