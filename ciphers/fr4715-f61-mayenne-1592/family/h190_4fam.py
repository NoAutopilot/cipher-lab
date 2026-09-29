#!/usr/bin/env python3
"""H190 (runner 7, 29 Sept 2026): do agreed-4TRI columns and A-4TRI/B-C43 split columns read different letter pairs on Desportes's leaves?
f.176v L01-L45 (clear fol. 177v V06-, build_f176v_key.py design) and f.176r L01-L47 (clear fol. 177r L01 - fol. 177v V05, h183 design). For each,
the DP pairs are split into agreed 4TRI columns and the A|B = 4TRI|C43 (either order) split columns; counts of {c,p} and {a,n} in each; Fisher
exact test (two-sided); the same under the wrong text f.184r. Descriptive.  python3 h190_4fam.py [--check]"""
import os, sys
from math import comb
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b, build_f176v_key as v, glob
from f61crib import align
g = b.g
def fisher(a, bb, c, d):
    n = a + bb + c + d; r1 = a + bb; c1 = a + c; p0 = comb(r1, a) * comb(n - r1, c1 - a) / comb(n, c1); p = 0.0
    for x in range(max(0, c1 - (n - r1)), min(r1, c1) + 1):
        px = comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
        if px <= p0 * (1 + 1e-9): p += px
    return p
def counts(seq, text, key):
    _, pairs = align(text, seq, key); ag = {"cp": 0, "an": 0}; sp = {"cp": 0, "an": 0}
    for i, j in pairs:
        s = seq[j]; L = text[i]; k = "cp" if L in "cp" else "an" if L in "an" else None
        if not k: continue
        if s == "4TRI": ag[k] += 1
        elif s.startswith("?") and sorted(s[1:].split("|")) == ["4TRI", "C43"]: sp[k] += 1
    return ag, sp
def leaf(name, A, B, rows, text):
    key = g.load_key(); seq = [s for l in rows for s in b.consensus(A[l], B[l])]; N = min(len(text), int(0.8 * len(seq)) if name == "f.176v" else len(seq))
    out = []
    for tag, t in (("true", text[:N]), ("wrong f.184r", g.fold(" ".join(r["word"] for r in g.rd(f"{b.P}/f184r_clear_rec.tsv")))[:N])):
        ag, sp = counts(seq, t, key); p = fisher(ag["cp"], ag["an"], sp["cp"], sp["an"])
        out.append(f"{name} {tag}: agreed 4TRI c/p {ag['cp']} a/n {ag['an']}; split 4TRI|C43 c/p {sp['cp']} a/n {sp['an']}; Fisher p {p:.2g}")
    return out
def main():
    lines = {}
    for f in sorted(glob.glob(f"{b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    t176r = v.clear177r() + "".join(g.fold(lines[f"V{k:02d}"]) for k in range(1, 6))
    out = leaf("f.176v", v.pass_rows("A"), v.pass_rows("B"), [f"L{k:02d}" for k in range(1, 46)], v.clear("V06")[0])
    out += leaf("f.176r", b.pass_rows("A"), b.pass_rows("B"), [f"L{k:02d}" for k in range(1, 48)], t176r)
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h190_4fam_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
