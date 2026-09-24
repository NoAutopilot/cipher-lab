#!/usr/bin/env python3
"""L3 (24 Sept 2026): reformat L1's ciphertext_6179.tsv / ciphertext_6467.tsv (columns page, line, idx, group,
left_context, right_context, doubt[, margin_note]) into the long format tools/reconcile_passes.py expects
(header starts with a single 'line' column), so L1 can be fed in as a third witness alongside the L3 passes.

  python3 ciphers/la-garde-1577/reindex_l1.py

Writes ciphertext_6179_L1.tsv and ciphertext_6467_L1.tsv in this folder. Line id = "p{page}L{line}", matching
the id scheme the L3 pass instructions used (e.g. "p2L22"). Exits 0.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))


def convert(infile, outfile, has_margin):
    rows = list(csv.DictReader(open(os.path.join(HERE, infile)), delimiter="\t"))
    header = ["line", "pos", "sign", "conf", "left", "right"] + (["margin_note"] if has_margin else [])
    with open(os.path.join(HERE, outfile), "w") as f:
        f.write("\t".join(header) + "\n")
        for r in rows:
            row = [f"p{r['page']}L{r['line']}", r["idx"], r["group"], r["doubt"], r["left_context"], r["right_context"]]
            if has_margin:
                row.append(r.get("margin_note", ""))
            f.write("\t".join(row) + "\n")


if __name__ == "__main__":
    convert("ciphertext_6179.tsv", "ciphertext_6179_L1.tsv", False)
    convert("ciphertext_6467.tsv", "ciphertext_6467_L1.tsv", True)
    print("wrote ciphertext_6179_L1.tsv, ciphertext_6467_L1.tsv")
