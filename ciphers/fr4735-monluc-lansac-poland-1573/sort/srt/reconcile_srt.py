#!/usr/bin/env python3
"""MONL-SORT2: reconcile sort/srt/sortA.tsv and sortB.tsv under sort/srt/PREREG-MONL-SORT2.md -> sort/srt/reconciled.tsv; prints each
family's control/reference counts, its decision and the relabel set (Family C: leads only, never relabelled). Run from the folder."""
import csv
def load(f): return {(r['page'].strip(), r['passage'].strip(), r['pos'].strip()): r for r in csv.DictReader(open(f), delimiter='\t')}
A, B = load('sort/srt/sortA.tsv'), load('sort/srt/sortB.tsv')
R = {(r['page'], r['passage'], r['pos']): r for r in csv.DictReader(open('sort/srt/roles.tsv'), delimiter='\t')}
assert set(A) == set(B) == set(R), (set(A) ^ set(R), set(B) ^ set(R))
goes = lambda k, to: A[k]['label'] == B[k]['label'] == to and 'L' not in (A[k]['conf'], B[k]['conf'])
fam = lambda f, ro: [k for k in R if R[k]['family'] == f and R[k]['role'] == ro]
dec = {}
ca = sum(goes(k, 'K12') for k in fam('A', 'control')); ra = sum(A[k]['label'] == B[k]['label'] == 'K04' for k in fam('A', 'ref'))
dec['A'] = 'non-discriminating' if ca >= 2 or ra == 2 else 'relabel-allowed'
cb = sum(goes(k, 'K37') for k in fam('B', 'control')); rb = sum(A[k]['label'] == B[k]['label'] == 'K14' for k in fam('B', 'ref'))
dec['B'] = 'non-discriminating' if cb >= 1 or rb == 2 else 'relabel-allowed'
refc = sum(goes(k, R[k]['current']) for k in fam('C', 'ref'))
dec['C'] = 'leads-only'
TO = {'A': 'K12', 'B': 'K37'}
out, rel = [], []
for k in sorted(R, key=lambda k: (int(R[k]['line'][1:]), int(R[k]['pos']))):
    r, a, b = R[k], A[k], B[k]
    if a['label'] == b['label'] and 'L' not in (a['conf'], b['conf']):
        v = 'keep-agree' if a['label'] == r['current'] else 'moves'
    elif a['label'] == b['label']: v = 'low-conf-agree'
    else: v = 'split'
    if v == 'moves' and r['role'] == 'lead' and r['family'] in TO and dec[r['family']] == 'relabel-allowed' and a['label'] == TO[r['family']]:
        v = 'relabel'; rel.append((r['line'], int(r['pos']), r['current'], a['label']))
    elif v == 'moves': v = 'moves-not-applied'
    out.append([r['line'], r['pos'], r['family'], r['role'], r['candidates'], r['current'], a['label'], a['conf'], b['label'], b['conf'], v])
with open('sort/srt/reconciled.tsv', 'w') as o:
    o.write('line\tpos\tfamily\trole\tcandidates\tcurrent\tA\tA_conf\tB\tB_conf\tverdict\n')
    for x in out: o.write('\t'.join(x) + '\n')
print(f'A (K04|K12): d-facing controls gone K12 {ca}/3; K12 refs gone K04 {ra}/2 -> {dec["A"]}')
print(f'B (K14|K37): p-facing controls gone K37 {cb}/2; K37 refs gone K14 {rb}/2 -> {dec["B"]}')
print(f'C (K40|K41, K39|K45): refs kept by both {refc}/4 -> leads only')
print('relabels:', rel)
