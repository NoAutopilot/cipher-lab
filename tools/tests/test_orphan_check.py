#!/usr/bin/env python3
"""Offline test for tools/orphan_check.py (worker ORPHAN-TOOL, 26 Sept 2026).

Builds small in-memory sessions/triggers JSON (both plain and envelope-wrapped, e.g. {"data": [...]}
or {"ccr": {"sessions": [...]}}), a ROOM.md excerpt and an ASSIGNMENTS.md excerpt under tmp_path, and
covers each of the five checks plus the clean case. No network, no dependence on the real repository's
current ROOM.md/hub-seed state.

Run: /root/.local/bin/pytest tools/tests/test_orphan_check.py -q
"""
import datetime
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import orphan_check as oc  # noqa: E402

NOW = datetime.datetime(2026, 9, 26, 5, 0)


def write_json(path, obj):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f)


def write_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


ASSIGNMENTS_HEADER = "| # | Raised | Project | Job | For | Brief | Status |\n|---|---|---|---|---|---|---|\n"


def test_unwrap_list_handles_plain_wrapped_and_envelope_shapes():
    assert oc.unwrap_list([{"id": "x"}]) == [{"id": "x"}]
    assert oc.unwrap_list({"data": [{"id": "x"}]}) == [{"id": "x"}]
    assert oc.unwrap_list({"sessions": [{"id": "x"}]}) == [{"id": "x"}]
    assert oc.unwrap_list({"ccr": {"sessions": [{"id": "x"}]}}) == [{"id": "x"}]
    assert oc.unwrap_list({"nothing": "here"}) == []


def test_clean_case_no_problems(tmp_path):
    sessions = [
        {"id": "session_LIVE1", "archived": False, "parent_session_id": "session_PARENTLIVE",
         "updated_at": "2026-09-26T04:55:00Z", "title": "LIVE worker A"},
        {"id": "session_PARENTLIVE", "archived": False, "parent_session_id": None,
         "updated_at": "2026-09-26T04:58:00Z", "title": "LIVE parent 7f"},
    ]
    triggers = [{"id": "trig1", "enabled": True, "persistent_session_id": "session_PARENTLIVE"}]
    write_json(tmp_path / "sessions.json", sessions)
    write_json(tmp_path / "triggers.json", triggers)
    write_text(tmp_path / "ROOM.md", "2026-09-26 04:59 | parent 7f (session_PARENTLIVE) | check-in: all clean\n")
    write_text(tmp_path / "ASSIGNMENTS.md", ASSIGNMENTS_HEADER)

    room_lines = oc.parse_room_lines(str(tmp_path / "ROOM.md"))
    rows = oc.parse_assignments_rows(str(tmp_path / "ASSIGNMENTS.md"))
    a, b, c, d, e, f = oc.run_all(sessions, triggers, room_lines, "", rows, NOW)
    assert (a, b, c, d, e, f) == ([], [], [], [], [], [])


def test_orphan_session_flagged_unless_adopted(tmp_path):
    # session_ORPHAN1's parent is archived, and it is named nowhere recent -- orphan.
    sessions = [
        {"id": "session_ORPHAN1", "archived": False, "parent_session_id": "session_DEADPARENT"},
        {"id": "session_DEADPARENT", "archived": True},
    ]
    room_lines = [{"ts": "2026-09-26 04:00", "ts_dt": datetime.datetime(2026, 9, 26, 4, 0),
                   "actor": "x", "signal": "irrelevant", "raw": "irrelevant line, no session id"}]
    a, *_ = oc.run_all(sessions, [], room_lines, "", [], NOW)
    assert len(a) == 1 and "session_ORPHAN1" in a[0]

    # Same shape, but named in the last 6 hours of ROOM.md -- adopted, not an orphan.
    room_lines2 = [{"ts": "2026-09-26 04:00", "ts_dt": datetime.datetime(2026, 9, 26, 4, 0),
                    "actor": "x", "signal": "adopt", "raw": "adopting session_ORPHAN1 into LANE B7"}]
    a2, *_ = oc.run_all(sessions, [], room_lines2, "", [], NOW)
    assert a2 == []

    # Same shape, but named in an ASSIGNMENTS.md row -- also adopted.
    a3, *_ = oc.run_all(sessions, [], room_lines, "row about session_ORPHAN1 somewhere", [], NOW)
    assert a3 == []


