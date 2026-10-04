#!/usr/bin/env python3
"""err_2reader between two sign reads of the same lines (PREREG-N8.md method).
    python3 err2.py A.tsv B.tsv OUT.json"""
import json, re, sys
from collections import Counter

def load(p):
    d = {}
    for l in open(p, encoding='utf-8').read().splitlines()[1:]:
        if '\t' in l:
            k, v = l.split('\t', 1); d[k] = v.split()
    return d

def ed_ops(a, b, same):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (0 if same(a[i-1], b[j-1]) else 1))
    pairs, i, j = [], n, m
    while i and j:
        if D[i][j] == D[i-1][j-1] + (0 if same(a[i-1], b[j-1]) else 1):
            pairs.append((a[i-1], b[j-1])); i -= 1; j -= 1
        elif D[i][j] == D[i-1][j] + 1: i -= 1
        else: j -= 1
    return D[n][m], pairs

def shared(t, other_inv):
    return (t.isdigit() or t in '#∆*+=' or re.fullmatch(r'[A-Za-z]{1,2}/?', t) is not None) and not re.fullmatch(r's\d+', t) and t in other_inv

def run(A, B, mapping):
    tot = mx = 0; allpairs = []
    for k in A:
        a, b = A[k], B.get(k, [])
        d, pr = ed_ops(a, b, lambda x, y: mapping.get(x, x) == y)
        tot += d; mx += max(len(a), len(b)); allpairs += pr
    return tot / mx, allpairs

A, B = load(sys.argv[1]), load(sys.argv[2])
invA = Counter(t for v in A.values() for t in v); invB = Counter(t for v in B.values() for t in v)
ident = {}
e0, pairs = run(A, B, ident)
adhocA = {t for t in invA if not shared(t, invB)}; adhocB = {t for t in invB if not shared(t, invA)}
co = Counter((x, y) for x, y in pairs if x in adhocA and y in adhocB)
mp, usedB = {}, set()
for (x, y), c in co.most_common():
    if x not in mp and y not in usedB and c >= 2:
        mp[x] = y; usedB.add(y)
e1, _ = run(A, B, mp)
res = {'err_identity': e0, 'err_mapped': e1, 'n_map': len(mp), 'mapping': mp, 'nA': sum(invA.values()), 'nB': sum(invB.values()),
       'KA': len(invA), 'KB': len(invB)}
print(json.dumps({k: v for k, v in res.items() if k != 'mapping'}))
json.dump(res, open(sys.argv[3], 'w'), indent=1, ensure_ascii=False)
