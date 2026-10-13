#!/usr/bin/env python3
"""BAL-SHAPE scoring, exactly PREREG-BAL-SHAPE.md items 6-7. Usage: python3 balshape/score.py READ.tsv [tiles/key_private.tsv]
G1 positive: P accuracy (exemplar letter == gloss label) >= 0.75 (labels are the same under pass A and pass B by construction:
gloss_labels.tsv keeps only signs both blind gloss reads agree on). G2 negative: N non-NONE rate <= 0.50 and <= P non-NONE - 0.25.
Target: per f.228 shape class (role), share of tiles read as the exemplar of the current value; CONFIRMED if >= 2/3 agree (the one
tile for a 1-tile class) and no tile is read as a different letter with high confidence. Overall T agreement vs a permutation null
(1000 shuffles of the T values, seed 20261013, p95), reported only."""
import collections, csv, random, sys
read = {r['id']: r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t')}
key = list(csv.DictReader(open(sys.argv[2] if len(sys.argv) > 2 else 'balshape/tiles/key_private.tsv'), delimiter='\t'))
let = lambda m: m[2:] if m and m.startswith('E-') else None
P = [k for k in key if k['role'].startswith('P:')]; N = [k for k in key if k['role'].startswith('N:')]
T = [k for k in key if k['role'].startswith('T:')]
pa = sum(let(read[k['id']]['match']) == k['value'] for k in P) / len(P)
pnn = sum(let(read[k['id']]['match']) is not None for k in P) / len(P)
nnn = sum(let(read[k['id']]['match']) is not None for k in N) / len(N)
g1, g2 = pa >= 0.75, nnn <= 0.50 and nnn <= pnn - 0.25
print(f'P n={len(P)} accuracy {pa:.3f} (gate 0.75) -> G1 {"PASS" if g1 else "FAIL"}; P non-NONE {pnn:.3f}')
print(f'N n={len(N)} non-NONE {nnn:.3f} (gate <= 0.50 and <= {pnn - 0.25:.3f}) -> G2 {"PASS" if g2 else "FAIL"}')
for k in P + N:
    r = read[k['id']]; print(f"  {k['id']} {k['role']:<10} gloss={k['value'] or '-'} read={r['match']} {r['conf']}")
agree = [let(read[k['id']]['match']) == k['value'] for k in T]
vals = [k['value'] for k in T]; rnd = random.Random(20261013); null = []
for _ in range(1000):
    rnd.shuffle(vals); null.append(sum(let(read[k['id']]['match']) == v for k, v in zip(T, vals)) / len(T))
null.sort()
print(f'T n={len(T)} agreement {sum(agree) / len(T):.3f}; permutation null mean {sum(null) / 1000:.3f} p95 {null[949]:.3f} (reported, not gating)')
cls = collections.defaultdict(list)
for k in T:
    cls[k['role']].append(k)
print('class\tvalue\ttiles\tagree\tother_high\tverdict')
for c, ks in sorted(cls.items()):
    a = sum(let(read[k['id']]['match']) == k['value'] for k in ks)
    oh = [read[k['id']]['match'] for k in ks if let(read[k['id']]['match']) not in (None, k['value']) and read[k['id']]['conf'] == 'high']
    ok = (a == len(ks)) if len(ks) == 1 else (a / len(ks) >= 2 / 3)
    v = 'CONFIRMED' if ok and not oh and g1 and g2 else ('gates-failed' if not (g1 and g2) else 'not-confirmed')
    print(f"{c}\t{ks[0]['value']}\t{len(ks)}\t{a}\t{','.join(oh) or '-'}\t{v}\t" + ' '.join(f"{k['id']}:{read[k['id']]['match']}/{read[k['id']]['conf']}" for k in ks))
