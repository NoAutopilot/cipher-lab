#!/usr/bin/env python3
"""MONL-K04: reconcile sortA/sortB under sort/k04/PREREG-MONL-K04.md -> sort/k04/reconciled.tsv; prints the relabel set. Run from the folder."""
import csv
SHIFT = {'c268d': 13, 'c268c': 5, 'c172': 0}
def load(f): return {(r['page'], r['passage'], r['pos']): r for r in csv.DictReader(open(f), delimiter='\t')}
A, B = load('sort/k04/sortA.tsv'), load('sort/k04/sortB.tsv')
cur = {}
for f in ('sort/k04/s268d_tiles.tsv', 'sort/k04/s268c_tiles.tsv', 'sort/k04/s172_tiles.tsv'):
    for r in csv.DictReader(open(f), delimiter='\t'):
        cur[({'s268d': 'c268d', 's268c': 'c268c', 's172': 'c172'}[r['run']], r['passage'], r['pos'])] = r['passC']
assert set(A) == set(B) == set(cur), (set(A) ^ set(cur), set(B) ^ set(cur))
ctl = [k for k in cur if k[0] == 'c172']; ref = [k for k in cur if k[0] != 'c172' and cur[k] == 'K12']
moved = lambda k, to: A[k]['label'] == B[k]['label'] == to
ctl_moved = sum(moved(k, 'K12') for k in ctl); ref_moved = sum(moved(k, 'K04') for k in ref)
block = ctl_moved >= 1 or ref_moved == len(ref)
out, rel = [], []
for k in sorted(cur, key=lambda k: (k[0], k[1], int(k[2]))):
    a, b = A[k], B[k]; line = f"L{int(k[1][1:]) + SHIFT[k[0]]:02d}" if k[0] != 'c172' else k[1]
    role = 'control' if k in ctl else 'k12-ref' if k in ref else 'lead'
    if a['label'] == b['label'] and 'L' not in (a['conf'], b['conf']):
        v = 'keep-agree' if a['label'] == cur[k] else 'relabel'
    elif a['label'] == b['label']: v = 'low-conf-agree'
    else: v = 'split'
    if v == 'relabel' and (role != 'lead' or block): v = 'relabel-blocked'
    if v == 'relabel': rel.append((line, k[2], cur[k], a['label']))
    out.append([k[0], line, k[2], role, cur[k], a['label'], a['conf'], b['label'], b['conf'], v])
with open('sort/k04/reconciled.tsv', 'w') as o:
    o.write('page\tline\tpos\trole\tcurrent\tA\tA_conf\tB\tB_conf\tverdict\n')
    for r in out: o.write('\t'.join(r) + '\n')
print(f'controls moved to K12 by both: {ctl_moved}/{len(ctl)}; K12 refs moved to K04 by both: {ref_moved}/{len(ref)}; blocked={block}')
print('relabels:', rel)
