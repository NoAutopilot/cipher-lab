"""Line B step B25 -- are adjacent rich rows (17/18, 47/48, 11/12) homophones of one word or two different words?
Statistic per pair (a, b): number of adjacent tokens whose rows are (a, b) in either order; null = token positions
permuted (10,000 draws). Positive control: en18 letters with the two commonest function words ('the', 'of') mapped
to rows 17 and 18 (their bigram 'of the' is frequent) -- must exceed its null p95 on >= 45 of 60; negative control:
'the' split at random between rows 17 and 18 (homophones) -- <= 6 of 60 above p95. Other words: 99 next commonest ->
rows, rest -> 3-digit values (a Bf-like book)."""
import random, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "b1"))
from padding_test import target_tokens, en18_words
def row_of(v):
    if v < 10: return None
    return v if v < 100 else (v // 10 if v < 1000 else (v - 1000) // 10)
def adj(rows, a, b): return sum(1 for x, y in zip(rows, rows[1:]) if (x == a and y == b) or (x == b and y == a))
def test(toks, a, b, rng, draws):
    rows = [row_of(v) for v in toks]; s = adj(rows, a, b); null = []
    for _ in range(draws):
        r = rows[:]; rng.shuffle(r); null.append(adj(r, a, b))
    null.sort(); return s, null[int(.95*draws)], 100*sum(1 for x in null if x < s)/draws
words = en18_words(); freq = Counter(w for ws in words for w in ws); top = [w for w, _ in freq.most_common(200)]
def build(homophone, rng):
    code = {}; pool = [r for r in range(10, 100) if r not in (17, 18)]; rng.shuffle(pool)
    others = [w for w in top if w not in ('the', 'of')]
    for w, r in zip(others[:88], pool): code[w] = r
    for i, w in enumerate(others[88:]): code[w] = 100 + i
    if homophone: code['the'] = (17, 18); code['of'] = 100 + 200
    else: code['the'] = 17; code['of'] = 18
    return code
def simulate(code, rng, n=369):
    ws = rng.choice(words); start = rng.randint(0, len(ws) - 3000); out = []
    for w in ws[start:]:
        if w in code:
            v = code[w]; out.append(rng.choice(v) if isinstance(v, tuple) else v)
        if len(out) == n: break
    return out
rng = random.Random(12)
pos = [test(simulate(build(False, random.Random(i)), random.Random(6000+i)), 17, 18, rng, 2000) for i in range(60)]
neg = [test(simulate(build(True, random.Random(i)), random.Random(6000+i)), 17, 18, rng, 2000) for i in range(60)]
pc = sum(1 for p in pos if p[2] >= 95); nc = sum(1 for p in neg if p[2] >= 95)
print(f"positive control (the=17, of=18): adjacency mean {sum(p[0] for p in pos)/60:.1f}, above own p95: {pc}/60")
print(f"negative control (the split 17/18): adjacency mean {sum(p[0] for p in neg)/60:.1f}, above own p95: {nc}/60")
gate = pc >= 45 and nc <= 6; print("GATE:", "MET" if gate else "NOT MET")
for a, b in ((17, 18), (47, 48), (11, 12), (17, 38), (18, 38)):
    s, p95, pct = test(target_tokens(), a, b, rng, 10000)
    print(f"TARGET rows {a}/{b}: adjacent {s}, null p95 {p95}, percentile {pct:.1f}" + ("" if gate else "  [unlicensed]"))

# addendum: adjacency among the FIVE richest rows as a set (17, 18, 38, 14, 16 by family tokens) vs the en18 control
# with the five commonest function words on five rows (of-the, to-the, in-the, and-the collocate strongly).
def adjset(rows, S): return sum(1 for x, y in zip(rows, rows[1:]) if x in S and y in S and x != y)
def testset(toks, S, rng, draws):
    rows = [row_of(v) for v in toks]; s = adjset(rows, S); null = []
    for _ in range(draws):
        r = rows[:]; rng.shuffle(r); null.append(adjset(r, S))
    null.sort(); return s, null[int(.05*draws)], null[int(.95*draws)], 100*sum(1 for x in null if x < s)/draws
def build5(rng):
    code = {}; five = ['the', 'of', 'to', 'and', 'in']; rows5 = [17, 18, 38, 14, 16]
    pool = [r for r in range(10, 100) if r not in rows5]; rng.shuffle(pool)
    others = [w for w in top if w not in five]
    for w, r in zip(others[:85], pool): code[w] = r
    for i, w in enumerate(others[85:]): code[w] = 100 + i
    for w, r in zip(five, rows5): code[w] = r
    return code
S = {17, 18, 38, 14, 16}
ctrl = [testset(simulate(build5(random.Random(i)), random.Random(7000+i)), S, rng, 1000) for i in range(60)]
print(f"\ncontrol (the/of/to/and/in on the five rows): adjacency mean {sum(c[0] for c in ctrl)/60:.1f}, above own p95: {sum(1 for c in ctrl if c[3] >= 95)}/60")
s, p05, p95, pct = testset(target_tokens(), S, rng, 10000)
print(f"TARGET five richest rows: adjacent {s}, null p05 {p05} p95 {p95}, percentile {pct:.1f}")
