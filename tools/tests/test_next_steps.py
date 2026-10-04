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

NO_NEXT_STEP_NOTES = """# empty-target

Status: open

## What this is

A control-backed negative on the masc family. No next-step trigger phrase appears anywhere in this
file.
"""

TRUNCATED_BLOCKER_NOTES = (
    "# trunc-target\n\nStatus: open\n\n## What this is\n\nNext step: "
    + ("re-run the coverage sweep " * 10)
    + "then ask the owner to confirm before continuing.\n"
)

SHORT_RUNNABLE_NOTES = """# short-target

Status: open

## What this is

Next step: run print_check on the decoded phrases.
"""

TWO_DATED_SECTIONS_NOTES = """# dated-target

Status: partial

## First pass, 20 Sept 2026

Some background on the first attempt. Next step: do X (superseded by the pass below).

## Second pass, 25 Sept 2026

A verifier graded the key N3 here. Next step: do Y, the current live next step.
"""

NO_DATED_SECTION_NOTES = """# undated-target

Status: open

## What this is

Next step: send the copy order first (superseded).

## Later pass

Next step: cut fresh line crops with tools/iiif_lines.py and run a second blind pass over folio
12r; about USD 4.
"""


BLOCKED_WITH_WAITING_NOTES = """other-target

blocked (REQUEST.md filed 20 Sept 2026)

Waiting on the owner: LOCAL-QUEUE row L9 asks him to check HathiTrust page 44 for the plaintext
before any more cryptanalysis. Next: once ASKS row 12 is answered, resume the key search.

## While waiting, 24 Sept 2026

- run the masc family control on the target's own N and K while the copy request stands
- a second bullet, not the first, must not be picked
"""

BLOCKED_NO_WAITING_NOTES = """third-target

blocked (REQUEST.md filed 20 Sept 2026)

Waiting on the owner: no parallel action has been written for this one yet. Next: resume once
the copy arrives.
"""

BLOCKED_TWO_WAITING_SECTIONS_NOTES = """fourth-target

blocked (REQUEST.md filed 20 Sept 2026)

Next: resume once the copy arrives.

## While waiting, 20 Sept 2026

- the stale bullet, superseded

## While waiting, 25 Sept 2026

- the live bullet, run the judge on the sibling reading
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


def test_next_step_prefers_the_newest_dated_section():
    """NX-FIX, 26 Sept 2026: a NOTES.md with two dated sections picks the next-step paragraph
    from the newer one, even though an earlier trigger phrase appears later in raw file-order
    scanning would not apply here -- both candidates are in order, so this also guards against
    a regression that reverts to plain last-block-in-file scanning."""
    step = ns.extract_next_step(TWO_DATED_SECTIONS_NOTES)
    assert "do Y" in step
    assert "do X" not in step


def test_next_step_falls_back_to_whole_file_when_no_dated_section():
    """NX-FIX, 26 Sept 2026: a file with no date anywhere in it (headings included) keeps the
    original whole-file "last matching block" behaviour."""
    step = ns.extract_next_step(NO_DATED_SECTION_NOTES)
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


def test_empty_next_step_is_needs_triage_not_runnable(tmp_path):
    """NX-TRIAGE, 27 Sept 2026 (CODEX-REVIEW-2026-09-27.md section 2), case (a): a NOTES.md with
    no next-step trigger phrase anywhere extracts an empty block, which must classify
    needs-triage/? rather than runnable/S -- pre-fix, classify_blocker("") and
    estimate_cost_band("") fell through every pattern to their bare defaults ("runnable", "S")."""
    assert ns.extract_next_step(NO_NEXT_STEP_NOTES) == ""
    assert ns.classify_blocker("") == "needs-triage"
    assert ns.classify_blocker("   \n  ") == "needs-triage"
    assert ns.estimate_cost_band("") == "?"

    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "empty-target", NO_NEXT_STEP_NOTES)
    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    r = rows[0]
    assert r["next_step"] == ""
    assert r["blocker"] == "needs-triage"
    assert r["cost_band"] == "?"


def test_blocker_classified_on_full_block_not_truncated_display_text(tmp_path):
    """NX-TRIAGE, 27 Sept 2026, case (b): the blocker keyword ("owner") sits past one_line()'s
    200-character truncation point, so build_rows() must classify on the full extracted block, not
    on the truncated display text -- pre-fix, build_rows() called classify_blocker()/
    estimate_cost_band() on `next_step` (already truncated), which never saw "owner" and mis-read
    this row as runnable."""
    block = ns.extract_next_step(TRUNCATED_BLOCKER_NOTES)
    truncated = ns.one_line(block)
    assert "owner" in block
    assert "owner" not in truncated, "fixture must place the blocker keyword past the truncation limit"
    assert ns.classify_blocker(truncated) == "runnable", "sanity: truncated text alone hides the blocker"
    assert ns.classify_blocker(block) == "needs-person"

    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "trunc-target", TRUNCATED_BLOCKER_NOTES)
    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    r = rows[0]
    assert r["blocker"] == "needs-person"
    assert "owner" not in r["next_step"]
    assert int(r["next_step_full_len"]) == len(block)


def test_short_real_instruction_without_blocker_keyword_stays_runnable(tmp_path):
    """Must-not-block case (CLAUDE.md Usage 8a): a short but real instruction with no blocker
    keyword in it (e.g. "run print_check on the decoded phrases") stays runnable/S -- the fix must
    not turn every terse next step into needs-triage, only a genuinely empty one."""
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "short-target", SHORT_RUNNABLE_NOTES)
    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    r = rows[0]
    assert r["next_step"] != ""
    assert r["blocker"] == "runnable"
    assert r["cost_band"] == "S"


def test_parallel_column_filled_from_while_waiting_section(tmp_path):
    """WAIT-CHECK, 27 Sept 2026: a blocked folder with a '## While waiting' section fills the
    `parallel` cell from its first bullet; a blocked folder without one is left empty (not '--',
    which is reserved for runnable/needs-triage rows) and shows up in --wait-only."""
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "some-target", RUNNABLE_NOTES)
    write_notes(ciphers_dir, "other-target", BLOCKED_WITH_WAITING_NOTES)
    write_notes(ciphers_dir, "third-target", BLOCKED_NO_WAITING_NOTES)

    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    by_folder = {r["folder"]: r for r in rows}

    assert by_folder["some-target"]["parallel"] == "--", "runnable row must show -- not a bullet"

    r = by_folder["other-target"]
    assert r["blocker"] == "needs-person"
    assert r["parallel"] == "run the masc family control on the target's own N and K while the copy request stands"

    r3 = by_folder["third-target"]
    assert r3["blocker"] == "needs-person"
    assert r3["parallel"] == ""

    blocked, missing = ns.wait_only_rows(rows)
    assert {r["folder"] for r in blocked} == {"other-target", "third-target"}
    assert [r["folder"] for r in missing] == ["third-target"]


PROSE_WAITING_HEAD = """t

