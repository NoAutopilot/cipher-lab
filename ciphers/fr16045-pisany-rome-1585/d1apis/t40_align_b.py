#!/usr/bin/env python3
"""D1A-PIS variant B (PREREG-D1A-PIS.md, Addendum B): as t40_align.py but each token is masked ONE AT A TIME, so its
witness is deterministic; witnesses are computed once for every T40 token and every one-letter token, then the gate,
null N0 and power control P are drawn from them.   python3 d1apis/t40_align_b.py [--check]"""
import os, sys, json
from collections import Counter
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, H)
from t40_align import DATA, KEY, witness, top


def main():
    W = {}  # (page index, token index) -> witness
    for pi, (p, toks, where, clear) in enumerate(DATA):
        for i, t in enumerate(toks):
            if t == 'T40' or len(KEY.get(t, '')) == 1:
                W[(pi, i)] = witness(toks, clear, {i})[i]
    rng = np.random.default_rng(20261008)
    rows, allw = [], []
    for pi, (p, toks, where, clear) in enumerate(DATA):
        for i, t in enumerate(toks):
            if t == 'T40':
                rows.append(f'{p}\t{where[i][0]}\t{where[i][1]}\t{W[(pi, i)]}'); allw.append(W[(pi, i)])
    v, n, s = top(allw)
    out = {'T40': dict(N=len(allw), letters=dict(Counter(allw).most_common()), top=v, count=n, share=round(s, 3),
                       per_page={p: dict(Counter(r.split('\t')[3] for r in rows if r.startswith(p + '\t'))) for p, *_ in DATA},
                       G=bool(s >= 0.70 and n >= 5))}
    nT = [sum(t == 'T40' for t in toks) for _, toks, _, _ in DATA]
    nulls = []
    for d in range(200):
        ws = []
        for pi, ((p, toks, where, clear), k) in enumerate(zip(DATA, nT)):
            pool = [i for i, t in enumerate(toks) if t != 'T40' and len(KEY.get(t, '')) == 1]
            ws += [W[(pi, i)] for i in rng.choice(pool, k, replace=False).tolist()]
        nulls.append(top(ws)[2])
    out['N0'] = dict(draws=200, mean=round(float(np.mean(nulls)), 3), p95=round(float(np.percentile(nulls, 95)), 3),
                     max=round(float(max(nulls)), 3), passes=bool(np.percentile(nulls, 95) < 0.70),
                     p_ge_obs=round(float(np.mean(np.array(nulls) >= s)), 3))
    for cell in ('T17', 'T46'):
        allT = [(pi, i) for pi, (_, toks, _, _) in enumerate(DATA) for i, t in enumerate(toks) if t == cell]
        k = min(len(allT), sum(nT)); hits, shares = 0, []
        for d in range(50):
            ws = [W[allT[x]] for x in rng.choice(len(allT), k, replace=False)]
            tv, tn, ts = top(ws); shares.append(ts); hits += (tv == KEY[cell] and ts >= 0.70)
        full = Counter(W[x] for x in allT)
        out['P_' + cell] = dict(key=KEY[cell], available=len(allT), masked=k, draws=50, hit_rate=hits / 50,
                                mean_share=round(float(np.mean(shares)), 3), passes=bool(hits / 50 >= 0.80),
                                all_tokens=dict(full.most_common(5)))
    return out, 'page\tline\tpos\taligned\n' + '\n'.join(rows) + '\n'


if __name__ == '__main__':
    out, tsv = main()
    js = json.dumps(out, indent=1, sort_keys=True) + '\n'
    rp, wp = os.path.join(H, 'result_b.json'), os.path.join(H, 't40_witness_b.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(rp) and open(rp).read() == js and open(wp).read() == tsv
        print('up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(rp, 'w').write(js); open(wp, 'w').write(tsv); print(js)
