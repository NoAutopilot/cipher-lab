#!/usr/bin/env python3
"""BAL169-F22B: do the 1-bearing acute numerals of the f.22r hand read the key's acute value under a period gloss?

Targets: 71', 51', 41', 13' (the four marks VER-BAL22 saw on 169 f.22r). Values are fixed in advance from key.tsv (acute column),
not learned from the gloss. Rule (stated before scoring): a mark call is S if >= 3 glossed occurrences in glossed_pairs.tsv give the
key's acute value and that is >= 3/4 of the sign's glossed occurrences, AND the real match count over the four targets beats every
one of 200 within-run gloss shuffles (the BAL-C275WL control form); otherwise M.
Wrong-mark negative: the same occurrences scored against the key's value for the same number with the other marks (13: Mr, 13 sued,
51: alliance; 41 and 71 have no other value in key.tsv) must give 0.
Usage: python3 score_marks.py [--seeds 200]
"""
import csv, os, random, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
KEY = os.path.join(HERE, '..', 'key.tsv')
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 200
key = {}
for l in open(KEY):
    if l.startswith('#') or l.startswith('code\t'):
        continue
    f = l.rstrip('\n').split('\t')
    if len(f) >= 2:
        key[f[0]] = f[1]
TARGET = ["71'", "51'", "41'", "13'"]
table = {s: key[s] for s in TARGET}
wrong = {s: [key[n] for n in (s[:-1], s[:-1] + ':', s[:-1] + '=') if n in key] for s in TARGET}
rows = list(csv.DictReader((l for l in open(os.path.join(HERE, 'glossed_pairs.tsv')) if not l.startswith('#')), delimiter='\t'))
runs = collections.OrderedDict()
for r in rows:
    runs.setdefault(r['run'], []).append((r['sign'], r['unit']))
print('sign\tkey_value\tglossed_n\tunits\tagree\twrong_mark_values\twrong_hits')
counts = {}
for s in TARGET:
    us = [u for run in runs.values() for x, u in run if x == s and u != '-']
    c = collections.Counter(us); k = c[table[s]]
    counts[s] = (k, len(us))
    wh = sum(1 for u in us if u in wrong[s])
    print(f"{s}\t{table[s]}\t{len(us)}\t{dict(c)}\t{k}\t{wrong[s] or '-'}\t{wh}")
def score(rs):
    return sum(1 for run in rs.values() for s, u in run if s in table and u == table[s])
real = score(runs); tot = sum(1 for run in runs.values() for s, u in run if s in table)
sh = []
for seed in range(seeds):
    rng = random.Random(seed); new = {}
    for k, run in runs.items():
        units = [u for _, u in run]; rng.shuffle(units)
        new[k] = [(s, u) for (s, _), u in zip(run, units)]
    sh.append(score(new))
sh.sort(); p95 = sh[int(0.95 * len(sh)) - 1]; ge = sum(1 for x in sh if x >= real)
print(f"real {real}/{tot}; within-run shuffle ({seeds} seeds) mean {sum(sh)/len(sh):.2f}, p95 {p95}, max {max(sh)}; shuffles >= real: {ge}/{seeds}")
ok_ctrl = ge == 0
for s in TARGET:
    k, n = counts[s]
    g = 'S' if k >= 3 and n and k / n >= 0.75 and ok_ctrl else 'M'
    print(f"call {s} = {table[s]}: {k}/{n} -> {g}")
