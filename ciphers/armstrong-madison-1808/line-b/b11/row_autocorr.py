"""Line B step B11 -- are the rows (decades 10-99) in an alphabetical (one-part) order?
Under alphabetical buckets, neighbouring rows share initial letters, so family totals are autocorrelated in row
index; under a two-part (random row order) layout they are not. Statistic: lag-1 and lag-2 autocorrelation of
family totals (head + 3-digit + 4-digit members) over rows 10..99; null: rows permuted (10,000 draws).
Positive control: B2's Bf layout (alphabetical buckets headed by the commonest word), 60 en18 letters; negative
control: the same layout with the row order shuffled, 60 letters. Gate: positive p95-clear on >= 45 of 60 letters,
negative on <= 6 of 60, before the target is read."""
import random, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "b1")); sys.path.insert(0, str(HERE.parent / "b2"))
from padding_test import target_tokens, en18_words
import designs
V = list(range(10, 100))
def fam(cc): return [cc[v] + sum(cc[10*v+u] + cc[1000+10*v+u] for u in range(10)) for v in V]
def ac(x, lag):
    a, b = x[:-lag], x[lag:]; ma = sum(a)/len(a); mb = sum(b)/len(b)
    sxy = sum((p-ma)*(q-mb) for p, q in zip(a, b)); sxx = sum((p-ma)**2 for p in a); syy = sum((q-mb)**2 for q in b)
    return sxy/(sxx*syy)**0.5 if sxx and syy else 0.0
def test(toks, rng, draws=10000):
    f = fam(Counter(toks)); r1, r2 = ac(f, 1), ac(f, 2); n1 = []; n2 = []
    for _ in range(draws):
        g = f[:]; rng.shuffle(g); n1.append(ac(g, 1)); n2.append(ac(g, 2))
    n1.sort(); n2.sort()
    return r1, n1[int(.95*draws)], 100*sum(1 for x in n1 if x < r1)/draws, r2, n2[int(.95*draws)], 100*sum(1 for x in n2 if x < r2)/draws
rng = random.Random(4); words = en18_words()
code = designs.build(words, "Bf", random.Random(7))
# shuffled-row variant of the same code
rows = list(range(10, 100)); perm = rows[:]; random.Random(8).shuffle(perm); rowmap = dict(zip(rows, perm))
def shuf(v):
    if v < 10: return v
    if v < 100: return rowmap[v]
    if v < 1000: return 10*rowmap[v//10] + v % 10
    return 1000 + 10*rowmap[(v-1000)//10] + v % 10
code_shuf = {w: shuf(v) for w, v in code.items()}
pos = [test(designs.simulate(words, code, random.Random(2000+i)), rng, 2000) for i in range(60)]
neg = [test(designs.simulate(words, code_shuf, random.Random(2000+i)), rng, 2000) for i in range(60)]
pc = sum(1 for p in pos if p[2] >= 95); nc = sum(1 for n in neg if n[2] >= 95)
print(f"positive control (Bf, alphabetical rows): lag-1 mean {sum(p[0] for p in pos)/60:+.3f}, letters above own p95: {pc}/60; lag-2 mean {sum(p[3] for p in pos)/60:+.3f}")
print(f"negative control (Bf, rows shuffled):    lag-1 mean {sum(n[0] for n in neg)/60:+.3f}, letters above own p95: {nc}/60")
gate = pc >= 45 and nc <= 6
print("GATE:", "MET" if gate else "NOT MET")
t = test(target_tokens(), rng)
print(f"TARGET: lag-1 {t[0]:+.3f} (null p95 {t[1]:+.3f}, pct {t[2]:.1f}); lag-2 {t[3]:+.3f} (null p95 {t[4]:+.3f}, pct {t[5]:.1f})" + ("" if gate else "  [printed, not licensed]"))
