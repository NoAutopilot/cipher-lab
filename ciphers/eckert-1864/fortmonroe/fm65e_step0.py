#!/usr/bin/env python3
"""FM65-E step 0 (Wave 3 ruling; informational on mssEC 25 under the Wave 2 RULING): (a) ordered LCS, (b) shuffled p95, (c) key-dependent words,
ms18/step0_ordered.py's functions unchanged, on the No. 1 decode of fm65e_entries.txt, and the same under one meaning-shuffled copy of No. 1 (seed 7). Disk only."""
import os, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent; sys.path.insert(0, str(T)); os.chdir(T/"ms18")
import decode
src = (T/"ms18"/"step0_ordered.py").read_text(); src = src[:src.index("EXTRA = ")]
g = {"__file__": str(T/"ms18"/"step0_ordered.py")}; exec(compile(src, "step0_ordered_head", "exec"), g)
k1 = decode.load_key(T/"key.md")
rows = [k for k, v in k1.items() if v[2] == "word"]; m = [k1[k] for k in rows]; random.Random(7).shuffle(m)
ks = dict(k1); ks.update(zip(rows, m))
print("entry\trow\tkey\twindow\ta\tlcs/n\tb_p95\thit\tc\tc_key_meanings")
for header, lines in decode.load_ciphertext(HERE/"fm65e_entries.txt"):
    xid, row, p = [x.strip() for x in header.split("|")[:3]]; p = int(p)
    for nm, key in (("no1", k1), ("no1shuf7", ks)):
        r, c = decode.decode_entry(decode.entry_text(lines), key)
        allw, codew = g["body"](r.replace("\n", " "))
        mm = g["measure"](xid, allw, codew, g["windows"](g["blocks"]([p])), sum(map(ord, xid)))
        print(f"{xid}\t{row}\t{nm}\t{mm['win']}\t{mm['a']:.3f}\t{mm['lcs']}/{mm['n']}\t{mm['b']:.3f}\t{'HIT' if mm['hit'] else '-'}\t{mm['c']}\t{' '.join(mm['ck'])}")
