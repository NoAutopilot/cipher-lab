#!/usr/bin/env python3
"""TXE4-6 unit 5: score the eval_heldout (376) restriction and summarise every pool with the controls and the gate.
Writes eval_eh.json and summary.txt. Run after the restrictions are committed (SHA256SUMS.prescore)."""
import json, sys, subprocess
sys.path.insert(0, 'benchmark-tx/txeng4/6'); sys.path.insert(0, 'tools')
import run_eval as R
import tx_bench as TB
O = R.O
res = json.load(open(f'{O}/eval.json'))
import os
eh = json.load(open(f'{O}/eval_eh.json')) if os.path.exists(f'{O}/eval_eh.json') else None
eh = eh or dict(T=R.score_one(f'{O}/out/no87_R_eh.tsv', f'{O}/out/no87_base_eh.tsv', 'birago1572-no87', ['--coverage-diagnostic']))
if 'perm' not in eh:
  eh['perm'] = [R.score_one(f'{O}/out/ctrl/no87_perm{s}_eh.tsv', f'{O}/out/no87_base_eh.tsv', 'birago1572-no87', ['--coverage-diagnostic']) for s in R.SEEDS]
  eh['coin'] = [R.score_one(f'{O}/out/ctrl/no87_coin{s}_eh.tsv', f'{O}/out/no87_base_eh.tsv', 'birago1572-no87', ['--coverage-diagnostic']) for s in R.SEEDS]
  json.dump(eh, open(f'{O}/eval_eh.json', 'w'), indent=1)
  txt = subprocess.run(['python3', 'tools/tx_bench.py', f'{O}/out/no87_R_eh.tsv', '--bench', 'BENCHMARK-TX.tsv', '--item', 'birago1572-no87',
                      '--exclude-flagged', '--paired', f'{O}/out/no87_base_eh.tsv', '--strict', '--coverage-diagnostic'], capture_output=True, text=True).stdout
  open(f'{O}/eval_tx_bench.txt', 'a').write('\n== no87 eval_heldout (376: f178v L13-23 + f179r L01-03): ' + txt)


def fb(j, mask):
    p = j['items'][0]['paired'][mask]
    return p['fixed'], p['broken']


def rate(j, mask):
    it = j['items'][0]
    d = it if mask == 'as_measured' else it['flagged_excluded']
    return d['errors'], d['scored']


out = []
pools = {'eval_heldout(376)+f152r': [('no87', eh['T'], eh['perm'], eh['coin']), ('f152r', res['f152r:f152r'], res['f152r:f152r:controls']['perm'], res['f152r:f152r:controls']['coin'])],
         'eval17(460, incl. f178r)+f152r': [('no87', res['no87:eval_heldout'], res['no87:eval_heldout:controls']['perm'], res['no87:eval_heldout:controls']['coin']),
                                           ('f152r', res['f152r:f152r'], res['f152r:f152r:controls']['perm'], res['f152r:f152r:controls']['coin'])]}
for mask in ('as_measured', 'flagged_excluded'):
    for pname, parts in pools.items():
        F = B = 0; nets_perm = [0] * 20; nets_coin = [0] * 20; lines = []
        for item, T, perm, coin in parts:
            f, b = fb(T, mask); F += f; B += b
            e, n = rate(T, mask)
            w = TB.wilson(e, n)
            lines.append(f'  {item}: fixed {f} broken {b}; err_true {e}/{n} = {e / n:.3f} (Wilson {w[0]:.3f}-{w[1]:.3f})')
            for s in range(20):
                pf, pb = fb(perm[s], mask); nets_perm[s] += pf - pb
                cf, cb = fb(coin[s], mask); nets_coin[s] += cf - cb
        sp = sorted(nets_perm); p95 = sp[int(round(0.95 * 19))]
        p = TB.sign_test(F, B)
        out.append(f'[{mask}] pool {pname}: pooled fixed {F} broken {B} net {F - B}, exact two-sided p = {p:.4f}; '
                   f'control (a) permuted labels net per seed {nets_perm} -> p95 {p95}, mean {sum(nets_perm) / 20:.2f}; '
                   f'control (b) coin net per seed {nets_coin} -> mean {sum(nets_coin) / 20:.2f}')
        out += lines
        g1 = F > B and p < 0.05; g2 = (F - B) > p95
        out.append(f'  gate: fixed > broken p < 0.05: {"PASS" if g1 else "FAIL"}; net > control (a) p95: {"PASS" if g2 else "FAIL"}')
# per-item err_true not higher (gate line 3), as measured
eT = rate(eh['T'], 'as_measured'); eB = rate(R.score_one(f'{O}/out/no87_base_eh.tsv', f'{O}/out/no87_base_eh.tsv', 'birago1572-no87', ['--coverage-diagnostic']), 'as_measured')
fT = rate(res['f152r:f152r'], 'as_measured'); fB = rate(R.score_one(R.ITEMS['f152r']['base'], R.ITEMS['f152r']['base'], 'birago1572-f152r'), 'as_measured')
out.append(f'gate line 3 (as-measured err_true not higher on any item): no87 eval_heldout T {eT[0]}/{eT[1]} vs base {eB[0]}/{eB[1]}; f152r T {fT[0]}/{fT[1]} vs base {fB[0]}/{fB[1]}; gunther: non-test (not pooled)')
open(f'{O}/summary.txt', 'w').write('\n'.join(out) + '\n')
print('\n'.join(out))
