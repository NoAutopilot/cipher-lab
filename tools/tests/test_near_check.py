#!/usr/bin/env python3
"""Offline pytest test for tools/near_check.py (worker NEAR-TOOL, 25 Sept 2026).

Builds temporary NEAR.md, status.json and NOTES.md fixtures under tmp_path -- no network, no
dependence on the real repository's current NEAR.md/status.json/ciphers state -- and covers the
three problem shapes the tool checks plus the clean case:
  (a) a near-solve target whose NOTES.md first status word is `closed-negative`.
  (b) a target present in only one of NEAR.md / status.json's `near` list.
  (c) a row whose "Last touched" is more than 48 hours before `now` (warning, exit 2 alone).
  clean: two targets, both in step, neither closed-negative nor stale -- exit 0.

Run: /root/.local/bin/pytest tools/tests/test_near_check.py -q
"""
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import near_check as nc  # noqa: E402

NOW = datetime.datetime(2026, 9, 25, 20, 0)


def write_near_md(path, rows):
    lines = ["# NEAR.md test fixture\n\n", "| Target | Evidence | Next | Lane | Blocker | Last touched (UTC) |\n",
             "|---|---|---|---|---|---|\n"]
    for target, touched in rows:
        lines.append(f"| {target} (a test row) | some evidence | some next step | LANE X | none | {touched} |\n")
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(lines)


def write_status_json(path, near_entries):
    json.dump({"updated": "25 Sep 2026, 20:00 UTC", "near": near_entries}, open(path, "w", encoding="utf-8"))


def write_notes(ciphers_dir, target, first_word):
    d = os.path.join(ciphers_dir, target)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "NOTES.md"), "w", encoding="utf-8") as f:
        f.write(f"{first_word}\n\nSome prose about {target}.\n")


def near_entry(target, touched):
    return {"target": target, "title": f"{target} test", "next": "do the thing", "lane": "X", "touched": touched}


def test_clean_case(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    write_near_md(tmp_path / "NEAR.md", [("targ-a", "25 Sept 19:00"), ("targ-b", "25 Sept 18:00")])
    write_status_json(tmp_path / "status.json", [near_entry("targ-a", "25 Sept 2026 19:00"), near_entry("targ-b", "25 Sept 2026 18:00")])
    write_notes(ciphers_dir, "targ-a", "partial")
    write_notes(ciphers_dir, "targ-b", "open")

    near_rows = nc.parse_near_md(str(tmp_path / "NEAR.md"), NOW.year)
    status_near = nc.load_status_near(str(tmp_path / "status.json"))
    code, problems, warnings = nc.run_checks(near_rows, status_near, str(ciphers_dir), NOW)

    assert code == 0
    assert problems == []
    assert warnings == []


def test_closed_negative_is_a_problem(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    write_near_md(tmp_path / "NEAR.md", [("targ-a", "25 Sept 19:00")])
    write_status_json(tmp_path / "status.json", [near_entry("targ-a", "25 Sept 2026 19:00")])
    write_notes(ciphers_dir, "targ-a", "closed-negative")

    near_rows = nc.parse_near_md(str(tmp_path / "NEAR.md"), NOW.year)
    status_near = nc.load_status_near(str(tmp_path / "status.json"))
    code, problems, warnings = nc.run_checks(near_rows, status_near, str(ciphers_dir), NOW)

    assert code == 1
    assert len(problems) == 1
    assert "closed-negative" in problems[0]
    assert "targ-a" in problems[0]


def test_drift_between_near_md_and_status_json_is_a_problem(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    # targ-a is in both; targ-only-near is in NEAR.md only; targ-only-status is in status.json only.
    write_near_md(tmp_path / "NEAR.md", [("targ-a", "25 Sept 19:00"), ("targ-only-near", "25 Sept 19:00")])
    write_status_json(tmp_path / "status.json", [near_entry("targ-a", "25 Sept 2026 19:00"), near_entry("targ-only-status", "25 Sept 2026 19:00")])
    write_notes(ciphers_dir, "targ-a", "partial")
    write_notes(ciphers_dir, "targ-only-near", "partial")
    write_notes(ciphers_dir, "targ-only-status", "partial")

    near_rows = nc.parse_near_md(str(tmp_path / "NEAR.md"), NOW.year)
    status_near = nc.load_status_near(str(tmp_path / "status.json"))
    code, problems, warnings = nc.run_checks(near_rows, status_near, str(ciphers_dir), NOW)

    assert code == 1
    assert any("targ-only-near" in p for p in problems)
    assert any("targ-only-status" in p for p in problems)
    assert len(problems) == 2


def test_stale_row_is_a_warning_only(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    # 25 Sept 2026 19:00 is 49 hours before 27 Sept 2026 20:00 -- over the 48h window.
    write_near_md(tmp_path / "NEAR.md", [("targ-a", "25 Sept 19:00")])
    write_status_json(tmp_path / "status.json", [near_entry("targ-a", "25 Sept 2026 19:00")])
    write_notes(ciphers_dir, "targ-a", "partial")

    later = datetime.datetime(2026, 9, 27, 20, 0)
    near_rows = nc.parse_near_md(str(tmp_path / "NEAR.md"), later.year)
    status_near = nc.load_status_near(str(tmp_path / "status.json"))
    code, problems, warnings = nc.run_checks(near_rows, status_near, str(ciphers_dir), later)

    assert code == 2
    assert problems == []
    assert len(warnings) == 1
    assert "targ-a" in warnings[0]


def test_year_less_near_md_date_is_read_as_current_year(tmp_path):
    # NEAR.md's own column has no year; confirm parse_dt fills it in from default_year.
    dt = nc.parse_dt("25 Sept 19:00", 2026)
    assert dt == datetime.datetime(2026, 9, 25, 19, 0)


def test_slug_of_strips_trailing_parenthetical():
    assert nc.slug_of("espagnol142-mercy-1648 (Mercy, Brussels, 1648; 521 code tokens, 38 values)") == "espagnol142-mercy-1648"
    assert nc.slug_of("targ-a") == "targ-a"


if __name__ == "__main__":
    import subprocess
    sys.exit(subprocess.call([sys.executable, "-m", "pytest", __file__, "-q"]))
