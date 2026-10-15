#!/usr/bin/env python3
"""MONL-CTL: reconcile sortA/sortB under sort/ctl/PREREG-MONL-CTL.md -> sort/ctl/reconciled.tsv; prints the control count, the
keep/revert decision and the lead relabel set. Run from the folder."""
import csv
SHIFT = {'c268d': 13, 'c268c': 5}
CTL = {('L17', '16'), ('L19', '2'), ('L20', '23'), ('L20', '33')}
REF = {('L19', '6'), ('L20', '32')}
def load(f): return {(r['page'], r['passage'], r['pos']): r for r in csv.DictReader(open(f), delimiter='\t')}
A, B = load('sort/ctl/sortA.tsv'), load('sort/ctl/sortB.tsv')
cur = {}
for f in ('sort/ctl/s268d_tiles.tsv', 'sort/ctl/s268c_tiles.tsv'):
    for r in csv.DictReader(open(f), delimiter='\t'):
        cur[({'s268d': 'c268d', 's268c': 'c268c'}[r['run']], r['passage'], r['pos'])] = r['passC']
assert set(A) == set(B) == set(cur), (set(A) ^ set(cur), set(B) ^ set(cur))
line = lambda k: f"L{int(k[1][1:]) + SHIFT[k[0]]:02d}"
goes = lambda k, to: A[k]['label'] == B[k]['label'] == to and 'L' not in (A[k]['conf'], B[k]['conf'])
role = lambda k: 'control-d' if (line(k), k[2]) in CTL else 'k12-ref' if (line(k), k[2]) in REF else 'lead'
ctl_k12 = sum(goes(k, 'K12') for k in cur if role(k) == 'control-d')
ref_k04 = sum(A[k]['label'] == B[k]['label'] == 'K04' for k in cur if role(k) == 'k12-ref')
decision = 'non-discriminating' if ref_k04 == len(REF) else 'revert' if ctl_k12 >= 2 else 'keep'
out, rel = [], []
for k in sorted(cur, key=lambda k: (line(k), int(k[2]))):
    a, b = A[k], B[k]
    if a['label'] == b['label'] and 'L' not in (a['conf'], b['conf']):
        v = 'keep-agree' if a['label'] == cur[k] else 'relabel'
    elif a['label'] == b['label']: v = 'low-conf-agree'
    else: v = 'split'
    if v == 'relabel' and (role(k) != 'lead' or decision != 'keep'): v = 'relabel-blocked'
    if v == 'relabel': rel.append((line(k), k[2], cur[k], a['label']))
    out.append([k[0], line(k), k[2], role(k), cur[k], a['label'], a['conf'], b['label'], b['conf'], v])
with open('sort/ctl/reconciled.tsv', 'w') as o:
    o.write('page\tline\tpos\trole\tcurrent\tA\tA_conf\tB\tB_conf\tverdict\n')
    for r in out: o.write('\t'.join(r) + '\n')
print(f'd-facing controls gone K12: {ctl_k12}/{len(CTL)}; K12 refs moved to K04 by both: {ref_k04}/{len(REF)}; decision={decision}'
      + (' (warning: 1 control moved)' if ctl_k12 == 1 else ''))
print('relabels:', rel)
