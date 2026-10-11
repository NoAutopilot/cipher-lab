#!/usr/bin/env python3
"""TXE3-7 RESCORE step 2 (the only step that reads truth; run after run_arms_la.py's outputs are committed). Scores with the
registered scorer call of ../score.py (tools/tx_bench.py --exclude-flagged --paired, Wilson 95% on err_true) and the
registered gate: TRANSFERS on a target iff A2 <= A1 - 0.02 AND fixed > broken with sign p < 0.05 AND gain > the p95 of the 20
null gains (p95 = sorted(null gains)[round(0.95 * 19)], as ../score.py).

Blocks written to results_la.json / results_la.tsv:
  scorer_drift   the registered outputs (../out) re-scored now, against ../results.json (must be identical);
  registered     the registered arms through the corrected no.87 map (out/*_birago1572-no87.tsv) and, for f152r, the
                 registered map unchanged (../out) -- the re-run the brief asks for;
  f152r_la       f152r through its label-aware twin map (sensitivity, out/*_birago1572-f152r.tsv);
  posthoc        A2x (X_NEW-l -> T19), POST HOC: under the registered maps (out_oldmap, reproduces the second check) and
                 under the corrected maps (out), each paired against A1 under the same map.
Run from the repo root: python3 benchmark-tx/txeng3/7/rescore/score_la.py"""
import json, math, os, subprocess, sys
X = 'benchmark-tx/txeng3/7'; R = f'{X}/rescore'
LR = {'birago1572-f152r': 'benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv',
      'birago1572-no87': 'benchmark-tx/outputs/birago1572-no87/passC.tsv'}
NULLS = [f'A3s{s}' for s in range(1, 21)]


def wilson(k, n, z=1.96):
    if not n: return (0, 0)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def bench(out, item, base):
    cmd = [sys.executable, 'tools/tx_bench.py', out, '--item', item, '--exclude-flagged', '--paired', base, '--json']
    j = json.loads(subprocess.run(cmd, check=True, capture_output=True, text=True).stdout)['items'][0]
    fe = j['flagged_excluded']; pa = j['paired']; am = pa['as_measured']; pf = pa['flagged_excluded']
    return dict(err=j['err_true'], k=j['errors'], n=j['scored'], ci=wilson(j['errors'], j['scored']),
                fe_err=fe['err_true'], fe_k=fe['errors'], fe_n=fe['scored'],
                fixed=am['fixed'], broken=am['broken'], p=am['p'], lines_improved=am['lines_improved'],
                lines_worsened=am['lines_worsened'], line_p=am['line_p'],
                fe_fixed=pf['fixed'], fe_broken=pf['broken'], fe_p=pf['p'], confusions=j['top_confusions'][:6])


def arm_set(odir, item, tags=('A0a', 'A1', 'A2'), nulls=True):
    o = {'lineread': bench(LR[item], item, LR[item])}
    for mode in ('atlas', 'override'):
        a1 = f'{odir}/A1_{mode}_{item}.tsv'
        for tag in list(tags) + (NULLS if nulls else []):
            base = a1 if (mode == 'atlas' and tag != 'A1') else LR[item]
            r = bench(f'{odir}/{tag}_{mode}_{item}.tsv', item, base); r['base'] = os.path.relpath(base, X)
            if tag in ('A2', 'A2x') and mode == 'atlas':
                r['vs_lineread'] = {k: v for k, v in bench(f'{odir}/{tag}_{mode}_{item}.tsv', item, LR[item]).items()
                                    if k in ('fixed', 'broken', 'p', 'line_p')}
            o[f'{tag}_{mode}'] = r
    return o


def gate(o, owner='A2'):
    r1, r2 = o['A1_atlas'], o[f'{owner}_atlas']
    gain = round(r1['err'] - r2['err'], 4)
    ng = sorted(round(r1['err'] - o[f'{s}_atlas']['err'], 4) for s in NULLS)
    p95 = ng[int(round(0.95 * 19))]
    ok = gain >= 0.02 and r2['fixed'] > r2['broken'] and r2['p'] < 0.05 and gain > p95
    return dict(A1=r1['err'], owner=r2['err'], gain=gain, fixed=r2['fixed'], broken=r2['broken'], p=r2['p'],
                line_p=r2['line_p'], null_gain_mean=round(sum(ng) / 20, 4), null_p95=p95, null_max=ng[-1],
                verdict='TRANSFERS (PASS)' if ok else 'FAIL / null')


OUT = {}
# 1. scorer drift: registered outputs re-scored now vs ../results.json
reg = json.load(open(f'{X}/results.json')); drift = {}
for item in LR:
    for key in ('lineread', 'A1_atlas', 'A2_atlas', 'A1_override', 'A2_override'):
        if key == 'lineread':
            r = bench(LR[item], item, LR[item])
        else:
            tag, mode = key.split('_'); base = f'{X}/out/A1_atlas_{item}.tsv' if (mode == 'atlas' and tag != 'A1') else LR[item]
            r = bench(f'{X}/out/{key}_{item}.tsv', item, base)
        then = reg[item][key]
        drift[f'{item}:{key}'] = dict(now=(r['k'], r['n'], r['fixed'], r['broken']), registered=(then['k'], then['n'], then['fixed'], then['broken']),
                                      same=(r['k'], r['n'], r['fixed'], r['broken']) == (then['k'], then['n'], then['fixed'], then['broken']))
OUT['scorer_drift'] = drift
print('scorer drift: all registered figures reproduce' if all(d['same'] for d in drift.values()) else f'SCORER DRIFT: {drift}')

