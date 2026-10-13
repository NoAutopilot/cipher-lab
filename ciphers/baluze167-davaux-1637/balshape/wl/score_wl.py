#!/usr/bin/env python3
"""BAL-WL scoring, exactly PREREG-BAL-WL.md. Usage (from the target folder): python3 balshape/wl/score_wl.py READ.tsv KEY.tsv
G1: P+ yes-rate >= 0.75. G2: P- yes-rate <= 0.25 and <= P+ - 0.50. Target (only if both pass): per f.228 class, CONFIRMED if >= 2/3 yes
(1-tile class: yes) and no high-confidence no."""
import collections, csv, sys
read = {r['id']: r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t')}
key = list(csv.DictReader(open(sys.argv[2]), delimiter='\t'))
arm = lambda p: [k for k in key if k['role'].startswith(p)]
yes = lambda ks: sum(read[k['id']]['verdict'] == 'yes' for k in ks) / len(ks)
pp, pm, t = yes(arm('P+:')), yes(arm('P-:')), yes(arm('T:'))
g1, g2 = pp >= 0.75, pm <= 0.25 and pm <= pp - 0.50
print(f"P+ n={len(arm('P+:'))} yes {pp:.3f} (gate >= 0.75) -> G1 {'PASS' if g1 else 'FAIL'}")
print(f"P- n={len(arm('P-:'))} yes {pm:.3f} (gate <= 0.25 and <= {pp - 0.5:.3f}) -> G2 {'PASS' if g2 else 'FAIL'}")
print(f"T n={len(arm('T:'))} yes {t:.3f} (reported)")
for k in arm('P+:') + arm('P-:'):
    r = read[k['id']]; print(f"  {k['id']} {k['role']:<9} true={k['true_or_current']} proposed={k['proposed']} -> {r['verdict']}/{r['conf']} best={r['best']}")
cls = collections.defaultdict(list)
for k in arm('T:'):
    cls[k['role']].append(k)
print('class\tvalue\ttiles\tyes\thigh_no\tverdict\ttiles')
for c, ks in sorted(cls.items()):
    a = sum(read[k['id']]['verdict'] == 'yes' for k in ks)
    hn = sum(read[k['id']]['verdict'] == 'no' and read[k['id']]['conf'] == 'high' for k in ks)
    ok = (a == len(ks)) if len(ks) == 1 else a / len(ks) >= 2 / 3
    v = 'gates-failed' if not (g1 and g2) else ('CONFIRMED' if ok and not hn else ('majority-no' if a / len(ks) < 0.5 else 'not-confirmed'))
    print(f"{c}\t{ks[0]['proposed']}\t{len(ks)}\t{a}\t{hn}\t{v}\t" + ' '.join(f"{k['id']}:{read[k['id']]['verdict']}/{read[k['id']]['conf']}/{read[k['id']]['best']}" for k in ks))
