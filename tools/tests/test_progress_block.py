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
hdr = text.splitlines()[0]; assert hdr.index("F") == text.splitlines()[1].index("read  ") + 6, (hdr, text.splitlines()[1])
print("passed: 0 failure(s)")
