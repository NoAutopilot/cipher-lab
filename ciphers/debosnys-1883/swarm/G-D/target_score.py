#!/usr/bin/env python3
"""The frozen score on the real c1/c2 (with X kept, and with X dropped), five shuffle seeds for stability."""
import dcore, random, json, statistics as st
res = {}
for dropx in (False, True):
    t1, t2 = dcore.target('c1', dropx), dcore.target('c2', dropx); out = []
    for seed in range(5):
        f = dcore.features(t1, t2, random.Random(1000 + seed), 400); out.append(f)
    key = 'noX' if dropx else 'withX'
    res[key] = dict(features_median={k: st.median(f[k] for f in out) for k in out[0]},
                    score={w: [round(dcore.score(f, w), 2) for f in out] for w in ('c1', 'c2', 'pair')}, N=(sum(map(len, t1)), sum(map(len, t2))))
    print(key, res[key]['N'], res[key]['score'], {k: v for k, v in res[key]['features_median'].items()})
json.dump(res, open('target_score.json', 'w'), indent=1)
