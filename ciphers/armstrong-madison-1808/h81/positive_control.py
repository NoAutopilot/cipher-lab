"""H81 positive control: do simulated 369-group letters (design/design_stats.py designs, en18 plaintext,
60 per design, seeds as ARM-DESIGN) and the real THE=972 / WE028 usage letters show numeral n-gram repeats?
Each simulated stream is cut at the target's own 35 mark positions (30 segments), so the break structure matches."""
import sys, random, re
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "design"))
import design_stats as D
toks = [t for l in open(HERE.parent / "ciphertext.txt") if not l.startswith('#') for t in l.split()]
mask = [bool(re.fullmatch(r'\d+', t)) for t in toks]
def cut(nums):  # place nums into the target's numeral slots, return segments
    it = iter(nums); segs, cur = [], []
    for m in mask:
        if m: cur.append(next(it))
        elif cur: segs.append(cur); cur = []
    if cur: segs.append(cur)
    return segs
def reps(segs, n):
    c = Counter(tuple(s[i:i+n]) for s in segs for i in range(len(s)-n+1))
    return sum(1 for v in c.values() if v >= 2)
# rebuild the designs exactly as design_stats.main does (copied construction, no file writes)
import argparse
we028 = D.load_table(D.US / "WE028.tsv"); the972 = D.load_table(D.US / "THE972_bourdeau.tsv")
corp = D.en18_words(); allw = Counter(w for f in corp for w in f)
particles = [w for w, _ in allw.most_common(400)][:99]; stopset = set(particles)
top3k = {w for w, _ in allw.most_common(4000)}
def lemma(w):
    for suf in D.SUFFIXES:
        if w.endswith(suf) and len(w) > len(suf) + 2:
            st = w[:-len(suf)]
            if st in top3k: return st
            if st + "e" in top3k: return st + "e"
    return w
lem = Counter()
for w, n in allw.most_common(6000):
    if w not in stopset and len(w) > 2: lem[lemma(w)] += n
roots = [w for w, _ in lem.most_common(180)]
extra = [w for w, _ in lem.most_common(800) if w not in roots][:450]
def sample_words(r, k):
    f = r.choice(corp); i = r.randrange(0, len(f) - k); return f[i:i + k]
vv0 = sorted(we028); vw = [we028[v] for v in vv0]
designs = {"blockwise_WE028": lambda r: D.TableCode(we028),
           "onepart": lambda r: D.TableCode(dict(zip(vv0, sorted(vw)))),
           "the972_partial": lambda r: D.TableCode(the972),
           "hdec": lambda r: D.DecadeCode(roots, particles, "hdec", r),
           "hhom_flat": lambda r: D.DecadeCode(roots, particles, "hhom_flat", r)}
def twopart(r):
    vv = vv0[:]; r.shuffle(vv); return D.TableCode(dict(zip(vv, vw)))
designs["twopart"] = twopart
N = sum(mask); print(f"target numeral groups {N}, segments {len(cut(['x']*N))}")
print("stream\tn_sims\tmean_rep2\tmean_rep3\tshare_rep3>=1\tmean_rep4\tmin_rep2\tp05_rep2")
for name, mk in designs.items():
    r2, r3, r4 = [], [], []
    for i in range(60):
        r = random.Random(1000 + i); code = mk(r); t = []
        while len(t) < N:
            if hasattr(code, "drops"): code.drops = 0
            t = code.encode(sample_words(r, N * 2), r)[:N]
        s = cut(t); r2.append(reps(s, 2)); r3.append(reps(s, 3)); r4.append(reps(s, 4))
    print(f"{name}\t60\t{sum(r2)/60:.2f}\t{sum(r3)/60:.2f}\t{sum(1 for x in r3 if x)/60:.2f}\t{sum(r4)/60:.2f}\t{min(r2)}\t{sorted(r2)[3]}")
for k, v in list(D.usage_instances().items()):
    s = [list(v)]; print(f"REAL THE972 {k} (N={len(v)}, unsegmented)\t1\t{reps(s,2)}\t{reps(s,3)}\t{int(reps(s,3)>0)}\t{reps(s,4)}")
s = cut([t for t,m in zip(toks,mask) if m]); print(f"TARGET\t1\t{reps(s,2)}\t{reps(s,3)}\t{int(reps(s,3)>0)}\t{reps(s,4)}")
