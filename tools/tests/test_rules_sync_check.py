#!/usr/bin/env python3
"""Offline test for tools/rules_sync_check.py (RULES-SLIM, 5 Oct 2026).

Run: python3 -m pytest tools/tests/test_rules_sync_check.py -q
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import rules_sync_check as rs  # noqa: E402

FULL = ("[R0] Edit both.\n3. [R3] **No negative without a matched control.** Long story.\n"
        "   [R3.c] A language corpus can be the wrong era. Lesson of ...\n4a. [R4a] Depth.\n"
        "[OUT.1] (1) AUDIT.md class; [USE.8a.b] gates; [ACC.cat] catalogue first.\n")
SLIM = ("[R0] Edit both.\n3. [R3] Matched control.\n   [R3.c] Era-matched corpus.\n4a. [R4a] D0-D4.\n"
        "[OUT.1] (1) class; [USE.8a.b] gate list; [ACC.cat] catalogue.\n")


def test_in_sync():
    assert rs.compare(SLIM, FULL) == []


def test_rule_added_to_one_file_only_is_caught():
    probs = rs.compare(SLIM + "[R3.n] New rule.\n", FULL)
    assert probs == ["id [R3.n] in slim only (add it to the full rulebook)"]
    probs = rs.compare(SLIM, FULL + "[GIT.4] New git rule.\n")
    assert probs == ["id [GIT.4] in full only (add it to the slim rulebook)"]


def test_duplicate_id_is_caught():
    assert rs.compare(SLIM + "[R3] again\n", FULL + "") == ["slim: id [R3] tagged 2 times"]


def test_wording_edit_inside_existing_id_not_blocked():
    reworded = SLIM.replace("Era-matched corpus.", "Check the judge corpus era and register; build one if needed.")
    assert rs.compare(reworded, FULL.replace("Long story.", "")) == []


def test_non_id_brackets_ignored():
    extra = "Placeholders [SIGN-OFF], [SO-<label>], [retired], [ ], [SENT-<id>], [x] are not ids.\n"
    assert rs.compare(SLIM + extra, FULL) == []


def test_main_exit_codes(tmp_path):
    s, f = tmp_path / "s.md", tmp_path / "f.md"
    s.write_text(SLIM)
    f.write_text(FULL)
    assert rs.main(["--slim", str(s), "--full", str(f)]) == 0
    s.write_text(SLIM + "[PIPE.8] new\n")
    assert rs.main(["--slim", str(s), "--full", str(f)]) == 1
    assert rs.main(["--slim", str(tmp_path / "nope.md"), "--full", str(f)]) == 2
