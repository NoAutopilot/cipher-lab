#!/usr/bin/env python3
"""AX-NAMES: counts only, no reading. For 4610/4611/4616 (N4 readings) and 5797's spots: how many U tokens
sit on a code that names.tsv now carries, by names.tsv grade and value class. Writes axnames/coverage.tsv."""
import csv, os, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
names = {r["code"]: r for r in csv.DictReader(open(os.path.join(T, "names.tsv")), delimiter="\t")}
out = [["letter", "U_before", "U_on_NULL_C", "U_on_NULL_M", "U_on_word_C", "U_on_word_M", "U_left", "word codes hit (code=value xN)"]]
for n in ("4610", "4611", "4616", "5797"):
    c = collections.Counter(); words = collections.Counter()
    for r in csv.DictReader(open(os.path.join(T, f"reading_{n}_tokens.tsv")), delimiter="\t"):
        if r["grade"] != "U":
            continue
        c["U"] += 1
        row = names.get(r["sign"])
        if not row or row["grade"] == "U" or " | " in row["value"]:
            c["left"] += 1; continue
        cls = "NULL" if row["value"] == "NULL" else "word"
        c[f"{cls}_{row['grade']}"] += 1
        if cls == "word":
            words[f'{r["sign"]}={row["value"]}'] += 1
    out.append([n, c["U"], c["NULL_C"], c["NULL_M"], c["word_C"], c["word_M"], c["left"], ", ".join(f"{k} x{v}" for k, v in words.most_common())])
with open(os.path.join(H, "coverage.tsv"), "w") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
for r in out: print("\t".join(map(str, r)))
