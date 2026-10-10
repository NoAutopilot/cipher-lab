#!/usr/bin/env python3
"""D1411-P6b (copy of d1411p5/make_numbers.py, paths changed): build p.6 numbers.tsv from the two blind passes (passA.tsv, passB.tsv), the tools/reconcile_passes.py
alignment (rec/ciphertext_draft.tsv) and the worker's crop settlements (reconcile_notes.tsv). Adapted from
d1411p4/make_numbers.py; differences: one-sided columns are handled in both directions (alt 'A:-' = B-only, 'B:-' =
A-only), and in-text figures are only those reconcile_notes.tsv marks 'intext' (the passes' own 'intext?' flags are
kept in the note column but do not exclude a number: a pass-flagged in-text figure stays in numbers.tsv at grade M with the flag in the note; score_p6.py excludes only notes containing "intext").
grade: ok only where both passes agree and neither flagged '?'; every settled or flagged number is M.
gloss: kept only where both passes wrote a non-blank gloss letter and the two agree after the fixed shape rule
1 -> i, 5 -> s, '?' stripped; numbers whose value the worker settled carry no gloss.
  python3 d1411p6/make_numbers.py [--check]"""
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
    aonly = r["why"] == "gap" and r["alt"].startswith("B:")
    bonly = r["why"] == "gap" and r["alt"].startswith("A:")
    ra = None if bonly else a[ln][ia]
    rb = None if aonly else b[ln][ib]
    ia += 0 if bonly else 1; ib += 0 if aonly else 1
    st = S.get((ln, col))
    if st and st["settled"] == "drop":
        continue
    pos += 1
    if st and st["settled"] == "intext":
        out.append([ln, str(pos), (ra or rb)["token"].rstrip("?"), "M", "intext: " + st["note"], ""]); continue
    if st:
        out.append([ln, str(pos), st["settled"], "M", st["note"], ""]); continue
    ta, tb = ra["token"], rb["token"]
    grade = "ok" if ("?" not in ta + tb and ta == tb) else "M"
    pn = ";".join(sorted({x for x in ((ra.get("note") or "").strip(), (rb.get("note") or "").strip()) if x}))
    pn = pn.replace("intext", "in-text")  # a pass's flag is a note, not an exclusion (score_p5.py excludes 'intext')
    if "in-text" in pn:
        grade = "M"  # a reader doubted the figure is cipher
    ga, gb = gl(ra.get("gloss")), gl(rb.get("gloss"))
    out.append([ln, str(pos), ta.rstrip("?"), grade, ("pass note: " + pn) if pn else "", ga if (ga and ga == gb) else ""])
txt = "\n".join("\t".join(x) for x in out) + "\n"
p = os.path.join(H, "numbers.tsv")
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt
    print("numbers.tsv", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt)
n = [x for x in out[1:] if x[2].isdigit() and "intext" not in x[4].split(":")[0]]
print(f"numbers {len(n)}, M {sum(x[3]=='M' for x in n)}, glossed {sum(bool(x[5]) for x in n)}")
