"""room.py --start counts only the active NEAR.md table, not the closed/left rows (V7-QA5, 26 Sept 2026)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import room  # noqa: E402


def test_near_rows_skip_closed_table():
    text = ("# NEAR\n\n| Target | Evidence |\n|---|---|\n| a-1600 (x) | e |\n| b-1700 (y) | e |\n\n"
            "## Closed rows (the named step ran)\n\n| Target | Why it left |\n|---|---|\n| c-1800 | gone |\n")
    rows = room.near_rows(text)
    assert [r.split("|")[1].strip().split(" ")[0] for r in rows] == ["a-1600", "b-1700"]


def test_near_rows_empty():
    assert room.near_rows("# NEAR\n\nno table\n") == []
