#!/usr/bin/env python3
"""MONL-ADH reconciliation (PREREG-MONL-ADH.md part 2, the MONL-VB rule): relabel only where both blind sorts give the other cell of the pair and
neither is conf L; nothing if both sorts move 2+ of the 7 c172 controls. Reads sort/adh/sort{A,B}.tsv (the 2 calls' answers each,
concatenated), writes sort/adh/reconciled.tsv with c268c band ids mapped back to c268 lines (band L0n = c268 L(n+5)).
Run from the folder: python3 sort/adh/reconcile_adh.py"""
import csv
def rd(p):
    return {(r['page'], r['passage'], r['pos']): r for r in csv.DictReader(open(p), delimiter='\t') if r.get('pos')}
A, B = rd('sort/adh/sortA.tsv'), rd('sort/adh/sortB.tsv')
cur = {}
for pg, f in (('c268c', 'sort/adh/s268c_tiles.tsv'), ('c172', 'sort/adh/s172_tiles.tsv')):
    for r in csv.DictReader(open(f), delimiter='\t'):
        cur[(pg, r['passage'], r['pos'])] = (r['passC'], r['candidates'].split(','))
def line(pg, p): return f'L{int(p[1:]) + 5:02d}' if pg == 'c268c' else p
out, n = [], {}
for k in sorted(cur, key=lambda k: (k[0], line(k[0], k[1]), int(k[2]))):
    a, b = A.get(k, {'label': 'MISSING', 'conf': 'L'}), B.get(k, {'label': 'MISSING', 'conf': 'L'})
    c, cands = cur[k]
    other = [x for x in cands if x != c][0]
    if a['label'] == b['label'] == other and 'L' not in (a['conf'], b['conf']):
        act = 'relabel'
    elif a['label'] == b['label'] == c:
        act = 'keep-agree'
    elif a['label'] == b['label'] == other:
        act = 'keep-low-conf'
    else:
        act = 'keep-split'
    n[act] = n.get(act, 0) + 1
    out.append([k[0], line(k[0], k[1]), k[2], c, a['label'], a['conf'], b['label'], b['conf'], 'control' if k[0] == 'c172' else '', act])
ctl_bad = sum(1 for r in out if r[8] and r[4] != r[3] and r[6] != r[3])
with open('sort/adh/reconciled.tsv', 'w') as o:
    o.write('page\tline\tpos\tcurrent\tsortA\tconfA\tsortB\tconfB\tcontrol\taction\n')
    for r in out: o.write('\t'.join(r) + '\n')
print(n, 'controls moved by both sorts:', ctl_bad, 'of 7', '-> GATE FAIL, relabel nothing' if ctl_bad >= 2 else '-> gate ok')
for r in out:
    if r[-1] == 'relabel': print(' '.join(r))
