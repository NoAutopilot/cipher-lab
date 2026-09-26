#!/usr/bin/env python3
"""Offline pytest test for tools/next_steps.py (worker NEXT-STEPS, 26 Sept 2026).

Builds two fixture ciphers/<t>/NOTES.md files under tmp_path -- one `open` with a runnable next
step in a "Status:" second line, one `blocked` needing a person -- plus a `closed-negative` folder
that must be excluded, a tiny LEDGER.md and NEAR.md, and checks build_rows()/render_tsv()/--check
against them, no network, no dependence on the real repository's own folders.

Run: /root/.local/bin/pytest tools/tests/test_next_steps.py -q
"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import next_steps as ns  # noqa: E402

RUNNABLE_NOTES = """# some-target

Status: open

## What this is

A control-backed negative on the masc family (target -1.9 vs control -1.1, gate -1.0). Next step:
cut fresh line crops with tools/iiif_lines.py and run a second blind pass over folio 12r; about
USD 4 (a two-blind-pass leaf, per README's per-unit pricing precedents).
"""

STALE_RUNNABLE_NOTES = """# some-target

Status: open

## What this is

Next step: send the copy order first (superseded).

## Later pass

Next step: cut fresh line crops with tools/iiif_lines.py and run a second blind pass over folio
12r; about USD 4.
"""

BLOCKED_NOTES = """other-target

blocked (REQUEST.md filed 20 Sept 2026)

Waiting on the owner: LOCAL-QUEUE row L9 asks him to check HathiTrust page 44 for the plaintext
before any more cryptanalysis. Next: once ASKS row 12 is answered, resume the key search.
"""

CLOSED_NOTES = """closed-target

closed-negative

Every family in the ladder ran against a matched control and failed. Next step: nothing -- this
target is done.
"""


def write_notes(ciphers_dir, target, text):
    d = os.path.join(ciphers_dir, target)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "NOTES.md"), "w", encoding="utf-8") as f:
        f.write(text)


LEDGER = """# Team ledger

| Date | Role | Model | Session | Cost | Outcome | Lesson |
|---|---|---|---|---|---|---|
| 20 Sep | worker on some-target: first pass | Sonnet | session_1 | 3.10 | D | first pass |
| 24 Sep | worker on other-target: request filed | Sonnet | session_2 | 1.00 | D | filed REQUEST.md |
| 25 Sep | worker on some-target: second look | Sonnet | session_3 | 2.00 | D | second look |
"""

NEAR = """# NEAR.md

| Target | Evidence | What would settle it | Lane | Blocker | Last touched (UTC) |
|---|---|---|---|---|---|
| some-target | control-backed margin | second blind pass | LANE X | none | 25 Sept 20:00 |
"""


def test_status_extraction_handles_label_and_bare_forms():
    assert ns.first_status_word(RUNNABLE_NOTES) == "open"
    assert ns.first_status_word(BLOCKED_NOTES) == "blocked"
    assert ns.first_status_word(CLOSED_NOTES) == "closed-negative"


def test_next_step_takes_the_most_recent_paragraph():
    step = ns.extract_next_step(STALE_RUNNABLE_NOTES)
    assert "second blind pass" in step
    assert "copy order" not in step


def test_build_rows_excludes_closed_negative_and_classifies(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "some-target", RUNNABLE_NOTES)
    write_notes(ciphers_dir, "other-target", BLOCKED_NOTES)
    write_notes(ciphers_dir, "closed-target", CLOSED_NOTES)

    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    by_folder = {r["folder"]: r for r in rows}

    assert set(by_folder) == {"some-target", "other-target"}

    r = by_folder["some-target"]
    assert r["status"] == "open"
    assert r["blocker"] == "runnable"
    assert r["cost_band"] == "M"
    assert r["near_row"] == "y"
    assert r["last_touched"] == "25 Sep"
    assert "second blind pass" in r["next_step"]
    assert len(r["next_step"]) <= 200

    r2 = by_folder["other-target"]
    assert r2["status"] == "blocked"
    assert r2["blocker"] == "needs-person"
    assert r2["near_row"] == "n"
    assert r2["last_touched"] == "24 Sep"


def test_render_tsv_idempotent_and_check_mode(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "some-target", RUNNABLE_NOTES)
    write_notes(ciphers_dir, "other-target", BLOCKED_NOTES)
    ledger_path = tmp_path / "LEDGER.md"
    near_path = tmp_path / "NEAR.md"
    out_path = tmp_path / "NEXT-STEPS.tsv"
    ledger_path.write_text(LEDGER, encoding="utf-8")
    near_path.write_text(NEAR, encoding="utf-8")

    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    tsv1 = ns.render_tsv(rows)
    tsv2 = ns.render_tsv(ns.build_rows(str(ciphers_dir), LEDGER, NEAR))
    assert tsv1 == tsv2
    assert "needs-person=1" in tsv1
    assert "runnable=1" in tsv1

    out_path.write_text(tsv1, encoding="utf-8")

    check = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "next_steps.py"),
         "--ciphers-dir", str(ciphers_dir), "--ledger", str(ledger_path),
         "--near", str(near_path), "--out", str(out_path), "--check"],
        capture_output=True, text=True,
    )
    assert check.returncode == 0, check.stdout + check.stderr

    write_notes(ciphers_dir, "third-target", BLOCKED_NOTES)
    check2 = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "next_steps.py"),
         "--ciphers-dir", str(ciphers_dir), "--ledger", str(ledger_path),
         "--near", str(near_path), "--out", str(out_path), "--check"],
        capture_output=True, text=True,
    )
    assert check2.returncode != 0, check2.stdout + check2.stderr


if __name__ == "__main__":
    import pytest
    sys.exit(pytest.main([__file__, "-q"]))
