#!/usr/bin/env python3
"""FM-S2 step 0x (10 Oct 2026): the Step-0 ruling's test with the entry's OWN transcription block removed from the windows.
Why: for a Fort Monroe (mssEC 25) row the page transcription of the entry's lines IS the cipher letter (arbitrary words and plain words together),
so the literal ruling's window always contains the row itself and (a) is high by construction (fm_s2_step0.out: 9 of 10 hit). Step 0x asks the
ruling's real question -- is a clear copy of the body on the page or at a pointer the holder search found? -- using step0_ordered.py's functions unchanged.
Windows: every block / adjacent pair of the row's page except the own block (the best-LCS block and, if the best window is a pair, both of its blocks);
plus, as extra candidate pages, the pointers named in fm_s2_hdl.out. Disk only."""
import json, os, sys, re
from pathlib import Path
HERE = Path(__file__).resolve().parent; T = HERE.parent; sys.path.insert(0, str(T)); os.chdir(T/"ms18")
import decode
src = (T/"ms18"/"step0_ordered.py").read_text(); src = src[:src.index("EXTRA = ")]
g = {"__file__": str(T/"ms18"/"step0_ordered.py")}; exec(compile(src, "step0_ordered_head", "exec"), g)
for f in (T/"sources"/"fortmonroe").glob("p*.json"): g["pagefile"][int(re.search(r"p(\d+)", f.name).group(1))] = str(f)
keys = {"no1": decode.load_key(T/"key.md"), "no2": decode.load_key(T/"key-no2.md")}
EXTRA = {"5698/0": [10356, 10364, 8934], "5627/1": [10266], "5814/0": [5813]}
print("entry\trow\tbook\tbody_words\tbest_other_window\ta_other\tlcs/n\tb_p95\thit_other")
for header, lines in decode.load_ciphertext(HERE/"fm_s2_entries.txt"):
    xid, row, p = [x.strip() for x in header.split("|")[:3]]; p = int(p)
    book = "no2" if row == "5756/1" else "no1"
    r, c = decode.decode_entry(decode.entry_text(lines), keys[book])
    allw, codew = g["body"](r.replace("\n", " "))
    bl = g["blocks"]([p]); win = g["windows"](bl)
    best = max(win, key=lambda kw: g["lcs"](allw, kw[1]))[0]; own = {int(x) for x in best.split("+")}
    rest = [b for i, b in enumerate(bl) if i not in own]
    for q in EXTRA.get(row, []):
        if q != p: rest += g["blocks"]([q]) if q in g["pagefile"] else []
    m = g["measure"](xid, allw, codew, g["windows"](rest), sum(map(ord, xid)))
    print(f"{xid}\t{row}\t{book}\t{len(allw)}\t{m['win']}\t{m['a']:.3f}\t{m['lcs']}/{m['n']}\t{m['b']:.3f}\t{'HIT' if m['hit'] else '-'}")
