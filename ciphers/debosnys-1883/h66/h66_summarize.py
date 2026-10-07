#!/usr/bin/env python3
"""Summarise runs.jsonl against PREREG.md's gates; writes result.json."""
import json, os, statistics as st
HERE = os.path.dirname(os.path.abspath(__file__))
R = [json.loads(l) for l in open(os.path.join(HERE, 'runs.jsonl')) if l.strip()]
def p95(v): v = sorted(v); return v[min(len(v) - 1, int(0.95 * len(v)))]
out = {}
for q in (0.35, 0.5):
    c = sorted((r for r in R if r['mode'] == 'ctl' and r['q'] == q), key=lambda r: r['seed'])
    n = [r['Smax'] for r in R if r['mode'] == 'ctlnull' and r['q'] == q]
    thr = p95(n); hits = sum(r['Smax'] > thr for r in c)
    out[f'ctl_q{q}'] = dict(ctl_Smax=[r['Smax'] for r in c], null_Smax=sorted(n), null_p95=thr, hits=hits,
                            n=len(c), passed=hits >= 8, sel_null_precision=[r['sel_null_precision'] for r in c])
real = [r['Smax'] for r in R if r['mode'] == 'real']; rn = [r['Smax'] for r in R if r['mode'] == 'realnull']
out['real'] = dict(Smax=real, median=st.median(real) if real else None, S0=[r['S0'] for r in R if r['mode'] == 'real'],
                   null_Smax=sorted(rn), null_p95=p95(rn) if rn else None)
out['real']['above_p95'] = bool(real and rn and st.median(real) > p95(rn))
out['real']['share_null_ge_real'] = round(sum(x >= st.median(real) for x in rn) / len(rn), 3) if real and rn else None
json.dump(out, open(os.path.join(HERE, 'result.json'), 'w'), indent=1); print(json.dumps(out, indent=1))
