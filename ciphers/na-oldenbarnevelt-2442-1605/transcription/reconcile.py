#!/usr/bin/env python3
"""Reconcile passA.tsv / passB.tsv for na-oldenbarnevelt-2442-1605: flatten each block to a reading-order
token list (line numbers are not trusted to align between the two blind passes -- both note approximate line
breaks), align with difflib.SequenceMatcher, and report per-block and overall raw-token agreement."""
import difflib
from collections import defaultdict

def load(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip()]
    h = rows[0]
    bi, li, ti, ri, ci = h.index("block"), h.index("line"), h.index("token_index"), h.index("raw_token"), h.index("confidence")
    data = rows[1:]
    data.sort(key=lambda r: (r[bi], int(r[li]), int(r[ti])))
    by_block = defaultdict(list)
    for r in data:
        by_block[r[bi]].append((r[ri], r[ci]))
    return by_block

A = load("passA.tsv")
B = load("passB.tsv")

total_agree = total_n = 0
for block in ["A", "B", "C1", "C2"]:
    a_toks = [t for t, c in A[block]]
    b_toks = [t for t, c in B[block]]
    sm = difflib.SequenceMatcher(None, a_toks, b_toks, autojunk=False)
    agree = 0
    n = 0
    disagreements = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            agree += i2 - i1
            n += i2 - i1
        elif tag == "replace":
            m = max(i2 - i1, j2 - j1)
            n += m
            for k in range(m):
                av = a_toks[i1 + k] if i1 + k < i2 else None
                bv = b_toks[j1 + k] if j1 + k < j2 else None
                disagreements.append((av, bv))
        elif tag == "delete":
            n += i2 - i1
            for k in range(i1, i2):
                disagreements.append((a_toks[k], None))
        elif tag == "insert":
            n += j2 - j1
            for k in range(j1, j2):
                disagreements.append((None, b_toks[k]))
    print(f"block {block}: A={len(a_toks)} tokens, B={len(b_toks)} tokens, aligned-agree {agree}/{n} = {agree/n:.1%}")
    for av, bv in disagreements:
        print(f"    DISAGREE: A={av!r}  B={bv!r}")
    total_agree += agree
    total_n += n

print(f"\nOVERALL: {total_agree}/{total_n} = {total_agree/total_n:.1%}")
