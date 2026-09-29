#!/usr/bin/env python3
"""H30 (29 Sept 2026): per verse line, signs excluding X and punctuation-class boxes, against the alexandrine (12/13)
and the c3 clear poem's syllable counts (9-15), two-sample KS with a 10,000-draw permutation p; ours from the settled
drafts (scripts/settled_lines.py), Bourdeau's from his verse read (his XD / X / XS2 / CX / BX codes are his X family;
only the plain dotted X 'XD' and 'X' are dropped, the crossed and cursive forms kept). Writes h30_minus_x.json."""
import os, sys, csv, json, random
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
ours = [sum(1 for s in v if s not in PUNCT and s != 'X') for v in settled_lines(root, 'c4').values()]
sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import verse_transcription as v
bour = [sum(1 for s in l if s not in ('XD', 'X')) for l in v.lines()]
poem = [int(r['syllables']) for r in csv.DictReader(open(os.path.join(root, 'clear_poems.tsv')), delimiter='\t') if r['page'] == 'c3']
alex = [12, 13] * 10
def ks(a, b):
    xs = sorted(set(a) | set(b)); return max(abs(sum(x <= t for x in a) / len(a) - sum(x <= t for x in b) / len(b)) for t in xs)
def perm_p(a, b, trials=10000, seed=1):
    rng = random.Random(seed); obs = ks(a, b); pool = a + b; n = len(a); c = 0
    for _ in range(trials): rng.shuffle(pool); c += ks(pool[:n], pool[n:]) >= obs
    return round(obs, 3), c / trials
out = {}
for name, x in (('ours-settled-minus-X', ours), ('bourdeau-minus-X', bour)):
    row = dict(counts=x, mean=round(sum(x) / len(x), 2), min=min(x), max=max(x), alexandrine=perm_p(x, alex), c3_poem=perm_p(x, poem)); out[name] = row; print(name, row)
json.dump(out, open(os.path.join(root, 'h30_minus_x.json'), 'w'), indent=1)
