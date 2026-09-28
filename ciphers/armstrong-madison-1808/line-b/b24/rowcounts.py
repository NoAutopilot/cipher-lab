"""Line B step B24 -- row-count distribution: top-10 share of row tokens and a Zipf slope (log count vs log rank,
rows with >= 2 tokens) for the target against (a) en18 windows with rows = words (design A of B2, one stem per row)
and (b) Bf bucket sums; 60 letters each."""
import math, random, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "b1")); sys.path.insert(0, str(HERE.parent / "b2"))
from padding_test import target_tokens, en18_words
import designs
def row_of(v):
    if v < 10: return None
    return v if v < 100 else (v // 10 if v < 1000 else (v - 1000) // 10)
def stat(toks):
    c = Counter(r for r in (row_of(v) for v in toks) if r is not None)
    counts = sorted(c.values(), reverse=True); tot = sum(counts)
    top10 = sum(counts[:10]) / tot
    xs = [math.log(i+1) for i, n in enumerate(counts) if n >= 2]; ys = [math.log(n) for n in counts if n >= 2]
    mx = sum(xs)/len(xs); my = sum(ys)/len(ys)
    slope = sum((x-mx)*(y-my) for x, y in zip(xs, ys)) / sum((x-mx)**2 for x in xs)
    return dict(top10=top10, zipf=slope, rows=len(c), max_row=counts[0]/tot)
words = en18_words(); tgt = stat(target_tokens()); print("TARGET", {k: round(v, 3) for k, v in tgt.items()})
for name, design in (("A rows=stems", "A"), ("Bf buckets", "Bf")):
    code = designs.build(words, design, random.Random(7))
    rows = [stat(designs.simulate(words, code, random.Random(5000+i))) for i in range(60)]
    for k in tgt:
        arr = sorted(r[k] for r in rows); print(f"{name:13s} {k:8s} mean {sum(arr)/60:7.3f} p05 {arr[3]:7.3f} p95 {arr[57]:7.3f} target {tgt[k]:7.3f} pct {100*sum(1 for x in arr if x < tgt[k])/60:5.0f}")
