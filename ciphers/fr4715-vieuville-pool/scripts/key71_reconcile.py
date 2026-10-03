#!/usr/bin/env python3
"""Build witness/key71/key71_reconciled.tsv from pass_a.tsv (blind Opus read of the key no.71 crops) plus the worker's
reconciliation of the header (GAPS-fr4715-vieuville-pool-14, 3 Oct 2026). Layer by heading and mark: Motz (one dot
over the tens digit) -> mots; Villes, Prouinces, Noms generaulx and the unheaded 73-100 box (a dot over each digit)
-> places; Noms propres and Dames (bar) -> persons. Header: pass A read the 22 number slots in order but the letter
row is half-hidden under a paper strip; the worker's look at a header crop reads the glyph tops as the 22-letter
alphabet a..z without j k v w, so slot i gets letter i (grade M)."""
import csv
from pathlib import Path
W = Path(__file__).resolve().parent.parent / "witness/key71"
ALPHA = "a b c d e f g h i l m n o p q r s t u x y z".split()
HDR = ["25", "10", "65", "75", "23/24", "20", "30", "40", "63/64", "50", "60", "73/74", "85", "70", "80", "1",
       "83/84", "95", "93/94", "▽", "90", "⊕"]  # worker's header crop; pass A agrees except 83/8? at s
LAYER = {"motz": "mots", "villes": "places", "prouinces": "places", "noms generaulx": "places", "(no heading": "places",
         "noms propres": "persons", "dames": "persons"}
rows = list(csv.DictReader(open(W / "pass_a.tsv", encoding="utf-8"), delimiter="\t"))
out = [("layer", "entry", "number", "mark", "grade", "source")]
for i, (l, n) in enumerate(zip(ALPHA, HDR)):
    out.append(("letter", l, n, "none", "M", "header slot %d (pass A numbers + worker crop; letter by order)" % (i + 1)))
for r in rows:
    h = r["column_heading"].strip().lower()
    if h.startswith("alphabet"):
        continue
    layer = next((v for k, v in LAYER.items() if h.startswith(k)), None)
    if layer is None or not r["number"].strip():
        continue
    g = {"H": "H", "M": "M"}.get(r["conf"].strip(), "L")
    out.append((layer, r["entry_as_written"], r["number"], r["mark"], g, r["crop"]))
with open(W / "key71_reconciled.tsv", "w", encoding="utf-8") as f:
    f.write("# key no.71, BnF fr.3995 f.133r (Gallica btv1b525085665 f256), reconciled; see scripts/key71_reconcile.py\n")
    for o in out:
        f.write("\t".join(o) + "\n")
print(len(out) - 1, "rows")
