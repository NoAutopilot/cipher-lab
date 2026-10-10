#!/usr/bin/env python3
"""FM-S3 step 0 (ms18/step0_ordered.py functions unchanged, source exec'd up to EXTRA) on fm_s3_entries.txt under No. 1, and under one
meaning-shuffled copy of No. 1 (seed 7) as information (RULING: a hit on mssEC 25 is a non-test). Page JSON read from disk. Disk only."""
import os, sys, random
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent; sys.path.insert(0, str(T)); os.chdir(T/"ms18")
import decode
src = (T/"ms18"/"step0_ordered.py").read_text(); src = src[:src.index("EXTRA = ")]
g = {"__file__": str(T/"ms18"/"step0_ordered.py")}; exec(compile(src, "step0_ordered_head", "exec"), g)
k1 = decode.load_key(T/"key.md")
rows = [k for k, v in k1.items() if v[2] == "word"]; m = [k1[k] for k in rows]; random.Random(7).shuffle(m)
ks = dict(k1)
for k, x in zip(rows, m): ks[k] = x
print("entry\trow\tkey\twindow\ta\tlcs/n\tb_p95\thit\tc_key_meanings\tc_plain_absent")
for header, lines in decode.load_ciphertext(HERE/"fm_s3_entries.txt"):
    xid, row, p = [x.strip() for x in header.split("|")[:3]]; p = int(p)
    for kn, key in (("no1", k1), ("no1shuf", ks)):
        r, c = decode.decode_entry(decode.entry_text(lines), key)
        allw, codew = g["body"](r.replace("\n", " "))
        mm = g["measure"](xid, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, xid)))
        print(f"{xid}\t{row}\t{kn}\t{mm['win']}\t{mm['a']:.3f}\t{mm['lcs']}/{mm['n']}\t{mm['b']:.3f}\t{'HIT' if mm['hit'] else '-'}\t{' '.join(mm['ck'])}\t{' '.join(mm['cp'])}")
