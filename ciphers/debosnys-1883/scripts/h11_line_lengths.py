#!/usr/bin/env python3
"""H11 (28 Sept 2026): signs per line of the cipher verse (20 lines; ours from passA.tsv with punctuation-class boxes
BLOB/HOOK-L/DASH-H/_/MULTI dropped; Bourdeau's with his , . - dropped) against (a) alexandrines: 12 or 13 syllables
(feminine ending), and (b) the c3 clear poem's own per-line syllable counts (clear_poems.tsv, 14 lines, 9-15), by a
two-sample Kolmogorov-Smirnov statistic with a permutation p (10,000 draws). A letter-level design would give 30-40 per
line. Writes h11_lines.json."""
import os, sys, csv, json, random, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
by = collections.OrderedDict()
for r in csv.DictReader(open(os.path.join(root, 'passA.tsv')), delimiter='\t'):
    if r['line'].startswith('c4'): by.setdefault(r['line'], []).append(r['sign'])
keys = sorted(by, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2, k))
ours = [sum(1 for s in by[k] if s not in PUNCT) for k in keys]
sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import verse_transcription as v
bour = [len(l) for l in v.lines()]
poem = [int(r['syllables']) for r in csv.DictReader(open(os.path.join(root, 'clear_poems.tsv')), delimiter='\t') if r['page'] == 'c3']
alex = [12, 13] * 10
def ks(a, b):
    xs = sorted(set(a) | set(b)); return max(abs(sum(x <= t for x in a) / len(a) - sum(x <= t for x in b) / len(b)) for t in xs)
def perm_p(a, b, trials=10000, seed=1):
    rng = random.Random(seed); obs = ks(a, b); pool = a + b; n = len(a); c = 0
    for _ in range(trials):
        rng.shuffle(pool); c += ks(pool[:n], pool[n:]) >= obs
    return obs, c / trials
out = {}
for name, x in (('ours', ours), ('bourdeau', bour)):
    row = dict(counts=x, mean=sum(x) / len(x), min=min(x), max=max(x))
    for ref, y in (('alexandrine12-13', alex), ('c3-poem-syllables', poem)):
        d, p = perm_p(x, y); row[ref] = dict(KS=round(d, 3), p=p)
    out[name] = row; print(name, row)
json.dump(out, open(os.path.join(root, 'h11_lines.json'), 'w'), indent=1)
