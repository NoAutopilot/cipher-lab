#!/usr/bin/env python3
"""Offline test for tools/room.py --digest (RETRO-2026-09-24d, subject 3): no
network, no push. Feeds a small in-memory ROOM.md-shaped sample to
room.filter_lines() and checks the since-timestamp and signal-keyword filter,
then checks --help documents --digest without touching ROOM.md on disk.
Run: python3 tools/tests/test_room_digest.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import room  # noqa: E402

SAMPLE = [
    "2026-09-24 08:00 | LANE R worker R6 (Sonnet) | claim: target-a -- files: ciphers/target-a/NOTES.md\n",
    "2026-09-24 08:05 | LANE R worker R6 (Sonnet) | note: reading progress, nothing decided yet\n",
    "2026-09-24 08:10 | LANE R worker R6 (Sonnet) | flag: cap looks tight, 80 percent spent\n",
    "2026-09-24 08:15 | LANE R worker R6 (Sonnet) | done: for LANE V: target-a reading ready, grade H\n",
    "2026-09-24 08:20 | LANE N orchestrator | nomination: ciphers/target-b | copy-order | kind recovery\n",
    "2026-09-24 08:25 | Orchestrator | note: window status allowed_warning, pausing new spawns\n",
    "2026-09-24 08:30 | VERIFIER V1 (Opus) | done: target-c classified N3, safe sentence in AUDIT.md\n",
    "2026-09-24 08:35 | LANE N2 orchestrator | note: window status rejected, resets 09:00\n",
    "2026-09-24 07:55 | LANE R worker R5 (Sonnet) | done: target-z reading ready (before the window)\n",
    "not a room line at all, malformed\n",
    "\n",
]

fails = 0

kept = room.filter_lines(SAMPLE, "2026-09-24 08:00")
kept_texts = [l.split(" | ", 2)[2] for l in kept]

# since-filter: the 07:55 line (before the window) must never appear, even though it says "done:"
if any("target-z" in t for t in kept_texts):
    print("FAIL: since filter let through a line before SINCE")
    fails += 1

# each of the documented signal kinds should be kept (note: claim: is deliberately not one of
# them -- the spec's keyword list is nomination:/for LANE/flag:/done:/handoff/retract plus
# contains allowed_warning/rejected/a bare N0-N5 token)
expect_present = ["flag:", "done:", "nomination:", "N3", "rejected"]
for tok in expect_present:
    if not any(tok in t for t in kept_texts):
        print(f"FAIL: expected a kept line containing {tok!r}, none found")
        fails += 1

# claim: is not a digest keyword on its own -- a claim line with no other signal is dropped
if any(t.startswith("claim:") for t in kept_texts):
    print("FAIL: a bare claim: line was kept, but claim: is not a documented digest keyword")
    fails += 1

# a bare "note:" line with no keyword, no class token, no allowed_warning/rejected must be dropped
if any(t.startswith("note: reading progress") for t in kept_texts):
    print("FAIL: a plain note: line with no digest keyword was kept")
    fails += 1

# allowed_warning is a *contains* match, not a startswith one, and must be kept
if not any("allowed_warning" in t for t in kept_texts):
    print("FAIL: a line containing allowed_warning was not kept")
    fails += 1

# malformed / blank lines must not raise and must not appear
if len(kept) != 6:
    print(f"FAIL: expected 6 kept lines, got {len(kept)}: {kept_texts}")
    fails += 1

# a SINCE that excludes everything returns an empty list, not an error
none_kept = room.filter_lines(SAMPLE, "2026-09-25 00:00")
if none_kept:
    print(f"FAIL: expected no lines for a future SINCE, got {len(none_kept)}")
    fails += 1

proc = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "room.py"), "--help"],
    cwd=ROOT, capture_output=True, text=True, timeout=30,
)
if proc.returncode != 0:
    print(f"FAIL: --help exit code {proc.returncode}")
    fails += 1
if "--digest" not in proc.stdout:
    print("FAIL: --help text missing --digest")
    fails += 1

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: room.py --digest filters by SINCE and signal keyword, --help documents it, offline")
