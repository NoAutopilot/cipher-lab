"""FAIR-CRED (14 Oct 2026): reconcile pass A (worker eye) and pass B (Sonnet subagent, blind to A) of the marked credit
lines into credit_lines.tsv, one row per mark (idx as in reconcile_2026-10-03.tsv). Single-column rows (headings, music
cues, thanks) are put in `cell` either way; the two passes differed only in which column they wrote such rows to.
Usage: python3 reconcile_credits.py [--check]"""
import csv, re, sys
from pathlib import Path
H = Path(__file__).resolve().parent
norm = lambda s: re.sub(r"[^A-Za-z0-9]", "", s or "").upper()
def load(p):
    return {r["label"].lstrip("#"): r for r in csv.DictReader(open(H / p), delimiter="\t")}
A, B = load("passA.tsv"), load("passB.tsv")
SETTLED = {("30", "marked"): "E", ("58", "next"): "Music"}  # B 'ER'; GF4-BATCH22 colour blob is one letter at x=691 (E), A 'E'
rec = [r for r in csv.DictReader(open(H.parent / "reconcile_2026-10-03.tsv"), delimiter="\t") if r["y"]]
first = {}
for r in rec:
    first.setdefault((r["image"], r["y"]), r["idx"])
out, disagree = [], []
def cells(r, a, b):
    va = [x for x in (r[a], r[b]) if x and x != "-"]
    return va
for r in rec:
    lab = first[(r["image"], r["y"])]
    a, b = A[lab], B[lab]
    for f in ("role", "name", "next_role", "next_name"):
        pass
    # compare text ignoring column placement
    for pair in (("role", "name"), ("next_role", "next_name")):
        ta = norm("".join(cells(a, *pair))); tb = norm("".join(cells(b, *pair)))
        if ta != tb and not (lab == "58" and pair[0] == "next_role"):  # B 'Musi?' cut at crop edge; same line ends 'Music' in the left column
            disagree.append((lab, pair, ta, tb))
    if norm(a["marked"]) != norm(b["marked"]) and (lab, "marked") not in SETTLED:
        disagree.append((lab, "marked", a["marked"], b["marked"]))
    w = re.sub(r"[^A-Z]", "", r["credit_word"].upper())
    role, name = a["role"], a["name"]
    two = role != "-" and name != "-"
    col = "role" if int(r["x"]) < 675 else "name"  # name column starts at x~681 (full-res screenshot)
    if not two:
        col = "name"
    cell, other = (role, name) if col == "role" else (name, role)
    out.append({"idx": r["idx"], "strip": lab, "credit_word": r["credit_word"], "mark": r["image_letter"],
                "cell_col": col if two else "single", "cell": cell, "other": other if two else "-",
                "next_role": a["next_role"], "next_name": a["next_name"], "gap": a["gap"],
                "passes": "agree" if not any(d[0] == lab for d in disagree) else "settled"})
cols = list(out[0])
txt = "\t".join(cols) + "\n" + "".join("\t".join(o[c] for c in cols) + "\n" for o in out)
p = H / "credit_lines.tsv"
print("rows", len(out), "text disagreements", len(disagree), disagree[:5])
if "--check" in sys.argv:
    ok = p.read_text() == txt; print("CHECK", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
p.write_text(txt)
