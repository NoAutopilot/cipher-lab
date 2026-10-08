#!/usr/bin/env python3
"""SIG-B228B: score the blind reads under prereg_sig2.md. Shapes: b167228/sig2/shapes{A,B}.tsv; marks: marks{A,B}.tsv; key_private2.tsv.
Writes b167228/sig2_shape_map.tsv (per-token u4/4u override for to_pipe.py) only if the decoy gate passes, and b167228/sig2_marks.tsv
(per-token 71 mark) only if the mark gate passes. Usage: python3 b167228/sig2_score.py (target folder)"""
import csv
D = 'b167228/sig2/'
rd = lambda f, k: {r[k]: r for r in csv.DictReader(open(D + f), delimiter='\t')}
K = rd('key_private2.tsv', 'id')
A, B = rd('shapesA.tsv', 'tile'), rd('shapesB.tsv', 'tile')
m = lambda r: r['match'].strip().lower()
dec = [k for k in K if K[k]['role'].startswith('DECOY')]
ok = sum(m(A[k]) == m(B[k]) == K[k]['role'].split('=')[1] for k in dec)
gate = ok >= 2
print(f'decoy gate: {ok}/3 matched right by both reads ->', 'PASS' if gate else 'FAIL')
out = ['line\tcol\tvalue\tA\tB']
for k in sorted(K, key=lambda k: K[k]['role']):
    if not k.startswith('U'):
        continue
    r = K[k]; a, b = m(A[k]), m(B[k])
    print(f"  {k} {r['role']:16s} {r['where']:14s} A {a:5s} B {b:5s} conf {A[k]['conf']}/{B[k]['conf']}")
    if r['role'].startswith('target') and a == b and a in ('a', 't'):
        page, line, col = 'v', r['where'][2:7], r['where'].split('_c')[1]
        out.append(f"{page}_{line}\t{col}\t{a}\t{a}\t{b}")
if gate:
    open('b167228/sig2_shape_map.tsv', 'w').write('\n'.join(out) + '\n')
print('shape overrides:', len(out) - 1, '(written)' if gate else '(not written: gate failed)')
MA, MB = rd('marksA.tsv', 'crop'), rd('marksB.tsv', 'crop')
acu = [k for k in K if K[k]['role'] == 'control:acute']; non = [k for k in K if K[k]['role'] == 'control:none']
ga = sum(MA[k]['mark'] == MB[k]['mark'] == 'acute' for k in acu); gn = sum(MA[k]['mark'] == MB[k]['mark'] == 'none' for k in non)
mg = ga >= 3 and gn >= 1
print(f'mark gate: acute controls {ga}/4, none controls {gn}/2 ->', 'PASS' if mg else 'FAIL')
for k in sorted(K):
    if k.startswith('N'):
        print(f"  {k} {K[k]['role']:14s} {K[k]['where']:14s} A {MA[k]['mark']:8s} B {MB[k]['mark']}")
mo = ['line\toccurrence\tcode\tmark\tA\tB']
for k in K:
    if K[k]['role'] == 'target:71' and MA[k]['mark'] == MB[k]['mark'] and MA[k]['mark'] in ('none', 'acute'):
        mo.append(f"v_a_L01\t{K[k]['where'][-1]}\t71\t{'' if MA[k]['mark'] == 'none' else chr(39)}\t{MA[k]['mark']}\t{MB[k]['mark']}")
if mg:
    open('b167228/sig2_marks.tsv', 'w').write('\n'.join(mo) + '\n')
print('mark changes:', len(mo) - 1, '(written)' if mg else '(not written: gate failed)')
