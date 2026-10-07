#!/usr/bin/env python3
"""H67 (DEB-RUN, 7 Oct 2026): H66's null-type design, selection scored OUT OF SAMPLE.
Lines split into two folds (alternate lines, both orientations). On the fit fold run h66's greedy; take the dropped
set at the fit fold's best share; delete those types from the held-out fold and score S there with 200 shuffles.
CV = mean of the two orientations' held-out S. Under no order the held-out S is centred near 0 whatever was selected;
null for the real text = the same CV on within-line shuffles of c2 (20 seeds). Same control as H66.
Usage: h67_cv.py {real|realnull|ctl|ctlnull} SEED [q]"""
import sys, random, json, h66_null_types as H
def heldout(lines, rng):
    vals = []
    for a in (0, 1):
        fit = lines[a::2]; test = lines[1 - a::2]
        r = H.greedy(fit, rng); p = r['path']; b = max(range(len(p)), key=lambda i: p[i][1])
        drop = {x[2] for x in p[1:b + 1]}
        ts = [[s for s in l if s not in drop] for l in test]; ts = [l for l in ts if len(l) > 1]
        T0 = H.T; H.T = 200; vals.append(H.S(ts, rng)); H.T = T0
    return sum(vals) / 2, vals
if __name__ == '__main__':
    mode, seed = sys.argv[1], int(sys.argv[2]); q = float(sys.argv[3]) if len(sys.argv) > 3 else None
    rng = random.Random(6700 + seed)
    if mode in ('real', 'realnull'):
        lines = H.dcore.target('c2'); lines = H.shuffled(lines, rng) if mode == 'realnull' else lines; ex = {}
    else:
        lines, nq, _ = H.control(q, rng); ex = dict(q=q)
        if mode == 'ctlnull': lines = H.shuffled(lines, rng)
    cv, v = heldout(lines, rng)
    print(json.dumps(dict(mode=mode, seed=seed, **ex, CV=round(cv, 2), folds=[round(x, 2) for x in v])), flush=True)