blocked (REQUEST.md filed 20 Sept 2026)

## While waiting, 3 Oct 2026

Run the homophonic family control at the target's N while the image request stands.
"""

PROSE_WAITING_SAME_BLOCK = """t

blocked (REQUEST.md filed 20 Sept 2026)

## While waiting
Score the sibling letter with the judge; it needs no one.
"""

PROSE_WAITING_DONE = """t

blocked (REQUEST.md filed 20 Sept 2026)

## While waiting

[done 3 Oct 2026, X] the sibling was scored; nothing else depends on nobody.
"""


def test_while_waiting_prose_paragraph_after_blank_line():
    """RETRO-2026-10-04-acct1 P1: a prose section (no bullet) fills `parallel`."""
    step = ns.extract_while_waiting(PROSE_WAITING_HEAD)
    assert step == "Run the homophonic family control at the target's N while the image request stands."


def test_while_waiting_prose_in_heading_block():
    """RETRO-2026-10-04-acct1 P1: prose with no blank line after the heading is still read."""
    step = ns.extract_while_waiting(PROSE_WAITING_SAME_BLOCK)
    assert step == "Score the sibling letter with the judge; it needs no one."


def test_while_waiting_done_paragraph_leaves_row_wait_only():
    """RETRO-2026-10-04-acct1 P1: a section whose only paragraph opens '[done' gives "" (stays wait-only)."""
    assert ns.extract_while_waiting(PROSE_WAITING_DONE) == ""


def test_while_waiting_prefers_newest_dated_section():
    step = ns.extract_while_waiting(BLOCKED_TWO_WAITING_SECTIONS_NOTES)
    assert "judge on the sibling" in step
    assert "stale bullet" not in step


def test_wait_only_flag_prints_only_the_missing_list(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "other-target", BLOCKED_WITH_WAITING_NOTES)
    write_notes(ciphers_dir, "third-target", BLOCKED_NO_WAITING_NOTES)
    ledger_path = tmp_path / "LEDGER.md"
    near_path = tmp_path / "NEAR.md"
    out_path = tmp_path / "NEXT-STEPS.tsv"
    ledger_path.write_text(LEDGER, encoding="utf-8")
    near_path.write_text(NEAR, encoding="utf-8")

    result = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "next_steps.py"),
         "--ciphers-dir", str(ciphers_dir), "--ledger", str(ledger_path),
         "--near", str(near_path), "--out", str(out_path), "--wait-only"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    lines = [l for l in result.stdout.splitlines() if l.strip()]
    assert lines == ["third-target | needs-person"]
    assert not os.path.exists(out_path), "--wait-only must not write NEXT-STEPS.tsv"


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


# TOOL-NS1, 3 Oct 2026 (flag from GAPS136): 'follow-up' triggers only as a line-head label.
FOLLOW_UP_PROSE_NOTES = """# decode-1411-like fixture
status: open

## Check-solved verdict (24 Sept 2026)

Blog site searches:
5. Cipherbrain: monthly archives. Also surfaced: Top 50
   no. 27 Ferdinand III letters and the 2017-10-07 Thomas Ernst follow-up -- Ferdinand III's own letters, not this
   fascicle. No post or comment naming this fascicle.
