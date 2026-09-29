#!/usr/bin/env python3
"""H328 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026), script-only, written before running: is H325's result (f.124r's held gloss, 148
letters in key v7's cells vs shuffled-cell p95 140) letter frequency rather than cells? Same words, signs and one-to-one count as
family/h325_124r_agreed.py (its data-building code is executed unchanged up to its scoring). Two frequency-matched controls:
 (a) BINNED: the keyed classes present are ranked by their token count on f.124r's reconciled draft and cut into bins of 3 adjacent ranks; cells are
     permuted only within a bin (1000 keys, seed 328), so a frequent class always gets another frequent class's cell;
 (b) FREQUENCY KEY: each keyed class gets the k most frequent letters of French (tools/data/fr16, j->i, v->u, y->i), k = its v7 cell size -- an
     upper bound for a key that knows only letter frequency.
Pre-stated: the H325 lead stands iff real > (a)'s p95 AND real > (b)'s score; else 'H325 explained by frequency'. No reading, no merge.
python3 h328_124r_freq.py [--check]"""
import glob, gzip, os, random, re, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
src = open(f"{HERE}/h325_124r_agreed.py").read(); src = src[:src.index("real, hits = score(cell, True)")]
_argv = sys.argv; g = {"__file__": f"{HERE}/h325_124r_agreed.py", "__name__": "h325"}; exec(compile(src, "h325_prefix", "exec"), g); sys.argv = _argv
score, cell, groups, rd, P = g["score"], g["cell"], g["groups"], g["rd"], g["P"]
real = score(cell)
cnt = Counter(r["sign"] for r in rd(f"{P}/recf124r/ciphertext_draft.tsv"))
classes = sorted({s[3] for _, ss in groups for s in ss if cell(s[3])}, key=lambda c: (-cnt[c], c))
bins = [classes[i:i + 3] for i in range(0, len(classes), 3)]
rng = random.Random(328); null = []
for _ in range(1000):
    mp = {}
    for bn in bins:
        cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
    null.append(score(lambda c: set(mp.get(c, ()))))
null.sort(); p95 = null[949]
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
lf = Counter()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read()
    lf.update(ch for ch in fold(t) if "a" <= ch <= "z")
order = [c for c, _ in lf.most_common()]
fk = {c: set(order[:len(cell(c))]) for c in classes}; fscore = score(lambda c: fk.get(c, set()))
out = [f"real {real}; (a) binned permutation (bins of 3 by f.124r token rank: " + " | ".join(",".join(b) for b in bins) + f"): mean {sum(null) / 1000:.1f}, p95 {p95}, max {null[-1]}, >= real {sum(n >= real for n in null)}/1000",
       f"(b) frequency key (top-k fr16 letters, k = v7 cell size; letter order {''.join(order[:10])}...): {fscore}",
       "read-out: " + ("H325 lead stands (real > (a) p95 and > (b))" if real > p95 and real > fscore else "H325 explained by frequency (real <= (a) p95 or <= (b))")]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h328_124r_freq_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
