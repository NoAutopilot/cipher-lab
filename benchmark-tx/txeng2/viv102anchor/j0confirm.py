#!/usr/bin/env python3
"""DV1c supplementary, POST HOC, NOT gating: j0scan.py's statistic at offsets 500 and 1250 with 200 shuffles (seed 20261009),
and the shuffled maximum taken over ALL 21 scan offsets per shuffle (a selection-fair null for 'best offset'). Shares only."""
import os, random, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import j0scan as J  # runs the 50-shuffle scan on import? no: guarded below
OFFS = list(range(0, 5001, 250))
ids, vv = list(J.pub), [J.pub[c] for c in J.pub]
real = {s: J.share(J.pub, J.allet[s:s + J.W]) for s in OFFS}
rng = random.Random(20261009)
per = {500: [], 1250: []}; best = []
for _ in range(200):
    rng.shuffle(vv); key = dict(zip(ids, vv))
    v = {s: J.share(key, J.allet[s:s + J.W]) for s in OFFS}
    for s in per: per[s].append(v[s])
    best.append(max(v.values()))
res = {'real': {s: round(real[s], 4) for s in OFFS}}
for s in per:
    x = sorted(per[s]); res['s%d' % s] = dict(real=round(real[s], 4), mean=round(sum(x) / 200, 4), p95=round(x[189], 4), max=round(x[-1], 4),
                                             margin_max=round(real[s] - x[-1], 4))
b = sorted(best); res['best_offset_null'] = dict(real_best=round(max(real.values()), 4), at=max(real, key=real.get), null_best_mean=round(sum(b) / 200, 4),
                                                 null_best_p95=round(b[189], 4), null_best_max=round(b[-1], 4), margin=round(max(real.values()) - b[-1], 4))
print(json.dumps(res, indent=1)); json.dump(res, open(os.path.join(HERE, 'j0confirm.json'), 'w'), indent=1)
