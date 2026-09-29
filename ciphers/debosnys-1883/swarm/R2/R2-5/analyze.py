#!/usr/bin/env python3
"""R2-5: thresholds, control verdicts and real calls as PREREG.md fixes them; writes result.json."""
import os, sys, json, glob, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..', 'G-D'))
import dcore
os.chdir(HERE)
LANG = ['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'LA-HOMO', 'FR-SYLL']
def med(v): v = sorted(v); return v[len(v) // 2]
def pct(v, q): v = sorted(v); return v[min(len(v) - 1, int(q * len(v)))]

res = {}
for f in sorted(glob.glob('calib_*.jsonl')):
    rows = [json.loads(l) for l in open(f)]
    if not rows: continue
    tid, p = rows[0]['text'], rows[0]['p']
    by = collections.defaultdict(list)
    for r in rows: by[r['design']].append(dcore.score(r['f'], 'pair'))
    best = None
    for t in [x / 10 for x in range(-50, 1000)]:
        tl = sum(s > t for d in LANG for s in by[d]) / max(1, sum(len(by[d]) for d in LANG))
        tn = sum(s <= t for s in by['NULL-SPLIT']) / max(1, len(by['NULL-SPLIT']))
        if best is None or (tl + tn) / 2 > best[0]: best = ((tl + tn) / 2, t, tl, tn)
    res.setdefault(tid, {})[str(p)] = dict(
        n={d: len(v) for d, v in by.items()}, threshold=best[1], bal_acc=round(best[0], 3), lang_recall=round(best[2], 3),
        null_recall=round(best[3], 3), null_split_p95=round(pct(by['NULL-SPLIT'], 0.95), 2),
        median={d: round(med(v), 2) for d, v in by.items()}, _scores=by)

out = {'calibration': {t: {p: {k: v for k, v in c.items() if k != '_scores'} for p, c in d.items()} for t, d in res.items()}}
for tid in ('folger', 'planted', 'folgerW'):
    fn = f'ctrl_{tid}_0.20.json'
    if not os.path.exists(fn) or tid not in res or '0.2' not in res[tid]: continue
    c = res[tid]['0.2']; rows = json.load(open(fn))['rows']
    sp = [dcore.score(r['split'], 'pair') for r in rows]; un = [dcore.score(r['unsplit'], 'pair') for r in rows]
    above = sum(s > c['threshold'] for s in sp)
    out[f'control_{tid}'] = dict(n=len(sp), split_above_threshold=above, gate_bal_acc=c['bal_acc'], threshold=c['threshold'],
                                 split_median=round(med(sp), 2), unsplit_median=round(med(un), 2),
                                 above_null_split_p95=sum(s > c['null_split_p95'] for s in sp),
                                 passes=(above >= 32 and c['bal_acc'] >= 0.80) if tid != 'folgerW' else 'descriptive')
for tid in ('real-T', 'real-N'):
    fn = f'real_{tid}.json'
    if not os.path.exists(fn) or tid not in res: continue
    r = json.load(open(fn)); s = med(r['score']['pair']); u = med(r['unsplit_score']['pair'])
    d = {}
    for p, c in res[tid].items():
        sc = c['_scores']
        d[p] = dict(threshold=c['threshold'], bal_acc=c['bal_acc'], null_split_p95=c['null_split_p95'],
                    null_split_as_high=sum(x >= s for x in sc['NULL-SPLIT']),
                    lang_as_low={k: sum(x <= s for x in sc[k]) for k in LANG},
                    null_iid_as_high=sum(x >= s for x in sc['NULL-IID']),
                    shuffle_level=(s <= c['threshold'] and s <= c['null_split_p95']))
    out[f'real_{tid}'] = dict(split_N=r['split_N'], K=r['K'], pair_split=r['score']['pair'], pair_split_median=s,
                              pair_unsplit=r['unsplit_score']['pair'], pair_unsplit_median=u,
                              c2_split=r['score']['c2'], c1_split=r['score']['c1'], by_noise=d)
bg = [json.load(open(f)) for f in sorted(glob.glob('bgap_*.json'))]
if bg: out['bgap'] = bg
json.dump(out, open('result.json', 'w'), indent=1); print(json.dumps(out, indent=1))

# diagnostic D2 (PREREG addendum) and its unsplit baseline
def d2(t): return [r['score'] for r in json.load(open(f'd2_{t}.json'))['rows']]
if os.path.exists('d2_null-T.json'):
    nT, nN = d2('null-T'), d2('null-N'); pT, pN = pct(nT, 0.95), pct(nN, 0.95)
    D = dict(null_T_p95=pT, null_T_max=max(nT), null_N_p95=pN, null_N_max=max(nN),
             planted_above=sum(x > pT for x in d2('planted')), planted_median=med(d2('planted')),
             folger_above=sum(x > pT for x in d2('folger')), folger_median=med(d2('folger')),
             real_T=d2('real-T'), real_T_median=med(d2('real-T')), real_T_null_as_high=sum(x >= med(d2('real-T')) for x in nT),
             real_N=d2('real-N'), real_N_median=med(d2('real-N')), real_N_null_as_high=sum(x >= med(d2('real-N')) for x in nN))
    if os.path.exists('d2_baseline.json'):
        b = json.load(open('d2_baseline.json')); D['unsplit_real'] = [x['score'] for x in b['unsplit']]
    D['control_passes'] = D['planted_above'] >= 32 and D['folger_above'] >= 32
    out['d2'] = D; json.dump(out, open('result.json', 'w'), indent=1); print(json.dumps(D, indent=1))
