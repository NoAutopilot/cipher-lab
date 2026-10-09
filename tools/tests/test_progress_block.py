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
# --no-notes and --check-board (PROGRESS-SYNC, 9 Oct 2026)
rn = [dict(name="N", firm="5", total="10", sent_star="", note="long note here", **H),
      dict(name="Z", firm="0", total="0", sent_star="", note="found-solved, N0 (Bourdeau)", **H)]
assert "long note here" in pb.render(rn)[0]
tn, _ = pb.render(rn, notes=False)
assert "long note" not in tn and "found-solved" in tn and "Bourdeau" not in tn, tn
def res(folder, title, depth="D2", nov="N3", aud="two audits", scope="recovered-passages", **kw):
    return dict(title=title, link="https://x/tree/main/ciphers/" + folder, documents=[title + " doc"], depth=depth,
                plaintext_novelty=nov, audit_status=aud, claim_scope=scope, **kw)
st = {"results": [res("one", "single letter"), res("multi", "alpha f.1"), res("multi", "beta f.2", depth="D1"),
                  res("multi", "gamma f.3", aud="one audit"), res("none", "n0 key", nov="N0"), res("qa", "held", qa_flag="x"),
                  res("kk", "key only", scope="key-to-known-text")]}
def row(name, folder, C, board=""): return dict(name=name, folder=folder, C=C, board=board, firm="1", total="2")
good = [row("one", "one", "x"), row("a", "multi", "x", "alpha"), row("b", "multi", ".", "beta"), row("g", "multi", ".", "-"),
        row("n", "none", "."), row("q", "qa", "."), row("k", "kk", ".")]
assert pb.check_board(good, st) == [], pb.check_board(good, st)
bad = pb.check_board([row("one", "one", "."), row("a", "multi", "x", "alpha"), row("b", "multi", "x", "beta"),
                      row("u", "multi", ".")], st)
assert any(m.startswith("one: C is '.'") for m in bad), bad            # counted, row says not
assert any(m.startswith("b: C is 'x'") for m in bad), bad              # D1 typed as counted (the old rule)
assert any("set `board`" in m for m in bad), bad                       # multi-row folder without a regex
assert pb.check_board([row("one", "one", "x")], st)[0].startswith("counted but no row"), "uncovered counted result"
assert not pb.result_counted(res("x", "t", depth="")) and not pb.result_counted(res("x", "t", scope="catalogue-contribution"))
print("passed: 0 failure(s)")
