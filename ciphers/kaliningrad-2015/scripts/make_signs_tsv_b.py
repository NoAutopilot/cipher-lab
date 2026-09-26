#!/usr/bin/env python3
"""Write ciphers/kaliningrad-2015/ciphertext_signs_B.tsv: convention B (apostrophe is its own sign,
immediately after the letter it follows), derived from convention A's tokenize_signs (ic_analysis.py) by
splitting every compound sign "X'" into two sign rows, "X" then "'", on the same line. Reproducible: re-run
any time, committed output must match.
Usage: python3 make_signs_tsv_b.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ic_analysis import tokenize_signs  # noqa: E402

HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "ciphertext.txt"
OUT = HERE.parent / "ciphertext_signs_B.tsv"

if __name__ == "__main__":
    text = SRC.read_text(encoding="utf-8")
    rows = []
    line_no = 0
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.startswith("#") or raw_line.startswith("[SECTION"):
            continue
        line_no += 1
        for sign in tokenize_signs(raw_line):
            if sign.endswith("'"):
                rows.append((str(line_no), sign[:-1]))
                rows.append((str(line_no), "'"))
            else:
                rows.append((str(line_no), sign))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("line\tsign\n")
        for line, sign in rows:
            f.write(f"{line}\t{sign}\n")
    signs = [s for _, s in rows]
    print(f"wrote {OUT} ({len(rows)} sign rows, {line_no} lines, K={len(set(signs))})")
