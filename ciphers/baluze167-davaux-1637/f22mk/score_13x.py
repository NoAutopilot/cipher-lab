#!/usr/bin/env python3
"""BAL-13X (15 Oct 2026, account 4): cross-run control for 13: = Mr, per f22mk/PREREG-BAL-13X.md (registered before scoring).
Data: the four committed pairs files (glossed_pairs.tsv, _r, _169, _169c), unchanged; '-' units excluded.
Statistic k = glossed occurrences of SIGN whose placed unit is VALUE. Null A: every placed unit permuted among every placed token (cross-run);
Null B: units permuted only within the same pairs file. Controls first: (a) 13' = co, (b) 13' = co subsampled to the target's n (power),
(c) wrong value 13: = co. Usage: python3 score_13x.py [--seeds 10000]
"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SEEDS = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 10000
FILES = ('glossed_pairs.tsv', 'glossed_pairs_r.tsv', 'glossed_pairs_169.tsv', 'glossed_pairs_169c.tsv')
toks = []  # (file index, sign, unit)
for i, fn in enumerate(FILES):
    for r in csv.DictReader((l for l in open(os.path.join(HERE, fn)) if not l.startswith('#')), delimiter='\t'):
        if r['unit'] != '-':
            toks.append((i, r['sign'], r['unit']))
units = [u for _, _, u in toks]
byfile = {}
for j, (i, _, _) in enumerate(toks):
    byfile.setdefault(i, []).append(j)

def k_of(idx, us, value):
    return sum(1 for j in idx if us[j] == value)

def null(idx, value, seeds, strat, seed0=0):
    out = []
    for s in range(seeds):
        rng = random.Random(seed0 + s)
        if strat:
            us = list(units)
            for js in byfile.values():
                vals = [units[j] for j in js]; rng.shuffle(vals)
                for j, v in zip(js, vals):
                    us[j] = v
        else:
            us = list(units); rng.shuffle(us)
        out.append(k_of(idx, us, value))
    return out

def report(label, sign, value, seeds=SEEDS):
    idx = [j for j, (_, s, _) in enumerate(toks) if s == sign]
    k = k_of(idx, units, value); n = len(idx)
    res = {}
    for name, strat in (('A', False), ('B', True)):
        d = sorted(null(idx, value, seeds, strat))
        ge = sum(1 for x in d if x >= k)
        res[name] = ge / seeds
        print(f"{label}\t{sign}={value}\tk {k}/{n}\tnull {name}: mean {sum(d)/seeds:.3f} p99 {d[int(0.99*seeds)-1]} max {max(d)} >=real {ge}/{seeds}")
    passed = k >= 3 and n and k / n >= 0.75 and res['A'] < 0.01 and res['B'] < 0.01
    print(f"{label}\tcall {sign}={value}: {'PASS' if passed else 'FAIL'}")
    return passed, k, n

print(f"pool: {len(toks)} placed tokens in {len(FILES)} files; Mr units in pool: {units.count('Mr')}; co units: {units.count('co')}")
a, _, _ = report('control(a)', "13'", 'co')
# (b) power at the target's n: 13' = co subsampled to 4 occurrences
idx_co = [j for j, (_, s, _) in enumerate(toks) if s == "13'"]
rng = random.Random(12345); passes = 0; SUB = 1000; NS = 1000
for t in range(SUB):
    sub = rng.sample(idx_co, 4)
    k = k_of(sub, units, 'co')
    d = null(sub, 'co', NS, False, seed0=100000 + t * NS)
    ge = sum(1 for x in d if x >= k)
    passes += (k >= 3 and k / 4 >= 0.75 and ge / NS < 0.01)
b = passes / SUB >= 0.95
print(f"control(b)\t13'=co subsampled to n=4, {SUB} subsets x {NS} null-A draws: pass rate {passes/SUB:.3f} -> {'PASS' if b else 'FAIL'} (gate 0.95)")
c, _, _ = report('control(c)', "13:", 'co')
print(f"control(c)\twrong value must not pass: {'OK' if not c else 'BROKEN'}")
if not (a and b and not c):
    print("CONTROLS FAIL: Part 1 is a non-test; 13: stays M"); sys.exit(3)
t, k, n = report('target', "13:", 'Mr')
print(f"target\tcall 13: = Mr: {k}/{n} -> {'S' if t else 'M'}")
