#!/usr/bin/env python3
"""H358 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: the control for H356/H357's pointers.
H342's order gain (mean over three within-run shuffle seeds 342/343/344, as H347/H356). (a) f.124r: 4TRI's cell c/p/t widened by a/n (the named
variant) vs widened by each of 30 random 2-letter sets drawn by fr16 letter frequency, excluding c/p/t (seed 358). (b) f.97r: EBR_B's cell replaced by
a/l/s (the named variant; EBR_A kept at a/l/s) vs replaced by each of 30 random 3-letter sets drawn the same way (seed 3580). Pre-stated: a pointer
stands iff the named variant's mean gain beats >= 95% of its random variants; else 'added letters, not these letters'. No cell is changed.
python3 h358_variant_ctl.py [--check]"""
import glob, gzip, os, random, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
lf = Counter()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read(); lf.update(ch for ch in fold(t) if "a" <= ch <= "z")
letters = sorted(lf); wts = [lf[c] for c in letters]
def draws(seed, k, excl, n=30):
    rng = random.Random(seed); got = []
    while len(got) < n:
        s = set()
        while len(s) < k:
            ch = rng.choices(letters, wts)[0]
            if ch not in excl: s.add(ch)
        if frozenset(s) not in got: got.append(frozenset(s))
    return got
def leaf(prefix):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h358"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    runs, cell, score = g["runs"], g["cell"], g["score"]; shufsets = []
    for seed in (342, 343, 344):
        rng = random.Random(seed); ss = []
        for _ in range(10):
            s = []
            for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
            ss.append(s)
        shufsets.append(ss)
    def gain(cf):
        res = []
        for ss in shufsets:
            g["runs"] = runs; real = score(cf); sh = []
            for s in ss: g["runs"] = s; sh.append(score(cf))
            res.append(real - sum(sh) / len(sh))
        g["runs"] = runs; return sum(res) / 3
    return cell, gain
cell, gain = leaf("recf124r"); T = set(cell("4TRI"))
named = gain(lambda c: T | {"a", "n"} if c == "4TRI" else cell(c))
rnd = [gain(lambda c, s=s: T | s if c == "4TRI" else cell(c)) for s in draws(358, 2, T)]
share = sum(named > x for x in rnd) / len(rnd)
out.append(f"(a) f.124r 4TRI c/p/t + a/n: mean gain {named:.4f}; 30 random 2-letter widenings mean {sum(rnd) / 30:.4f} max {max(rnd):.4f}; beats {share:.2f} -> {'pointer stands' if share >= 0.95 else 'added letters, not these letters'}")
cell, gain = leaf("recf97r"); ALS = {"a", "l", "s"}
named = gain(lambda c: ALS if c == "EBR_B" else cell(c))
rnd = [gain(lambda c, s=s: set(s) if c == "EBR_B" else cell(c)) for s in draws(3580, 3, set())]
share = sum(named > x for x in rnd) / len(rnd)
out.append(f"(b) f.97r EBR_B <- a/l/s: mean gain {named:.4f}; 30 random 3-letter cells mean {sum(rnd) / 30:.4f} max {max(rnd):.4f}; beats {share:.2f} -> {'pointer stands' if share >= 0.95 else 'added letters, not these letters'}")
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h358_variant_ctl_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
