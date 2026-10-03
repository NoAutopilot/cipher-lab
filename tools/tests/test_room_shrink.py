#!/usr/bin/env python3
"""Offline test for tools/room.py's shrink guard (26 Sept 2026, RETRO-2026-09-26i item 1, PR-LAND-3: a
plain `git commit` outside room.py replaced LOCAL-QUEUE.tsv and a completed verifier AUDIT.md with the
single word "PLACEHOLDER" each, with zero ROOM.md trace). room.shrink_ok() is a pure function (given a
before-sizes dict and an explicit message) checked directly against temp files -- no network, no push.
Run: python3 tools/tests/test_room_shrink.py"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402

fails = 0


def report(name, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), name, detail)


TSV_26 = "\n".join(f"row{i}\tval{i}" for i in range(26)) + "\n"
PLACEHOLDER = "PLACEHOLDER\n"
TSV_24 = "\n".join(f"row{i}\tval{i}" for i in range(24)) + "\n"

with tempfile.TemporaryDirectory() as d:
    lq = os.path.join(d, "LOCAL-QUEUE.tsv")
    missing = os.path.join(d, "no-such-file.md")

    # a path with no before-snapshot (None, e.g. a brand-new file) never blocks a push
    open(lq, "w").write(PLACEHOLDER)
    bad = room.shrink_ok({lq: None}, message="ROOM: some update")
    report("None before-snapshot never blocks", bad is None, bad)

    # 26 -> 1 (PLACEHOLDER), ordinary message -> refused, naming the path and both counts
    bad = room.shrink_ok({lq: 26}, message="PR-LAND-3: land JSTOR hits into LOCAL-QUEUE.tsv")
    report("26 -> 1 line collapse is refused", bad is not None, bad)
    if bad:
        report("refusal names the path", "LOCAL-QUEUE.tsv" in bad, bad)
        report("refusal names both counts", "26" in bad and "1" in bad, bad)

    # same collapse, but the commit message is exempt -> no refusal
    bad = room.shrink_ok({lq: 26}, message="AX2-SHRINK: intentional placeholder for a follow-up regen")
    report("an exempt commit message clears the collapse", bad is None, bad)

    # a legitimate 26 -> 24 edit -> no refusal, regardless of message
    open(lq, "w").write(TSV_24)
    bad = room.shrink_ok({lq: 26}, message="ROOM: trimmed two stale rows")
    report("a legitimate row-count edit is not refused", bad is None, bad)

    # a path that vanished from the working tree entirely is skipped (not this guard's job -- headings_ok
    # or the caller's own missing-file handling covers a deleted shared file)
    bad = room.shrink_ok({missing: 26}, message="ROOM: some update")
    report("a path absent from the working tree is skipped, not refused", bad is None, bad)

# binary snapshots (3 Oct 2026, TOOL-FSG-JPEG): line_count_from_ref() now returns bytes, and a JPEG in a
# --push used to crash the text read with UnicodeDecodeError
JPEG = b"\xff\xd8\xff\xe0" + bytes(range(256)) * 400 + b"\xff\xd9"
with tempfile.TemporaryDirectory() as d:
    jp = os.path.join(d, "f.jpg")
    open(jp, "wb").write(JPEG)
    bad = room.shrink_ok({jp: JPEG}, message="ROOM: images")
    report("an unchanged JPEG pushes (no crash, no refusal)", bad is None, bad)
    open(jp, "wb").write(JPEG[:6000])
    bad = room.shrink_ok({jp: JPEG}, message="ROOM: images")
    report("a JPEG shrunk but above 1 KB is not refused", bad is None, bad)
    open(jp, "w").write(PLACEHOLDER)
    bad = room.shrink_ok({jp: JPEG}, message="ROOM: images")
    report("a JPEG replaced by PLACEHOLDER is refused", bad is not None and "bytes" in bad, bad)
    tq = os.path.join(d, "q.tsv")
    open(tq, "w").write(PLACEHOLDER)
    bad = room.shrink_ok({tq: TSV_26.encode()}, message="ROOM: x")
    report("a bytes snapshot of a text file keeps the line rule", bad is not None and "lines" in bad, bad)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: room.py shrink_ok() catches the PR-LAND-3 collapse shape, passes a legitimate edit, and honors "
      "the shrink/regen/restore/AX2-SHRINK commit-message exemption, offline")
