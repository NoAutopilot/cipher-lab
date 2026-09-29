#!/usr/bin/env python3
"""H325 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026), script-only, written before running: H318's design at a larger N on a leaf never
loaded into key v7. fr.3982 f.124r (de Diou to Mayenne, 12 Nov 1592) carries an interlinear gloss whose two blind passes agreed on 42% of words (HELD,
family/key_period_f124_held.tsv, never merged). Words: gloss rows (kind 'gloss') that passes A and B (family/passes/f124r_gloss{A,B}.tsv) read
identically (case/accent-folded, j->i, v->u, y->i), on the same line and segment with overlapping x spans. Signs: the reconciled draft
(family/passes/recf124r/ciphertext_draft.tsv) with x from pass A where pass A's sign at the same line/position equals the draft's (H220's rule).
Letters of each agreed word are matched one-to-one, order-free, to the signs whose x falls inside the word's span (same line, segment), a letter
counting when the sign's key v7 cell holds it (build_key_v7.load_key_v7, pooled; EBR_A -> form A, EBR_B -> form B; classes with no v7 cell -- LOOPS,
OTHER, ... -- hold nothing). Control: 1000 keys with v7's cells permuted across the classes present (seed 325), the same words and signs.
Pre-stated: 'consistent with key v7 on a held leaf' iff real > the shuffled p95; else 'no signal'. Per-class hits reported for DBL, SBS, VBAR_A, EBR
(the classes f.211r's run would test). Gloss letters are two-pass agreed, grade M at best; nothing here is a reading or a merge.
python3 h325_124r_agreed.py [--check]"""
import csv, os, random, sys, unicodedata
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE)
sys.argv, _a = sys.argv[:1], sys.argv
import build_key_v7 as b
sys.argv = _a
KB, KA = b.load_key_v7(ebr="B"), b.load_key_v7(ebr="A")
def cell(c): return set(KA["EBR"]) if c == "EBR_A" else set(KB["EBR"]) if c == "EBR_B" else set(KB.get(c, ()))
rd = lambda f: list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
fold = lambda w: unicodedata.normalize("NFKD", w).encode("ascii", "ignore").decode().lower().translate(str.maketrans("jvy", "iui"))
gA = [r for r in rd(f"{P}/f124r_glossA.tsv") if r["kind"] == "gloss"]; gB = [r for r in rd(f"{P}/f124r_glossB.tsv") if r["kind"] == "gloss"]
words = []
for a in gA:
    for bb in gB:
        if a["line"] == bb["line"] and a["segment"] == bb["segment"] and fold(a["word"]) == fold(bb["word"]) and "?" not in a["word"]:
            x0, x1 = max(int(a["x0_px"]), int(bb["x0_px"])), min(int(a["x1_px"]), int(bb["x1_px"]))
            if x1 > x0: words.append((a["line"], a["segment"], int(a["x0_px"]), int(a["x1_px"]), "".join(ch for ch in fold(a["word"]) if ch.isalpha()))); break
A = {(r["line"], int(r["pos"])): r for r in rd(f"{P}/f124r_signsA.tsv")}; signs = []
for r in rd(f"{P}/recf124r/ciphertext_draft.tsv"):
    a = A.get((r["line"], int(r["position"])))
    if a and a["sign"] == r["sign"]: signs.append((r["line"], a["segment"], int(float(a["x_px"])), r["sign"]))
def match(letters, cells):
    m = {}
    def aug(i, seen):
        for j, c in enumerate(cells):
            if letters[i] in c and j not in seen:
                seen.add(j)
                if j not in m or aug(m[j], seen): m[j] = i; return True
        return False
    return [m[j] for j in m], sum(aug(i, set()) for i in range(len(letters)))
groups = [(w, [s for s in signs if s[0] == w[0] and s[1] == w[1] and w[2] <= s[2] <= w[3]]) for w in words]
def score(cf, per=False):
    tot = 0; hits = Counter()
    for w, ss in groups:
        cs = [cf(s[3]) for s in ss]; m = {}
        def aug(i, seen, L=w[4]):
            for j, c in enumerate(cs):
                if L[i] in c and j not in seen:
                    seen.add(j)
                    if j not in m or aug(m[j], seen): m[j] = i; return True
            return False
        tot += sum(aug(i, set()) for i in range(len(w[4])))
        if per:
            for j in m: hits[ss[j][3]] += 1
    return (tot, hits) if per else tot
real, hits = score(cell, True); nlet = sum(len(w[4]) for w, _ in groups); nsig = sum(len(ss) for _, ss in groups)
classes = sorted({s[3] for _, ss in groups for s in ss if cell(s[3])}); pool = [frozenset(cell(c)) for c in classes]
rng = random.Random(325); null = []
for _ in range(1000):
    p = pool[:]; rng.shuffle(p); mp = dict(zip(classes, p)); null.append(score(lambda c: set(mp.get(c, ()))))
null.sort(); p95 = null[949]
sc = Counter(s[3] for _, ss in groups for s in ss)
out = [f"agreed gloss words {len(words)} (of A {len(gA)}, B {len(gB)}), letters {nlet}, signs under them {nsig} (keyed classes {len(classes)})",
       f"real {real} letters matched; shuffled mean {sum(null) / 1000:.1f}, p95 {p95}, max {null[-1]}; >= real {sum(n >= real for n in null)}/1000",
       "hits by class (signs under words): " + " ".join(f"{c}={hits[c]}/{sc[c]}" for c in ("DBL", "SBS", "VBAR_A", "EBR_A", "EBR_B", "PHI", "4TRI", "C43", "H24", "HASH4")),
       "read-out: " + ("consistent with key v7 on a held leaf (real > shuffled p95)" if real > p95 else "no signal (real <= shuffled p95)")]
txt = "\n".join(out) + "\n"; res = f"{HERE}/h325_124r_agreed_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
