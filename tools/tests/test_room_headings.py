#!/usr/bin/env python3
"""Offline test for tools/room.py's STATUS.md/QUEUE.md section-heading guard (25 Sept 2026, LEDGER.md:810,
LANE B3: "STATUS.md sections can be dropped by another session's room.py --push merge"). No network, no push:
room.headings() and room.headings_ok() are pure functions checked directly against temp files.
Run: python3 tools/tests/test_room_headings.py"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402

BEFORE = """# STATUS

## Parent handoff
some text

## Lane structure
a table

## LANE B3 handoff
notes
"""

AFTER_INTACT = """# STATUS

## Parent handoff
some text, edited by another session

## Lane structure
a table, also edited

## LANE B3 handoff
notes

## LANE B4 handoff
a new section, added by someone else
"""

AFTER_DROPPED = """# STATUS

## Parent handoff
some text

## LANE B3 handoff
notes
"""

fails = 0

with tempfile.TemporaryDirectory() as d:
    status = os.path.join(d, "STATUS.md")
    queue = os.path.join(d, "QUEUE.md")
    missing = os.path.join(d, "no-such-file.md")

    # headings() on a nonexistent file returns None, not an error
    if room.headings(missing) is not None:
        print("FAIL: headings() of a nonexistent file should be None")
        fails += 1

    open(status, "w").write(BEFORE)
    before = {status: room.headings(status), queue: room.headings(queue)}

    # queue.md never existed -> its None snapshot must never block a push
    if before[queue] is not None:
        print("FAIL: headings() of a missing QUEUE.md should be None")
        fails += 1

    # a rebase that adds sections and edits body text, dropping none, is fine
    open(status, "w").write(AFTER_INTACT)
    bad = room.headings_ok(before)
    if bad is not None:
        print(f"FAIL: expected no complaint when no heading vanished, got: {bad}")
        fails += 1

    # a rebase that drops a '## Lane structure' section must be refused, naming it
    open(status, "w").write(AFTER_DROPPED)
    bad = room.headings_ok(before)
    if bad is None:
        print("FAIL: expected a refusal when a heading vanished")
        fails += 1
    elif "Lane structure" not in bad:
        print(f"FAIL: refusal did not name the lost section: {bad}")
        fails += 1

    # the file disappearing entirely is also refused, distinctly
    os.remove(status)
    bad = room.headings_ok(before)
    if bad is None or "disappeared" not in bad:
        print(f"FAIL: expected a 'disappeared' refusal, got: {bad}")
        fails += 1

    # a path with no headings before the rebase (None in the snapshot) is never checked
    empty_before = {status: None}
    open(status, "w").write("no headings here at all\n")
    bad = room.headings_ok(empty_before)
    if bad is not None:
        print(f"FAIL: a None before-snapshot must never block a push, got: {bad}")
        fails += 1

    # a34cd00-shaped failure (25-26 Sept 2026, RETRO-2026-09-26a): the session's own local edit drops a
    # heading before any commit or rebase happens at all, not during one. The "before" snapshot here stands
    # in for origin/main (a separate pristine copy, not the working file after the drop); the working file is
    # written straight to AFTER_DROPPED with no intervening AFTER_INTACT/rebase step. push()'s fix reads this
    # snapshot from origin/main via headings_from_ref() rather than from the local file post-commit; this test
    # exercises headings_ok() with an origin-shaped "before" to confirm it still flags the drop when a local
    # edit, not a merge, is what removed the heading.
    pristine_before_path = os.path.join(d, "origin-STATUS.md")
    open(pristine_before_path, "w").write(BEFORE)
    origin_shaped_before = {status: room.headings(pristine_before_path), queue: None}
    open(status, "w").write(AFTER_DROPPED)
    bad = room.headings_ok(origin_shaped_before)
    if bad is None:
        print("FAIL: expected a refusal when a local pre-commit edit dropped a heading")
        fails += 1
    elif "Lane structure" not in bad:
        print(f"FAIL: refusal did not name the lost section: {bad}")
        fails += 1

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: room.py headings()/headings_ok() catch a dropped STATUS.md section, offline")
