#!/usr/bin/env python3
"""GAPS155, 3 Oct 2026: leave-one-out check on the code -> gloss pairs of transcription/gloss_pairs.tsv (pages 1-2).
For each occurrence of a code seen at least twice, predict its gloss from the other occurrences (majority) and score a hit
when the first min(8, len) folded letters agree ('?' matches any letter). Control (rule 3): the same statistic after
permuting glosses among all occurrences (codes and counts fixed, so the control can vary on the statistic), 10000 draws.
Usage: python3 keys/gloss_heldout.py [--seed N]"""
import csv, os, random, re, sys
P = os.path.join(os.path.dirname(__file__), '..', 'transcription', 'gloss_pairs.tsv')
seed = int(sys.argv[sys.argv.index('--seed') + 1]) if '--seed' in sys.argv else 1
rows = list(csv.DictReader(open(P, encoding='utf-8'), delimiter='\t'))
codes = [r['cipher_raw'] for r in rows]
gl = [re.sub(r'[^a-z?]', '', r['plain_raw'].lower()) for r in rows]
def same(a, b):
    k = min(8, len(a), len(b))
    return k > 0 and all(x == y or '?' in (x, y) for x, y in zip(a[:k], b[:k]))
def score(glosses):
    hits = tests = 0
    for i, c in enumerate(codes):
        others = [glosses[j] for j in range(len(codes)) if j != i and codes[j] == c]
        if not others:
            continue
        tests += 1
        hits += any(same(glosses[i], o) for o in others)
    return hits, tests
h, t = score(gl)
rng = random.Random(seed); ctrl = []
for _ in range(10000):
    g = gl[:]; rng.shuffle(g); ctrl.append(score(g)[0])
ctrl.sort()
print(f"held-out: {h}/{t} occurrences of recurring codes predicted by their other occurrences")
print(f"shuffled-gloss control: mean {sum(ctrl)/len(ctrl):.3f} hits, p95 {ctrl[int(.95*len(ctrl))]}, p99 {ctrl[int(.99*len(ctrl))]}, "
      f"P(ctrl >= {h}) = {sum(c >= h for c in ctrl)/len(ctrl):.4f}")
