#!/usr/bin/env python3
"""STEP0-KEYCTL part 2: key-only (a) null over 20 meaning-shuffled copies (seeds 1-20) for every entry in step0_keyctl.tsv, against the window the
true book chose; reports p95 (19th of 20) and how many of the 20 reach the book's key-only LCS count. Imports step0_keyctl.py (re-runs it). Disk only."""
import os, sys, io, contextlib
sys.argv = [sys.argv[0]]; HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
with contextlib.redirect_stdout(io.StringIO()): import step0_keyctl as K
out = ["set\tentry\tbook\tkeyonly_book_lcs/n\tkeyonly_book\tkeyonly_null_p95_20\tnull_ge_book_of_20\tbeats_p95_and_lcs>=3"]
for kind, eid, b, pages, text, rec in K.targets:
    wins = dict(K.g["windows"](K.g["blocks"](pages)))
    r, _ = K.decode.decode_entry(text, K.keys[b]); allw, codew, kseq = K.prep(r)
    m = K.g["measure"](eid, allw, codew, list(wins.items()), sum(map(ord, eid))); w = wins[m["win"]]
    if not kseq: out.append(f"{kind}\t{eid}\t{b}\t0/0\t-\t-\t-\t-"); continue
    kb = K.g["lcs"](kseq, w); ko = kb / len(kseq); null = []
    for sd in range(1, 21):
        r2, _ = K.decode.decode_entry(text, K.shuffled(K.keys[b], sd)); _, _, ks = K.prep(r2)
        null.append(K.g["lcs"](ks, w) / len(ks) if ks else 0.0)
    p95 = sorted(null)[18]; ge = sum(x >= ko for x in null)
    out.append(f"{kind}\t{eid}\t{b}\t{kb}/{len(kseq)}\t{ko:.3f}\t{p95:.3f}\t{ge}\t{'yes' if ko > p95 and kb >= 3 else 'no'}")
open(os.path.join(HERE, "step0_keyctl_null.tsv"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
