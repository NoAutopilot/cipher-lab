#!/usr/bin/env python3
"""Compute index of coincidence per page/cryptogram from clusters.tsv, plus matched controls
(English, French text at same N; uniform random string at same K). Single machine-segmented
pass (draft) -- see NOTES.md."""
import csv, sys, random, argparse
from collections import defaultdict, Counter

def ic(seq):
    n = len(seq)
    if n < 2:
        return 0.0
    counts = Counter(seq)
    num = sum(c * (c - 1) for c in counts.values())
    den = n * (n - 1)
    return num / den if den else 0.0

def load_clusters(path):
    page_syms = defaultdict(list)
    with open(path) as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            if row['kind'] != 'sign':
                continue
            pid = row['id']
            page = pid.split('_')[0]
            page_syms[page].append(row['cluster'])
    return page_syms

def load_text_letters(path, n_needed, seed):
    import gzip
    opener = gzip.open if path.endswith('.gz') else open
    with opener(path, 'rt', encoding='utf-8', errors='ignore') as f:
        text = f.read()
    letters = [c.upper() for c in text if c.isalpha()]
    rng = random.Random(seed)
    if len(letters) <= n_needed:
        return letters
    start = rng.randint(0, len(letters) - n_needed)
    return letters[start:start+n_needed]

def random_string(n, k, seed):
    rng = random.Random(seed)
    alphabet = list(range(k))
    return [rng.choice(alphabet) for _ in range(n)]

def find_corpus_file(root):
    import os
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.endswith('.txt') or fn.endswith('.txt.gz'):
                return os.path.join(dirpath, fn)
    return None

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('clusters_tsv')
    ap.add_argument('--fr', default='../../tools/data/fr16')
    ap.add_argument('--en', default='../../tools/data/en16_repo')
    ap.add_argument('--trials', type=int, default=20)
    args = ap.parse_args()

    page_syms = load_clusters(args.clusters_tsv)
    groups = {
        'c1': ['c1'],
        'c2 (2a+2b)': ['c2a', 'c2b'],
        'c3': ['c3'],
        'combined (all 4 pages)': ['c1', 'c2a', 'c2b', 'c3'],
    }

    fr_file = find_corpus_file(args.fr)
    en_file = find_corpus_file(args.en)

    print(f"{'group':<24}{'N':>6}{'K':>6}{'IC_target':>12}{'IC_fr_mean':>12}{'IC_en_mean':>12}{'IC_random_mean':>16}")
    for gname, pages in groups.items():
        seq = []
        for p in pages:
            seq.extend(page_syms.get(p, []))
        n = len(seq)
        k = len(set(seq))
        target_ic = ic(seq)

        fr_ics = []
        en_ics = []
        rand_ics = []
        for t in range(args.trials):
            if fr_file:
                fr_letters = load_text_letters(fr_file, n, seed=1000+t)
                fr_ics.append(ic(fr_letters))
            if en_file:
                en_letters = load_text_letters(en_file, n, seed=2000+t)
                en_ics.append(ic(en_letters))
            rand_seq = random_string(n, k, seed=3000+t)
            rand_ics.append(ic(rand_seq))

        fr_mean = sum(fr_ics)/len(fr_ics) if fr_ics else float('nan')
        en_mean = sum(en_ics)/len(en_ics) if en_ics else float('nan')
        rand_mean = sum(rand_ics)/len(rand_ics) if rand_ics else float('nan')
        print(f"{gname:<24}{n:>6}{k:>6}{target_ic:>12.4f}{fr_mean:>12.4f}{en_mean:>12.4f}{rand_mean:>16.4f}")
