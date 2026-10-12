#!/usr/bin/env python3
"""TXE4-4 dev grid (PREREG-txeng4-4 step 5): apply every frozen (tau, eps) to pass A on dev_tune, score each with
tools/tx_bench.py --paired against the pass-A dev unit, choose max net subject to broken <= 1 (ties: larger tau, then
smaller eps). Writes dev_grid.tsv and dev_choice.json. Run from the repo root."""
import json, subprocess, sys, csv
W = 'benchmark-tx/txeng4/4'
DEV = [f'f178v_L{i:02d}' for i in range(1, 13)]
rows = []
for tau in (0.6, 0.7, 0.8, 0.9):
    for eps in (0.05, 0.1, 0.2):
        out = f'{W}/dev/A_tau{tau}_eps{eps}.tsv'
        subprocess.run([sys.executable, 'tools/tx_selfcheck.py', 'apply', '--topk', f'{W}/topk/no87_A.tsv', '--read',
                        'benchmark-tx/outputs/birago1572-no87/passA.tsv', '--fit', f'{W}/calib_fit.json', '--tau', str(tau),
                        '--eps', str(eps), '--out', out, '--lines'] + DEV, check=True, capture_output=True)
        nfl = sum(1 for _ in open(out + '.flips.tsv')) - 1
        j = json.loads(subprocess.run([sys.executable, 'tools/tx_bench.py', '--item', 'birago1572-no87', '--exclude-flagged',
                                       '--paired', 'benchmark-tx/txeng/units/passA_dev_tune.tsv', '--coverage-diagnostic',
                                       '--json', out], check=True, capture_output=True, text=True).stdout)
        it = j['items'][0]; am = it['paired']['as_measured']; fe = it['paired']['flagged_excluded']
        rows.append(dict(tau=tau, eps=eps, flips=nfl, fixed=am['fixed'], broken=am['broken'], net=am['fixed'] - am['broken'],
                         p=am['p'], err=it['err_true'], errors=it['errors'], scored=it['scored'],
                         fe_fixed=fe['fixed'], fe_broken=fe['broken'], fe_err=it['flagged_excluded']['err_true']))
cols = list(rows[0])
with open(f'{W}/dev_grid.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for r in rows:
        f.write('\t'.join(str(r[c]) for c in cols) + '\n')
ok = [r for r in rows if r['broken'] <= 1]
best = max(ok, key=lambda r: (r['net'], r['tau'], -r['eps'])) if ok else None
stop = all(r['net'] <= 0 for r in rows)
json.dump(dict(choice=best, stop_rule_dev_net_le_0_everywhere=stop), open(f'{W}/dev_choice.json', 'w'), indent=1)
for r in rows:
    print(r)
print('CHOICE', best, '| STOP before eval:', stop)