- Follow-up 2017-10-07 (.../top-50-crypto-mystery-solved-thomas-ernst/):
  Ernst's solution. No shelfmark.
"""

FOLLOW_UP_HEADING_NOTES = """# rumpf-vandebie-heinsius-like fixture
status: partial

## H1 pass (25 Sept 2026)

Letters 309 and 446 read at grade H.

Follow-up suggestions (one line each): (1) the NA originals of letters 309 and 446/455 against the edition.
"""


def test_follow_up_in_prose_is_not_a_next_step():
    """Must NOT fire: 'follow-up' inside a sentence (a cited blog title) or heading a bullet that
    names a post ('- Follow-up 2017-10-07 (<url>)') -- the decode-1411-hhsta-vienna-1600 shape."""
    assert ns.extract_next_step(FOLLOW_UP_PROSE_NOTES) == ""


def test_follow_up_label_heading_is_a_next_step():
    """Must catch: 'Follow-up suggestions (one line each):' heading a line, and the other
    labelled forms the corpus uses."""
    step = ns.extract_next_step(FOLLOW_UP_HEADING_NOTES)
    assert "NA originals" in step
    for label in ("Follow-up:", "## Follow-ups", "**Follow-up (not done):**",
                  "Follow-ups (suggestions, not done): x", "**Follow-up for the next job:** x",
                  "Suggested follow-ups (one line each, not run):"):
        assert ns.NEXT_STEP_RE.search("Some prose.\n" + label), label
    for prose in ("a narrower follow-up, not completed.", "follow-up pass with crop tooling",
                  "- Follow-up by hand (Google Books API)"):
        assert not ns.NEXT_STEP_RE.search(prose), prose


# TOOL-NS2 (3 Oct 2026, flagged by GAPS144 on ciphers/thurloe-printed): rule 5's Verdict line wins.
THURLOE_SHAPED_NOTES = """# thurloe-like fixture
status: partial

## s.20 (24 Sept 2026)

Pages 188-189 on archive.org are the next step, and this brief did not allow fetching them.

## Remaining gaps (GAPS-fixture, 3 Oct 2026)
Read so far: 402 of 424 tokens at H or C (94.8%)
- codes 143 and 70 - blocker: not-attempted; key image never compared; next: fetch stamford.jpg, ~$1.5
- a contemporary decipherment - blocker: waiting-on LOCAL-QUEUE L45 and the Bodleian's reply

## Escalation (GAPS-fixture, 3 Oct 2026)
- [x] siblings: printed decipherments aligned (s.16)
- [ ] known-keys: stamford.jpg not yet compared; planned as the cheapest next step
- [x] clear-pages: clear text used as context
- [x] print: phrase searches done (s.14)
- [x] key-rebuild: rebuilt from siblings
- [x] image-check: pages read from the image
- [ ] retry: one-vote M boundary test, disk only
Verdict: keep going: 1 internal gaps; cheapest next: fetch stamford.jpg and compare against key_stamford.tsv, ~$1.5
"""

PARKED_NOTES = THURLOE_SHAPED_NOTES.replace(
    "Verdict: keep going: 1 internal gaps; cheapest next: fetch stamford.jpg and compare against key_stamford.tsv, ~$1.5",
    "Verdict: parked: every gap has an outside blocker")


def test_remaining_gaps_verdict_wins_over_escalation_and_prose(tmp_path):
    """Must catch: a thurloe-shaped NOTES with Remaining gaps + Escalation -> the Verdict line is the
    next step, not the Escalation block (which matched 'next step') nor the older s.20 prose."""
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "thurloe-like", THURLOE_SHAPED_NOTES)
    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    assert len(rows) == 1
    step = rows[0]["next_step"]
    assert step.startswith("Verdict: keep going: 1 internal gaps; cheapest next: fetch stamford.jpg")
    assert "Escalation" not in step and "archive.org" not in step
    assert rows[0]["blocker"] == "runnable"


def test_parked_verdict_classifies_from_gap_blockers(tmp_path):
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "parked-like", PARKED_NOTES)
    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    assert rows[0]["next_step"] == "Verdict: parked: every gap has an outside blocker"
    assert rows[0]["blocker"] == "needs-person"  # LOCAL-QUEUE L45 in the gap lines


def test_no_remaining_gaps_keeps_prose_next_step(tmp_path):
    """Must NOT change: a folder with no Remaining gaps / Escalation sections keeps its prose next
    step exactly as extract_next_step() + one_line() gave it before TOOL-NS2."""
    assert ns.verdict_step(RUNNABLE_NOTES) == ("", "")
    ciphers_dir = tmp_path / "ciphers"
    write_notes(ciphers_dir, "some-target", RUNNABLE_NOTES)
    rows = ns.build_rows(str(ciphers_dir), LEDGER, NEAR)
    assert rows[0]["next_step"] == ns.one_line(ns.extract_next_step(RUNNABLE_NOTES))
    assert rows[0]["next_step"].startswith("Next step: cut fresh line crops")
