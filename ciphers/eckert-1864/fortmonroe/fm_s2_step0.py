#!/usr/bin/env python3
"""FM-S2 step 0 (Wave 3 ruling, LANE LEDGER-10 jobs file): (a) ordered LCS overlap, (b) shuffled-window p95, (c) key-dependent words, using
ms18/step0_ordered.py's functions unchanged (source exec'd up to its EXTRA line), on the decode of fm_s2_entries.txt under the share_book key
(No. 1 except F6 = No. 2). The holder page JSON is read from disk (sources/fortmonroe/p<pointer>.json). Disk only."""
import os, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent; sys.path.insert(0, str(T)); os.chdir(T/"ms18")
import decode
src = (T/"ms18"/"step0_ordered.py").read_text(); src = src[:src.index("EXTRA = ")]
g = {"__file__": str(T/"ms18"/"step0_ordered.py")}; exec(compile(src, "step0_ordered_head", "exec"), g)
keys = {"no1": decode.load_key(T/"key.md"), "no2": decode.load_key(T/"key-no2.md")}
print("entry\trow\tbook\twindow\ta\tlcs/n\tb_p95\tb2_p95\thit\tc\tc_key_meanings\tc_plain_absent")
for header, lines in decode.load_ciphertext(HERE/"fm_s2_entries.txt"):
    xid, row, p = [x.strip() for x in header.split("|")[:3]]; p = int(p)
    book = "no2" if row == "5756/1" else "no1"
    r, c = decode.decode_entry(decode.entry_text(lines), keys[book])
    allw, codew = g["body"](r.replace("\n", " "))
    m = g["measure"](xid, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, xid)))
    print(f"{xid}\t{row}\t{book}\t{m['win']}\t{m['a']:.3f}\t{m['lcs']}/{m['n']}\t{m['b']:.3f}\t{m['b2']:.3f}\t{'HIT' if m['hit'] else '-'}\t{m['c']}\t{' '.join(m['ck'])}\t{' '.join(m['cp'])}")
