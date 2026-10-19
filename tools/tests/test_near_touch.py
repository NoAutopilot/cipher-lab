#!/usr/bin/env python3
"""Offline pytest test for tools/near_touch.py (RETRO-2026-10-19 P1, applied 19 Oct 2026).

Covers:
  round trip: touching a real six-column row appends a dated note to Evidence and stamps
    Last-touched to the given --now, in the same write.
  must NOT block: touching with no --note still bumps Last-touched alone.
  refuse, exit 1: a target with no row in the active table.
  refuse, exit 2: a target whose row's own cell count does not match the header's (the
    near_audit_columns.py drift shape) -- never patched blindly into the wrong column.

Run: /root/.local/bin/pytest tools/tests/test_near_touch.py -q
"""
import datetime
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import near_touch as nt  # noqa: E402

HEADER = "| Target | Evidence | What would settle it | Lane / owner | Blocker or ASKS row | Last touched (UTC) |\n"
SEP = "|---|---|---|---|---|---|\n"
NOW = datetime.datetime(2026, 10, 19, 7, 30)


def write_fixture(path, extra_row=None):
    lines = (
        "# NEAR.md test fixture\n\n" + HEADER + SEP +
        "| targ-a (a test row) | old evidence | some next step | LANE X | none | 18 Oct 2026 10:00 UTC |\n"
    )
    if extra_row:
        lines += extra_row
    path.write_text(lines, encoding="utf-8")


def test_touch_with_note_round_trip(tmp_path):
    path = tmp_path / "NEAR.md"
    write_fixture(path)

    code, message, evidence, touched = nt.touch(str(path), "targ-a", "new finding", NOW)
    assert code == 0
    assert message is None
    assert "new finding" in evidence
    assert "old evidence" in evidence
    assert touched == "19 Oct 2026 07:30 UTC"

    # the write actually landed
    _, cells, _ = nt.find_row(path.read_text(encoding="utf-8").splitlines(keepends=True), "targ-a")
    assert cells[-1] == "19 Oct 2026 07:30 UTC"
    assert "new finding" in cells[1]


def test_touch_with_no_note_bumps_last_touched_only(tmp_path):
    path = tmp_path / "NEAR.md"
    write_fixture(path)

    code, message, evidence, touched = nt.touch(str(path), "targ-a", None, NOW)
    assert code == 0
    assert evidence == "old evidence"
    assert touched == "19 Oct 2026 07:30 UTC"


def test_refuses_missing_target(tmp_path):
    path = tmp_path / "NEAR.md"
    write_fixture(path)

    code, message, evidence, touched = nt.touch(str(path), "targ-nonexistent", "note", NOW)
    assert code == 1
    assert evidence is None and touched is None
    assert "no active-table row" in message


def test_refuses_drifted_row(tmp_path):
    path = tmp_path / "NEAR.md"
    drifted_row = (
        "| targ-drift (a test row) | some evidence | some next step | LANE X | none | "
        "2 Oct 2026 09:0x UTC (first) | 3 Oct 2026 05:0x UTC (second) |\n"
    )
    write_fixture(path, extra_row=drifted_row)
    before = path.read_text(encoding="utf-8")

    code, message, evidence, touched = nt.touch(str(path), "targ-drift", "note", NOW)
    assert code == 2
    assert evidence is None and touched is None
    assert "near_audit_columns.py" in message

    # the file itself must be untouched
    assert path.read_text(encoding="utf-8") == before
