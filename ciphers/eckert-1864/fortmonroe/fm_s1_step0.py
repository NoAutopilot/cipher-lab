#!/usr/bin/env python3
"""FM-S1 (10 Oct 2026): Step-0 ruling (ms18/step0_ordered.py functions, run first) for the ten FM-S1 rows. Disk only.
Decoded body = decode_entry under the chosen book (F10: plain text, no book). Holder window = page JSON transcription of the row's page."""
import sys, re, json
from pathlib import Path
H = Path(__file__).resolve().parent.parent
src = (H/"ms18"/"step0_ordered.py").read_text().split("EXTRA =")[0]
sys.argv = ["x"]; g = {"__file__": str(H/"ms18"/"step0_ordered.py")}; exec(src, g)
sys.path.insert(0, str(H)); import decode
BOOK = dict(F1="key.md", F2="key.md", F3="key.md", F4="key.md", F5="key.md", F6="key.md", F7="key.md", F8="key.md", F9="key.md", F10="key.md")
keys = {f: decode.load_key(H/f) for f in set(BOOK.values())}
for header, lines in decode.load_ciphertext(H/"fortmonroe"/"fm_s1_entries.txt"):
    fid = header.split("|")[0].replace("###","").strip(); ptr = int(header.split("|")[2]); text = decode.entry_text(lines)
    r, c = decode.decode_entry(text, keys[BOOK[fid]]); line = r.replace("\n", " ")
    allw, codew = g["body"](line)
    m = g["measure"](fid, allw, codew, g["windows"](g["blocks"]([ptr])), sum(map(ord, fid)))
    print(f"{fid} {header.split('|')[1].strip()} a={m['a']:.3f} ({m['lcs']}/{m['n']}) b95={m['b']:.3f} b2={m['b2']:.3f} win={m['win']} {'HIT' if m['hit'] else 'no-hit'} c={m['c']} key-meanings={' '.join(m['ck'])} | plain-absent={' '.join(m['cp'])}")
