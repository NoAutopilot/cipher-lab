#!/usr/bin/env python3
"""R12A-D1411P4: build numbers.tsv from the two blind passes (passA.tsv, passB.tsv), the tools/reconcile_passes.py
alignment (rec/ciphertext_draft.tsv) and the worker's crop settlements (reconcile_notes.tsv).
grade: ok only where both passes agree and neither flagged '?'; every settled or flagged number is M.
gloss: kept only where both passes wrote a non-blank gloss letter and the two agree after the fixed shape rule
1 -> i, 5 -> s (the gloss hand's bare-stroke i and 5-like s, GAPS150/D4-1411P3), '?' stripped; numbers whose value the
worker settled carry no gloss (so the gloss test never rests on a value the reconciler chose).
  python3 d1411p4/make_numbers.py [--check]"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda f: list(csv.DictReader(open(os.path.join(H, f)), delimiter="\t"))
A, B, D = rd("passA.tsv"), rd("passB.tsv"), rd("rec/ciphertext_draft.tsv")
S = {(r["line"], r["col"]): r for r in rd("reconcile_notes.tsv")}
NORM = {"1": "i", "5": "s"}
def gl(x):
    x = (x or "").strip().rstrip("?").lower()
    return NORM.get(x, x)
by = lambda P: {ln: [r for r in P if r["line"] == ln] for ln in {r["line"] for r in P}}
a, b = by(A), by(B)
out = [["line", "pos", "token", "grade", "note", "gloss"]]
ia = ib = 0; cur = None; pos = 0
for r in D:
    ln, col = r["line"], r["position"]
    if ln != cur:
        cur, ia, ib, pos = ln, 0, 0, 0
    ra = a.get(ln, [])[ia] if ia < len(a.get(ln, [])) else None
    gap = r["why"] == "gap"
    rb = None if gap else (b.get(ln, [])[ib] if ib < len(b.get(ln, [])) else None)
    ia += 1; ib += 0 if gap else 1
    st = S.get((ln, col))
    if st and st["settled"] == "drop":
        continue
    pos += 1
    if st:
        tok, grade, note, g = st["settled"].rstrip("?"), "M", st.get("note", "") or "", ""
    else:
        ta, tb = ra["token"], rb["token"]
        tok = ta.rstrip("?")
        grade = "ok" if ("?" not in ta + tb and ta == tb) else "M"
        note = "intext" if "intext" in (ra.get("note") or "") + (rb.get("note") or "") else ""
        ga, gb = gl(ra.get("gloss")), gl(rb.get("gloss"))
        g = ga if (ga and ga == gb) else ""
    out.append([ln, str(pos), tok, grade, note, g])
txt = "\n".join("\t".join(x) for x in out) + "\n"
p = os.path.join(H, "numbers.tsv")
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt
    print("numbers.tsv", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt)
n = [x for x in out[1:] if x[2].isdigit() and "intext" not in x[4]]
print(f"numbers {len(n)}, M {sum(x[3]=='M' for x in n)}, glossed {sum(bool(x[5]) for x in n)}")
