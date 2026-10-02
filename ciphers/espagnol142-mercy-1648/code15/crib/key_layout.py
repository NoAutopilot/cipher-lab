#!/usr/bin/env python3
"""key_layout.py -- does the recovered key (Bourdeau's key.tsv, 1 Oct 2026, built without any ordering assumption)
follow a period table layout, and what does that layout leave for code 15? Issue 16, code 15 crib pass.
Rule tested: evens 10..32 = a b c d e f g h i l m n; 2..8 = o p q r s t u; odds 17..33 = a e i o u u o i e."""
import csv, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[4]
key = {r["code"]: r["value"] for r in csv.DictReader(open(ROOT/"sources/cyphersolver/2026-10-01/mercy1648/key.tsv"), delimiter="\t")}
pred = {}
for i, c in enumerate("abcdefghilmn"): pred[str(10 + 2*i)] = c
for i, c in enumerate("opqrstu"): pred[str(2 + i)] = c
for i, c in enumerate("aeiouuoie"): pred[str(17 + 2*i)] = c
ok = [k for k in pred if key.get(k) == pred[k]]
bad = [k for k in pred if key.get(k) != pred[k]]
print(f"layout predicts {len(pred)} codes; agree with the recovered key: {len(ok)}; disagree: {bad}")
rest = sorted((k for k in key if k not in pred and k.isdigit()), key=int)
print("outside the rule:", ", ".join(f"{k}={key[k]}" for k in rest), "| unused: 11")
alpha = set("abcdefghilmnopqrstuxyz")
print("letters of the 22-letter alphabet with no code:", sorted(alpha - set(key.values())))
# chance level: probability a random assignment of the 28 values (multiset from the key) matches the layout exactly
import math, collections
m = collections.Counter(key[k] for k in pred)
print("chance of an exact match by permutation of these 28 values: 1 in %.3g" % (math.factorial(28) / math.prod(math.factorial(v) for v in m.values())))
