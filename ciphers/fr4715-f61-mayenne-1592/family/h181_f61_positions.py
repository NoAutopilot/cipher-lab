#!/usr/bin/env python3
"""H181 (runner 6, 28 Sept 2026): at f.61r's own VBAR_A and bracket (EBR) positions, compare the letter fr.3984 f.176r's period
decipherment gives those classes (VBAR_A t, H177b; form-B bracket l, H180) with Tomokiyo's published letter at the same position, via
the F61-CAL DP alignment of his five spans under the test key key_period_v4n176.tsv (H179). Descriptive, for the verifier; writes
h181_f61_positions_result.txt; --check fails if stale.  python3 h181_f61_positions.py [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.abspath(f"{HERE}/../scripts"))
sys.argv[1:1] = ["--key", "key_period_v4n176.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1", "--sbs"]
import test_period_key as T
from f61crib import align, load_read, load_spans
from f61crib4 import split_lines
from sbs_relabel import relabel
F176 = {"VBAR_A": "t", "EBR": "l"}
key = T.load_key(); lines = split_lines(load_read()); relabel(lines); out = ["span\tline\tpos\tclass\tf176_letter\ttomokiyo\tagree"]; n = a = 0
for s, l, m in load_spans():
    for i, j in align(m, lines[l], key)[1]:
        c = lines[l][j]
        if c in F176:
            n += 1; ok = m[i] == F176[c]; a += ok; out.append(f"{s}\t{l}\t{j + 1}\t{c}\t{F176[c]}\t{m[i]}\t{'yes' if ok else 'NO'}")
out.append(f"agree {a}/{n}")
txt = "\n".join(out) + "\n"; res = f"{HERE}/h181_f61_positions_result.txt"
if "--check" in sys.argv:
    ok = open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
