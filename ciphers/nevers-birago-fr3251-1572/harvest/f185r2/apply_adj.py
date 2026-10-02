#!/usr/bin/env python3
"""NEVBIR-185B (2 Oct 2026): build passC.tsv for f.185r L01-L14 from passC_r_agreement.tsv + adjudicate_out.tsv
(rows keyed by passage + agreement-row index), then append f.185v (passC_v.tsv). NONE drops a position.
Conf: agree -> lower of the two; adjudicated -> the adjudicator's conf capped at M (rule 4: settled by a third eye)."""
import csv
from pathlib import Path
H = Path(__file__).resolve().parent
adj = {(r["passage"], r["row"]): r for r in csv.DictReader(open(H / "adjudicate_out.tsv"), delimiter="\t")}
by = {}
for r in csv.DictReader(open(H / "passC_r_agreement.tsv"), delimiter="\t"):
    by.setdefault(r["passage"], []).append(r)
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
        k += 1; out.append((p, k, sid, conf, note))
for r in csv.DictReader(open(H / "passC_v.tsv"), delimiter="\t"):
    out.append((r["passage"], int(r["pos"]), r["sign_id"], r["conf"], r["note"]))
with open(H / "passC.tsv", "w") as f:
    f.write("passage\tpos\tsign_id\tconf\tnote\n")
    for o in out:
        f.write("\t".join(map(str, o)) + "\n")
print(len(out), "signs -> passC.tsv")
