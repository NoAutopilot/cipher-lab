#!/usr/bin/env python3
"""BAL-169C (15 Oct 2026, account 4): score_marks_169.py unchanged except a fourth pairs file, glossed_pairs_169c.tsv (Baluze 169 c298-c346), TARGET 13: and plain 65 (= 65' ra, PREREG-BAL-169C step 3).
BAL-169 (15 Oct 2026): score_marks_r.py unchanged except a third pairs file, glossed_pairs_169.tsv (Baluze 169 c174-c188).
BAL-F22R: the BAL169-F22B exemplar test (score_marks.py) applied to the remaining f.22r numerals 16' (acute), 16 (plain), 45', 12:, 13:.

Values fixed before scoring from key.tsv: 16' de, 45' ma, 12: ment, 13: Mr; plain 16 has no key row, so it is scored against the acute value
de (hypothesis: the mark-free form of the same number), stated here before scoring. Plain 65 has no glossed occurrence with a settled mark
(the two 65? rows are not scored), so it is not tested. Rule unchanged from score_marks.py: a call is S if >= 3 glossed occurrences give the
value and that is >= 3/4 of the sign's glossed occurrences, AND the real match count over the targets beats every one of 200 within-run gloss
shuffles; otherwise M. Pairs: glossed_pairs.tsv (BAL169-F22B) + glossed_pairs_r.tsv (BAL-F22R).
Wrong-mark negative: occurrences scored against the key value of the same number with another mark (45: holandois, 12' ci, 13' co, 13 sued).
Usage: python3 score_marks_r.py [--seeds 200]
"""
import csv, os, random, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 200
key = {}
for l in open(os.path.join(HERE, '..', 'key.tsv')):
    if l.startswith('#') or l.startswith('code\t'):
        continue
    f = l.rstrip('\n').split('\t')
    if len(f) >= 2:
        key[f[0]] = f[1]
TARGET = ["13:", "65"]
table = {"13:": key["13:"], "65": key["65'"]}
def others(s):
    n = s.rstrip("':=")
    return [key[x] for x in (n, n + "'", n + ':', n + '=') if x in key and x != s and key[x] != table[s]]
runs = collections.OrderedDict()
for fn in ('glossed_pairs.tsv', 'glossed_pairs_r.tsv', 'glossed_pairs_169.tsv', 'glossed_pairs_169c.tsv'):
    for r in csv.DictReader((l for l in open(os.path.join(HERE, fn)) if not l.startswith('#')), delimiter='\t'):
        runs.setdefault(r['run'], []).append((r['sign'], r['unit']))
print('sign\tvalue\tglossed_n\tunits\tagree\twrong_mark_values\twrong_hits')
counts = {}
for s in TARGET:
    us = [u for run in runs.values() for x, u in run if x == s and u != '-']
    c = collections.Counter(us); k = c[table[s]]; counts[s] = (k, len(us))
    print(f"{s}\t{table[s]}\t{len(us)}\t{dict(c)}\t{k}\t{others(s) or '-'}\t{sum(1 for u in us if u in others(s))}")
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
for s in TARGET:
    k, n = counts[s]
    g = 'S' if k >= 3 and n and k / n >= 0.75 and ge == 0 else 'M'
    print(f"call {s} = {table[s]}: {k}/{n} -> {g}")
