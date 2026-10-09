#!/usr/bin/env python3
"""Selection-bias control for TXE2-DOUBT (X9): the best OR-of-<=3 rule at <= 15% flagged, re-chosen on dev_tune with L's
wrong-position labels permuted across the scored positions (200 seeds). The truth is opened only through
tools/tx_doubt.errors_for (tools/tx_bench.position_errors). Run from the repo root:
    python3 benchmark-tx/txeng2/doubt/selection_null.py"""
import json, os, random, sys
sys.path.insert(0, 'tools')
import tx_doubt as TD
O = 'benchmark-tx/txeng2/doubt'
rows = TD.rd(f'{O}/dev_tune_signals2.tsv')
wrong = TD.errors_for(TD.D['truth'], 'benchmark-tx/txeng/units/labels_dev_tune.tsv')
sigs = TD.signal_cols(rows[0])
keys = sorted(wrong)
real = TD.best_combos(rows, wrong, sigs, 3, [0.15])[(3, 0.15)]
vals = [wrong[k] for k in keys]
null = []
for seed in range(200):
    random.Random(seed).shuffle(vals)
    w = dict(zip(keys, vals))
    null.append(TD.best_combos(rows, w, sigs, 3, [0.15])[(3, 0.15)]['recall'])
null.sort()
p = (1 + sum(1 for x in null if x >= real['recall'])) / (1 + len(null))
out = dict(real=real, null_mean=sum(null) / len(null), null_p95=null[int(0.95 * len(null)) - 1], null_max=null[-1],
           n_null_ge_0p7=sum(1 for x in null if x >= 0.7), p=p, seeds=len(null))
json.dump(out, open(f'{O}/selection_null.json', 'w'), indent=1)
print(json.dumps(out, indent=1))
