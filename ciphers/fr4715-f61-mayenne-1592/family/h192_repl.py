#!/usr/bin/env python3
"""H192 (runner 7, 29 Sept 2026): two-leaf replication table for the verifier. Per class (agreed columns only): top letters and shares on
fr.3984 f.176r (clear fol. 177r L01 - fol. 177v V05, N = signs; the h183 run) and on f.176v (clear fol. 177v V06 - fol. 178r, build_f176v_key.py
L01-L45 design), each beside the wrong-text (f.184r) share of the same letter. A class REPLICATES when both leaves give the same top letter with
share >= 0.5 and that letter's wrong-text share < 0.3 on both. Descriptive; reader codes may not map to the same sign on both leaves (H190).
  python3 h192_repl.py [--check]"""
import glob, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_f176_key as b, build_f176v_key as v
g = b.g
def run(A, B, rows, text, n_rule):
    key = g.load_key(); seq = [s for l in rows for s in b.consensus(A[l], B[l])]; N = min(len(text), n_rule(len(seq)))
    w = g.fold(" ".join(r["word"] for r in g.rd(f"{b.P}/f184r_clear_rec.tsv")))[:N]
    return b.run(seq, text[:N], key, "true")[0], b.run(seq, w, key, "wrong")[0]
def main():
    lines = {}
    for f in sorted(glob.glob(f"{b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    t176r = v.clear177r() + "".join(g.fold(lines[f"V{k:02d}"]) for k in range(1, 6))
    R = run(b.pass_rows("A"), b.pass_rows("B"), [f"L{k:02d}" for k in range(1, 48)], t176r, lambda n: n)
    V = run(v.pass_rows("A"), v.pass_rows("B"), [f"L{k:02d}" for k in range(1, 46)], v.clear("V06")[0], lambda n: int(0.8 * n))
    sh = lambda C, x: C[x] / sum(C.values()) if sum(C.values()) else 0
    top = lambda C: max(C, key=lambda x: (C[x], x)) if C else "-"
    out = ["class\tf.176r top (share; wrong)\tn\tf.176v top (share; wrong)\tn\treplicates"]; rep = 0
    for c in sorted(set(R[0]) | set(V[0]), key=lambda c: -(sum(R[0][c].values()) + sum(V[0][c].values()))):
        tr, tv = top(R[0][c]), top(V[0][c]); nr, nv = sum(R[0][c].values()), sum(V[0][c].values())
        ok = tr == tv and sh(R[0][c], tr) >= 0.5 and sh(V[0][c], tv) >= 0.5 and sh(R[1][c], tr) < 0.3 and sh(V[1][c], tv) < 0.3 and nr >= 10 and nv >= 10
        rep += ok
        out.append(f"{c}\t{tr} ({sh(R[0][c], tr):.2f}; {sh(R[1][c], tr):.2f})\t{nr}\t{tv} ({sh(V[0][c], tv):.2f}; {sh(V[1][c], tv):.2f})\t{nv}\t{'YES' if ok else 'no'}")
    out.append(f"replicating classes (n >= 10 on both): {rep}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h192_repl_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
