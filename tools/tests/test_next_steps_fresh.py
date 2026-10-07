#!/usr/bin/env python3
"""Offline test for tools/next_steps_fresh.py (FRESH-0914, 7 Oct 2026). Scope, as its docstring states:
  must FLAG  a step whose identifiers reappear in a later done line (Verdict 'f.174r L04 85' + a later done line
             fixing f.174r L04 '85');
  must KEEP  (not flag) a later done line on the same folder sharing only rule-5 boilerplate or one identifier, and a
             done line posted within ROOM_MARGIN_S of the anchor (the worker that restated the Verdict).
Run: python3 tools/tests/test_next_steps_fresh.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import next_steps_fresh as nf

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


step = ("Verdict: keep going: 4 internal gaps; cheapest next: the f.174r L04 '85' reading fix against the line crop "
        "(birago no.86), ~$0.5")
kw = nf.keywords(step)
check('keywords carry identifiers', {'f.174r', 'l04'} <= kw)
check('keywords drop boilerplate', not ({'verdict', 'internal', 'cheapest'} & kw))
done = "done: nevers-birago-fr3251-1572 no.86 f.174r L04 '85' reading fixed on the line crop, decode --check exit 0"
check('identifiers in a later done line flag', nf.is_stale(kw, done)[0])
boiler = "done: nevers-birago-fr3251-1572 gaps_check OK, verdict internal gaps keep going unchanged, f.174r"
check('boilerplate + one identifier does not flag', not nf.is_stale(kw, boiler)[0])

room = ["2026-10-07 10:00 | W1 | done: fold-x f.174r L04 '85' reading fixed on the crop",
        "2026-10-07 12:00 | W2 | done: fold-x f.174r L04 '85' reading fixed on the crop",
        "2026-10-07 12:00 | W3 | claim: fold-x f.174r L04 '85'"]
anchor = 1791367200  # 2026-10-07 10:00 UTC
got = nf.room_done_lines(room, 'fold-x', anchor)
check('margin drops the restating worker, claims ignored', got == [room[1]])

lines = ["# t", "", "Verdict: keep going: 1 internal gap; cheapest next: x", "", "later para one", "", "old para"]
times = {1: 10, 3: 10, 5: 30, 7: 5}
paras = nf.later_paragraphs(lines, times, 20, 3)
check('later_paragraphs keeps only lines written after the anchor', paras == ["later para one"])
check('anchor_line finds the Verdict', nf.anchor_line(lines, "Verdict: keep going: 1 internal gap; cheapest next: x") == 3)

print('ALL PASS' if not fails else f'{fails} FAIL')
sys.exit(1 if fails else 0)
