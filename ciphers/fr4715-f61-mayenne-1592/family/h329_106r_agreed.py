#!/usr/bin/env python3
"""H329 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026), script-only, written before running: H325's count and H328's controls on
fr.3983 f.106r -- HELD (gloss word agreement 0.339, key_period_f106_held.tsv, never loaded into a key) and in Mayenne's secretary's hand, f.61's hand.
H325's data-building code is executed with 'f124r' replaced by 'f106r' (same pass formats: family/passes/f106r_gloss{A,B}.tsv, f106r_signsA.tsv,
recf106r/ciphertext_draft.tsv). Controls: (a) shuffled cells across the keyed classes present (1000, seed 329); (b) binned permutation within bins
of 3 classes adjacent in f.106r token rank (1000, seed 3290); (c) frequency-only key (top-k fr16 letters, k = v7 cell size).
Pre-stated: 'consistent with key v7 on a held leaf in f.61's hand' iff real > (b) p95 AND real > (c); else 'no signal beyond frequency'.
No reading, no merge.  python3 h329_106r_agreed.py [--check]"""
import glob, gzip, os, random, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
src = open(f"{HERE}/h325_124r_agreed.py").read(); src = src[:src.index("real, hits = score(cell, True)")].replace("f124r", "f106r")
_argv = sys.argv; g = {"__file__": f"{HERE}/h325_124r_agreed.py", "__name__": "h329"}; exec(compile(src, "h325_prefix_f106r", "exec"), g); sys.argv = _argv
score, cell, groups, rd, P, words = g["score"], g["cell"], g["groups"], g["rd"], g["P"], g["words"]
real, hits = score(cell, True)
nlet = sum(len(w[4]) for w, _ in groups); nsig = sum(len(ss) for _, ss in groups)
cnt = Counter(r["sign"] for r in rd(f"{P}/recf106r/ciphertext_draft.tsv"))
classes = sorted({s[3] for _, ss in groups for s in ss if cell(s[3])}, key=lambda c: (-cnt[c], c))
def perm(seed, bins):
    rng = random.Random(seed); out = []
    for _ in range(1000):
        mp = {}
        for bn in bins:
            cs = [frozenset(cell(c)) for c in bn]; rng.shuffle(cs); mp.update(zip(bn, cs))
        out.append(score(lambda c: set(mp.get(c, ()))))
    return sorted(out)
na = perm(329, [classes]); nb = perm(3290, [classes[i:i + 3] for i in range(0, len(classes), 3)])
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
lf = Counter()
for f in glob.glob(f"{ROOT}/tools/data/fr16/*.txt.gz") + glob.glob(f"{ROOT}/tools/data/fr16/*.txt"):
    t = (gzip.open(f, "rt", errors="ignore") if f.endswith(".gz") else open(f, errors="ignore")).read(); lf.update(ch for ch in fold(t) if "a" <= ch <= "z")
order = [c for c, _ in lf.most_common()]; fscore = score(lambda c: set(order[:len(cell(c))]) if c in classes else set())
sc = Counter(s[3] for _, ss in groups for s in ss)
out = [f"agreed gloss words {len(words)}, letters {nlet}, signs under them {nsig}, keyed classes {len(classes)}: {' '.join(classes)}",
       f"real {real}; (a) shuffled cells mean {sum(na) / 1000:.1f} p95 {na[949]} >= real {sum(n >= real for n in na)}/1000; (b) binned mean {sum(nb) / 1000:.1f} p95 {nb[949]} >= real {sum(n >= real for n in nb)}/1000; (c) frequency key {fscore}",
       "hits by class: " + " ".join(f"{c}={hits[c]}/{sc[c]}" for c in classes),
       "read-out: " + ("consistent with key v7 on a held leaf in f.61's hand" if real > nb[949] and real > fscore else "no signal beyond frequency")]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h329_106r_agreed_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
