#!/usr/bin/env python3
"""Offline pytest test for tools/near_audit_columns.py (RETRO-2026-10-19 P1, applied 19 Oct 2026).

Covers:
  catch: a row with a literal unescaped '|' inside a cell (the shape found for real in NEAR.md's
         own antt-msliv0638-brochado-1712 / birago-fr3252-1571-72 / pollaky-1865-1875 /
         hellen-frederick-1752 rows -- a pipe used to separate two dated stamps inside the
         Last-touched cell, splitting it into an extra column) -- must flag, exit 1.
  must NOT block: a clean six-column row, and a '## Closed rows' row of the *other* table's shape
         (3 columns) -- that table is a different header entirely and is out of this tool's scope,
         the same way near_check.py's own parse_near_md stops at that heading.

Run: /root/.local/bin/pytest tools/tests/test_near_audit_columns.py -q
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import near_audit_columns as nac  # noqa: E402

HEADER = "| Target | Evidence | What would settle it | Lane / owner | Blocker or ASKS row | Last touched (UTC) |\n"
SEP = "|---|---|---|---|---|---|\n"


def test_clean_table_has_no_mismatch(tmp_path):
    path = tmp_path / "NEAR.md"
    path.write_text(
        "# NEAR.md test fixture\n\n" + HEADER + SEP +
        "| targ-a (a test row) | some evidence | some next step | LANE X | none | 19 Oct 2026 07:00 UTC |\n" +
        "| targ-b (another row) | more evidence | another step | LANE Y | none | 19 Oct 2026 06:00 UTC |\n" +
        "\n## Closed rows\n\n| Target | Why it left | Date |\n|---|---|---|\n" +
        "| targ-c | found-solved elsewhere | 18 Oct 2026 |\n",
        encoding="utf-8",
    )
    header_count, mismatches = nac.audit(str(path))
    assert header_count == 6
    assert mismatches == []


def test_pipe_in_cell_is_flagged(tmp_path):
    path = tmp_path / "NEAR.md"
    # Last-touched cell carries two stamps joined by a literal '|' (parse_dt's own documented
    # shape for a hand-edited cell) -- this splits the row into 7 cells against a 6-cell header.
    path.write_text(
        "# NEAR.md test fixture\n\n" + HEADER + SEP +
        "| targ-drift (a test row) | some evidence | some next step | LANE X | none | "
        "2 Oct 2026 09:0x UTC (first review) | 3 Oct 2026 05:0x UTC (second review) |\n" +
        "| targ-clean (clean row) | more evidence | another step | LANE Y | none | 19 Oct 2026 06:00 UTC |\n",
        encoding="utf-8",
    )
    header_count, mismatches = nac.audit(str(path))
    assert header_count == 6
    assert len(mismatches) == 1
    lineno, target, count = mismatches[0]
    assert target == "targ-drift"
    assert count == 7


def test_closed_table_three_column_row_is_not_flagged(tmp_path):
    """A '## Closed rows' row is a different, 3-column table -- out of scope entirely, not a
    mismatch against the active table's 6-column header."""
    path = tmp_path / "NEAR.md"
    path.write_text(
        "# NEAR.md test fixture\n\n" + HEADER + SEP +
        "| targ-a (a test row) | some evidence | some next step | LANE X | none | 19 Oct 2026 07:00 UTC |\n" +
        "\n## Closed rows\n\n| Target | Why it left | Date |\n|---|---|---|\n" +
        "| targ-b | found-solved elsewhere | 18 Oct 2026 |\n" +
        "| targ-c | closed-negative, every family logged | 17 Oct 2026 |\n",
        encoding="utf-8",
    )
    header_count, mismatches = nac.audit(str(path))
    assert header_count == 6
    assert mismatches == []