def test_stale_session_needs_a_done_line(tmp_path):
    sessions = [{"id": "session_STALE1", "archived": False, "updated_at": "2026-09-26T01:00:00Z", "title": "bWORKER"}]
    no_done = [{"ts": "2026-09-26 04:00", "ts_dt": datetime.datetime(2026, 9, 26, 4, 0),
                "actor": "x", "signal": "flag", "raw": "flag: nothing about that worker"}]
    _, b, *_ = oc.run_all(sessions, [], no_done, "", [], NOW)
    assert len(b) == 1 and "session_STALE1" in b[0]

    with_done = [{"ts": "2026-09-26 04:00", "ts_dt": datetime.datetime(2026, 9, 26, 4, 0),
                  "actor": "x", "signal": "done", "raw": "done: session_STALE1 finished its job"}]
    _, b2, *_ = oc.run_all(sessions, [], with_done, "", [], NOW)
    assert b2 == []


def test_orphan_trigger_archived_or_missing_session():
    sessions = [{"id": "session_ARCHIVED", "archived": True}]
    triggers = [
        {"id": "trig_a", "enabled": True, "persistent_session_id": "session_ARCHIVED"},
        {"id": "trig_b", "enabled": True, "persistent_session_id": "session_MISSING"},
        {"id": "trig_c", "enabled": False, "persistent_session_id": "session_ARCHIVED"},
    ]
    *_, c, _, _ = (oc.check_orphan_sessions([], [], "", NOW), oc.check_stale_sessions([], [], NOW),
                   oc.check_orphan_triggers(triggers, sessions), [], [])
    ids = [p for p in c]
    assert any("trig_a" in p for p in ids)
    assert any("trig_b" in p for p in ids)
    assert not any("trig_c" in p for p in ids)  # disabled trigger is never flagged


def test_stale_claim_needs_a_later_done_or_handoff_from_the_same_actor():
    old_claim = {"ts": "2026-09-25 22:00", "ts_dt": datetime.datetime(2026, 9, 25, 22, 0),
                 "actor": "bWORKER", "signal": "claim: target-x", "raw": "line"}
    unresolved = [old_claim]
    d = oc.check_stale_claims(unresolved, NOW)
    assert len(d) == 1 and "bWORKER" in d[0]

    later_done = {"ts": "2026-09-25 23:00", "ts_dt": datetime.datetime(2026, 9, 25, 23, 0),
                  "actor": "bWORKER", "signal": "done: target-x finished", "raw": "line2"}
    resolved = [old_claim, later_done]
    d2 = oc.check_stale_claims(resolved, NOW)
    assert d2 == []

    # A claim under 6 hours old is never stale, done line or not.
    recent_claim = {"ts": "2026-09-26 04:00", "ts_dt": datetime.datetime(2026, 9, 26, 4, 0),
                    "actor": "bWORKER2", "signal": "claim: target-y", "raw": "line3"}
    d3 = oc.check_stale_claims([recent_claim], NOW)
    assert d3 == []


def test_unledgered_close(tmp_path):
    sessions = [{"id": "session_CLOSED1", "archived": True}]
    open_row = {"raw": "| 5 | 26 Sept | cipher-lab | some job | any | brief.md | claimed by session_CLOSED1 |",
                "status": "claimed by session_CLOSED1"}
    done_row = {"raw": "| 6 | 26 Sept | cipher-lab | some job | any | brief.md | done, session_CLOSED1 pushed abc123 |",
                "status": "done, session_CLOSED1 pushed abc123"}
    e = oc.check_unledgered_closes([open_row], sessions)
    assert len(e) == 1 and "session_CLOSED1" in e[0]
    e2 = oc.check_unledgered_closes([done_row], sessions)
    assert e2 == []


