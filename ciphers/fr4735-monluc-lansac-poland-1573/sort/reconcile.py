#!/usr/bin/env python3
"""MONL-SORT reconciliation (PREREG-MONL-SORT.md rule): relabel only where both blind sorts give the other cell of the pair and
neither is conf L. Writes sort/reconciled.tsv. Run from the folder: python3 sort/reconcile.py"""
import csv
def rd(p): return {(r['page'], r['passage'], r['pos']): r for r in csv.DictReader(open(p), delimiter='\t')}
A = {**rd('sort/sortA_c268.tsv'), **rd('sort/sortA_c172.tsv')}; B = {**rd('sort/sortB_c268.tsv'), **rd('sort/sortB_c172.tsv')}
cur = {}
for pg, f in (('c268', 'sort/c268_tiles.tsv'), ('c172', 'sort/c172_tiles.tsv')):
    for r in csv.DictReader(open(f), delimiter='\t'):
        cur[(pg, r['passage'], r['pos'])] = r['passC']
CTL = {('c172', 'L03', '26'), ('c172', 'L03', '52'), ('c172', 'L04', '13'), ('c172', 'L04', '19'),
       ('c172', 'L02', '48'), ('c172', 'L02', '54'), ('c172', 'L03', '40')}
out, n = [], {}
for k in sorted(cur):
    a, b, c = A[k], B[k], cur[k]
    if a['label'] == b['label'] != c and 'L' not in (a['conf'], b['conf']):
        act = 'relabel'
    elif a['label'] == b['label'] == c:
        act = 'keep-agree'
    else:
        act = 'keep-' + ('low-conf' if a['label'] == b['label'] else 'split')
    n[act] = n.get(act, 0) + 1
    out.append([*k, c, a['label'], a['conf'], b['label'], b['conf'], 'control' if k in CTL else '', act])
ctl_bad = sum(1 for k in CTL if A[k]['label'] != cur[k] and B[k]['label'] != cur[k])
with open('sort/reconciled.tsv', 'w') as o:
    o.write('page\tpassage\tpos\tcurrent\tsortA\tconfA\tsortB\tconfB\tcontrol\taction\n')
    for r in out: o.write('\t'.join(r) + '\n')
print(n, 'controls moved by both sorts:', ctl_bad, 'of', len(CTL))
for r in out:
    if r[-1] == 'relabel': print(' '.join(r))
