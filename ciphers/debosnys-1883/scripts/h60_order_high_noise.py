#!/usr/bin/env python3
"""H60 (29 Sept 2026): D's order battery at H51's upper bound. swarm/R2/R2-1's calibration (r21.py calib, dcore.py
unchanged) re-run for texts raw, b, c (the c1/c2 shape) at 30, 35 and 40 pct mixed noise (3:1 replace:indel), 40 pairs
x 6 designs each, outputs in h60/. Scoring declared before the numbers were read: the threshold is R2-1's own, fitted at
its decision noise (20 pct) on R2-1's calib files; at each new noise level, balanced accuracy of that fixed threshold
(primary) and the level's own best threshold (secondary); per design, how many of 40 control pairs score as low as the
real text's on-file median (R2-1 real_*.json). Kill for the objection "noise hides order": primary separation >= 0.80
at 40 pct; otherwise c2's no-order result is stated as conditional on true error below the level where it fails.
Writes h60/result.json."""
import json, glob, os, sys, statistics as st, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
R21 = os.path.join(root, 'swarm/R2/R2-1'); sys.path.insert(0, os.path.join(root, 'swarm/G-D')); import dcore
sys.argv = [sys.argv[0]]
LANG = {'FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'LA-HOMO', 'FR-SYLL'}
def load(pattern): return [json.loads(l) for f in sorted(glob.glob(pattern)) for l in open(f)]
old = load(os.path.join(R21, 'calib_*.jsonl')); new = load(os.path.join(root, 'h60', 'calib_*.jsonl'))
def thresh(cal, w):
    best = None
    for t in [x / 10 for x in range(-50, 300)]:
        tl = sum(dcore.score(r['f'], w) > t for r in cal if r['design'] in LANG) / max(1, sum(r['design'] in LANG for r in cal))
        tn = sum(dcore.score(r['f'], w) <= t for r in cal if r['design'] == 'NULL-IID') / max(1, sum(r['design'] == 'NULL-IID' for r in cal))
        if best is None or (tl + tn) / 2 > best[0]: best = ((tl + tn) / 2, t)
    return best
def balacc(cal, w, t):
    tl = sum(dcore.score(r['f'], w) > t for r in cal if r['design'] in LANG) / max(1, sum(r['design'] in LANG for r in cal))
    tn = sum(dcore.score(r['f'], w) <= t for r in cal if r['design'] == 'NULL-IID') / max(1, sum(r['design'] == 'NULL-IID' for r in cal))
    return round((tl + tn) / 2, 3)
out = {}
for tid in ('raw', 'b', 'c'):
    R = json.load(open(os.path.join(R21, f'real_{tid}.json'))); res = {}
    for w in ('pair', 'c2'):
        real = st.median(R['score'][w]); dec = [r for r in old if r['text'] == tid and r['p'] == 0.20]
        t = thresh(dec, w)[1]; cell = dict(real_median=real, threshold_at_20pct=t, by_noise={})
        for p in sorted({r['p'] for r in new if r['text'] == tid}):
            cal = [r for r in new if r['text'] == tid and r['p'] == p]; by = collections.defaultdict(list)
            for r in cal: by[r['design']].append(dcore.score(r['f'], w))
            cell['by_noise'][p] = dict(bal_acc_fixed_threshold=balacc(cal, w, t), bal_acc_own_best=round(thresh(cal, w)[0], 3),
                                       as_low_as_real={k: f'{sum(x <= real for x in v)}/{len(v)}' for k, v in sorted(by.items())},
                                       median={k: round(st.median(v), 2) for k, v in sorted(by.items())})
        res[w] = cell
    out[tid] = res
    for w in ('pair', 'c2'):
        c = res[w]; print(tid, w, 'real', c['real_median'], 'thr', c['threshold_at_20pct'])
        for p, q in c['by_noise'].items(): print('   ', p, q['bal_acc_fixed_threshold'], q['bal_acc_own_best'], q['as_low_as_real'])
out['kill_met'] = {tid: out[tid]['pair']['by_noise'].get(0.4, {}).get('bal_acc_fixed_threshold', 0) >= 0.80 for tid in ('raw', 'b', 'c')}
print('kill (fixed-threshold separation >= 0.80 at 40 pct):', out['kill_met'])
json.dump(out, open(os.path.join(root, 'h60', 'result.json'), 'w'), indent=1)
