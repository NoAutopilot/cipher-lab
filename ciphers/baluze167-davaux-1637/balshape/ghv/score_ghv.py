#!/usr/bin/env python3
"""BAL167-GHV scorer (PREREG-BAL-GHV.md gates). Usage (target folder): python3 balshape/ghv/score_ghv.py READ.tsv KEY.tsv"""
import csv, sys
rd = {r['id']: r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t')}
key = list(csv.DictReader(open(sys.argv[2]), delimiter='\t'))
arms = {}
for k in key:
    arm = k['role'].split(':')[0]; r = rd[k['id']]
    arms.setdefault(arm, []).append((k['id'], k['role'], r['same_as_E-s2'], r['confidence'], r['best_exemplar']))
rate = lambda a: sum(x[2] == 'yes' for x in arms.get(a, [])) / max(1, len(arms.get(a, [])))
for a in ('P+', 'P-', 'T'):
    print(f"{a}\tn={len(arms.get(a, []))}\tyes-rate={rate(a):.3f}\t" + ' '.join(f'{i}:{r}={y}/{c}/{b}' for i, r, y, c, b in arms.get(a, [])))
g1 = rate('P+') >= 0.75; g2 = rate('P-') <= 0.25 and rate('P-') <= rate('P+') - 0.50
print(f"G1 P+ >= 0.75: {'PASS' if g1 else 'FAIL'}\nG2 P- <= 0.25 and <= P+ - 0.50: {'PASS' if g2 else 'FAIL'}")
if g1 and g2:
    for i, r, y, c, b in arms.get('T', []):
        print(f"{r}\t{'CONFIRMED' if y == 'yes' else ('NO-high' if c == 'high' else 'NO-low')}")
