#!/usr/bin/env python3
"""R12A-D1411LA: tile list for the 4/5 look-alike re-read of p.4 (hand: 5 is an r-form, 4 a cross).
A tile = one numbers.tsv number in which pass A, pass B or the committed token (passC) has a digit 4 or 5. Same alignment as
make_numbers.py. Writes la/tiles.tsv (line, pos, A, B, C, mask) and la/prompt.md: per crop the committed sequence with every
4/5 digit of a tile replaced by '#' (value-blind for the pair under test; other digits shown for orientation only).
  python3 la/build_tiles.py"""
import csv, os
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = lambda f: list(csv.DictReader(open(os.path.join(H, f)), delimiter="\t"))
A, B, D = rd("passA.tsv"), rd("passB.tsv"), rd("rec/ciphertext_draft.tsv")
S = {(r["line"], r["col"]): r for r in rd("reconcile_notes.tsv")}
by = lambda P: {ln: [r for r in P if r["line"] == ln] for ln in {r["line"] for r in P}}
a, b = by(A), by(B)
rows = []; ia = ib = 0; cur = None; pos = 0
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
    rows.append((ln, pos, (ra or {}).get("token", "").rstrip("?"), (rb or {}).get("token", "").rstrip("?")))
N = {(r["line"], int(r["pos"])): r["token"].rstrip("?") for r in rd("numbers.tsv")}
out = [["line", "pos", "A", "B", "C", "mask"]]; seqs = {}
for ln, pos, ta, tb in rows:
    c = N[(ln, pos)]
    tile = any(ch in "45" for ch in ta + tb + c) and c.isdigit()
    m = "".join("#" if ch in "45" else ch for ch in c) if tile else c
    if tile and "#" not in m:  # committed token has no 4/5 but a pass did: mask the digit where the passes put it
        alt = ta if any(ch in "45" for ch in ta) and len(ta) == len(c) else tb
        m = "".join("#" if (len(alt) == len(c) and alt[i] in "45") else ch for i, ch in enumerate(c))
    if tile:
        out.append([ln, str(pos), ta, tb, c, m])
    seqs.setdefault(ln, []).append(f"[{pos}]{m}" if tile else m)
open(os.path.join(H, "la", "tiles.tsv"), "w").write("\n".join("\t".join(x) for x in out) + "\n")
P = ["# Look-alike re-read, p.4 (value-blind for 4/5)", "",
     "In this hand two digits look alike: one is written as a CROSS (like '+', two crossing strokes) and one as an R-FORM",
     "(like a small cursive 'r': an upright with a flag or hook to the upper right). Each line below lists the cipher numbers on",
     "the crop in reading order. A number marked [k] contains one or more digits written '#': for each '#', look at the crop and",
     "say whether that digit is a CROSS (X), an R-FORM (R), or some OTHER digit (O); if you cannot tell, write ?. Ignore the small letters written above",
     "the numbers. Answer one row per [k] number: crop<TAB>k<TAB>shapes (one letter per '#', left to right, e.g. XR)<TAB>H|M",
     "(H = clear, M = probable).", ""]
for ln, s in seqs.items():
    if any(x.startswith("[") for x in s):
        P.append(f"- images/d1411p4_crops/{ln}.jpg : " + " ".join(s))
open(os.path.join(H, "la", "prompt.md"), "w").write("\n".join(P) + "\n")
print(len(out) - 1, "tiles on", sum(any(x.startswith('[') for x in s) for s in seqs.values()), "crops")
