#!/usr/bin/env python3
"""NO9-L (10 Oct 2026, account 1, LANE LEDGER-N2): decode ms18/no9l_entries.txt under No. 1, No. 9, No. 2 (H counts) and show the No. 9 reading with unresolved tokens.
Usage: python3 ms18/o9r1.py [--show]"""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE)); import decode
keys = {n: decode.load_key(HERE/f) for n, f in [("no1","key.md"),("no2","key-no2.md"),("no9","key-no9.md")]}
for header, lines in decode.load_ciphertext(HERE/"ms18"/"no9l_entries.txt"):
    text = decode.entry_text(lines); res = {}
    for n in keys: res[n] = decode.decode_entry(text, keys[n])
    print(f"{header.split('|')[0].strip()} {header.split('|')[3].strip()}: H no1={res['no1'][1]['H']} no2={res['no2'][1]['H']} no9={res['no9'][1]['H']} (M {res['no9'][1]['M']}) tokens={len(text.split())}")
    if "--show" in sys.argv:
        for n in ("no9","no1","no2"): print(f"  {n}: {res[n][0].replace(chr(10),' ')}")
