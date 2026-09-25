#!/usr/bin/env python3
"""Matched controls for a homophonic-cipher-style symbol count: IC of an English
text at the same N (letters only, uppercased) and of a uniform random string over
K symbols at the same N, several seeds, mean and range reported."""
import sys, random, re
from collections import Counter

def ic(seq):
    n = len(seq)
    c = Counter(seq)
    return sum(v*(v-1) for v in c.values()) / (n*(n-1))

def main():
    corpus_path = sys.argv[1]
    N = int(sys.argv[2])
    K = int(sys.argv[3])
    seeds = int(sys.argv[4]) if len(sys.argv) > 4 else 5

    text = open(corpus_path, encoding='utf-8', errors='replace').read()
    letters = re.sub(r'[^A-Za-z]', '', text).upper()

    rng = random.Random(12345)
    eng_ics = []
    for s in range(seeds):
        start = rng.randrange(0, len(letters) - N)
        sample = letters[start:start+N]
        eng_ics.append(ic(sample))

    rand_ics = []
    for s in range(seeds):
        rng2 = random.Random(1000 + s)
        sample = [rng2.randrange(K) for _ in range(N)]
        rand_ics.append(ic(sample))

    flat = 1.0 / K
    print(f"N={N} K={K}")
    print(f"english IC: mean={sum(eng_ics)/len(eng_ics):.4f} range=[{min(eng_ics):.4f},{max(eng_ics):.4f}] (n_seeds={seeds})")
    print(f"uniform-random IC: mean={sum(rand_ics)/len(rand_ics):.4f} range=[{min(rand_ics):.4f},{max(rand_ics):.4f}] (n_seeds={seeds}) flat_theory={flat:.4f}")

if __name__ == '__main__':
    main()
