#!/usr/bin/env python3
"""TXE2-LATT post-hoc diagnostic (NOT a gate, written after score.tsv): per-position fixed/broken for lw0.5 and lw4, and a
lam_w = 0 arm (lattice d, same N-best, no word term, same disagree+latt fix rule) to isolate the word term's contribution."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import run_word as W  # noqa: E402
import tx_bench as B  # noqa: E402
W.LAMW = (0.0,)
lat = W.load_lat(HERE / "topk_d.tsv")
key = W.K.read_key(W.RC.H / "key_1572_sheet.tsv")
model = W.NgramModel([W.read_corpus(p) for p in W.LANG_CORPORA["it16dip"]])
lm = W.K.LM(model); lex = W.SG.Lexicon.load("it16dip")
flags = W.flagged(); Lr = W.L_rows()
W.write(HERE / "diag_lw0.tsv", W.apply_fix(Lr, W.run_key(lat, key, lm, lex)[0.0], flags))
T = B.read_tsv(W.RC.TRUTH)
base = {k: v for k, v in B.load_output([str(W.RC.OUTD / "labels.tsv")]).items() if k in W.DEV}
e0 = B.position_errors(T, base)
tv = {(r["line"], r["pos"]): (r["truth"], r["plain"]) for r in T}
Ls = {(r["line"], r["pos"]): r["sign"] for r in Lr}
for f in ("diag_lw0.tsv", "out/word_lw0.5.tsv", "out/word_lw4.tsv"):
    o = B.load_output([str(HERE / f)]); e1 = B.position_errors(T, o)
    os_ = {(r["line"], r["pos"]): r["sign"] for r in W.rd(HERE / f)}
    fx = [k for k in e0 if e0[k] and not e1[k]]; br = [k for k in e0 if not e0[k] and e1[k]]
    print(f, "fixed", len(fx), "broken", len(br), "p %.3f" % B.sign_test(len(fx), len(br)))
    for tag, ks in (("fixed", fx), ("broken", br)):
        for k in sorted(ks):
            print("  ", tag, k[0][-3:], k[1], Ls[k], "->", os_[k], "truth", tv[k][1], tv[k][0])