def test_title_mismatch_live_and_archived(tmp_path):
    sessions = [
        {"id": "session_OK1", "archived": False, "title": "LIVE parent 7f"},
        {"id": "session_BAD1", "archived": False, "title": "parent 7f (no LIVE prefix)"},
        {"id": "session_OK2", "archived": True, "title": "ARCHIVED parent 7e (handed over 04:48)"},
        {"id": "session_BAD2", "archived": True, "title": "parent 7e"},
    ]
    f = oc.check_title_mismatch(sessions)
    assert len(f) == 2
    assert any("session_BAD1" in p for p in f)
    assert any("session_BAD2" in p for p in f)
    assert not any("session_OK1" in p for p in f)
    assert not any("session_OK2" in p for p in f)


def test_parse_room_lines_and_assignments_rows(tmp_path):
    room_path = tmp_path / "ROOM.md"
    write_text(str(room_path), (
        "2026-09-26 04:13 | parent (owner account) | check-in: rate allowed everywhere\n"
        "\n"
        "not a room line at all, no pipes\n"
        "2026-09-26 04:14 | bUNT8 (LANE B6 worker, Sonnet) | done: untersberg-code reconciled\n"
    ))
    lines = oc.parse_room_lines(str(room_path))
    assert len(lines) == 2
    assert lines[0]["actor"] == "parent (owner account)"
    assert lines[0]["ts_dt"] == datetime.datetime(2026, 9, 26, 4, 13)
    assert lines[1]["signal"].startswith("done:")

    assignments_path = tmp_path / "ASSIGNMENTS.md"
    write_text(str(assignments_path), ASSIGNMENTS_HEADER + "| 1 | 21 Sept | cipher-lab | a job | any | brief.md | open |\n")
    rows = oc.parse_assignments_rows(str(assignments_path))
    assert len(rows) == 1
    assert rows[0]["status"] == "open"


def test_main_exit_codes_via_cli(tmp_path, capsys):
    import subprocess
    sessions_path = tmp_path / "sessions.json"
    triggers_path = tmp_path / "triggers.json"
    room_path = tmp_path / "ROOM.md"
    assignments_path = tmp_path / "ASSIGNMENTS.md"
    write_json(str(sessions_path), [])
    write_json(str(triggers_path), [])
    write_text(str(room_path), "2026-09-26 04:59 | someone | check-in: clean\n")
    write_text(str(assignments_path), ASSIGNMENTS_HEADER)

    r = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "orphan_check.py"),
         "--sessions", str(sessions_path), "--triggers", str(triggers_path),
         "--room-file", str(room_path), "--assignments", str(assignments_path),
         "--now", "2026-09-26 05:00"],
        capture_output=True, text=True,
    )
    assert r.returncode == 0
    assert "orphans: 0 sessions, 0 triggers, 0 claims, 0 unledgered" in r.stdout

    r2 = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "orphan_check.py")],
        capture_output=True, text=True,
    )
    assert r2.returncode != 0  # missing --sessions/--triggers and no --no-sessions

    r3 = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "orphan_check.py"), "--no-sessions",
         "--room-file", str(room_path), "--assignments", str(assignments_path),
         "--now", "2026-09-26 05:00"],
        capture_output=True, text=True,
    )
    assert r3.returncode == 0
    assert "orphans: 0 sessions, 0 triggers, 0 claims, 0 unledgered" in r3.stdout


if __name__ == "__main__":
    import subprocess
    sys.exit(subprocess.call([sys.executable, "-m", "pytest", __file__, "-q"]))
