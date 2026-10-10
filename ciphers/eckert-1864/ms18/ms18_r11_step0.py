#!/usr/bin/env python3
"""MS18-R11 step 0 (Wave 3 ruling, LANE LEDGER-10 jobs file): (a) ordered LCS overlap, (b) shuffled-window p95, (c) key-dependent words,
using step0_ordered.py's functions unchanged (its source up to the EXTRA line is exec'd), on the No. 1 decode of ms18_r11_entries.txt. Disk only."""
import os, sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent; sys.path.insert(0, str(T)); os.chdir(HERE)
import decode
src = (HERE/"step0_ordered.py").read_text(); src = src[:src.index("EXTRA = ")]
g = {"__file__": str(HERE/"step0_ordered.py")}; exec(compile(src, "step0_ordered_head", "exec"), g)
key = decode.load_key(T/"key.md")
print("entry\tpointer\tpage\twindow\ta\tlcs/n\tb_p95\tb2_p95\thit\tc\tc_key_meanings\tc_plain_absent")
for header, lines in decode.load_ciphertext(HERE/"ms18_r11_entries.txt"):
    xid = header.split("|")[0].strip(); p = int(header.split("|")[2])
    r, c = decode.decode_entry(decode.entry_text(lines), key)
    allw, codew = g["body"](r.replace("\n", " "))
    m = g["measure"](xid, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, xid)))
    print(f"{xid}\t{p}\t{p}\t{m['win']}\t{m['a']:.3f}\t{m['lcs']}/{m['n']}\t{m['b']:.3f}\t{m['b2']:.3f}\t{'HIT' if m['hit'] else '-'}\t{m['c']}\t{' '.join(m['ck'])}\t{' '.join(m['cp'])}")
