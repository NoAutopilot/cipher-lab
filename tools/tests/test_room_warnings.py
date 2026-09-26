#!/usr/bin/env python3
"""Offline test for tools/room.py's done-line warnings (25 Sept 2026, UPDATES.md). No network, no push: the
pure function room.warnings_for() is checked directly, then room.main() is run with room.push mocked and ROOM
pointed at a temp file, so nothing is committed. Run: python3 tools/tests/test_room_warnings.py"""
import os, sys, tempfile, io, contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402

RULE3 = "WARNING: done line reports a test or negative without a control number (rule 3)"
COST = "WARNING: cost figures in ROOM lines are the orchestrator's to read (COMMON item 1)"


def test_warnings():
    W = room.warnings_for
    # done line with a test/negative/FAIL and no control -> rule 3 warning
    assert W("LANE X worker", "done: target-a test 1 negative, no decode") == [RULE3]
    assert W("w", "done: judge FAIL on all seeds") == [RULE3]
    assert W("w", "Done: closed-negative, nothing read") == [RULE3]
    assert W("w", "done: the anneal fails at N=45") == [RULE3]
    # the same with the word control -> no warning (case-insensitive)
    assert W("w", "done: test 1 negative; matched CONTROL reads 0.93 on 3 seeds") == []
    assert W("w", "done: judge FAIL, controls 0.2-0.4 at this N") == []
    # not a done line -> no rule 3 warning even with 'test'
    assert W("w", "claim: target-a test 1 -- files: specs/a.json") == []
    assert W("w", "flag: the latest negative needs a look") == []
    # 'test' inside another word does not fire
    assert W("w", "done: attested reading, grade H") == []
    # dollar figures anywhere -> cost warning (any line kind, role or signal)
    assert W("w", "claim: cap $8, target-a") == [COST]
    assert W("w", "done: finished well under 5 dollars") == [COST]
    assert W("w", "note: 12 USD spent") == [COST]
    assert W("parent (cost $ 3)", "check-in") == [COST]
    # both at once, in this order
    assert W("w", "done: test negative, cost $2") == [RULE3, COST]
    # no false positive on a plain done line or a bare $ without a digit
    assert W("w", "done: for LANE V6: reading ready, grade H 120/130") == []
    assert W("w", "done: shell variable $HOME not expanded") == []

    # "please change"/"still says" with no commit id -> WARNING
    CITE = ("WARNING: 'please change'/'still says' with no commit id -- name the commit you read the file "
            "at (`git log -1 --format=%h -- <path>`) or grep the exact old text, so a reader can tell a "
            "live ask from a stale one (RETRO-2026-09-26f, parent.md 'Cite what you read')")
    assert W("w", "for LANE B: please change status.json's lodewijk grade text") == [CITE]
    assert W("w", "flag: status.json still says N2 for lodewijk") == [CITE]
    # same, but with a 7-hex commit id present -> no warning
    assert W("w", "for LANE B: please change status.json (read at a1b2c3d)") == []
    assert W("w", "flag: status.json still says N2 (as of 9f8e7d6c)") == []
    # no "please change"/"still says" at all -> no warning from this check
    assert W("w", "flag: status.json needs a look") == []

    # typed clock time far from the line's own stamp -> WARNING; near or absent -> none
    import time as _time
    frozen = _time.struct_time((2026, 9, 26, 7, 37, 0, 5, 269, 0))
    old_gmtime = room.time.gmtime
    room.time.gmtime = lambda *a: frozen
    try:
        w = W("parent 7g", "handoff: took over from 7f at 07:41 UTC 26 Sept 2026 (clock read)")
        assert any(s.startswith("WARNING: signal text says 'at 07:41 UTC'") for s in w), w
        assert W("parent 7g", "handoff: took over at 07:38 UTC (clock read)") == []
        assert W("parent 7g", "handoff: took over (clock read)") == []
    finally:
        room.time.gmtime = old_gmtime

    # main() prints the warning and still appends, with push mocked so nothing is committed
    calls = []
    with tempfile.TemporaryDirectory() as d:
        tmp = os.path.join(d, "ROOM.md")
        open(tmp, "w").write("2026-09-25 00:00 | seed | note: existing line\n")
        old_room, old_push = room.ROOM, room.push
        room.ROOM = tmp
        room.push = lambda msg, paths: calls.append((msg, paths)) or 0
        try:
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = room.main(["LANE T worker", "done: test 1 negative on target-a"])
        finally:
            room.ROOM, room.push = old_room, old_push
        assert rc == 0
        assert RULE3 in buf.getvalue(), buf.getvalue()
        lines = open(tmp).read().splitlines()
        assert len(lines) == 2 and lines[1].endswith("| LANE T worker | done: test 1 negative on target-a"), lines
        assert calls == [("ROOM: done: test 1 negative on target-a", ["ROOM.md"])], calls
    print("ok room warnings: 24 cases, append still happens, push mocked")


if __name__ == "__main__":
    test_warnings()
