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
# --on-it / --unassigned (PROGRESS-ONIT, 9 Oct 2026)
NOW = 1760000000
def rl(mins_ago, role, text): return (NOW - mins_ago * 60, role, text)
orow = lambda n, f, **k: dict(name=n, folder=f, firm="1", total="10", sent_star="", note="", **{**H, "R": ".", "C": ".", **k})
orows = [orow("a", "alpha-1"), orow("b", "beta-2"), orow("c", "gamma-3"), orow("d", "delta-4"), orow("e", "eps-5", R="x", C="x")]
wq = [dict(job_id="FAM-9", brief=".claude/briefs/lane-family.md", status="claimed sess 2026", note="target alpha-1"),
      dict(job_id="OLD-1", brief="x.md", status="done 2026-10-09", note="alpha-1 beta-2"),
      dict(job_id="SIG-4", brief="x.md", status="queued", note="beta-2xx")]          # beta-2xx is a different folder
room = [rl(30, "LEDGER worker (account 2)", "claim: ciphers/beta-2 re-audit"),
        rl(500, "AUD (account 1)", "claim: gamma-3 audit"),
        rl(20, "WEB (account 1)", "claim: delta-4 check"), rl(5, "WEB (account 1)", "done: delta-4 checked"),
        rl(10, "key_crossmatch nightly (tools/key_crossmatch.py)", "alpha-1 scanned"),
        rl(900, "OLDLANE worker", "claim: gamma-3"),
        rl(40, "x (account 3)", "LANE MQS-2 handoff: eps-5 held")]
o = pb.on_it(orows, wq, room, NOW)
assert o["e"] == "MQS", o
assert o["a"] == "FAMILY" and o["b"] == "LEDGER" and o["c"] == "AUD" and o["d"] == "-", o   # done role cleared; ignored role; old line outside 12 h
assert pb._lane("LANE-VERIFY-4 (account 3)") == "VERIFY"
assert pb._lane("x (account 3)", "LANE MQS-2 handoff") == "MQS"
to, _ = pb.render(orows, onit=o)
assert to.splitlines()[0].rstrip().endswith("ON") and to.splitlines()[1].rstrip().endswith("FAMILY"), to
assert "ON = lane" in to and "ON" not in pb.render(orows)[0].splitlines()[0]
steps = [dict(folder="alpha-1", blocker="runnable", cost_band="S", next_step="do it ~$3 now"),
         dict(folder="beta-2", blocker="runnable", cost_band="M", next_step="busy row"),
         dict(folder="gamma-3", blocker="needs-person", cost_band="S", next_step="ask owner"),
         dict(folder="delta-4", blocker="runnable", cost_band="M", next_step="read the leaf"),
         dict(folder="eps-5", blocker="runnable", cost_band="S", next_step="finished row")]
u = pb.unassigned(orows, steps, o)
assert u == ["d | delta-4 | M | read the leaf"], u     # on-row, person-blocked and fully-counted rows are skipped
assert pb.unassigned(orows, steps, {**o, "a": "-"})[0].startswith("a | alpha-1 | ~$3 |")
print("passed: 0 failure(s)")
