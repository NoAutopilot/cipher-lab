#!/usr/bin/env python3
"""AM-D1411P5 grade step (PREREG-D1411P5.md "Grades"): the registered score (score_p5.json) gives PASS for T21r_h12, the
preferred variant (PASS and cover above T21r's). Under it, p.5 numerals graded 'ok' in numbers.tsv whose residue letter is
gloss-backed (tables.py source 'gloss', or residue 21) move M -> S; residue 12 (h in this variant, not gloss-backed),
alphabet-filled residues and every M number stay M; in-text figures are not graded. Writes grades.tsv and the decode
with S in lower case, M in upper case.  python3 d1411p5/grades.py [--check]"""
import csv, json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(H, "..", "def1411"))
import tables  # noqa: E402
sc = json.load(open(os.path.join(H, "score_p5.json")))
V = "T21r_h12"; assert sc[V]["PASS"] and sc[V]["cover"] > sc["T21r"]["cover"]
t = tables.tables()["T21r"]; t = dict(t); t[12] = ("h", "variant-h12", "")
out = [["line", "pos", "token", "residue", "letter", "grade"]]; cnt = {"S": 0, "M": 0}
for r in csv.DictReader(open(os.path.join(H, "numbers.tsv")), delimiter="\t"):
    if "intext" in r["note"] or not r["token"].isdigit():
        continue
    n = int(r["token"]); res = n % 24; L, src = t[res][0], t[res][1]
    g = "S" if (r["grade"] == "ok" and (src == "gloss" or res == 21)) else "M"
    cnt[g] += 1; out.append([r["line"], r["pos"], r["token"], str(res), L, g])
txt = "\n".join("\t".join(x) for x in out) + "\n"
p = os.path.join(H, "grades.tsv")
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == txt; print("grades.tsv", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(txt); print(cnt)
