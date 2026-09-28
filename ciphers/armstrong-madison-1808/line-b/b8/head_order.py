"""Line B step B8 (re-scoped after B1/B2) -- do the 2-digit heads follow an alphabetical or a frequency order?
Prediction under 'alphabetical 99-word function list': head value = alphabetical rank of the word; expected count of
head v = frequency of the v-th function word (en18, 99 most frequent words). Under 'frequency order': head 1 = the
commonest word, etc. Statistic: Spearman correlation between predicted and observed head counts over v = 1..99;
null: the 99 predicted counts randomly permuted (10,000 draws). The same for the family totals (head + members)."""
import random, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "b1"))
from padding_test import target_tokens, en18_words
toks = target_tokens(); c = Counter(toks)
words = en18_words(); freq = Counter(w for ws in words for w in ws)
top = freq.most_common(99)
def rank(x):
    s = sorted(range(len(x)), key=lambda i: x[i]); r = [0]*len(x)
    for k, i in enumerate(s): r[i] = k
    return r
def spearman(a, b):
    ra, rb = rank(a), rank(b); n = len(a); ma = (n-1)/2
    sxy = sum((x-ma)*(y-ma) for x, y in zip(ra, rb)); sxx = sum((x-ma)**2 for x in ra)
    return sxy / sxx
obs_head = [c[v] for v in range(1, 100)]
obs_fam = [c[v] + (sum(c[10*v+u] + c[1000+10*v+u] for u in range(10)) if v >= 10 else 0) for v in range(1, 100)]
alpha = [n for _, n in sorted(top, key=lambda wn: wn[0])]
freqo = [n for _, n in top]
rng = random.Random(3)
for name, pred in (("alphabetical", alpha), ("frequency-ordered", freqo)):
    for oname, obs in (("bare heads", obs_head), ("families", obs_fam)):
        r = spearman(pred, obs); null = []
        for _ in range(10000):
            p = pred[:]; rng.shuffle(p); null.append(spearman(p, obs))
        null.sort(); print(f"{name:18s} vs {oname:10s}: rho {r:+.3f}  null p05 {null[500]:+.3f} p95 {null[9500]:+.3f} p99 {null[9900]:+.3f}  pct {100*sum(1 for x in null if x < r)/len(null):.1f}")
print("alphabetical list, first 20:", [w for w, _ in sorted(top, key=lambda wn: wn[0])][:20])
print("observed heads with count >= 3:", sorted(((v, c[v]) for v in range(1, 100) if c[v] >= 3), key=lambda x: -x[1]))

# positive control: en18 letters (60 windows of 369 tokens) whose heads ARE the alphabetical 99-word list -> rho
rng2 = random.Random(11)
alpha_words = [w for w, _ in sorted(top, key=lambda wn: wn[0])]; code = {w: i+1 for i, w in enumerate(alpha_words)}
rhos = []
for k in range(60):
    ws = rng2.choice(words); start = rng2.randint(0, len(ws) - 3000); out = []
    for w in ws[start:]:
        out.append(code.get(w, 0))
        if len(out) == 369: break
    cc = Counter(out); rhos.append(spearman(alpha, [cc[v] for v in range(1, 100)]))
rhos.sort(); print(f"positive control (heads = alphabetical en18 list, 60 letters): rho mean {sum(rhos)/60:+.3f} p05 {rhos[3]:+.3f} p95 {rhos[57]:+.3f}")
