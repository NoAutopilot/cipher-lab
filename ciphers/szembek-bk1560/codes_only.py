#!/usr/bin/env python3
"""Rebuild codes_only.txt (decoded-letters-only text, excluding the manuscript's own clear Latin words) from
reading_tokens.tsv, for judging the decode itself rather than the clear words already visible on the page
(bLAJ, 26 Sept 2026). A run of consecutive positions on the same leaf/line is one decoded word (no interior
space); a position gap (a clear word intervened) or a leaf/line change starts a new word."""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent


def build():
    rows = list(csv.DictReader(open(HERE / "reading_tokens.tsv"), delimiter="\t"))
    out, prev = [], None
    for r in rows:
        key, pos = (r["leaf"], r["line"]), int(r["pos"])
        if prev is not None and prev[0] == key and pos == prev[1] + 1:
            out.append(r["value"])
        else:
            out.append(" " + r["value"])
        prev = (key, pos)
    return "".join(out).strip()


if __name__ == "__main__":
    (HERE / "codes_only.txt").write_text(build() + "\n")
    print("wrote codes_only.txt,", len(build().replace(" ", "")), "letters")
