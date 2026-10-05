#!/usr/bin/env python3
"""D2-B117M step 2: T88=q u-follow test on no.86 (PREREG-M16.md, fixed before scoring). Run from harvest/f117."""
import csv, json, random, collections
M = {x['id']: x for x in json.load(open('map_printed.json'))}
U = {'T33', 'T49'}
OFF = '../../../nevers-birago-fr3251-1572/harvest/offsheet/'
def F(pool):
    seq = collections.defaultdict(list)
    for r in csv.DictReader(open(OFF + pool), delimiter='\t'): seq[r['passage']].append(r['sign_id'])
    n, f = collections.Counter(), collections.Counter()
    for s in seq.values():
        for i, c in enumerate(s):
            n[c] += 1
            if i + 1 < len(s) and s[i + 1] in U: f[c] += 1
    return n, f
for pool, gate in (('pool_no86.tsv', True), ('pool_no87.tsv', False), ('pool_no90.tsv', False)):
    n, f = F(pool)
    ft = f['T88'] / n['T88'] if n['T88'] else float('nan')
    cells = sorted(c for c in n if c in M and M[c].get('kind') == 'letter' and c not in U | {'T88'} and n[c] >= 3)
    rnd = random.Random(1); draws = [f[c] / n[c] for c in (rnd.choice(cells) for _ in range(200))]
    below = sum(d < ft for d in draws)
    v = ('PASS' if ft >= 0.6 and below >= 190 else 'FAIL') if gate else 'secondary'
    print(f"{pool}\tT88 n={n['T88']} u-follow={f['T88']}/{n['T88']}={ft:.3f}\tcontrol cells={len(cells)} draws below={below}/200 "
          f"median={sorted(draws)[100]:.3f} max={max(draws):.3f}\t{v}")
