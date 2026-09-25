#!/usr/bin/env python3
"""Write ciphers/kaliningrad-2015/ciphertext_signs.tsv: a long-format sign TSV (line, sign columns) under
convention A (letter+apostrophe merges to one sign, K=36, ic_analysis.py's own tokenisation), for
tools/family_run.py --cipher. Reproducible: re-run any time, committed output must match.
Usage: python3 make_signs_tsv.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ic_analysis import tokenize_signs  # noqa: E402

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "ciphertext.txt"
OUT = HERE.parent / "ciphertext_signs.tsv"

if __name__ == "__main__":
    text = SRC.read_text(encoding="utf-8")
    rows = [("header", "sign")]
    line_no = 0
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.startswith("#") or raw_line.startswith("[SECTION"):
            continue
        line_no += 1
        for sign in tokenize_signs(raw_line):
            rows.append((str(line_no), sign))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("line\tsign\n")
        for line, sign in rows[1:]:
            f.write(f"{line}\t{sign}\n")
    print(f"wrote {OUT} ({len(rows) - 1} sign rows, {line_no} lines)")
