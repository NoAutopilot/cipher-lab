#!/usr/bin/env python3
"""VERIFY-F61-V6 task 2b: word context of every H193 f.176r target under the runner's alignment (key v4, whose 4TRI set is {a,c,n,p,t},
so the DP scores c/p and a/n alike at a 4TRI column and cannot steer the split). Per target: runner's bowl answer, 10 letters each side of
the paired letter, and the 3 sign columns each side with their paired letters. The verifier reads the word by eye (verdicts in AUDIT.md).
  python3 context_check.py [--check]"""
import os, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../family"))
import align_check as A
H = A.H; g = H.g
def main():
    lines = {}
    for f in sorted(glob.glob(f"{H.b.P}/f177v_clearA_*.tsv")):
        for r in g.rd(f): lines.setdefault("V" + r["line"].lstrip("LV"), r["text"])
    sr, orr = H.cons_origin(H.rows_full("f176r_signsA_*.tsv"), H.rows_full("f176r_signsB_*.tsv"), [f"L{k:02d}" for k in range(1, 48)])
    tr = H.v.clear177r() + "".join(g.fold(lines[f"V{k:02d}"]) for k in range(1, 6)); tr = tr[:len(sr)]
    kf = g.load_key(); _, pf = A.align(tr, sr, kf); mf = {j: i for i, j in pf}
    out = ["# key v4 4-family sets: " + ", ".join(f"{c} {''.join(sorted(v))}" for c, v in sorted(kf.items()) if A.fam(c))]
    ans = {r["item"]: r["answer"].strip().lower() for r in g.rd(f"{HERE}/../family/passes/h193_attribute.tsv")}
    for r in g.rd(f"{HERE}/../family/h193_items.tsv"):
        if r["group"] != "T": continue
        j = orr.index((r["line"], r["segment"], int(r["x_px"]))); i = mf[j]
        nb = " ".join(f"{sr[jj][:6]}={tr[mf[jj]] if jj in mf else '-'}" for jj in range(j - 3, j + 4))
        out.append(f"{r['item']}\t{ans.get(r['item'])}\t{tr[i-10:i]}[{tr[i]}]{tr[i+1:i+10]}\t{nb}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/context_check_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
