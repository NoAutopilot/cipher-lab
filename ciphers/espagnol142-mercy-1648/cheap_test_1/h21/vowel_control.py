#!/usr/bin/env python3
"""H21 (28 Sept 2026): design-matched control for espagnol142-mercy-1648 -- the target's DESIGN, not its exact profile:
three homophones per vowel (each occurrence drawn uniformly among the three), one code per consonant present, and
eight rare extra codes (as the target's 48/52/65/72/9/15 and marks: each replaces one or two occurrences of a random
letter), on an N-letter Cartas window. An exact-profile version under the same constraints (15 largest counts to
vowels, next 15 to consonants) found no window in 20,000 tries: the target's count profile is not realisable on real
text with that assignment, so the profile itself is part of what makes the target look the way it does.
  python3 .../vowel_control.py --control PLAIN.txt --n 521 --seed S --out X.tsv
"""
import argparse, random, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'tools'))
import homophonic_anneal as ha
from collections import Counter
V = 'aeiou'
ap = argparse.ArgumentParser(); ap.add_argument('--control'); ap.add_argument('--n', type=int, default=521); ap.add_argument('--seed', type=int, default=1); ap.add_argument('--out')
a = ap.parse_args(); rng = random.Random(a.seed + 5000)
p_all = ha.fold(open(a.control, encoding='utf-8').read()); start = rng.randrange(0, len(p_all) - a.n + 1); p = p_all[start:start + a.n]
letters = sorted(set(p)); k = 0; homs = {}
for l in letters:
    homs[l] = [f's{k + j}' for j in range(3 if l in V else 1)]; k += len(homs[l])
seq = [rng.choice(homs[l]) for l in p]
extra = 8; n = len(seq)
for e in range(extra):
    reps = rng.choice([1, 1, 1, 2, 2]); s = f's{k}'; k += 1
    for _ in range(reps): seq[rng.randrange(n)] = s
with open(a.out, 'w') as f:
    f.write('line\tposition\tsign\n'); [f.write(f'l1\t{i+1}\t{s}\n') for i, s in enumerate(seq)]
open(a.out + '.plain', 'w').write(p)
print(f'window {start} N={n} K={len(set(seq))} letters {len(letters)}')
