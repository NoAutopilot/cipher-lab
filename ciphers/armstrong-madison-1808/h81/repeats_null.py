"""H81: numeral-only repeated n-grams in the 369 groups vs a shuffled-order null.
Shorthand/star marks (*, **) are breaks: an n-gram never spans one. Null: permute the numeral
groups over the same slots (marks stay put), 1000 draws, seed 81. Order is the axis repeat
counts depend on, so the null can differ from the target (CLAUDE.md rule 3)."""
import random, re, sys
from collections import Counter
src = sys.argv[1]
toks = [t for l in open(src) if not l.startswith('#') for t in l.split()]
def segs(ts):
    out, cur = [], []
    for t in ts:
        if re.fullmatch(r'\d+', t): cur.append(t)
        else:
            if cur: out.append(cur); cur = []
    if cur: out.append(cur)
    return out
def stats(ts):
    r = {}
    for n in (2, 3, 4):
        c = Counter(tuple(s[i:i+n]) for s in segs(ts) for i in range(len(s)-n+1))
        r[n] = sum(1 for v in c.values() if v >= 2)
    return r
obs = stats(toks)
num_idx = [i for i, t in enumerate(toks) if re.fullmatch(r'\d+', t)]
nums = [toks[i] for i in num_idx]
rng = random.Random(81); null = {2: [], 3: [], 4: []}
for _ in range(1000):
    rng.shuffle(nums); ts = list(toks)
    for i, v in zip(num_idx, nums): ts[i] = v
    for n, v in stats(ts).items(): null[n].append(v)
print(f"groups {len(num_idx)}  segments {len(segs(toks))}  marks {len(toks)-len(num_idx)}")
print("n\tobserved\tnull_mean\tnull_p95\tP(null>=obs)")
for n in (2, 3, 4):
    xs = sorted(null[n]); p95 = xs[int(0.95*len(xs))]
    p = sum(1 for x in xs if x >= obs[n]) / len(xs)
    print(f"{n}\t{obs[n]}\t{sum(xs)/len(xs):.2f}\t{p95}\t{p:.3f}")
