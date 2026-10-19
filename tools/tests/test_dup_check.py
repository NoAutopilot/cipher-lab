#!/usr/bin/env python3
"""Offline pytest test for tools/dup_check.py (RETRO-2026-10-19 P2, applied 19 Oct 2026).

The three motivating shapes from RETRO-2026-10-19 section 3, as fixtures -- must catch, exit 1:
  OBRED-TRY2/MAT-F91 shape: a claim for job A on target T with no done line, then (what a
    job-name-keyed dup check would miss) a second job under a *different* name B about to start
    on the same T.
  MAT-EYE shape: a claim for job C on target T with no done line, then a second claim under the
    *identical* job name C -- even a literal job-name grep should have caught this and historically
    did not; this tool never keys on job name at all, so there is no special case to get right.

Must NOT block, exit 0:
  a target whose only ROOM.md lines in the window are done lines (every claim already closed).
  a target with no ROOM.md mention at all in the window.

Run: /root/.local/bin/pytest tools/tests/test_dup_check.py -q
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import dup_check as dc  # noqa: E402

NOW = dc.datetime.datetime(2026, 10, 19, 7, 30)


def write_room(path, lines):
    path.write_text("".join(lines), encoding="utf-8")


def test_different_job_name_duplicate_is_caught(tmp_path):
    """OBRED-TRY2/MAT-F91 shape: job A claims target T, no done; job B (different name) is about
    to claim the same T -- a check keyed to job B's own name would find nothing."""
    path = tmp_path / "ROOM.md"
    write_room(path, [
        "2026-10-19 06:00 | worker OBRED-TRY (account 2) | claim for LANE X (account 2) (06:0x UTC 19 Oct): "
        "oldenbarnevelt-brederode-1605 stride-3 sweep. usage: not readable here\n",
        "2026-10-19 06:30 | LANE X (account 2) | check-in: wave spawning. usage: five_hour allowed\n",
    ])
    code, matches = dc.check(str(path), "oldenbarnevelt-brederode-1605", 24, NOW)
    assert code == 1
    assert any(kind == "claim" for _, kind, _ in matches)


def test_identical_job_name_duplicate_is_caught(tmp_path):
    """MAT-EYE shape: job C claims target T, no done; a second claim under the identical job name
    C on the same T. Caught the same way as the different-name case, since this tool never keys
    on job name."""
    path = tmp_path / "ROOM.md"
    write_room(path, [
        "2026-10-19 05:00 | worker MAT-EYE (account 2) | claim for LANE Y (account 2) (05:0x UTC 19 Oct): "
        "matignon-mayenne-1586 eye-bisection pass. usage: not readable here\n",
        "2026-10-19 06:00 | worker MAT-EYE (account 3) | claim for LANE Z (account 3) (06:0x UTC 19 Oct): "
        "matignon-mayenne-1586 eye-bisection pass. usage: not readable here\n",
    ])
    code, matches = dc.check(str(path), "matignon-mayenne-1586", 24, NOW)
    assert code == 1
    assert len([m for m in matches if m[1] == "claim"]) == 2


def test_target_with_only_done_lines_is_not_blocked(tmp_path):
    path = tmp_path / "ROOM.md"
    write_room(path, [
        "2026-10-19 05:00 | worker FOO (account 2) | claim for LANE Y (account 2) (05:0x UTC 19 Oct): "
        "harley-287-1587 known-keys rung. usage: not readable here\n",
        "2026-10-19 06:00 | worker FOO (account 2) | done (05:0x-06:0x UTC 19 Oct) for LANE Y (account 2): "
        "harley-287-1587 no key fits f.11. usage: not readable here\n",
    ])
    code, matches = dc.check(str(path), "harley-287-1587", 24, NOW)
    assert code == 0
    assert len(matches) == 2


def test_target_with_no_mention_is_not_blocked(tmp_path):
    path = tmp_path / "ROOM.md"
    write_room(path, [
        "2026-10-19 05:00 | worker FOO (account 2) | claim for LANE Y (account 2) (05:0x UTC 19 Oct): "
        "harley-287-1587 known-keys rung. usage: not readable here\n",
    ])
    code, matches = dc.check(str(path), "some-other-target-1700", 24, NOW)
    assert code == 0
    assert matches == []
