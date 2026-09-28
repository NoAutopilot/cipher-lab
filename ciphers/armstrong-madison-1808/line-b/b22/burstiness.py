"""Line B step B22 -- row burstiness. For each row (decade family) with >= 3 tokens: median gap between consecutive
occurrences; statistic = mean over rows of median_gap / expected_gap, expected_gap = N / count (uniform placement).
Lower = burstier. Null: token positions permuted (10,000 draws target, 2,000 per control letter); percentile of the
target BELOW its null. Positive control = design A (rows = crude stems: one word per row); negative = Bf buckets."""
import random, sys
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "b1")); sys.path.insert(0, str(HERE.parent / "b2"))
from padding_test import target_tokens, en18_words
import designs
def row_of(v):
    if v < 10: return None
    return v if v < 100 else (v // 10 if v < 1000 else (v - 1000) // 10)
def stat(toks):
    pos = defaultdict(list)
    for i, v in enumerate(toks):
        r = row_of(v)
        if r is not None: pos[r].append(i)
    N = len(toks); vals = []
    for r, ps in pos.items():
        if len(ps) < 3: continue
        gaps = sorted(b - a for a, b in zip(ps, ps[1:])); med = gaps[len(gaps)//2]
        vals.append(med / (N / len(ps)))
    return sum(vals) / len(vals) if vals else 1.0, len(vals)
def test(toks, rng, draws):
    s, n = stat(toks); null = []
    for _ in range(draws):
        t = toks[:]; rng.shuffle(t); null.append(stat(t)[0])
    null.sort(); return s, n, null[int(.05*draws)], 100*sum(1 for x in null if x < s)/draws
rng = random.Random(6); words = en18_words()
codeA = designs.build(words, "A", random.Random(7)); codeB = designs.build(words, "Bf", random.Random(7))
pos = [test(designs.simulate(words, codeA, random.Random(4000+i)), rng, 2000) for i in range(60)]
neg = [test(designs.simulate(words, codeB, random.Random(4000+i)), rng, 2000) for i in range(60)]
pc = sum(1 for p in pos if p[3] <= 5); nc = sum(1 for n in neg if n[3] <= 5)
print(f"positive control (A, rows = stems): stat mean {sum(p[0] for p in pos)/60:.3f}, letters below own p05: {pc}/60")
print(f"negative control (Bf buckets):      stat mean {sum(n[0] for n in neg)/60:.3f}, letters below own p05: {nc}/60")
gate = pc >= 45 and nc <= 6; print("GATE:", "MET" if gate else "NOT MET")
t = test(target_tokens(), rng, 10000)
print(f"TARGET: stat {t[0]:.3f} over {t[1]} rows; null p05 {t[2]:.3f}; percentile {t[3]:.1f}" + ("" if gate else "  [printed, not licensed]"))
