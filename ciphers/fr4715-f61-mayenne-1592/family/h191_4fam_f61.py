#!/usr/bin/env python3
"""H191 (runner 7, 29 Sept 2026): at f.61r's own 4-family positions inside Tomokiyo's five spans (the H181/H187 alignment under
key_period_v4n176.tsv), his letters by the f.61 readers' code (4TRI, C43, 4STEM, 4PI, HASH4). Does the c/p vs a/n split H190 found on f.176v show in
f.61's hand? Descriptive; small N; his letters come from his own table.  python3 h191_4fam_f61.py [--check]"""
import os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
sys.argv[1:1] = ["--key", "key_period_v4n176.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
import test_period_key as T
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
FAM = ("4TRI", "C43", "4STEM", "4PI", "HASH4")
key = T.load_key(); lines = split_lines(load_read()); relabel(lines); by = defaultdict(Counter); rows = ["span\tline\tpos\tclass\ttomokiyo"]
for s, l, m in load_spans():
    for i, j in align(m, lines[l], key)[1]:
        c = lines[l][j]
        if c in FAM: by[c][m[i]] += 1; rows.append(f"{s}\t{l}\t{j + 1}\t{c}\t{m[i]}")
rows += ["", "class\ttomokiyo letters"] + [f"{c}\t{' '.join(f'{x}{n}' for x, n in by[c].most_common())}" for c in FAM]
all_ = [(c, x) for c in FAM for x, n in by[c].items() for _ in range(n)]
cp = {c: sum(n for x, n in by[c].items() if x in "cp") for c in FAM}; an = {c: sum(n for x, n in by[c].items() if x in "an") for c in FAM}
rows.append("c/p vs a/n by code: " + "; ".join(f"{c} {cp[c]}/{an[c]}" for c in FAM))
txt = "\n".join(rows) + "\n"; res = f"{HERE}/h191_4fam_f61_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print("\n".join(rows[rows.index(""):]))
