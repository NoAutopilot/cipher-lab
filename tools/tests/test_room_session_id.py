#!/usr/bin/env python3
"""Offline test for tools/room.py's role-session-id check (26 Sept 2026, RETRO-2026-09-26d): a ROOM.md role
field is self-referential ('parent worker X (session_...)'), so any session_... id it names should be the
appending session's own, taken from CLAUDE_CODE_REMOTE_SESSION_ID ('cse_<id>' -> 'session_<id>', confirmed
against this retrospective's own id). DECODE-ACCESS's done line (26 Sept 2026, LEDGER.md) named a different
session's id instead of its own, undetected until a human read the ledger. Run:
python3 tools/tests/test_room_session_id.py"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402


def test_own_session_id():
    old = os.environ.get("CLAUDE_CODE_REMOTE_SESSION_ID")
    try:
        os.environ["CLAUDE_CODE_REMOTE_SESSION_ID"] = "cse_01Gny4j6pxVrzWP5F9wXjDdE"
        assert room._own_session_id() == "session_01Gny4j6pxVrzWP5F9wXjDdE"
        os.environ["CLAUDE_CODE_REMOTE_SESSION_ID"] = "not-a-cse-id"
        assert room._own_session_id() is None
        del os.environ["CLAUDE_CODE_REMOTE_SESSION_ID"]
        assert room._own_session_id() is None
    finally:
        if old is None:
            os.environ.pop("CLAUDE_CODE_REMOTE_SESSION_ID", None)
        else:
            os.environ["CLAUDE_CODE_REMOTE_SESSION_ID"] = old


def test_warnings_role_session_mismatch():
    W = room.warnings_for
    own = "session_01AQwk5zWLCGvxyuPFhwaHDD"
    ws = W("parent worker DECODE-ACCESS (Sonnet, session_01SvjMDFfJZJ3uK47RYxAQrM)", "done: verdict account-wide",
           own_id=own)
    assert any("session_01SvjMDFfJZJ3uK47RYxAQrM" in w and own in w for w in ws), ws
    assert W(f"parent worker DECODE-ACCESS (Sonnet, {own})", "done: verdict account-wide", own_id=own) == []
    assert W("LANE B7 orchestrator", "for the parent: check-in", own_id=own) == []
    assert W("parent worker X (session_ANYTHING)", "done: x", own_id=None) == []
    print("ok room session-id check: 4 cases + _own_session_id 3 cases")


if __name__ == "__main__":
    test_own_session_id()
    test_warnings_role_session_mismatch()
