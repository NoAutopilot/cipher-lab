#!/usr/bin/env python3
"""TXE2-CELLS post-hoc movement table (after the scores; not a gate): per row, L, pick, new sign, L wrong?, new wrong?"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools')); import tx_bench as B
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
T = B.read_tsv(os.path.join(ROOT, 'benchmark-tx', 'birago1572-no87.truth.tsv'))
O = os.path.join(ROOT, 'benchmark-tx', 'outputs', 'birago1572-no87')
Lp = os.path.join(ROOT, 'benchmark-tx', 'txeng', 'units', 'labels_dev_tune.tsv')
Lout = B.load_output([Lp]); eL = B.position_errors(T, Lout)
for arm in ('real', 'control'):
    eX = B.position_errors(T, B.load_output([os.path.join(O, f'passX13_{arm}_dev_tune.tsv')]))
    picks = {}
    for f in sorted(os.listdir(HERE)):
        if f.startswith(f'reads_{arm}_'):
            for r in rd(os.path.join(HERE, f)): picks[r['row'].strip()] = r
    rows = []
    for k in rd(os.path.join(HERE, f'key_{arm}.tsv')):
        p = picks[k['row']]; pk = p['pick'].strip()
        new = k[pk.upper()] if pk.upper() in ('A', 'B') else k['L']
        kk = (k['line'], k['pos'])
        rows.append(dict(row=k['row'], line=k['line'], pos=k['pos'], L=k['L'], other=k['B'] if k['A'] == k['L'] else k['A'],
                         pick=pk, conf=p['conf'], new=new, L_wrong=int(bool(eL.get(kk))), new_wrong=int(bool(eX.get(kk))),
                         unscored=int(kk not in eL)))
    with open(os.path.join(HERE, f'movement_{arm}.tsv'), 'w') as f:
        cols = list(rows[0]); f.write('\t'.join(cols) + '\n')
        for r in rows: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    sc = [r for r in rows if not r['unscored']]
    print(arm, 'rows', len(rows), 'scored', len(sc), 'L wrong at rows', sum(r['L_wrong'] for r in sc),
          'moved', sum(r['new'] != r['L'] for r in sc), 'fixed', sum(r['L_wrong'] and not r['new_wrong'] for r in sc),
          'broken', sum(r['new_wrong'] and not r['L_wrong'] for r in sc))
