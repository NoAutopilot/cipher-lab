"""Line B step B7 -- is the 1700-1900 block a distinct sub-block (flatter units, clustered)?
After B1 the 4-digit tier is prefix 1 + rows 10-99, so the question becomes: do rows 70-89 of the 4-digit tier
(values 1700-1899, plus 1900) differ from the rest of that tier? Statistics: units-0 share of the block; adjacent-pair
count among block tokens. Nulls (2,000 draws): (a) block label permuted among 4-digit values of the same count bin
(1, 2, 3+), keeping the block's distinct-value count; (b) positions of all tokens shuffled (adjacency)."""
import random, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "b1"))
from padding_test import target_tokens
toks = target_tokens(); c = Counter(toks); rng = random.Random(5)
four = sorted(v for v in c if v >= 1000); blk = [v for v in four if v >= 1700]
def bins(n): return 0 if n == 1 else 1 if n == 2 else 2
def z0(vals): t = [v for v in toks if v in set(vals)]; return sum(1 for v in t if v % 10 == 0) / len(t), len(t)
s0, n = z0(blk); print(f"block >=1700: {len(blk)} distinct, {n} tokens, units-0 share {s0:.3f}; rest of 4-digit tier {z0([v for v in four if v < 1700])[0]:.3f}")
null = []
groups = {}
for v in four: groups.setdefault(bins(c[v]), []).append(v)
need = Counter(bins(c[v]) for v in blk)
for _ in range(2000):
    pick = []
    for b, k in need.items(): pick += rng.sample(groups[b], k)
    null.append(z0(pick)[0])
null.sort(); print(f"null (a) mean {sum(null)/len(null):.3f} p05 {null[int(.05*len(null))]:.3f} p95 {null[int(.95*len(null))]:.3f} pct {100*sum(1 for x in null if x < s0)/len(null):.1f}")
# adjacency
seq = []
for line in open(Path(__file__).resolve().parents[2] / "ciphertext.txt"):
    if line.startswith("#"): continue
    seq += [int(t) if t.isdigit() else -1 for t in line.split()]
def adj(s): return sum(1 for a, b in zip(s, s[1:]) if a >= 1700 and b >= 1700)
a0 = adj(seq); nulls = []
for _ in range(2000):
    s = seq[:]; rng.shuffle(s); nulls.append(adj(s))
nulls.sort(); print(f"adjacent >=1700 pairs: target {a0}; null (b) mean {sum(nulls)/len(nulls):.2f} p95 {nulls[int(.95*len(nulls))]} pct {100*sum(1 for x in nulls if x < a0)/len(nulls):.1f}")
