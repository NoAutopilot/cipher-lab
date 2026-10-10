#!/usr/bin/env python3
"""SCAN-103 (PREREG-txeng2-18, TXE2-SCAN103, 10 Oct 2026): DV1c's j0scan/j0confirm statistic re-pointed at the f.103r collapsed
stretch (build_vivonne_confirm2.py: i0 = first f103r token to the end of the stream). Reuses ../viv102anchor/anchor.py (stream())
and the frozen builder's align (B.align, band 400). Registered offset R = j0 + lo, the builder's own control window let[lo:hi]
in dec_norm coordinates; window W = round(1.25 * (hi - lo)); offsets s = 0..len(dec_norm)-W step 50.
    python3 scan103.py info     # sizes, R, W, one timing (no shares)
    python3 scan103.py scan     # published key vs 50 value-shuffled keys per offset (seed 20261009) -> scan.json
    python3 scan103.py confirm  # 200 shuffles at best and registered offsets + best-over-scan (selection-fair) null -> confirm.json
Prints counts and shares only: never a truth value, a plain letter or a decode. j0 read from vivk_result.json by script (key 'j0')."""
import json, os, random, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), 'viv102anchor'))
import anchor as A  # noqa: E402
B = A.B
pub, let, st, seq, amap, dec = A.stream()
j0 = json.load(open(os.path.join(B.TX, 'vivk_result.json')))['j0']
allet = B.sa.letters(open(os.path.join(B.TX, 'dec_norm.txt'), encoding='utf-8').read())
i0 = next(k for k, t in enumerate(st) if t[0] == 'f103r')
seg = seq[i0:]
js = [amap[k] for k in range(i0, len(st)) if k in amap]
lo, hi = max(0, min(js) - 200), min(len(let), max(js) + 200)
R, SPAN = j0 + lo, hi - lo
W = round(1.25 * SPAN)
# DEVIATION (declared in RESULTS.md): the PREREG grid 0..len-W stops at 5930 < R (end-anchored stretch; the builder's own window is
# clipped at the end of dec_norm). The grid is extended to len-SPAN; windows past len-W are truncated at the end (length >= SPAN).
OFFS_PREREG = list(range(0, len(allet) - W + 1, 50))
OFFS = list(range(0, len(allet) - SPAN + 1, 50))

def share(key, s):
    w = allet[s:s + W]
    am, dc = B.align(seg, w, key)
    n = sum(1 for k in range(len(seg)) if dc[k] >= 0 and k in am)
    return sum(1 for k in range(len(seg)) if dc[k] >= 0 and k in am and dc[k] == w[am[k]]) / max(1, n)

def keys(n):
    ids, vv = list(pub), [pub[c] for c in pub]
    rng = random.Random(20261009)
    for _ in range(n):
        rng.shuffle(vv); yield dict(zip(ids, vv))

def scan_row(s):
    real = share(pub, s); sh = [share(k, s) for k in keys(50)]
    return dict(s=s, win=len(allet[s:s + W]), real=round(real, 4), shuf_max=round(max(sh), 4), shuf_mean=round(sum(sh) / 50, 4),
                margin=round(real - max(sh), 4))

def conf_row(a):
    key, pts = a
    v = {s: share(key, s) for s in OFFS}
    return v, {s: share(key, s) for s in pts if s not in v}

if sys.argv[1] == 'info':
    t = time.time(); share(pub, OFFS[0]); dt = time.time() - t
    print(json.dumps(dict(n_dec_norm=len(allet), n_seg=len(seg), i0=i0, R=R, span=SPAN, W=W, n_offs=len(OFFS), n_offs_prereg=len(OFFS_PREREG),
                          R_on_grid=R % 50 == 0, secs_per_share=round(dt, 2))))
elif sys.argv[1] == 'scan':
    with Pool(4) as P:
        out = P.map(scan_row, OFFS)
    for r in out: print(json.dumps(r))
    json.dump(dict(R=R, W=W, span=SPAN, rows=out), open(os.path.join(HERE, 'scan.json'), 'w'), indent=1)
elif sys.argv[1] == 'confirm':
    sc = json.load(open(os.path.join(HERE, 'scan.json')))['rows']
    real = {r['s']: r['real'] for r in sc}
    best_s = max(real, key=real.get)
    Rg = min(OFFS, key=lambda s: abs(s - R))  # nearest grid offset to R
    pts = sorted({best_s, Rg, R})
    realp = {s: share(pub, s) for s in pts}
    per = {s: [] for s in pts}; best = []
    with Pool(4) as P:
        rows = P.map(conf_row, [(key, pts) for key in keys(200)])
    for v, extra in rows:
        for s in pts:
            per[s].append(v[s] if s in v else extra[s])
        best.append(max(v.values()))
    b = sorted(best)
    res = dict(R=R, R_grid=Rg, best_s=best_s, distance_letters=abs(best_s - R), points={})
    for s in pts:
        x = sorted(per[s])
        res['points'][s] = dict(real=round(realp[s], 4), mean=round(sum(x) / 200, 4), p95=round(x[189], 4), max=round(x[-1], 4),
                                margin_max=round(realp[s] - x[-1], 4), margin_fair=round(realp[s] - b[-1], 4),
                                rank=1 + sum(1 for y in x if y >= realp[s]))
    res['best_offset_null'] = dict(null_best_mean=round(sum(b) / 200, 4), null_best_p95=round(b[189], 4), null_best_max=round(b[-1], 4))
    print(json.dumps(res, indent=1)); json.dump(res, open(os.path.join(HERE, 'confirm.json'), 'w'), indent=1)
