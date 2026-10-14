#!/usr/bin/env python3
"""BAL-C275WL: per-sign counts from glossed_pairs.tsv and a within-run gloss-shuffle control.

Rule (stated in NOTES before adoption): a sign gets value V at grade S if >= 3 glossed occurrences give V and V is >= 3/4 of
its glossed occurrences; otherwise its majority value is M. Only the target signs (this hand's letter signs and unmarked numerals
that key.tsv does not cover) are scored.  Control: the gloss units are shuffled within each run (200 seeds); the same value table
is scored against the shuffled units.  Statistic: matches of the table's value to the aligned unit, over target-sign occurrences.
Usage: python3 count_shuffle.py [--seeds 200]
"""
import csv, random, sys, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = {'s:i', 's:dloop', 's:u4', 's:x', 's:pbar', 's:c', '6', '30', '77', '14', '66', '55', '16', 'L:w', 'L:h', 'L:longs'}
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 200
rows = [r for r in csv.DictReader((l for l in open(os.path.join(HERE, 'glossed_pairs.tsv')) if not l.startswith('#')), delimiter='\t')]
occ = collections.defaultdict(collections.Counter)
for r in rows:
    if r['sign'] in TARGET and r['unit'] != '-':
        occ[r['sign']][r['unit']] += 1
table = {}
print('sign\tn\tvalues\tvalue\tgrade')
for s in sorted(occ):
    c = occ[s]; n = sum(c.values()); v, k = c.most_common(1)[0]
    g = 'S' if k >= 3 and k / n >= 0.75 else 'M'
    table[s] = v
    print(f"{s}\t{n}\t{dict(c)}\t{v}\t{g}")
runs = collections.defaultdict(list)
for r in rows:
    runs[r['run']].append((r['sign'], r['unit']))
def score(rs):
    return sum(1 for run in rs.values() for s, u in run if s in table and u == table[s])
real = score(runs)
tot = sum(1 for run in runs.values() for s, u in run if s in table)
sh = []
for seed in range(seeds):
    rng = random.Random(seed); new = {}
    for k, run in runs.items():
        units = [u for _, u in run]; rng.shuffle(units)
        new[k] = [(s, u) for (s, _), u in zip(run, units)]
    sh.append(score(new))
sh.sort()
p95 = sh[int(0.95 * len(sh)) - 1]
ge = sum(1 for x in sh if x >= real)
print(f"real {real}/{tot}; shuffle mean {sum(sh)/len(sh):.2f}, p95 {p95}, max {max(sh)}; shuffles >= real: {ge}/{len(sh)}")
# Leave-one-run-out: the table is rebuilt without each run and scored on that run's target signs (removes the circularity of
# scoring the table on the data it was built from); same within-run shuffle, 200 seeds, for the held-out statistic.
def loro(rs):
    hit = n = 0
    for k in rs:
        c = collections.defaultdict(collections.Counter)
        for k2, run in runs.items():
            if k2 != k:
                for s, u in run:
                    if s in TARGET and u != '-':
                        c[s][u] += 1
        t = {s: c[s].most_common(1)[0][0] for s in c}
        for s, u in rs[k]:
            if s in t and s in TARGET:
                n += 1; hit += (u == t[s])
    return hit, n
rh, rn = loro(runs)
lsh = []
for seed in range(seeds):
    rng = random.Random(1000 + seed); new = {}
    for k, run in runs.items():
        units = [u for _, u in run]; rng.shuffle(units)
        new[k] = [(s, u) for (s, _), u in zip(run, units)]
    lsh.append(loro(new)[0])
lsh.sort()
print(f"leave-one-run-out real {rh}/{rn}; shuffled-run held-out mean {sum(lsh)/len(lsh):.2f}, p95 {lsh[int(0.95*len(lsh))-1]}, max {max(lsh)}; >= real: {sum(1 for x in lsh if x >= rh)}/{len(lsh)}")
