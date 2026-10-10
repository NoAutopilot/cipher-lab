#!/usr/bin/env python3
"""OBRED-DP structure of no. 92 + the scan-187 postscript (PREREG-OBREDDP.md). Runs of code groups in clear context, shared
ordered pairs across the two texts against an order-permutation control (G1), the 600+ name band against a value permutation
(G2), value range by run length. Descriptive except G1/G2. --check re-runs and exits 1 if obred187/structure.json is stale."""
import json, os, re, sys
from collections import Counter
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import overlap as o
NUM = re.compile(r'(?<![\w.])\d+(?![\w.])')
def runs92():
    t = open(os.path.join(T, 'ciphertext.txt')).read()
    body = t[t.index('Edele, erntfesten'):t.index('Uyt Heydelberg')]
    body = body.replace('30.000', ' ').replace('13.000', ' ').replace('12 off', ' off').replace('=== p.111 ===', ' ')
    toks = re.findall(r"[\w'.]+|[^\w\s]", body)
    runs, cur, clear = [], [], []
    for w in toks:
        if NUM.fullmatch(w):
            if not cur: start = len(clear)
            cur.append(int(w))
        else:
            if cur: runs.append({'vals': cur, 'ci': start}); cur = []
            clear.append(w)
    if cur: runs.append({'vals': cur, 'ci': len(clear)})
    for r in runs:
        r['before'] = ' '.join(clear[max(0, r['ci'] - 4):r['ci']]); r['after'] = ' '.join(clear[r['ci']:r['ci'] + 4]); del r['ci']
    assert sum(len(r['vals']) for r in runs) == len(o.v92())
    return runs
def runs187():
    runs, cur = [], []
    for l in open(os.path.join(T, 'ciphertext_187.tsv')):
        if l.startswith('#') or l.startswith('line\t'): continue
        g = l.split('\t')[2]
        if g.startswith('['):
            if cur: runs.append({'vals': cur, 'after': g}); cur = []
        else: cur.append(int(g))
    if cur: runs.append({'vals': cur, 'after': '(end)'})
    return runs
def pairs(rs, k=2):
    return {tuple(v[i:i + k]) for v in rs for i in range(len(v) - k + 1)}
def permute(rs, rng):
    flat = rng.permutation([x for v in rs for x in v]).tolist(); out, i = [], 0
    for v in rs: out.append(flat[i:i + len(v)]); i += len(v)
    return out
def run():
    rng = np.random.default_rng(92); N = 10000
    R92 = runs92(); R187 = runs187(); v92 = [r['vals'] for r in R92]; v187 = [r['vals'] for r in R187]
    sh2 = sorted(pairs(v92) & pairs(v187)); sh3 = sorted(pairs(v92, 3) & pairs(v187, 3))
    b = np.array([len(pairs(permute(v92, rng)) & pairs(permute(v187, rng))) for _ in range(N)])
    p = lambda arr, s: round((1 + int((arr >= s).sum())) / (1 + N), 4)
    g1 = {'B_obs': len(sh2), 'pairs': [list(x) for x in sh2], 'trigrams': [list(x) for x in sh3], 'ctrl_mean': round(float(b.mean()), 3),
          'ctrl_p99': float(np.percentile(b, 99)), 'p': p(b, len(sh2))}
    g1['pass'] = g1['p'] < 0.01
    def hshare(rs):
        hi = [len(v) == 1 for v in rs for x in v if x >= 600]; return sum(hi) / len(hi)
    h = hshare(v92); hc = np.array([hshare(permute(v92, rng)) for _ in range(N)])
    g2 = {'n_hi': sum(1 for v in v92 for x in v if x >= 600), 'H_obs': round(h, 4), 'ctrl_mean': round(float(hc.mean()), 4),
          'ctrl_p99': round(float(np.percentile(hc, 99)), 4), 'p': p(hc, h - 1e-12)}
    g2['pass'] = g2['p'] < 0.01
    bylen = {}
    for v in v92 + v187:
        k = 'len1' if len(v) == 1 else 'len2-5' if len(v) <= 5 else 'len6+'
        bylen.setdefault(k, []).extend(v)
    desc = {k: {'tokens': len(x), 'min': min(x), 'max': max(x), 'share_ge600': round(sum(y >= 600 for y in x) / len(x), 3),
                'hundreds': dict(sorted(Counter(y // 100 * 100 for y in x).items()))} for k, x in sorted(bylen.items())}
    rep = Counter(x for v in v92 + v187 for x in v)
    return {'runs92': R92, 'runs187': R187, 'run_lengths92': [len(v) for v in v92], 'run_lengths187': [len(v) for v in v187],
            'G1_shared_order': g1, 'G2_name_band': g2, 'value_range_by_run_length': desc,
            'repeated_values_pooled': {str(k): c for k, c in sorted(rep.items()) if c >= 3}}
if __name__ == '__main__':
    r = run(); out = os.path.join(HERE, 'structure.json')
    if '--check' in sys.argv:
        ok = json.load(open(out)) == json.loads(json.dumps(r)); print('check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    json.dump(r, open(out, 'w'), indent=1)
    print(json.dumps({k: r[k] for k in ['run_lengths92', 'run_lengths187', 'G1_shared_order', 'G2_name_band', 'value_range_by_run_length',
                                         'repeated_values_pooled']}, indent=None))
    for x in r['runs92']: print(len(x['vals']), x['vals'], '|', x['before'], '<>', x['after'])
