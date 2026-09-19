#!/usr/bin/env python3
"""Render the four Charles II to Hamilton letters (1650) under a key.

Usage: python3 apply_key.py key.tsv [--witness A|C]

key.tsv: one entry per line, "number<TAB>value". Values may be a letter, a
syllable, a word, or "null". Numbers absent from the key render as [n].
Until the key arrives from NRS GD406/1/2197 this only prints the runs.
"""
import re
import sys

WITNESS = "A"
if "--witness" in sys.argv:
    WITNESS = sys.argv[sys.argv.index("--witness") + 1]

key = {}
if len(sys.argv) > 1 and not sys.argv[1].startswith("--"):
    for line in open(sys.argv[1], encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        n, v = line.split("\t", 1)
        key[int(n)] = v.strip()


def render(nums):
    out = []
    for n in nums:
        v = key.get(n)
        if v is None:
            out.append(f"[{n}]")
        elif v == "null":
            continue
        else:
            out.append(v)
    return " ".join(out)


current = None
for raw in open("ciphertext.txt", encoding="utf-8"):
    raw = raw.rstrip("\n")
    if not raw or raw.startswith("#"):
        continue
    parts = [p.strip() for p in raw.split("|")]
    if parts[0]:
        current = parts[0]
    body = parts[1] if len(parts) > 1 else ""
    m = re.match(r"([AC]):\s*(.*)", body)
    if m:
        if m.group(1) != WITNESS:
            continue
        body = m.group(2)
    if re.fullmatch(r"[\d\so]+(\s+\(.*\))?", body):
        nums = [int(x.replace("o", "5")) for x in re.findall(r"[\do]+", body.split("(")[0])]
        print(f"{current:6} {render(nums)}")
    else:
        # clear context with bracketed bare code words
        def sub(mm):
            n = int(mm.group(1))
            return key.get(n, f"[{n}]")
        print(f"{current:6} {re.sub(r'\[(\d+)\]', sub, body)}")
