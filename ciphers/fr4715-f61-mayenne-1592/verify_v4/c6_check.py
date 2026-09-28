#!/usr/bin/env python3
"""VERIFY-F61-V4 step 4b: for each firm-graded class of the v4 f.61r decode, what Tomokiyo's markup puts at its positions
inside the five spans (under key v4's own span alignment, test_period_key's DP), and the period attestation behind it.
-> verify_v4/c6_check_result.txt"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{H}/../family"); sys.path.insert(0, F)
sys.argv = ["x", "--key", f"{F}/key_period_v4.tsv", "--collapse-ebr", "--min", "2", "--frac", "0.1"]
import test_period_key as T
from sbs_relabel import relabel
key = T.load_key(); L = T.split_lines(T.load_read()); L.update(T.f108_lines()); relabel(L)
out = []
for s, line, m in T.load_spans():
    _, pairs = T.align(m, L[line], key); byj = {j: m[i] for i, j in pairs}
    first, last = min(byj), max(byj)
    cells = [f"{L[line][j]}:{byj.get(j, '^')}" for j in range(first, last + 1)]
    out.append(f"{s} {line} '{m}' -> " + " ".join(cells))
from collections import Counter
cnt = Counter()
for s, line, m in T.load_spans():
    _, pairs = T.align(m, L[line], key); byj = {j: m[i] for i, j in pairs}
    for j in range(min(byj), max(byj) + 1):
        c = L[line][j]
        if c in ("C6", "ELOOP", "INF", "VBAR_B"): cnt[(c, byj.get(j, "^"))] += 1
out.append("firm classes inside spans (class, Tomokiyo char; '-' his dash, '^' skipped by the DP): " + " ".join(f"{c}/{t}:{n}" for (c, t), n in sorted(cnt.items())))
txt = "\n".join(out) + "\n"; open(f"{H}/c6_check_result.txt", "w").write(txt); print(txt, end="")
