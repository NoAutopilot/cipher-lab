#!/usr/bin/env python3
"""FM-F1 (10 Oct 2026): decode the 15 held Fort Monroe rows under No. 1 (and shuffled copy) for the filing headers. Prints only."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)); import decode
H = Path(__file__).resolve().parent.parent
k = decode.load_key(H/"key.md")
for fn, want in [("fm_r9_entries.txt", None), ("fm_s1_entries.txt", None), ("fm_s2_entries.txt", None)]:
    for header, lines in decode.load_ciphertext(H/"fortmonroe"/fn):
        tag = header.split("|")
        if tag[1].strip() not in {"5752/0","5699/1","5707/0","5785/1","5799/0","5816/2","5583/2","5827/0","5793/1","5822/2","5638/0","5632/2","5810/1","5720/0","5814/0"}: continue
        r, c = decode.decode_entry(decode.entry_text(lines), k)
        print(fn[:5], tag[1].strip(), dict(c)); print("   ", r.replace("\n", " "))