# 2. registered arms, corrected no.87 map; f152r registered map unchanged
OUT['registered'] = {'birago1572-no87': arm_set(f'{R}/out', 'birago1572-no87'),
                     'birago1572-f152r': arm_set(f'{X}/out', 'birago1572-f152r')}
OUT['f152r_la'] = arm_set(f'{R}/out', 'birago1572-f152r')
OUT['gate'] = {'no87 corrected map': gate(OUT['registered']['birago1572-no87']),
               'f152r registered map': gate(OUT['registered']['birago1572-f152r']),
               'f152r label-aware map (sensitivity)': gate(OUT['f152r_la'])}
# 3. POST HOC A2x
ph = {}
for item in LR:
    ph[f'{item} registered maps'] = {}
    for mode in ('atlas', 'override'):
        base_old = f'{X}/out/A1_{mode}_{item}.tsv' if mode == 'atlas' else LR[item]
        base_new = f'{R}/out/A1_{mode}_{item}.tsv' if mode == 'atlas' else LR[item]
        ph[f'{item} registered maps'][f'A2x_{mode}'] = bench(f'{R}/out_oldmap/A2x_{mode}_{item}.tsv', item, base_old)
    ph[f'{item} corrected maps'] = {f'A2x_{mode}': bench(f'{R}/out/A2x_{mode}_{item}.tsv', item,
                                                        f'{R}/out/A1_{mode}_{item}.tsv' if mode == 'atlas' else LR[item]) for mode in ('atlas', 'override')}
    ph[f'{item} corrected maps']['A2x_atlas_vs_A2'] = bench(f'{R}/out/A2x_atlas_{item}.tsv', item, f'{R}/out/A2_atlas_{item}.tsv')
OUT['posthoc'] = ph
gx = {}
for item in LR:
    corrected = OUT['registered'][item] if item.endswith('no87') else OUT['f152r_la']
    for lab, base_set in (('registered maps', reg[item]), ('corrected maps', corrected)):
        o = dict(base_set); o['A2x_atlas'] = ph[f'{item} {lab}']['A2x_atlas']   # A2x paired vs A1 under the same map
        gx[f'{item} {lab}'] = gate(o, owner='A2x')
OUT['posthoc_gate_shape'] = gx


def pooled(rows):
    f = sum(r['fixed'] for r in rows); b = sum(r['broken'] for r in rows)
    from math import comb
    n = f + b; k = min(f, b); p = min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n) if n else 1.0
    return dict(fixed=f, broken=b, p=round(p, 4))


OUT['pooled'] = {'registered A2 vs A1 (no87 corrected + f152r registered)': pooled([OUT['registered'][i]['A2_atlas'] for i in LR]),
                 'registered A2 vs A1 (no87 corrected + f152r label-aware)': pooled([OUT['registered']['birago1572-no87']['A2_atlas'], OUT['f152r_la']['A2_atlas']]),
                 'POST HOC A2x vs A1 (corrected maps)': pooled([ph[f'{i} corrected maps']['A2x_atlas'] for i in LR])}
json.dump(OUT, open(f'{R}/results_la.json', 'w'), indent=1)
with open(f'{R}/results_la.tsv', 'w') as f:
    f.write('block\titem\tarm\tmode\terr_true\tk/n\twilson95\tfe_err_true\tfe_k/n\tpaired_base\tfixed\tbroken\tp\tline_p\n')
    for blk, items in (('registered', OUT['registered']), ('f152r_la', {'birago1572-f152r': OUT['f152r_la']})):
        for item, o in items.items():
            for key, r in o.items():
                arm, _, mode = key.partition('_')
                f.write('\t'.join(map(str, (blk, item, arm, mode or 'lineread', r['err'], f"{r['k']}/{r['n']}", f"{r['ci'][0]:.3f}-{r['ci'][1]:.3f}",
                                             r['fe_err'], f"{r['fe_k']}/{r['fe_n']}", r.get('base', ''), r['fixed'], r['broken'], r['p'], r['line_p']))) + '\n')
    for blk, o in ph.items():
        for key, r in o.items():
            f.write('\t'.join(map(str, ('POSTHOC ' + blk, blk.split()[0], 'A2x', key, r['err'], f"{r['k']}/{r['n']}", f"{r['ci'][0]:.3f}-{r['ci'][1]:.3f}",
                                         r['fe_err'], f"{r['fe_k']}/{r['fe_n']}", 'A2' if key.endswith('vs_A2') else ('A1' if 'atlas' in key else 'lineread'),
                                         r['fixed'], r['broken'], r['p'], r['line_p']))) + '\n')
for k, g in OUT['gate'].items():
    print(f'REGISTERED GATE {k}: A1 {g["A1"]} A2 {g["owner"]} gain {g["gain"]:+.4f} fixed/broken {g["fixed"]}/{g["broken"]} p {g["p"]} line_p {g["line_p"]} null p95 {g["null_p95"]:+.4f} -> {g["verdict"]}')
for k, g in gx.items():
    print(f'POST HOC (gate shape only) {k}: A1 {g["A1"]} A2x {g["owner"]} gain {g["gain"]:+.4f} fixed/broken {g["fixed"]}/{g["broken"]} p {g["p"]} line_p {g["line_p"]} -> {g["verdict"]} (post hoc, not reportable as a PASS)')
for k, v in OUT['pooled'].items():
    print('pooled', k, v)
for item in LR:
    for t in ('A1', 'A2'):
        o = OUT['registered'][item][f'{t}_override']; print(f'override {item} {t}: {o["err"]} ({o["k"]}/{o["n"]}) vs line read fixed {o["fixed"]} broken {o["broken"]} p {o["p"]}')
    print(f'{item} lineread {OUT["registered"][item]["lineread"]["err"]} A0a {OUT["registered"][item]["A0a_atlas"]["err"]}')
