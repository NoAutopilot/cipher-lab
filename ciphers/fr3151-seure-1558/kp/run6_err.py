#!/usr/bin/env python3
"""RUN6-SEURE pilot: err_R between two reconcilers (err2.py edit-distance method, identity labels) + per-line A/B err.
    python3 kp/run6_err.py   (from the target folder; writes kp/run6_result.json)"""
import json
from collections import Counter
def ed(a, b):
    D = [[i + j if not i * j else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    return D[-1][-1]
rows = [l.rstrip('\n').split('\t') for l in open('kp/run6_recon.tsv', encoding='utf-8')][1:]
R = {(r[0], r[1]): (r[2].split(), r[3].split()) for r in rows}
assert all(len(s) == len(c) for s, c in R.values())
tot = mx = 0; per = {}
for L in ('L04', 'L06'):
    a, b = R[(L, 'R1')][0], R[(L, 'R2')][0]
    d = ed(a, b); tot += d; mx += max(len(a), len(b)); per[L] = round(d / max(len(a), len(b)), 4)
src = Counter(x for s, c in R.values() for x in c)
n = sum(src.values())
res = {'err_R_pooled': round(tot / mx, 4), 'err_R_per_line': per, 'edits': tot, 'max_len_sum': mx,
       'src_share': {k: round(v / n, 3) for k, v in sorted(src.items())}, 'gate': 0.24,
       'verdict': 'PASS' if tot / mx < 0.24 else 'FAIL'}
print(json.dumps(res)); json.dump(res, open('kp/run6_result.json', 'w'), indent=1)
