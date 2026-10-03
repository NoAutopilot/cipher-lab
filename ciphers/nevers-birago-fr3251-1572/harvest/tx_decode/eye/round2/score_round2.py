#!/usr/bin/env python3
"""BIR-ROUND2 gate (PREREG-ROUND2.md), run from this folder after r2answers_<leaf>.tsv (qid, answer A/B/U, conf H/M/L)
exist: per leaf c = changed answered key-implied (other), d = mdecoy answered swap (other); PASS iff c/n_c > d/n_d AND
binomial P(X >= c | n_c, p0=(d+1)/(n_d+2)) < 0.05 AND ../../posnull_r2 gate PASS for the leaf (r2posnull.json).
Survivors: changed positions on a passing leaf answered key-implied at H or M. Writes r2score.json."""
import csv, json, math, os
def binom_sf(c, n, p):
    return sum(math.comb(n, k) * p**k * (1 - p)**(n - k) for k in range(c, n + 1))
pos = list(csv.DictReader(open('r2positions.tsv'), delimiter='\t'))
pn = json.load(open('r2posnull.json')) if os.path.exists('r2posnull.json') else {}
out = {}
for L in ['f117', 'f168', 'f144r']:
    mine = [p for p in pos if p['leaf'] == L]
    if not mine or not os.path.exists(f'r2answers_{L}.tsv'):
        out[L] = {'n_changed': sum(p['kind'] == 'changed' for p in mine), 'gate': 'NOT RUN'}; continue
    ans = {r['qid']: r for r in csv.DictReader(open(f'r2answers_{L}.tsv'), delimiter='\t')}
    c = n_c = d = n_d = 0; kept = []
    for p in mine:
        a = ans.get(p['qid'], {}); pick = p.get(a.get('answer', 'U'), None)
        hit = pick == p['other']
        if p['kind'] == 'changed':
            n_c += 1; c += hit
            if hit and a.get('conf') in ('H', 'M'):
                kept.append(f"{p['passage']}:{p['pos']} {p['original']}->{p['other']}")
        else:
            n_d += 1; d += hit
    p0 = (d + 1) / (n_d + 2); pv = binom_sf(c, n_c, p0) if n_c else 1.0
    g_eye = n_c > 0 and n_d > 0 and c / n_c > d / n_d and pv < 0.05
    g_pn = pn.get(L, {}).get('gate') == 'PASS'
    out[L] = dict(c=c, n_changed=n_c, d=d, n_mdecoy=n_d, p0=round(p0, 4), p=pv, eye_gate='PASS' if g_eye else 'FAIL',
                  posnull_gate=pn.get(L, {}).get('gate', 'NOT RUN'), gate='PASS' if g_eye and g_pn else 'FAIL',
                  kept=kept if g_eye and g_pn else [], kept_if_eye_only=kept)
    print(L, {k: v for k, v in out[L].items() if not k.startswith('kept')}, 'kept', len(out[L]['kept']))
json.dump(out, open('r2score.json', 'w'), indent=1)
