#!/usr/bin/env python3
"""DIN-23P one-line pilot: consensus of two blind sign passes on fr.3623 f.23r row 4, DP alignment to the
interlinear Italian gloss with the f.128 key_print values, rotated-gloss null (PREREG.md). Writes result.json.
Usage: python3 align_pilot.py [--check]  (exits non-zero if result.json is stale)."""
import json, sys, os
H = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(H, '../../f128/print_align/key_print.tsv')

def read_pass(fn):
    seg = {}
    for ln in open(os.path.join(H, fn)):
        if ln.startswith(('s1:', 's2:')):
            seg[ln[:2]] = ln[3:].split()
    return seg['s1'], seg['s2']

def lcs_align(a, b, match=lambda x, y: x == y):
    """global DP, returns list of (x|None, y|None)"""
    n, m = len(a), len(b)
    S = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1): S[i][0] = -i
    for j in range(1, m+1): S[0][j] = -j
    for i in range(1, n+1):
        for j in range(1, m+1):
            S[i][j] = max(S[i-1][j-1] + (1 if match(a[i-1], b[j-1]) else -1), S[i-1][j]-1, S[i][j-1]-1)
    out, i, j = [], n, m
    while i or j:
        if i and j and S[i][j] == S[i-1][j-1] + (1 if match(a[i-1], b[j-1]) else -1):
            out.append((a[i-1], b[j-1])); i -= 1; j -= 1
        elif i and S[i][j] == S[i-1][j]-1:
            out.append((a[i-1], None)); i -= 1
        else:
            out.append((None, b[j-1])); j -= 1
    return out[::-1]

def join_segments(s1, s2, maxov=16):
    """drop the overlap: best suffix of s1 == prefix of s2 (allowing 1 mismatch per 4)."""
    best = (0, 0)
    for k in range(3, min(maxov, len(s1), len(s2))+1):
        same = sum(x == y for x, y in zip(s1[-k:], s2[:k]))
        if same >= 0.75*k and same > best[1]:
            best = (k, same)
    return s1 + s2[best[0]:], best[0]

def consensus(a, b):
    out = []
    for x, y in lcs_align(a, b):
        out.append(x if x == y else '?')
    return out

def fold(c):
    return {'v': 'u', 'j': 'i'}.get(c, c)

def key():
    k = {}
    for ln in list(open(KEY))[1:]:
        f = ln.rstrip('\n').split('\t')
        k[f[0]] = fold(f[1])
    return k

WILD = {"0'", "v'", '?'}

def dp(signs, letters, K):
    """semi-global: free leading/trailing cipher gaps. returns pairs (sign, letter|None)"""
    n, m = len(signs), len(letters)
    def sc(s, l):
        if s in WILD or s.startswith('NEW') or s not in K: return 0
        return 2 if K[s] == l else -1
    NEG = -10**9
    S = [[NEG]*(m+1) for _ in range(n+1)]; B = [[None]*(m+1) for _ in range(n+1)]
    for i in range(n+1): S[i][0] = 0; B[i][0] = 'u'
    for j in range(1, m+1): S[0][j] = -j; B[0][j] = 'l'
    for i in range(1, n+1):
        for j in range(1, m+1):
            c = [(S[i-1][j-1] + sc(signs[i-1], letters[j-1]), 'd'), (S[i-1][j] - 1, 'u'), (S[i][j-1] - 1, 'l')]
            S[i][j], B[i][j] = max(c)
    i = max(range(n+1), key=lambda r: S[r][m]); best = S[i][m]
    pairs = [(s, None) for s in signs[i:]][::-1]
    j = m
    while i > 0 or j > 0:
        b = B[i][j]
        if b == 'd': pairs.append((signs[i-1], letters[j-1])); i -= 1; j -= 1
        elif b == 'u': pairs.append((signs[i-1], None)); i -= 1
        else: j -= 1
    return best, pairs[::-1]

def stats(pairs, K):
    kv = [(s, l) for s, l in pairs if l and s in K and s not in WILD]
    g1 = sum(K[s] == l for s, l in kv) / max(1, len(kv))
    z = [l for s, l in pairs if s == "0'" and l]
    v = [l for s, l in pairs if s == "v'" and l]
    return dict(g1=round(g1, 4), n_keyed=len(kv), zero_prime=z, zp_sp=sum(l in 'sp' for l in z),
                v_prime=v, vp_at=sum(l in 'at' for l in v))

def main():
    K = key()
    a1, a2 = read_pass('passA.txt'); b1, b2 = read_pass('passB.txt')
    A, ovA = join_segments(a1, a2); Bs, ovB = join_segments(b1, b2)
    C = consensus(A, Bs)
    gloss = [ln.split('\t')[2] for ln in list(open(os.path.join(H, 'gloss.tsv')))[1:]]
    letters = [fold(c) for c in ''.join(gloss)]
    sc, pairs = dp(C, letters, K)
    real = stats(pairs, K); real['score'] = sc
    nulls = []
    for k in range(5, len(letters)-4):
        rot = letters[k:] + letters[:k]
        s2, p2 = dp(C, rot, K); st = stats(p2, K); st['k'] = k; st['score'] = s2
        nulls.append(st)
    def p95(xs):
        xs = sorted(xs); return xs[int(0.95*(len(xs)-1))]
    res = dict(passA_len=len(A), passB_len=len(Bs), overlapA=ovA, overlapB=ovB,
               agree=sum(x == y for x, y in lcs_align(A, Bs)) / max(len(A), len(Bs)),
               consensus=' '.join(C), letters=''.join(letters), real=real,
               aligned=' '.join(f'{s}={l or "-"}' for s, l in pairs),
               null_n=len(nulls), null_g1_max=max(n['g1'] for n in nulls),
               null_zp_sp_p95=p95([n['zp_sp'] for n in nulls]), null_vp_at_p95=p95([n['vp_at'] for n in nulls]),
               null_zp_sp_max=max(n['zp_sp'] for n in nulls), null_vp_at_max=max(n['vp_at'] for n in nulls),
               null_g1_mean=round(sum(n['g1'] for n in nulls)/len(nulls), 4))
    out = json.dumps(res, indent=1, ensure_ascii=False)
    fn = os.path.join(H, 'result.json')
    if '--check' in sys.argv:
        if open(fn).read() != out: print('STALE'); sys.exit(1)
        print('ok'); return
    open(fn, 'w').write(out); print(out)

if __name__ == '__main__':
    main()
