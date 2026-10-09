#!/usr/bin/env python3
"""TXE2-BASE-SPIN: per-position detail of the one score (same truth load, label map and alignment as tools/tx_bench.py).
Prints flagged-excluded wrong/deleted counts per file, the paired fixed/broken positions old->new, and the three
sheet-defect positions (PREREG-txeng2-0 Amendments 4-5) separately. Writes score/positions.tsv."""
import os, sys
sys.path.insert(0, 'tools')
import tx_bench as T
O = 'benchmark-tx/outputs/spinelli-c1519-confirm/'
item = [r for r in T.read_tsv('BENCHMARK-TX.tsv') if r['item'] == 'spinelli-c1519-confirm'][0]
truth = T.map_truth(T.read_tsv(os.path.join('.', item['truth'])), T.load_label_map('benchmark-tx/txeng/confirm/collapse_map.tsv'))
files = {'pipeline_old': 'passZ_pipeline.tsv', 'passZ_v4': 'passZ_v4.tsv', 'passA_v4': 'passA_v4.tsv', 'passB_v4': 'passB_v4.tsv'}
lm = T.load_label_map('benchmark-tx/txeng/confirm/collapse_map.tsv')
E = {}
for k, f in files.items():
    ol = T.load_output([O + f], None)
    ol = {ln: [lm.get(s, s) for s in v] for ln, v in ol.items()}
    E[k] = T.position_errors(truth, ol)
    Ef = T.position_errors(T.drop_flagged(truth), ol)
    print('%-13s position errors (wrong+deleted): as measured %d/%d | flagged-excluded %d/%d' % (k, sum(E[k].values()), len(E[k]), sum(Ef.values()), len(Ef)))
    E[k + '_fx'] = Ef
flag = {(r['line'], r['pos']) for r in truth if r['status'] == 'scored' and T.is_flagged(r)}
defect = [('p1c_L01', '14'), ('p1c_L01', '15'), ('p1c_L03', '25')]
b, n = E['pipeline_old'], E['passZ_v4']
with open('benchmark-tx/txeng2/basespin/score/positions.tsv', 'w') as f:
    f.write('line\tpos\told_err\tnew_err\tflagged\tsheet_defect\tchange\n')
    for k in sorted(set(b) | set(n), key=lambda t: (t[0], float(t[1]))):
        ch = 'fixed' if b.get(k) and not n.get(k) else 'broken' if n.get(k) and not b.get(k) else ''
        if b.get(k) or n.get(k):
            f.write('%s\t%s\t%d\t%d\t%s\t%s\t%s\n' % (k[0], k[1], b.get(k, 0), n.get(k, 0), 'y' if k in flag else '', 'y' if k in defect else '', ch))
for k in sorted(set(b) & set(n), key=lambda t: (t[0], float(t[1]))):
    if b[k] != n[k]:
        print('%s %s.%s%s%s' % ('fixed ' if b[k] else 'broken', k[0], k[1], ' [flagged]' if k in flag else '', ' [sheet-defect]' if k in defect else ''))
for k in defect:
    print('sheet-defect %s.%s: in scored set %s; old err %s, new err %s' % (k[0], k[1], k in b, b.get(k), n.get(k)))
