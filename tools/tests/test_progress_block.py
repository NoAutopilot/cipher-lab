#!/usr/bin/env python3
"""Offline test for tools/progress_block.py."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import progress_block as pb

H = {"F": "x", "K": "x", "R": "x", "1": "x", "2": ".", "C": ".", "S": "."}
rows = [dict(name="A", firm="50", total="100", sent_star="*", note="", **H),
        dict(name="B", firm="0", total="0", sent_star="", note="found-solved", **H),
        dict(name="C", firm="5", total="10", sent_star="", note="", **{**H, "K": "q"})]
text, problems = pb.render(rows)
assert "*A" in text and "[#####.....]" in text and "50/100" in text, text
assert "found-solved" in text            # total 0 renders the note, not blocked
assert any("stage K" in p for p in problems) and "?" in text   # bad mark reported, row kept
rows2 = [dict(name="D", firm="1", total="10", sent_star="", note="", ksrc="b+o", txt="n", **H),
         dict(name="E", firm="1", total="10", sent_star="", note="", ksrc="p", txt="k", **{**H, "K": "."}),
         dict(name="F", firm="1", total="10", sent_star="", note="", **H)]
t2, p2 = pb.render(rows2)
l = t2.splitlines()
assert l[1].endswith("x B x x . . . n"), l[1]      # mixed key letter, T column
assert l[2].endswith("x . x x . . . k"), l[2]      # K '.' stays '.' even with ksrc set
assert l[3].endswith("x ? x x . . . ?") and not p2, (l[3], p2)  # old rows without ksrc/txt: ?, not a problem
_, p3 = pb.render([dict(rows2[0], ksrc="zz", txt="q")])
assert any("ksrc" in p for p in p3) and any("txt" in p for p in p3), p3
assert "o ours, p period, b published" in t2
hdr = text.splitlines()[0]; assert hdr.index("F") == text.splitlines()[1].index("read  ") + 6, (hdr, text.splitlines()[1])
print("passed: 0 failure(s)")
