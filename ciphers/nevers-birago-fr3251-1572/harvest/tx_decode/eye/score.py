#!/usr/bin/env python3
"""A1-BIR-EYE scoring (gate as PREREG.md, pushed 632c8786 before any crop was shown). Run from this folder:
python3 score.py ANSWERS_DIR  (answers_<leaf>.tsv from the blind readers) -> score.json, printed table."""
import csv, json, math, sys
from math import comb

def binom_sf(c, n, p):  # P(X >= c)
    return sum(comb(n, k) * p**k * (1 - p)**(n - k) for k in range(c, n + 1))

def fisher_greater(a, b, c, d):  # one-sided: changed row picks 'other' more than decoy row
    n1, n2, k = a + b, c + d, a + c; N = n1 + n2
    def h(x): return comb(n1, x) * comb(n2, k - x) / comb(N, k)
    return sum(h(x) for x in range(a, min(n1, k) + 1))

pos = list(csv.DictReader(open('positions.tsv'), delimiter='\t'))
D = sys.argv[1]; out = {}; tot = dict(c=0, nc=0, d=0, nd=0)
for L in ['f117', 'f168', 'f144r']:
    try:
        ans = {r['qid']: r for r in csv.DictReader(open(f'{D}/answers_{L}.tsv'), delimiter='\t')}
    except FileNotFoundError:
        continue
    c = nc = d = nd = 0; cand = []; rows = []
    for p in pos:
        if p['leaf'] != L:
            continue
        a = ans.get(p['qid'], {}); pick = {'A': p['A'], 'B': p['B']}.get((a.get('answer') or 'U').strip())
        took_other = pick == p['other']
        rows.append(dict(qid=p['qid'], kind=p['kind'], passage=p['passage'], pos=p['pos'], original=p['original'],
                         other=p['other'], pick=pick, conf=a.get('conf'), note=a.get('note')))
        if p['kind'] == 'changed':
            nc += 1; c += took_other
            if took_other and a.get('conf') in ('H', 'M'):
                cand.append(f"{p['passage']}:{p['pos']} {p['original']}->{p['other']}")
        else:
            nd += 1; d += took_other
    p0 = (d + 1) / (nd + 2); pb = binom_sf(c, nc, p0); pf = fisher_greater(c, nc - c, d, nd - d)
    g = 'PASS' if c / nc > d / nd and pb < 0.05 else 'FAIL'
    out[L] = dict(n_changed=nc, c=c, r_c=c / nc, n_decoy=nd, d=d, r_d=d / nd, p0=p0, p_binom=pb, p_fisher=pf, gate=g,
                  s_candidates=cand if g == 'PASS' else [], rows=rows)
    for k, v in zip(['c', 'nc', 'd', 'nd'], [c, nc, d, nd]):
        tot[k] += v
    print(L, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in out[L].items() if k != 'rows'})
c, nc, d, nd = tot['c'], tot['nc'], tot['d'], tot['nd']
if nc:
    p0 = (d + 1) / (nd + 2)
    out['pooled'] = dict(n_changed=nc, c=c, r_c=c / nc, n_decoy=nd, d=d, r_d=d / nd, p0=p0, p_binom=binom_sf(c, nc, p0),
                         p_fisher=fisher_greater(c, nc - c, d, nd - d))
    out['pooled']['gate'] = 'PASS' if c / nc > d / nd and out['pooled']['p_binom'] < 0.05 else 'FAIL'
    print('pooled', out['pooled'])
json.dump(out, open('score.json', 'w'), indent=1)
