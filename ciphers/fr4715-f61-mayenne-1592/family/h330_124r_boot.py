#!/usr/bin/env python3
"""H330 + H331 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026), script-only, written before running, on H328's f.124r count
(H325's data code executed unchanged; H328's bins and frequency-only key).
H330: 200 bootstrap resamples of the agreed gloss words (seed 330); each resample scored with v7, against its own binned permutation null (200 keys,
seed 331 + resample index) and the frequency-only key. Pre-stated: 'robust' iff real > binned p95 in >= 80% of resamples AND > frequency key in >= 95%;
else 'fragile, rests on a few words'.
H331: per keyed class, (i) hits under v7 vs the class's mean and p95 hits under H328's binned permutation (1000 keys, seed 328 as H328), and (ii) the
drop in the total when that class's cell is blanked; descriptive (the AX-NAMES per-class lesson).  python3 h330_124r_boot.py [--check]"""
import glob, gzip, os, random, sys, unicodedata
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
src = open(f"{HERE}/h325_124r_agreed.py").read(); src = src[:src.index("real, hits = score(cell, True)")]
_argv = sys.argv; g = {"__file__": f"{HERE}/h325_124r_agreed.py", "__name__": "h330"}; exec(compile(src, "h325_prefix", "exec"), g); sys.argv = _argv
cell, groups, rd, P = g["cell"], g["groups"], g["rd"], g["P"]
def score(cf, grp, per=False):
    tot = 0; hits = Counter()
    for w, ss in grp:
        cs = [cf(s[3]) for s in ss]; m = {}; L = w[4]
        def aug(i, seen):
            for j, c in enumerate(cs):
                if L[i] in c and j not in seen:
                    seen.add(j)
                    if j not in m or aug(m[j], seen): m[j] = i; return True
            return False
        tot += sum(aug(i, set()) for i in range(len(L)))
        for j in m: hits[ss[j][3]] += 1
    return (tot, hits) if per else tot
cnt = Counter(r["sign"] for r in rd(f"{P}/recf124r/ciphertext_draft.tsv"))
classes = sorted({s[3] for _, ss in groups for s in ss if cell(s[3])}, key=lambda c: (-cnt[c], c)); bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]
def binkey(rng):
    mp = {}
    for bn in bins:
        cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
    return lambda c: set(mp.get(c, ()))
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
lf = Counter()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read(); lf.update(ch for ch in fold(t) if "a" <= ch <= "z")
order = [c for c, _ in lf.most_common()]; fkey = lambda c: set(order[:len(cell(c))]) if c in classes else set()
rng = random.Random(330); beat_b = beat_f = 0; R = 200
for k in range(R):
    grp = [groups[rng.randrange(len(groups))] for _ in groups]; r = score(cell, grp); r2 = random.Random(331 + k)
    nb = sorted(score(binkey(r2), grp) for _ in range(200)); beat_b += r > nb[189]; beat_f += r > score(fkey, grp)
out = [f"H330 bootstrap ({R} resamples of {len(groups)} words): real > binned p95 in {beat_b}/{R} ({beat_b / R:.0%}); real > frequency key in {beat_f}/{R} ({beat_f / R:.0%})",
       "H330 read-out: " + ("robust" if beat_b >= 0.8 * R and beat_f >= 0.95 * R else "fragile, rests on a few words")]
real, hits = score(cell, groups, True); rng = random.Random(328); per = defaultdict(list)
for _ in range(1000):
    _, h = score(binkey(rng), groups, True)
    for c in classes: per[c].append(h[c])
sc = Counter(s[3] for _, ss in groups for s in ss); rows = []
for c in classes:
    v = sorted(per[c]); blank = score(lambda x, c=c: set() if x == c else cell(x), groups)
    rows.append(f"{c}: v7 {hits[c]}/{sc[c]} signs, binned mean {sum(v) / 1000:.1f} p95 {v[949]}{' ABOVE' if hits[c] > v[949] else ''}; total without its cell {blank} ({blank - real:+d})")
out += ["H331 per class (f.124r token rank order):"] + rows
txt = "\n".join(out) + "\n"; res = f"{HERE}/h330_124r_boot_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
