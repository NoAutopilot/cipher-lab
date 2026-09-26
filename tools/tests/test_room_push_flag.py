#!/usr/bin/env python3
"""Offline test: tools/room.py --push refuses a flag-like or missing path instead of silently dropping the
real paths from the commit (LEARN-2026-09-26-0022 item 2 = LEARN-2026-09-26-0058 item 3: a stray -m "message"
passed after --push used to be handed straight to `git add --` as a literal pathspec). bad_paths() is a pure
function checked directly; push() is checked to refuse before touching git at all when a bad path is present.
Run: python3 tools/tests/test_room_push_flag.py"""
import os, sys, io, contextlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402


def test_flag_like_path_is_bad():
    # "-m" is flag-like; "tools/room.py" is a real path, so only "-m" is bad here
    bad = room.bad_paths(["-m", "tools/room.py"])
    assert bad == ["-m"], bad


def test_existing_path_is_fine():
    bad = room.bad_paths(["tools/room.py"])
    assert bad == [], bad


def test_missing_path_is_bad():
    bad = room.bad_paths(["tools/no-such-file-xyz-does-not-exist.md"])
    assert bad == ["tools/no-such-file-xyz-does-not-exist.md"], bad


def test_push_refuses_without_touching_git():
    calls = []
    real_sh = room.sh
    def spy(*args, **kwargs):
        calls.append(args)
        return real_sh(*args, **kwargs)
    room.sh = spy
    try:
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            rc = room.push("some message", ["-m", "tools/room.py"])
        assert rc == 2, rc
        assert "refusing" in out.getvalue()
        assert "-m" in out.getvalue()
        mutating = [c for c in calls if c[1] in ("add", "commit", "push")]
        assert not mutating, f"push() ran a mutating git command before refusing: {mutating}"
    finally:
        room.sh = real_sh


if __name__ == "__main__":
    test_flag_like_path_is_bad()
    test_existing_path_is_fine()
    test_missing_path_is_bad()
    test_push_refuses_without_touching_git()
    print("ok")
