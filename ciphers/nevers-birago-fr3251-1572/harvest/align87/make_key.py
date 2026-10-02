#!/usr/bin/env python3
"""keys/key_1572_clerk.tsv and harvest/key_1572_clerkvar.tsv from the real-sheet alignment (NEVBIR-87ALIGN, 2 Oct 2026).
key_1572_clerk.tsv: every sign of no.87 with the clerk sheet's value (grade C: known plaintext), counts, Tomokiyo's printed
value and the relation (agrees / CONFLICT / not-in-table); per-tile off-sheet rows carry their folio, line, pos and the
NEVBIR-OFFSHEET shape class. key_1572_clerkvar.tsv: key_1572_sheet.tsv with only the PREREG.md rule-2 rows replaced.
  python3 make_key.py [--check]   (--check: exit 1 if either committed file differs from a regeneration)"""
import csv, sys
from pathlib import Path
D = Path(__file__).resolve().parent; H = D.parent; F = H.parent
WORD = {"T11", "T15", "T26", "T29", "T46", "T78", "T84", "T89"}
sheet = {r["sign"]: r for r in csv.DictReader(open(H / "key_1572_sheet.tsv"), delimiter="\t")}
printed = {s: r["value"] for s, r in sheet.items()}; printed["T42"] = "g"
codes = {r["code"]: r for r in csv.DictReader(open(D / "codes.tsv"), delimiter="\t")}
shape = {(r["passage"], r["pos"]): r["sign"] for r in csv.DictReader(open(H / "offsheet/known_no87.tsv"), delimiter="\t")}
pref = {"f178r": "R", "f178v": "L", "f179r": "V"}
kr = list(csv.DictReader(open(D / "key_real.tsv"), delimiter="\t"))
al = list(csv.DictReader(open(D / "align_real.tsv"), delimiter="\t"))
# a one-tile value is C only where the alignment is locally sound: both neighbouring signs 'agrees'; else M
tile_grade = {}
for i, r in enumerate(al):
    if 1000 <= int(r["raw"]) < 6000:
        nb = [al[j]["status"] for j in (i - 1, i + 1) if 0 <= j < len(al) and al[j]["cipher_line"] == r["cipher_line"]]
        tile_grade[r["raw"]] = "C" if nb and all(x == "agrees" for x in nb) else "M"
out = ["sign\tvalue\tgrade\tn\tagree\tothers\tprinted\trelation\tapplied\tnote"]
apply = {}
for r in kr:
    v, n, ag = int(r["value"]), int(r["n"]), int(r["agree"])
    if v >= 6000 or v < 1000:
        s = f"T{v - 6000 if v >= 6000 else v}"
        p = printed.get(s, "")
        rel = "not-in-table" if not p else ("agrees" if p == r["meaning"] else "CONFLICT")
        ok = rel != "agrees" and s not in WORD and n >= 3 and ag >= 3 and ag / n >= 0.75
        if ok:
            apply[s] = r["meaning"]
        grade = "C" if ag >= 2 and ag / n >= 0.6 else "M"
        note = "clerk sheet (canvas 182) aligned to the no.87 blind transcription by tools/interlinear_align.py, seeded with the printed table; " + (
            "word sign (printed table's structure)" if s in WORD else "letter sign")
        out.append("\t".join([s, r["meaning"], grade, str(n), str(ag), r["others"], p, rel, "yes" if ok else "no", note]))
    else:
        c = codes[str(v)]; key = (pref[c["folio"]] + c["line"].lstrip("L"), c["pos"])
        out.append("\t".join([f"{c['sign_id']}@{c['folio']}_{c['line']}_{c['pos']}", r["meaning"], tile_grade[str(v)], "1", "1", "",
                              "", "off-sheet tile", "no (one tile, no.87 only)",
                              f"shape class {shape.get(key, '?')} (NEVBIR-OFFSHEET); transcription conf {c['conf']}"]))
for c in codes.values():  # off-sheet tiles the alignment left without a letter
    if int(c["code"]) >= 1000 and c["code"] not in {r["value"] for r in kr}:
        key = (pref[c["folio"]] + c["line"].lstrip("L"), c["pos"])
        out.append("\t".join([f"{c['sign_id']}@{c['folio']}_{c['line']}_{c['pos']}", "null", tile_grade.get(c["code"], "M"), "1", "1", "", "",
                              "off-sheet tile", "no (one tile, no.87 only)",
                              f"aligned to no sheet letter (struck/line-end signs); shape class {shape.get(key, '?')}"]))
var = ["\t".join(["sign", "value", "grade", "source", "note"])]
for s, r in sheet.items():
    if s in apply:
        var.append("\t".join([s, apply[s], "C", "keys/key_1572_clerk.tsv (NEVBIR-87ALIGN)",
                              f"clerk sheet value replaces printed {printed[s]} (PREREG.md rule 2)"]))
    else:
        var.append("\t".join([s, r["value"], r["grade"], r["source"], r["note"]]))
targets = {F / "keys/key_1572_clerk.tsv": "\n".join(out) + "\n", H / "key_1572_clerkvar.tsv": "\n".join(var) + "\n"}
if "--check" in sys.argv:
    bad = [p for p, t in targets.items() if not p.exists() or p.read_text() != t]
    print("stale: " + ", ".join(map(str, bad)) if bad else "key files up to date"); sys.exit(1 if bad else 0)
for p, t in targets.items():
    p.write_text(t)
print("applied:", apply)
