#!/usr/bin/env python3
"""MS18-R1: append the ten filed reader rows to ciphertext.txt as E200-E209 (transcription as printed by the Huntington volunteers, unrepaired).
Rows X3 (9836/0) and X4 (9830/2) are step-0 skips (body in clear) and are not filed. Idempotent: refuses if E200 already exists."""
import re
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
ct = HERE/"ciphertext.txt"; cur = ct.read_text()
if "### E200 " in cur: raise SystemExit("E200 already filed")
src = (HERE/"ms18"/"ms18_r1_entries.txt").read_text().split("### ")[1:]
ids = {"X1":"E200","X2":"E201","X5":"E202","X6":"E203","X7":"E204","X8":"E205","X9":"E206","X10":"E207","X11":"E208","X12":"E209"}
out = []
for blk in src:
    head, body = blk.split("\n",1); x = head.split()[0]
    if x not in ids: continue
    page, ptr = [p.strip() for p in head.split("|")[1:3]]
    row = re.search(r"row (\S+)\)", head).group(1)
    out.append(f"### {ids[x]} | {page} | {ptr} | mssEC 18 (obj 10074, pointer {ptr}) MS18-R1, row {row}\n{body.strip()}\n")
ct.write_text(cur.rstrip("\n") + "\n\n" + "\n".join(out))
print(len(out), "filed")
