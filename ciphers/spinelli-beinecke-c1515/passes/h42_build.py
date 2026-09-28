#!/usr/bin/env python3
"""H42 (28 Sept 2026): build the two blind texts for the word-segmentation call.
Text REAL = reading_tokens.tsv as decoded (v6, Domnina's key). Text CTRL = the same tokens with the letter
values permuted among the sign codes that carry a letter (seed 42; nulls and unkeyed signs kept in place, grades
copied) -- the matched control for a model-in-the-loop reading step: how much 'Italian' does the same reader
find in a decode of the same length, letter inventory, grade pattern and null positions under a wrong key?
Writes passes/h42_text_{real,ctrl}.txt (one line per cipher line: letters, '?' for an unkeyed sign, grade
under each letter as a second row) and passes/h42_blind_map.json (which label is which)."""
import csv, json, random, sys
from pathlib import Path
D = Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(D / "reading_tokens.tsv"), delimiter="\t"))
page, prev = 1, 0  # the token file restarts line numbers on p.[2]; page follows the token order
for r in rows:
    if int(r["line"]) < prev: page = 2
    prev = int(r["line"]); r["lab"] = f"p{page} {r['line']}"
LABS = list(dict.fromkeys(r["lab"] for r in rows))
def is_letter(v): return v not in ("null", "?")
codes = sorted({r["sign"] for r in rows if is_letter(r["value"])})
cval = {}
for r in rows:
    if is_letter(r["value"]): cval.setdefault(r["sign"], r["value"])
vals = [cval[c] for c in codes]
rng = random.Random(42)
perm = vals[:]
for _ in range(1000):
    rng.shuffle(perm)
    if sum(a == b for a, b in zip(vals, perm)) <= 2: break
pmap = dict(zip(codes, perm))
def render(valfun):
    out = []
    for lab in LABS:
        toks = [r for r in rows if r["lab"] == lab and r["value"] != "null"]
        letters = [("?" if r["value"] == "?" else valfun(r)) for r in toks]
        grades = [r["grade"] for r in toks]
        out.append((lab, letters, grades))
    return out
real = render(lambda r: r["value"])
ctrl = render(lambda r: pmap[r["sign"]])
for name, t in (("real", real), ("ctrl", ctrl)):
    with open(D / f"passes/h42_text_{name}.txt", "w") as f:
        for lab, L, G in t:
            f.write(f"{lab}\t{' '.join(L)}\n{lab} grades\t{' '.join(g for g in G)}\n")
json.dump({"A": "ctrl", "B": "real", "seed": 42, "perm_fixed_points": sum(a == b for a, b in zip(vals, perm)),
           "codes": len(codes)}, open(D / "passes/h42_blind_map.json", "w"), indent=1)
print("codes", len(codes), "fixed points", sum(a == b for a, b in zip(vals, perm)))
