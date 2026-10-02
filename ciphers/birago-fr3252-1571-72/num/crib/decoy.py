"""Post-hoc qualifier (BIRAGO-NUM2, 2 Oct 2026; not part of PREREG's accept rule): drag 300 random 6-letter it16dip
words over the real stream with the same score; how often does a decoy reach maesta's real max, and where?"""
import sys, random, re
from collections import Counter
sys.path.insert(0, 'crib'); import crib_drag as C
P, lix = C.pmi_matrix(); runs = C.read_runs('pooled_tokens.txt')
codes = {c: i for i, c in enumerate(sorted({x for r in runs for x in r}))}; A = C.adjacency(runs, codes)
words = Counter(w for w in re.findall(r'[a-z]+', ' '.join(C.clean(x) for x in __import__('gzip').open(
    sorted(__import__('glob').glob('../../../tools/data/it16dip/*.txt.gz'))[0], 'rt', errors='ignore').read().lower().split()))
    if len(w) == 6)
pool = [w for w, n in words.most_common(2000)]; rng = random.Random(5); dec = rng.sample(pool, 300)
ge = 0; spot = Counter(); scores = []
for w in dec:
    pl = C.drag(runs, w, codes, A, P, lix)
    if not pl: continue
    b = max(pl, key=lambda t: t[0]); scores.append(b[0]); spot[(b[1], b[2])] += 1; ge += b[0] >= 10.09
print(f'decoys {len(scores)}; real max >= 10.09 (maesta): {ge}; best placement at run 52 pos 0-2: '
      f'{sum(v for k, v in spot.items() if k[0] == 52 and k[1] <= 2)}; top spots {spot.most_common(5)}')
