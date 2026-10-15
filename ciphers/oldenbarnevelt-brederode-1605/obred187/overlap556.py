#!/usr/bin/env python3
"""OBRED-556 overlap gate (PREREG-OBRED556.md). S = |V556 & (V92 | V187)| against uniform, band-matched, two negative texts,
and a power control (187 subsampled to n556, scored against V92). --check re-runs and exits 1 if obred187/overlap556.json is stale."""
import json, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from overlap import v92, v187, neg
def v556(h_only=False):
    out = []
    for l in open(os.path.join(T, 'ciphertext_556.tsv')):
        if l.startswith('#') or l.startswith('scan\t'): continue
        f = l.rstrip('\n').split('\t')
        if not f[3].isdigit(): continue
        if h_only and f[4] != 'H-read': continue
        out.append(int(f[3]))
    return out
def run():
    rng = np.random.default_rng(556); N = 10000
    a = v556(); A = set(a); n = len(a)
    R = set(v92()) | set(v187()); s = len(A & R); M = max(max(a), max(R))
    c1 = np.array([len(set(rng.integers(1, M + 1, n).tolist()) & R) for _ in range(N)])
    def band(v):
        lo = (v // 100) * 100; return int(rng.integers(max(lo, 1), lo + 100))
    c2 = np.array([len({band(v) for v in a} & R) for _ in range(N)])
    p = lambda arr: (1 + int((arr >= s).sum())) / (1 + N)
    negs = {}
    for name, path, col in [('N1 lodewijk 7206', 'lodewijk-van-nassau-1573-74/ciphertext_7206.tsv', 2),
                            ('N2 jan 5551', 'jan-van-nassau-1572-75/ciphertext_5551.tsv', 2)]:
        vals = neg(path, col); repl = len(vals) < n
        arr = np.array([len(set(rng.choice(vals, n, replace=repl).tolist()) & R) for _ in range(N)])
        negs[name] = {'tokens': len(vals), 'max': max(vals), 'mean': round(float(arr.mean()), 2), 'p95': float(np.percentile(arr, 95))}
    # power: 187 subsampled to n556 against V92 only, vs C1 against V92 at the same n
    b92 = set(v92()); t187 = v187(); M92 = max(max(t187), max(b92))
    c1p = np.array([len(set(rng.integers(1, M92 + 1, n).tolist()) & b92) for _ in range(N)]); thr = float(np.percentile(c1p, 99))
    pos = np.array([len(set(rng.choice(t187, n, replace=len(t187) < n).tolist()) & b92) for _ in range(N)])
    ah = v556(True)
    res = {'n556': n, 'distinct556': len(A), 'R_distinct': len(R), 'M': M, 'S_obs': s, 'shared': sorted(A & R),
           'shared_with_92': sorted(A & b92), 'shared_with_187': sorted(A & set(t187)),
           'C1_uniform': {'mean': round(float(c1.mean()), 2), 'p99': float(np.percentile(c1, 99)), 'p': round(p(c1), 4)},
           'C2_band': {'mean': round(float(c2.mean()), 2), 'p99': float(np.percentile(c2, 99)), 'p': round(p(c2), 4)},
           'negatives': negs,
           'power': {'C1_vs_V92_p99': thr, 'pos_mean': round(float(pos.mean()), 2), 'power': round(float((pos > thr).mean()), 4)},
           'H_only': {'n': len(ah), 'S': len(set(ah) & R)}}
    res['clears'] = bool(res['C1_uniform']['p'] < 0.01 and res['C2_band']['p'] < 0.01 and all(s > v['p95'] for v in negs.values()))
    return res
if __name__ == '__main__':
    r = run(); out = os.path.join(HERE, 'overlap556.json')
    if '--check' in sys.argv:
        ok = json.load(open(out)) == json.loads(json.dumps(r)); print('check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    json.dump(r, open(out, 'w'), indent=1); print(json.dumps(r, indent=1))
