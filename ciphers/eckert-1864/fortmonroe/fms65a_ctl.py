#!/usr/bin/env python3
"""FM-S65A shuffled-key control (BOOK-FM65's shuffled(): meanings of the word rows permuted, seeds 1-3) for the rows to file:
the No. 1 decode beside the decode under each meaning-shuffled copy. Disk only. Usage: python3 fms65a_ctl.py"""
import random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent; sys.path.insert(0, str(HERE)); import decode
key = decode.load_key(HERE/"key.md")
def shuffled(key, seed):
    rows = [k for k, v in key.items() if v[2] == "word"]; ms = [key[k] for k in rows]; random.Random(seed).shuffle(ms)
    out = dict(key)
    for k, m in zip(rows, ms): out[k] = m
    return out
FILE = {"F4": "5862/0", "F5": "5862/2", "F6": "5872/0", "F8": "5872/2", "F9": "5874/1", "F10": "5883/2"}
for header, lines in decode.load_ciphertext(Path(__file__).resolve().parent/"fms65a_entries.txt"):
    xid, row = [x.strip() for x in header.split("|")[:2]]
    text = decode.entry_text(lines)
    r, c = decode.decode_entry(text, key)
    print(f"{xid} {row} no1 H{c['H']}: {r.replace(chr(10),' ')}")
    for sd in (1, 2, 3):
        r, c = decode.decode_entry(text, shuffled(key, sd)); print(f"   shuf{sd} H{c['H']}: {r.replace(chr(10),' ')}")
