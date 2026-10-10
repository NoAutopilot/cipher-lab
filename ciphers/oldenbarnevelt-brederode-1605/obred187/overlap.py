#!/usr/bin/env python3
"""OBRED-187 overlap gate (PREREG-OBRED187.md). S = |V187 & V92| against uniform, band-matched and two negative texts.
--check re-runs and exits 1 if obred187/overlap.json is stale."""
import json, re, sys, os
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); C = os.path.dirname(T)
def v187(h_only=False):
    out = []
    for l in open(os.path.join(T, 'ciphertext_187.tsv')):
        if l.startswith('#') or l.startswith('line\t'): continue
        f = l.rstrip('\n').split('\t')
        if f[2].startswith('['): continue
        if h_only and f[3] != 'H-read': continue
        out.append(int(f[2]))
    return out
def v92():
    t = open(os.path.join(T, 'ciphertext.txt')).read()
    body = t[t.index('Edele, erntfesten'):t.index('Uyt Heydelberg')]
    body = body.replace('30.000', ' ').replace('13.000', ' ').replace('12 off', ' off').replace('=== p.111 ===', ' ')
    return [int(x) for x in re.findall(r'(?<![\w.])\d+(?![\w.])', body)]
def neg(path, col=None):
    vals = []
    for l in open(os.path.join(C, path)):
        if l.startswith('#'): continue
        f = l.rstrip('\n').split('\t')
        if col is not None:
            if len(f) > col and f[col].isdigit(): vals.append(int(f[col]))
        else:
            vals += [int(x) for x in re.findall(r'(?<![\w.])\d{1,3}(?![\w.])', '\t'.join(f[2:3]) if len(f) > 2 else '')]
    return vals
def run():
    rng = np.random.default_rng(187); N = 10000
    a = v187(); b = set(v92()); n = len(a); A = set(a)
    s = len(A & b); M = max(max(a), max(b))
    c1 = np.array([len(set(rng.integers(1, M + 1, n).tolist()) & b) for _ in range(N)])
    def band(v):
        lo = (v // 100) * 100; return int(rng.integers(max(lo, 1), lo + 100))
    c2 = np.array([len({band(v) for v in a} & b) for _ in range(N)])
    p = lambda arr: (1 + int((arr >= s).sum())) / (1 + N)
    negs = {}
    for name, path, col in [('N1 lodewijk 7206', 'lodewijk-van-nassau-1573-74/ciphertext_7206.tsv', 2),
                            ('N2 jan 5551', 'jan-van-nassau-1572-75/ciphertext_5551.tsv', 2)]:
        vals = neg(path, col); repl = len(vals) < n
        arr = np.array([len(set(rng.choice(vals, n, replace=repl).tolist()) & b) for _ in range(N)])
        negs[name] = {'tokens': len(vals), 'max': max(vals), 'mean': round(float(arr.mean()), 2), 'p95': float(np.percentile(arr, 95))}
    ah = v187(True); sh = len(set(ah) & b)
    res = {'n187': n, 'distinct187': len(A), 'n92_tokens': len(v92()), 'distinct92': len(b), 'M': M, 'S_obs': s,
           'shared': sorted(A & b),
           'C1_uniform': {'mean': round(float(c1.mean()), 2), 'p99': float(np.percentile(c1, 99)), 'p': round(p(c1), 4)},
           'C2_band': {'mean': round(float(c2.mean()), 2), 'p99': float(np.percentile(c2, 99)), 'p': round(p(c2), 4)},
           'negatives': negs, 'H_only': {'n': len(ah), 'S': sh}}
    res['clears'] = bool(res['C1_uniform']['p'] < 0.01 and res['C2_band']['p'] < 0.01 and all(s > v['p95'] for v in negs.values()))
    return res
if __name__ == '__main__':
    r = run(); out = os.path.join(HERE, 'overlap.json')
    if '--check' in sys.argv:
        ok = json.load(open(out)) == json.loads(json.dumps(r)); print('check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    json.dump(r, open(out, 'w'), indent=1); print(json.dumps(r, indent=1))
