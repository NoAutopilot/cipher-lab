#!/usr/bin/env python3
"""H55 addendum: B35's crops 12/13 (page2_L02/page2_L03) and 15/16 (page2_L06/page2_L07) are the SAME physical line cut
from the two exposures (frames 0032 and 0031; h55/fuse_log.tsv puts each pair at one position, NCC 0.999-1.000 in its
own frame). So each B35 reader read two lines twice, blind. Within-reader agreement across exposures (a reader against
itself, image nearly identical) vs between-reader agreement on the same crop: if a reader disagrees with itself as
much as with the other reader, the disagreement is the reading, not the image. Positional agreement over the aligned
prefix (difflib ratio also given). Reads line-b/b35 through its own loader; edits nothing there.
usage: python3 h55/self_consistency.py"""
import os, sys, difflib, io, contextlib
B35 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "line-b", "b35")
sys.path.insert(0, B35); cwd = os.getcwd(); os.chdir(B35); sys.argv = ["x"]
with contextlib.redirect_stdout(io.StringIO()):
    from reconcile import A, B, glyphs
os.chdir(cwd)
def pos(a, b):
    n = min(len(a), len(b)); return (sum(x == y for x, y in zip(a, b)) / n if n else 0.0), len(a), len(b)
def ratio(a, b): return difflib.SequenceMatcher(None, a, b, autojunk=False).ratio()
for c1, c2 in ((12, 13), (15, 16)):
    for name, R in (("reader A", A), ("reader B", B)):
        g1, g2 = glyphs(R[c1]), glyphs(R[c2]); p, n1, n2 = pos(g1, g2)
        print(f"crops {c1}/{c2} same line, {name} vs itself: glyphs {n1}/{n2}, positional {p:.2f}, sequence ratio {ratio(g1, g2):.2f}")
    for c in (c1, c2):
        g1, g2 = glyphs(A[c]), glyphs(B[c]); p, n1, n2 = pos(g1, g2)
        print(f"crop {c}, reader A vs reader B: glyphs {n1}/{n2}, positional {p:.2f}, sequence ratio {ratio(g1, g2):.2f}")
