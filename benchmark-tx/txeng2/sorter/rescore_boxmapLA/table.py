#!/usr/bin/env python3
"""BOXMAP-RESCORE: X6 before (committed summaries, benchmark-tx/txeng2/sorter/summary_*.json) vs after (this folder's, run.sh with the
label-aware map) for the a-d orderings; prints the markdown table in RESCORE.md and writes rescore_x6.json. From the repo root:
  python3 benchmark-tx/txeng2/sorter/rescore_boxmapLA/table.py"""
import json, os
H = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(H)
KEYS = ('to_2pct', 'removed_10', 'removed_20')


def pick(d):
    o = {}
    for k, v in d['orderings'].items():
        if k in ('a_doubt', 'b_size', 'd_oracle'):
            o[k] = {x: v[x] for x in KEYS} | ({'steps': v['steps']} if k == 'd_oracle' else {})
        elif k == 'c_random':
            o[k] = dict(reach=sum(1 for t in v['to_2pct'] if not str(t).startswith('not')), r10=v['removed_10_mean'],
                        r20=v['removed_20_mean'], band=v['removed_20_band'])
    return dict(base=f"{d['base_wrong']}/{d['scored']}", tiles=d.get('tiles_in_clusters'), clusters=d.get('clusters'), **o)


rows = []
for unit in ('dev_tune', 'eval_heldout', 'whole'):
    for mode in ('cluster', 'pile'):
        for mask in ('x', 'm'):
            n = f'summary_{unit}_{mode}_{mask}.json'
            rows.append((unit, mode, mask, pick(json.load(open(os.path.join(B, n)))), pick(json.load(open(os.path.join(H, n))))))
f = lambda o, k: f"{o[k]['to_2pct'] if not str(o[k]['to_2pct']).startswith('not') else 'nr'}; {o[k]['removed_10']} / {o[k]['removed_20']}"
fr = lambda o: f"{o['c_random']['reach']}/10; {o['c_random']['r10']} / {o['c_random']['r20']} [{o['c_random']['band'][0]}, {o['c_random']['band'][1]}]"
print('| unit | mode | mask | base | (a) doubt before -> after | (b) size before -> after | (c) random before -> after | (d) oracle before -> after |')
print('|---|---|---|---|---|---|---|---|')
for unit, mode, mask, o, n in rows:
    print(f"| {unit} | {mode} | {mask} | {o['base']} | {f(o,'a_doubt')} -> **{f(n,'a_doubt')}** | {f(o,'b_size')} -> **{f(n,'b_size')}** | "
          f"{fr(o)} -> **{fr(n)}** | {f(o,'d_oracle')} -> **{f(n,'d_oracle')}** |")
json.dump([dict(unit=u, mode=m, mask=k, before=o, after=n) for u, m, k, o, n in rows], open(os.path.join(H, 'rescore_x6.json'), 'w'), indent=1)
