#!/usr/bin/env python3
"""Letters-only text of a tools/decode_key.py reading for tools/judge_plaintext.py (GAPS-nevers-birago, 2 Oct 2026).
Drops the '#' header, the 'f178v L01 |' prefix, the [word-code] brackets (the word stays), the U-token placeholder
and anything that is not a-z; one manuscript line per output line.
  python3 letters_from_reading.py reading_f178v.txt [--lines L01-L10] > f178v/reading_f178v_letters.txt
"""
import argparse, re, sys
ap = argparse.ArgumentParser(); ap.add_argument("reading"); ap.add_argument("--lines", help="e.g. L11-L23")
a = ap.parse_args()
lo = hi = None
if a.lines:
    lo, hi = (int(x.lstrip("L")) for x in a.lines.split("-"))
out = []
for ln in open(a.reading, encoding="utf-8"):
    if ln.startswith("#") or "|" not in ln:
        continue
    head, body = ln.split("|", 1)
    m = re.search(r"L(\d+)", head)
    if lo is not None and m and not (lo <= int(m.group(1)) <= hi):
        continue
    out.append(re.sub(r"[^a-z]", "", body.lower()))
print("\n".join(out))
