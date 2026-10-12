#!/usr/bin/env python3
"""TXE4-4: controls (a) permuted labels and (b) random flips, on dev_tune, at the grid's best-net setting (tau 0.8, eps 0.1,
identical flips to every tau >= 0.7 cell), scored the same way as the grid. Beside the dev result; the eval gate was never
reached (no feasible dev setting). Run from the repo root."""
import json, subprocess, sys
W = 'benchmark-tx/txeng4/4'
DEV = [f'f178v_L{i:02d}' for i in range(1, 13)]
TAU, EPS = 0.8, 0.1
def score(out):
    j = json.loads(subprocess.run([sys.executable, 'tools/tx_bench.py', '--item', 'birago1572-no87', '--exclude-flagged', '--paired',
                                   'benchmark-tx/txeng/units/passA_dev_tune.tsv', '--coverage-diagnostic', '--json', out],
                                  check=True, capture_output=True, text=True).stdout)['items'][0]['paired']['as_measured']
    return j['fixed'], j['broken']
res = {'a_permuted': [], 'b_random': []}
for s in range(1, 21):
    out = f'{W}/dev_ctrl/a_perm{s}.tsv'
    subprocess.run([sys.executable, 'tools/tx_selfcheck.py', 'apply', '--topk', f'{W}/topk/no87_A_perm{s}.tsv', '--read',
                    'benchmark-tx/outputs/birago1572-no87/passA.tsv', '--fit', f'{W}/calib_fit.json', '--tau', str(TAU), '--eps', str(EPS),
                    '--out', out, '--lines'] + DEV, check=True, capture_output=True)
    nfl = sum(1 for _ in open(out + '.flips.tsv')) - 1
    f, b = score(out); res['a_permuted'].append(dict(seed=s, flips=nfl, fixed=f, broken=b, net=f - b))
    out = f'{W}/dev_ctrl/b_rand{s}.tsv'
    subprocess.run([sys.executable, 'tools/tx_selfcheck.py', 'apply', '--topk', f'{W}/topk/no87_A.tsv', '--read',
                    'benchmark-tx/outputs/birago1572-no87/passA.tsv', '--random', '11', '--seed', str(s), '--out', out, '--lines'] + DEV,
                   check=True, capture_output=True)
    f, b = score(out); res['b_random'].append(dict(seed=s, flips=11, fixed=f, broken=b, net=f - b))
for k, v in list(res.items()):
    nets = sorted(r['net'] for r in v)
    res[k + '_summary'] = dict(net_min=nets[0], net_max=nets[-1], net_mean=sum(nets) / len(nets), net_p95=nets[int(round(0.95 * (len(nets) - 1)))],
                               flips_mean=sum(r['flips'] for r in v) / len(v), fixed_mean=sum(r['fixed'] for r in v) / len(v),
                               broken_mean=sum(r['broken'] for r in v) / len(v))
json.dump(res, open(f'{W}/dev_controls.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k.endswith('summary')}, indent=1))
print('a nets', [r['net'] for r in res['a_permuted']]); print('b nets', [r['net'] for r in res['b_random']])
