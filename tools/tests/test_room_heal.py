#!/usr/bin/env python3
"""Offline test for tools/room.py's ROOM.md self-heal (27 Sept 2026, after an outside agent -- Codex, which
does not go through this script -- replaced ROOM.md outright at 14:48 UTC that day; the existing stub guard
correctly refused to build on it, but every worker that hit the guard just parked waiting for a person until
another worker restored the file by hand). heal_stub_content() is a pure function checked directly against a
real temp git repo (git log/git show, no network, no push).

Covers: (1) a 200-line seed, a stub commit, two appends on the stub -> the candidate is the seed commit and
the healed text is the 200 seed lines followed by the stub's own line (still real content, just misplaced)
and the two appended lines, all in commit order; (2) when nothing in the sampled history clears the stub floor
(every commit is itself stub-sized), heal_stub_content() returns None rather than "restoring" one stub from
another.

Run: python3 tools/tests/test_room_heal.py"""
import os
import subprocess
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


def git(root, *args):
    return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True)


SEED_LINES = [f"2026-09-27 12:{i:02d} | worker {i} | did thing {i}" for i in range(200)]
SEED_TEXT = "\n".join(SEED_LINES) + "\n"
STUB_TEXT = "2026-09-27 14:48 | Codex ARM-REATTACK | claim: owner-directed investigation\n"

with tempfile.TemporaryDirectory() as d:
    git(d, "init", "-q")
    git(d, "config", "user.email", "test@example.com")
    git(d, "config", "user.name", "test")

    path = os.path.join(d, "ROOM.md")

    # seed: a real 200-line room
    open(path, "w").write(SEED_TEXT)
    git(d, "add", "ROOM.md")
    git(d, "commit", "-q", "-m", "seed: 200-line room")
    seed_sha = git(d, "rev-parse", "--short", "HEAD").stdout.strip()

    # wipe: an outside agent replaces the whole file with a 1-line stub
    open(path, "w").write(STUB_TEXT)
    git(d, "add", "ROOM.md")
    git(d, "commit", "-q", "-m", "wipe: outside agent replaced ROOM.md")

    # two appends land on the stub, as room.py's own append-only writes would
    append1 = STUB_TEXT + "2026-09-27 14:53 | LANE VO2 | claim: waiting, ROOM.md looks empty\n"
    open(path, "w").write(append1)
    git(d, "add", "ROOM.md")
    git(d, "commit", "-q", "-m", "append 1 after stub")

    append2 = append1 + "2026-09-27 15:02 | LANE VO2 | flag: still waiting, no reading arrived\n"
    open(path, "w").write(append2)
    git(d, "add", "ROOM.md")
    git(d, "commit", "-q", "-m", "append 2 after stub")

    result = room.heal_stub_content(root=d, ref="HEAD")
    report("heal_stub_content() finds a candidate", result is not None, result)

    if result:
        healed_text, candidate, restored_n, appended_n = result
        report("candidate is the seed commit", candidate == seed_sha, (candidate, seed_sha))
        report("restored_n is 200", restored_n == 200, restored_n)
        # the wipe commit's own stub line is real (if misplaced) content, so it counts as one of the
        # "later" lines too: stub's own claim line, plus the two appends made on top of the stub = 3.
        report("appended_n is 3 (the stub's own line + its two appends)", appended_n == 3, appended_n)

        healed_lines = healed_text.splitlines()
        report("healed text is 200 + 3 = 203 lines", len(healed_lines) == 203, len(healed_lines))
        report("first 200 lines are the seed content, in order", healed_lines[:200] == SEED_LINES,
               healed_lines[:5])
        report("line 201 is the stub's own line, not dropped", "Codex ARM-REATTACK" in healed_lines[200],
               healed_lines[200])
        report("line 202 is the first append", "LANE VO2 | claim" in healed_lines[201], healed_lines[201])
        report("line 203 is the second append", "LANE VO2 | flag" in healed_lines[202], healed_lines[202])
        report("healed text ends with a trailing newline", healed_text.endswith("\n"), repr(healed_text[-5:]))

    # a second temp repo where every commit touching ROOM.md is stub-sized: nothing safe to restore from
    with tempfile.TemporaryDirectory() as d2:
        git(d2, "init", "-q")
        git(d2, "config", "user.email", "test@example.com")
        git(d2, "config", "user.name", "test")
        path2 = os.path.join(d2, "ROOM.md")
        open(path2, "w").write("one line\n")
        git(d2, "add", "ROOM.md")
        git(d2, "commit", "-q", "-m", "seed: a 1-line room, never grew")

        result2 = room.heal_stub_content(root=d2, ref="HEAD")
        report("no candidate clearing the stub floor -> None, not a false restore", result2 is None, result2)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: room.py heal_stub_content() rebuilds a wiped ROOM.md from git history (seed + appends since, in "
      "order) and returns None rather than restoring one stub from another, offline")
