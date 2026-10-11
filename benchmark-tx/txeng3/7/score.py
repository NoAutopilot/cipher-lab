#!/usr/bin/env python3
"""TXE3-7 step 4 (the only step that reads truth): score every arm output with tools/tx_bench.py --exclude-flagged --paired,
as measured AND flagged-excluded, Wilson 95%. Paired bases: atlas outputs vs A1_atlas (the machine control) and vs the line read
of record; override outputs vs the line read. Writes results.tsv and results.json. Run from the repo root after run_arms.py."""
import csv, json, math, os, subprocess, sys
W = 'benchmark-tx/txeng3/7'; O = f'{W}/out'
ITEMS = {'birago1572-f152r': 'benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv',
         'birago1572-no87': 'benchmark-tx/outputs/birago1572-no87/passC.tsv'}
def wilson(k, n, z=1.96):
    if not n: return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)
def bench(out, item, base):
    cmd = [sys.executable, 'tools/tx_bench.py', out, '--item', item, '--exclude-flagged', '--paired', base, '--json']
    j = json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True).stdout)['items'][0]
    fe = j['flagged_excluded']; pa = j['paired']
    return dict(err=j['err_true'], k=j['errors'], n=j['scored'], ci=wilson(j['errors'], j['scored']),
                fe_err=fe['err_true'], fe_k=fe['errors'], fe_n=fe['scored'], fe_ci=wilson(fe['errors'], fe['scored']),
                fixed=pa['as_measured']['fixed'], broken=pa['as_measured']['broken'], p=pa['as_measured']['p'],
                fe_fixed=pa['flagged_excluded']['fixed'], fe_broken=pa['flagged_excluded']['broken'], fe_p=pa['flagged_excluded']['p'],
                lines_missing=j['lines_missing'], confusions=j['top_confusions'][:5])
rows = []; R = {}
for item, lineread in ITEMS.items():
    R[item] = {}
    R[item]['lineread'] = bench(lineread, item, lineread)
    for mode in ('atlas', 'override'):
        a1 = f'{O}/A1_{mode}_{item}.tsv'
        for tag in ['A0a', 'A1', 'A2'] + [f'A3s{s}' for s in range(1, 21)]:
            out = f'{O}/{tag}_{mode}_{item}.tsv'
            base = a1 if (mode == 'atlas' and tag != 'A1') else lineread
            r = bench(out, item, base); r['base'] = os.path.basename(base)
            if mode == 'atlas' and tag == 'A2':      # also vs the line read
                r['vs_lineread'] = {k: v for k, v in bench(out, item, lineread).items() if k in ('fixed', 'broken', 'p', 'fe_fixed', 'fe_broken', 'fe_p')}
            R[item][f'{tag}_{mode}'] = r
            rows.append((item, tag, mode, r['err'], f"{r['k']}/{r['n']}", f"{r['ci'][0]:.3f}-{r['ci'][1]:.3f}", r['fe_err'], f"{r['fe_k']}/{r['fe_n']}",
                         f"{r['fe_ci'][0]:.3f}-{r['fe_ci'][1]:.3f}", r['base'], r['fixed'], r['broken'], r['p'], r['fe_fixed'], r['fe_broken'], r['fe_p']))
with open(f'{W}/results.tsv', 'w') as f:
    f.write('item\tarm\tmode\terr_true\tk/n\twilson95\tfe_err_true\tfe_k/n\tfe_wilson95\tpaired_base\tfixed\tbroken\tp\tfe_fixed\tfe_broken\tfe_p\n')
    for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
json.dump(R, open(f'{W}/results.json', 'w'), indent=1)
# summary: the gate per item (atlas mode), null gains
for item in ITEMS:
    r1, r2 = R[item]['A1_atlas'], R[item]['A2_atlas']
    gain = r1['err'] - r2['err']; nulls = [r1['err'] - R[item][f'A3s{s}_atlas']['err'] for s in range(1, 21)]
    p95 = sorted(nulls)[int(round(0.95 * (20 - 1)))]
    print(f"{item}: lineread {R[item]['lineread']['err']:.3f} ({R[item]['lineread']['k']}/{R[item]['lineread']['n']}) | A0a {R[item]['A0a_atlas']['err']:.3f} | "
          f"A1 machine {r1['err']:.3f} ({r1['k']}/{r1['n']}) | A2 owner {r2['err']:.3f} ({r2['k']}/{r2['n']}) | gain A1-A2 {gain:+.4f} | "
          f"paired A2 vs A1 fixed {r2['fixed']} broken {r2['broken']} p {r2['p']} | null gains mean {sum(nulls)/20:+.4f} p95 {p95:+.4f} max {max(nulls):+.4f} | "
          f"gate transfers: {'PASS' if gain >= 0.02 and r2['fixed'] > r2['broken'] and r2['p'] < 0.05 and gain > p95 else 'FAIL/null'}")
    for tag in ('A1', 'A2'):
        o = R[item][f'{tag}_override']
        print(f"   {tag} override vs line read: {o['err']:.3f} ({o['k']}/{o['n']}) fixed {o['fixed']} broken {o['broken']} p {o['p']}")
