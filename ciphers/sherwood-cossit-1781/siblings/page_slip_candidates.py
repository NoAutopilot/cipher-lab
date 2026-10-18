#!/usr/bin/env python3
"""List, for every M row of reading.tsv, the OCR text of line W in both columns of pages P-1 and P+1 of Entick 1781.

Why: Sherwood to Mathews, 1 March 1783 (BL Add MS 21838 p.105, LAC H-1736 frame 1560) says the Cossit/Sumner
letters were written "in a very blundering manner and frequent mistakes made in numbering the pages". This lists
the neighbouring-page candidates for a person or verifier to read on the page image; it grades nothing and never
edits reading.tsv. OCR from book/entick_lines.tsv is poor (NOTES.md): an empty or garbled cell is not a negative.
Usage: page_slip_candidates.py [--out siblings/page_slip_candidates.tsv]
"""
import argparse, csv, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(here)
ap = argparse.ArgumentParser(); ap.add_argument("--out", default=os.path.join(here, "page_slip_candidates.tsv"))
a = ap.parse_args()
ocr = {}
for r in csv.DictReader(open(os.path.join(root, "book/entick_lines.tsv")), delimiter="\t"):
    ocr[(int(r["page"]), int(r["col"]), int(r["line"]))] = r["ocr"][:60]
rows = [r for r in csv.reader(open(os.path.join(root, "reading.tsv")), delimiter="\t") if r and not r[0].startswith("#")]
hdr, body = rows[0], rows[1:]
ix = {k: i for i, k in enumerate(hdr)}
out = []
for r in body:
    if r[ix["grade"]] != "M" or not r[ix["page"]].isdigit() or not r[ix["W"]].isdigit():
        continue
    p, w = int(r[ix["page"]]), int(r[ix["W"]])
    cells = [ocr.get((pp, c, w), "") for pp in (p - 1, p + 1) for c in (1, 2)]
    out.append([r[ix["message"]], r[ix["line"]], r[ix["group"]], r[ix["entry"]]] + cells)
with open(a.out, "w", newline="") as f:
    wr = csv.writer(f, delimiter="\t", lineterminator="\n")
    wr.writerow(["message", "line", "group", "current_entry_M", "P-1_col1_ocr", "P-1_col2_ocr", "P+1_col1_ocr", "P+1_col2_ocr"])
    wr.writerows(out)
print(len(out), "M rows listed")
