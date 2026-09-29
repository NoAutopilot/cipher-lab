#!/usr/bin/env python3
"""R2-1 analysis per PREREG.md: per text, threshold by D's rule at the decision noise, balanced accuracy at every
noise level, real median score, and per design how many of 40 control pairs score as low as the real text."""
import json, glob, os, sys, statistics as st, collections
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..', 'G-D')); import dcore
DEC = {'a': 0.15, 'b': 0.20, 'c': 0.20, 'raw': 0.20}
LANG = {'FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'LA-HOMO', 'FR-SYLL'}
rows = [json.loads(l) for f in sorted(glob.glob(os.path.join(HERE, 'calib_*.jsonl'))) for l in open(f)]
def thresh(cal, w):
    best = None
    for t in [x / 10 for x in range(-50, 300)]:
        tl = sum(dcore.score(r['f'], w) > t for r in cal if r['design'] in LANG) / max(1, sum(r['design'] in LANG for r in cal))
        tn = sum(dcore.score(r['f'], w) <= t for r in cal if r['design'] == 'NULL-IID') / max(1, sum(r['design'] == 'NULL-IID' for r in cal))
        if best is None or (tl + tn) / 2 > best[0]: best = ((tl + tn) / 2, t, tl, tn)
    return best
def balacc(cal, w, t):
    tl = sum(dcore.score(r['f'], w) > t for r in cal if r['design'] in LANG) / max(1, sum(r['design'] in LANG for r in cal))
    tn = sum(dcore.score(r['f'], w) <= t for r in cal if r['design'] == 'NULL-IID') / max(1, sum(r['design'] == 'NULL-IID' for r in cal))
    return round((tl + tn) / 2, 3)
out = {}
for tid in ('a', 'b', 'c', 'raw'):
    realf = os.path.join(HERE, f'real_{tid}.json')
    if not os.path.exists(realf): continue
    R = json.load(open(realf)); res = dict(N=R['N'], K=R['K'])
    for w in ('pair', 'c2', 'c1'):
        real = st.median(R['score'][w]); d = [r for r in rows if r['text'] == tid and r['p'] == DEC[tid]]
        if not d: continue
        b = thresh(d, w); cell = dict(real_median=real, real_seeds=R['score'][w], threshold=b[1], bal_acc=round(b[0], 3),
                                      lang_recall=round(b[2], 3), null_recall=round(b[3], 3), call='LANGUAGE' if real > b[1] else 'NULL')
        per = {}
        for p in sorted({r['p'] for r in rows if r['text'] == tid}):
            cal = [r for r in rows if r['text'] == tid and r['p'] == p]; by = collections.defaultdict(list)
            for r in cal: by[r['design']].append(dcore.score(r['f'], w))
            per[p] = dict(bal_acc_at_dec_threshold=balacc(cal, w, b[1]), own_best=round(thresh(cal, w)[0], 3),
                          as_low_as_real={k: f'{sum(x <= real for x in v)}/{len(v)}' for k, v in by.items()},
                          median={k: round(st.median(v), 2) for k, v in by.items()})
        cell['by_noise'] = per; res[w] = cell
    out[tid] = res
json.dump(out, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
for tid, r in out.items():
    for w in ('pair', 'c2'):
        if w not in r: continue
        c = r[w]; print(f"{tid} {w}: real {c['real_median']} thr {c['threshold']} bal {c['bal_acc']} -> {c['call']}")
        for p, q in c['by_noise'].items(): print('   ', p, q['bal_acc_at_dec_threshold'], q['own_best'], q['as_low_as_real'], q['median'])
