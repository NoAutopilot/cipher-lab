#!/usr/bin/env python3
"""Offline test: tools/room.py refuses an unknown leading option instead of writing it into ROOM.md as the role
(26 Sept 2026, V7-QA4 found 23 lines with role '--append'). room.push is mocked and ROOM points at a temp file.
Run: python3 tools/tests/test_room_unknown_flag.py"""
import os, sys, tempfile, io, contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402


def test_unknown_flag_refused():
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "ROOM.md")
        open(path, "w").write("x\n")
        room.ROOM = path
        room.push = lambda *a, **k: 0
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            rc = room.main(["--append", "for LANE V7: done: something"])
        assert rc == 2, rc
        assert "unknown option" in err.getvalue()
        assert open(path).read() == "x\n"
        # a normal role still appends
        with contextlib.redirect_stdout(io.StringIO()):
            rc = room.main(["worker X", "claim: target-a"])
        assert rc == 0, rc
        assert "| worker X | claim: target-a" in open(path).read()


if __name__ == "__main__":
    test_unknown_flag_refused()
    print("ok")
