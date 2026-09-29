#!/usr/bin/env python3
"""H349 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only, written before running: H345 without its cell-size confound. For each
keyed class with >= 30 signs in runs on f.124r and f.97r, v7's cell (size k) is compared by H342's gain (the same 10 within-run shuffles, seed 342) with
size-matched alternatives only: every distinct v7 cell of size k held by another class, plus 30 random letter sets of size k drawn without replacement,
weighted by fr16 letter frequency (seed 349 per class and leaf), v7's own set excluded. Pre-stated per class: 'supported' iff v7's gain beats >= 95% of
its alternatives on BOTH leaves; 'mixed' iff on one; else 'not supported'. EBR_B and VBAR_A named in the output. No cell is changed. Fix (16:23 UTC, before any output was seen): the draw loop is capped at the number of possible sets of size k
(a one-letter cell has 25 alternatives; the first run looped forever on f.97r's VBAR_B).
python3 h349_seqgain_sizematch.py [--check]"""
import glob, gzip, os, random, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); ARGS = sys.argv[1:]; out = []
src = open(f"{HERE}/h335_106r_v7_beam.py").read(); src = src[:src.index("real = score(cell)")]
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
lf = Counter()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read(); lf.update(ch for ch in fold(t) if "a" <= ch <= "z")
letters = sorted(lf); wts = [lf[c] for c in letters]
def draw(rng, k):
    s = set()
    while len(s) < k: s.add(rng.choices(letters, wts)[0])
    return frozenset(s)
verdict = {}
for prefix in ("recf124r", "recf97r"):
    g = {"__file__": f"{HERE}/h335_106r_v7_beam.py", "__name__": "h349"}; sys.argv = [sys.argv[0]]
    exec(compile(src.replace("recf106rall/", f"{prefix}/"), f"h335_on_{prefix}", "exec"), g)
    runs, cell, classes, score = g["runs"], g["cell"], g["classes"], g["score"]
    rng = random.Random(342); shuf = []
    for _ in range(10):
        s = []
        for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
        shuf.append(s)
    def gain(cf):
        g["runs"] = runs; real = score(cf); sh = []
        for s in shuf: g["runs"] = s; sh.append(score(cf))
        g["runs"] = runs; return real - sum(sh) / len(sh)
    n_in = Counter(c for r in runs for c in r); gv = gain(cell); out.append(f"{prefix}: gain(v7) {gv:.4f}")
    for c in [c for c in classes if n_in[c] >= 30]:
        own = frozenset(cell(c)); k = len(own); alts = {frozenset(cell(d)) for d in classes if d != c and len(cell(d)) == k} - {own}
        r2 = random.Random(f"349-{prefix}-{c}")
        from math import comb
        cap = min(30 + len(alts), comb(len(letters), k) - 1)   # H349 fix before any output: a 1-letter cell has at most 25 alternatives
        while len(alts) < cap:
            a = draw(r2, k)
            if a != own: alts.add(a)
        ga = [gain(lambda x, c=c, a=a: set(a) if x == c else cell(x)) for a in sorted(alts, key=sorted)]
        share = sum(gv > x for x in ga) / len(ga); ok = share >= 0.95; verdict.setdefault(c, []).append(ok)
        out.append(f"  {c:8s} cell {'/'.join(sorted(own)):8s} k {k} signs {n_in[c]:4d}: beats {share:.2f} of {len(ga)} size-matched alternatives -> {'pass' if ok else 'miss'}")
out.append("per class (both leaves): " + " ".join(f"{c}={'supported' if all(v) and len(v) == 2 else 'mixed' if any(v) else 'not supported'}{'' if len(v) == 2 else '(one leaf only)'}" for c, v in verdict.items()))
txt = "\n".join(out) + "\n"; rs = f"{HERE}/h349_seqgain_sizematch_result.txt"
if "--check" in ARGS:
    ok = os.path.exists(rs) and open(rs).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(rs, "w").write(txt); print(txt, end="")
