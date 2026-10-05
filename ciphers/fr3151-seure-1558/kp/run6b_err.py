#!/usr/bin/env python3
"""RUN6-SEURE2: err_R (R1 vs R2, run6_err.py method, identity labels) over all 20 f81R lines; writes the full reconciled reads
kp/f81R_recon_R1.tsv / _R2.tsv (line order L01-L20) and kp/run6b_result.json; also A/B err (identity, err2.json mapping).
    python3 kp/run6b_err.py [--check]   (from the target folder; --check exits 1 if the committed outputs are stale)"""
import json, sys
from collections import Counter
def ed(a, b):
    D = [[i + j if not i * j else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + (a[i-1] != b[j-1]))
    return D[-1][-1]
rows = [l.rstrip('\n').split('\t') for l in open('kp/run6b_recon.tsv', encoding='utf-8')][1:]
R = {(r[0], r[1]): (r[2].split(), r[3].split()) for r in rows}
inp = {l.split('\t')[0]: [x.split() for x in l.rstrip('\n').split('\t')[1:]] for l in open('kp/run6b_inputs.tsv', encoding='utf-8').read().splitlines()[1:]}
lines = ['L%02d' % i for i in range(1, 21)]
assert all((L, r) in R for L in lines for r in ('R1', 'R2')), 'missing line'
tot = mx = ab = abmx = 0; per = {}; src = Counter(); src_bad = []
for L in lines:
    a, b = R[(L, 'R1')][0], R[(L, 'R2')][0]
    d = ed(a, b); tot += d; mx += max(len(a), len(b)); per[L] = round(d / max(len(a), len(b)), 3)
    A, B = inp[L]; ab += ed(A, B); abmx += max(len(A), len(B))
    for r in ('R1', 'R2'):
        s, c = R[(L, r)]
        if len(s) == len(c): src.update(c)
        else: src_bad.append(L + r)
n = sum(src.values())
res = {'err_R_pooled': round(tot / mx, 4), 'edits': tot, 'max_len_sum': mx, 'err_R_per_line': per,
       'err_AB_same_lines_A_labels': round(ab / abmx, 4), 'lines_identical': sum(v == 0 for v in per.values()),
       'src_share': {k: round(v / n, 3) for k, v in sorted(src.items())}, 'src_count_mismatch': src_bad,
       'n_R1': sum(len(R[(L, 'R1')][0]) for L in lines), 'n_R2': sum(len(R[(L, 'R2')][0]) for L in lines)}
outs = {}
for r in ('R1', 'R2'):
    outs['kp/f81R_recon_%s.tsv' % r] = 'line\tsigns\n' + ''.join('%s\t%s\n' % (L, ' '.join(R[(L, r)][0])) for L in lines)
outs['kp/run6b_result.json'] = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
if '--check' in sys.argv:
    stale = [p for p, t in outs.items() if open(p, encoding='utf-8').read() != t]
    print('STALE' if stale else 'OK', stale); sys.exit(1 if stale else 0)
for p, t in outs.items(): open(p, 'w', encoding='utf-8').write(t)
print(json.dumps({k: v for k, v in res.items() if k != 'err_R_per_line'}, ensure_ascii=False)); print(per)
