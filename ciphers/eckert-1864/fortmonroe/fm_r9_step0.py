#!/usr/bin/env python3
"""FM-R9 Step-0 ruling on the four rows (disk only): (a) ordered LCS of decoded content words vs the best window of the page's holder transcription,
(b) shuffled-window p95 (20 draws), (c) decoded content words absent from the whole page transcription. Functions of ms18/step0_ordered.py
(words, lcs, windows, measure) are copied verbatim by exec of its definitions block. Usage: python3 fm_r9_step0.py"""
import re, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
src = (HERE/"ms18"/"step0_ordered.py").read_text()
a = src.index("STOP = set"); b = src.index("ents = {}")
exec(src[a:b].replace("T = ", "T_ = "))
exec(src[src.index("def body(line):"):src.index("pagefile = {}")])
exec(src[src.index("def windows(bl)"):src.index("def route(")])
exec(src[src.index("def measure("):src.index("EXTRA =")])
def blocks_p(p):
    t = json.load(open(HERE/f"sources/fortmonroe/p{p}.json")).get("transc") or ""
    return [words(x) for x in re.split(r"\n\s*\n", t) if words(x)]
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
for header, lines in decode.load_ciphertext(HERE/"fortmonroe"/"fm_r9_entries.txt"):
    row = header.split("|")[1].strip(); p = int(row.split("/")[0]); text = decode.entry_text(lines)
    for n in ("no1","no2","no9"):
        r, c = decode.decode_entry(text, keys[n])
        line = r.replace("\n", " ")
        allw, codew = body(line)
        if not allw: continue
        m = measure(row+"/"+n, allw, codew, windows(blocks_p(p)), sum(map(ord, row+n)))
        print(f"{row} {n}: a={m['a']:.3f} ({m['lcs']}/{m['n']}) b95={m['b']:.3f} b2={m['b2']:.3f} win={m['win']} hit={m['hit']} c={m['c']} key-dep={m['ck']} plain-absent={m['cp']}")
