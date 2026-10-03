#!/usr/bin/env python3
"""A1B-CEPPO-CRIB power control: plant each crib word into a run at the run's own M rate and see if crib_match finds it.
  python3 plant_power.py TOKENS.tsv CRIBS.txt [--trials 200] [--corrupt 0.5] [--seed 1]
Each trial: pick a line and offset, overwrite len(w) tokens with w's letters; each planted token is M with the run's M
fraction (else S), and an M token's letter is replaced by a random letter with probability --corrupt (an M token that is
wrong). Reports the fraction of trials in which crib_match finds the planted word."""
import argparse, random, string, sys, os
sys.path.insert(0, os.path.dirname(__file__))
import crib_match as cm
ap = argparse.ArgumentParser(); ap.add_argument('tokens'); ap.add_argument('cribs')
ap.add_argument('--trials', type=int, default=200); ap.add_argument('--corrupt', type=float, default=0.5)
ap.add_argument('--seed', type=int, default=1); a = ap.parse_args()
rng = random.Random(a.seed); lines = cm.load_tokens(a.tokens); words = cm.load_words(a.cribs)
allt = [t for ts in lines.values() for t in ts]; mfrac = sum(1 for t in allt if not t[1]) / len(allt)
tot = found = 0
for w in words:
    f = 0
    for _ in range(a.trials):
        ln = rng.choice([l for l in lines if len(lines[l]) > len(w)]); toks = lines[ln][:]
        o = rng.randrange(len(toks) - len(w) + 1)
        for i, c in enumerate(w):
            m = rng.random() < mfrac
            if m and rng.random() < a.corrupt:
                c = rng.choice([x for x in string.ascii_lowercase if x != c])
            toks[o + i] = (c, not m, (ln, f'p{i}'))
        if any(h[0] == w for h in cm.matches({ln: toks}, [w])):
            f += 1
    print(f'{w}\t{f}/{a.trials}'); tot += a.trials; found += f
print(f'M fraction {mfrac:.2f}, corrupt {a.corrupt}: planted words found {found}/{tot} = {found/tot:.2f}')
