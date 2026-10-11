#!/usr/bin/env python3
"""BOXMAP-RESCORE: TXE3-1 before (committed eval/ dev/ summaries) vs after (this folder, run.sh); wrong at k=10/20/50/100, questions
to 3% and 2%, random k=20 band and 2% median. From the repo root: python3 benchmark-tx/txeng3/1/rescore_boxmapLA/table.py"""
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(H)
ORD = ('disagree', 'lattice', 'margin', 'a_doubt', 'disagree_margin', 'b_size', 'd_oracle')
def wr(d, k):
    o = d['orderings'][k]; w = o['wrong_at']; tp = o['to_pct']
    return f"{w['10']}/{w['20']}/{w['50']}/{w['100']}; 3% {tp['0.03']}; 2% {tp['0.02']}"
def rnd(d):
    r = d['orderings']['c_random']; e = r['err_at_min_mean_max']['20']; sc = d['scored']
    mn, me, mx = [round(x * sc, 1) for x in e]
    med = r['to_pct_median']
    reach = sum(1 for t in r['to_2pct'] if not str(t).startswith('not'))
    return f"k20 min/mean/max {mn:g}/{me:g}/{mx:g}; 2% median {med['0.02']} ({reach}/20 reach)"
out = []
for unit in ('eval', 'dev'):
    for mode in ('pile', 'none', 'cluster'):
        for mask in ('x', 'm'):
            n = f'summary_{unit}_{mode}_{mask}_lam1.json'
            b = json.load(open(os.path.join(B, unit, n)))
            a = json.load(open(os.path.join(H, unit, n)))
            out.append(dict(unit=unit, mode=mode, mask=mask, base=f"{b['base_wrong']}/{b['scored']}",
                            before={k: wr(b, k) for k in ORD if k in b["orderings"]} | {'random': rnd(b)},
                            after={k: wr(a, k) for k in ORD if k in a["orderings"]} | {'random': rnd(a)},
                            clusters=(b['clusters'], a['clusters']), tiles=(b['tiles_in_clusters'], a['tiles_in_clusters'])))
n = 'summary_dev_pile_x_lam4.json'
b = json.load(open(os.path.join(B, 'dev', n))); a = json.load(open(os.path.join(H, 'dev', n)))
out.append(dict(unit='dev', mode='pile', mask='x lam4', base=f"{b['base_wrong']}/{b['scored']}",
                before={'lattice': wr(b, 'lattice')}, after={'lattice': wr(a, 'lattice')}))
for r in out:
    print(f"== {r['unit']} {r['mode']} {r['mask']} base {r['base']} clusters {r.get('clusters')} tiles {r.get('tiles')}")
    for k in r['before']:
        ch = '' if r['before'][k] == r['after'][k] else '   <-- CHANGED'
        print(f"  {k:16s} {r['before'][k]}  ->  {r['after'][k]}{ch}")
json.dump(out, open(os.path.join(H, 'rescore_t31.json'), 'w'), indent=1)
