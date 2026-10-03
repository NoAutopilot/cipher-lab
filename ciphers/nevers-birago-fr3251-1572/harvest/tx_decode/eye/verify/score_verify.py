#!/usr/bin/env python3
"""A1-BIR-VERIFY scoring, written before any answer exists (PREREG-VERIFY.md). Run from this folder:
python3 score_verify.py -> vscore.json + printed table. Reads vanswers_<leaf>.tsv (qid, answer A/B/U, conf, note)."""
import csv, json, os
from math import comb
def binom_sf(c, n, p): return sum(comb(n, k) * p**k * (1 - p)**(n - k) for k in range(c, n + 1))
def gate(c, nc, d, nd):
    p0 = (d + 1) / (nd + 2); pb = binom_sf(c, nc, p0) if nc else 1.0
    return dict(c=c, n_c=nc, d=d, n_d=nd, p0=round(p0, 4), p_binom=pb,
                gate='PASS' if nc and nd and c / nc > d / nd and pb < 0.05 else 'FAIL')
pos = list(csv.DictReader(open('vpositions.tsv'), delimiter='\t'))
eye = json.load(open('../score.json')); out = {}
for L in ['f117', 'f168', 'f144r']:
    fn = f'vanswers_{L}.tsv'
    if not os.path.exists(fn):
        continue
    ans = {r['qid']: r for r in csv.DictReader(open(fn), delimiter='\t')}
    R = []
    for p in pos:
        if p['leaf'] != L: continue
        a = ans.get(p['qid'], {}); pick = {'A': p['A'], 'B': p['B']}.get((a.get('answer') or 'U').strip())
        R.append(dict(p, took_other=pick == p['other'], conf=a.get('conf'), note=a.get('note')))
    ch = [r for r in R if r['kind'] == 'changed']; de = [r for r in R if r['kind'] == 'decoy']
    md = [r for r in R if r['kind'] == 'mdecoy']; chm = [r for r in ch if float(r['ratio']) >= 0.3]
    g1 = gate(sum(r['took_other'] for r in ch), len(ch), sum(r['took_other'] for r in de), len(de))
    g2 = gate(sum(r['took_other'] for r in chm), len(chm), sum(r['took_other'] for r in md), len(md))
    cands = set(eye[L]['s_candidates'])
    keep, drop = [], []
    for r in ch:
        tag = f"{r['passage']}:{r['pos']} {r['original']}->{r['other']}"
        if tag not in cands: continue
        ok = g1['gate'] == 'PASS' and g2['gate'] == 'PASS' and r['took_other'] and r['conf'] in ('H', 'M')
        (keep if ok else drop).append(tag)
    out[L] = dict(G1_orig=g1, G2_matched=g2, eye_candidates=len(cands), kept=keep, dropped=drop,
                  agree_with_eye=sum(1 for r in R if r['arm'] == 'orig' and r['eye_qid']), rows=R)
    print(L, 'G1', {k: g1[k] for k in ('c', 'n_c', 'd', 'n_d', 'p_binom', 'gate')},
          'G2', {k: g2[k] for k in ('c', 'n_c', 'd', 'n_d', 'p_binom', 'gate')}, f'kept {len(keep)}/{len(cands)}')
json.dump(out, open('vscore.json', 'w'), indent=1, default=str)
