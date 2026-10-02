#!/usr/bin/env python3
"""NEVBIR-185B (2 Oct 2026): build passC.tsv for f.185r L01-L14 from passC_r_agreement.tsv + adjudicate_out.tsv
(rows keyed by passage + agreement-row index), then append f.185v (passC_v.tsv). NONE drops a position.
Passage ids are renamed to manuscript line numbers on f.185r, continuing NEVBIR-185's count (its f185r_L08 ends at
"Mons. di Sanfre"; L09 is the clear line "qsta settimana"): band L01 -> L10 ("dal re"), L02 -> L11, L03 -> L12 (to "che"),
L04 -> L15 ("cose sue da di qua, che"; L13 "non si sa", L14 "pensa mai" are clear), L05.x -> L16.x, L06..L14 -> L17..L25
(L25 ends at "Chi io no so").
Conf: agree -> lower of the two; adjudicated -> the adjudicator's conf capped at M (rule 4: settled by a third eye)."""
import csv
from pathlib import Path
H = Path(__file__).resolve().parent
adj = {(r["passage"], r["row"]): r for r in csv.DictReader(open(H / "adjudicate_out.tsv"), delimiter="\t")}
by = {}
for r in csv.DictReader(open(H / "passC_r_agreement.tsv"), delimiter="\t"):
    by.setdefault(r["passage"], []).append(r)
def MS(p):
    b, _, sub = p.partition(".")
    n = int(b[-2:]); n = n + 9 if n <= 3 else n + 11
    return f"f185r_L{n:02d}" + ("." + sub if sub else "")
out = []
for p, rows in by.items():
    k = 0
    for i, r in enumerate(rows, 1):
        if r["status"] == "agree":
            sid, conf, note = r["merged"], r["merged_conf"], ""
        else:
            a = adj[(p, str(i))]; sid, conf, note = a["sign_id"].strip(), "M", "adj: " + (a.get("note") or "")
        if sid == "NONE":
            continue
        k += 1; out.append((MS(p), k, sid, conf, note))
for r in csv.DictReader(open(H / "passC_v.tsv"), delimiter="\t"):
    out.append((r["passage"], int(r["pos"]), r["sign_id"], r["conf"], r["note"]))
with open(H / "passC.tsv", "w") as f:
    f.write("passage\tpos\tsign_id\tconf\tnote\n")
    for o in out:
        f.write("\t".join(map(str, o)) + "\n")
print(len(out), "signs -> passC.tsv")
