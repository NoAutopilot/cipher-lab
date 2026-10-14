#!/usr/bin/env python3
"""BAL22-SHAPE scorer (PREREG-BAL22-SHAPE.md): per read, G1 P+ yes-rate >= 0.75, G2 P- yes-rate <= 0.25 and <= P+ - 0.50;
T tile CONFIRMED only if both reads pass and both say yes. Usage: python3 balshape/f22/score_f22.py"""
import csv
R = {'A': ('balshape/f22/readA.tsv', 'balshape/f22/r20261014/key_private.tsv'),
     'B': ('balshape/f22/readB.tsv', 'balshape/f22/r20261015/key_private.tsv')}
ok, tans = {}, {}
for name, (rf, kf) in R.items():
    rd = {r['tile']: r for r in csv.DictReader(open(rf), delimiter='\t')}
    key = list(csv.DictReader(open(kf), delimiter='\t'))
    arm = lambda p: [k for k in key if k['role'].startswith(p)]
    yes = lambda ks: sum(rd[k['id']]['same'].strip().lower() == 'yes' for k in ks)
    pp, pm = arm('P+'), arm('P-'); yp, ym = yes(pp) / len(pp), yes(pm) / len(pm)
    g1, g2 = yp >= 0.75, ym <= 0.25 and ym <= yp - 0.50
    ok[name] = g1 and g2
    print(f'read {name}: P+ {yes(pp)}/{len(pp)} = {yp:.3f} G1 {"PASS" if g1 else "FAIL"}; '
          f'P- {yes(pm)}/{len(pm)} = {ym:.3f} G2 {"PASS" if g2 else "FAIL"}')
    for k in arm('P-'):
        r = rd[k['id']]; print(f'   P- {k["id"]} true {k["true_or_current"]} proposed {k["proposed"]}: {r["same"]} {r["conf"]} best {r["best"]}')
    for k in arm('T:'):
        r = rd[k['id']]; tans.setdefault(k['role'], []).append((name, r['same'].strip().lower(), r['conf'], r['best'], k['proposed']))
print('T tiles:')
for role, a in tans.items():
    conf = all(ok.values()) and all(s == 'yes' for _, s, *_ in a)
    print(f'  {role} value {a[0][4]}: ' + '; '.join(f'{n} {s} {c} best {b}' for n, s, c, b, _ in a) + (' -> CONFIRMED' if conf else ' -> not confirmed'))
