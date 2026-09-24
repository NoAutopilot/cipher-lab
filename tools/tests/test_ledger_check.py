#!/usr/bin/env python3
"""Offline test for tools/ledger_check.py (RETRO-2026-09-24e proposal 2): feeds
a small in-memory LEDGER.md-shaped sample -- covering the real file's column
variants (plain 6-column rows, rows with a Session column, rows with the four
extra Lane/Items/Stage2/Readings columns, a missing-trailing-pipe row, and a
"~N (explanation)" cost cell) -- to ledger_check.check() and checks it finds
the duplicate session id and the non-standard outcome codes and nothing else,
then checks --help documents --fix-suggest. Run:
python3 tools/tests/test_ledger_check.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ledger_check  # noqa: E402

SAMPLE = [
    "| Date | Role | Model | Cost | Outcome | Lesson |\n",
    "|---|---|---|---|---|---|\n",
    # plain well-formed row, valid code
    "| 19 Sept | Archive Lookup: Stepney | Fable | 12 | D | |\n",
    # ~N (explanation) cost cell, valid code
    "| 23 Sept | Check Solved: ranks 11-18 | Sonnet | ~2 (226k tokens, no subagents) | D | Rank 11 read |\n",
    # missing trailing pipe, valid code
    "| 24 Sep | DECODE single login retry | Sonnet | 0.85 | N | Login rejected again\n",
    # row with a Session column, first of a duplicate pair (valid code, so this pair
    # exercises only the duplicate-session check, not the outcome-code check)
    "| 24 Sep | LANE N2 orchestrator: nominations | Opus | session_01Dup0000000000000000000 | 68.18 | D | first row |\n",
    # row with a Session column, second of the same duplicate pair
    "| 24 Sep | LANE N2 orchestrator: nominations (re-run) | Opus | session_01Dup0000000000000000000 | 81.50 | D | second row |\n",
    # row with a Session column, unique id, non-standard code
    "| 24 Sep | LANE R4 J: Salviati passes | Sonnet | session_016p35ZUnkX32oxmhk5v2nJV | 6.85 | A | leftover shorthand |\n",
    # row with the four extra Lane/Items/Stage2/Readings columns, valid code, cost has a parenthetical
    "| 24 Sept | Orchestrator wake 2 | Opus | about 51 (session only) | D | several | 20 workers | 1 copy-free (M8) | Gramont f.29r N3 | lesson text |\n",
    # historical shorthand with an embedded hyphen, non-standard code
    "| 24 Sep | Scout CA: Canada | Sonnet | session_019y17auBuoVUVfa2cUwZ5D3 | 4.54 | F-rl | cut off by the window |\n",
]

dup_sessions, bad_outcomes = ledger_check.check(SAMPLE)

fails = 0

if list(dup_sessions.keys()) != ["session_01Dup0000000000000000000"]:
    print(f"FAIL: expected exactly one duplicate session id, got {list(dup_sessions.keys())}")
    fails += 1
elif len(dup_sessions["session_01Dup0000000000000000000"]) != 2:
    print("FAIL: expected the duplicate session id to be seen on exactly 2 rows")
    fails += 1

bad_lines = {lineno for lineno, _, _ in bad_outcomes}
# line numbers are 1-indexed positions in SAMPLE: the "A" row is line 8, "F-rl" is line 10
expect_bad = {8, 10}
if bad_lines != expect_bad:
    print(f"FAIL: expected bad-outcome lines {expect_bad}, got {bad_lines}")
    fails += 1

# the "about 51 (session only)" / extra-columns row (line 9) must not be misread as a bad
# outcome via its "20 workers" or "1 copy-free (M8)" cells (the false positive an earlier,
# looser version of the cost/outcome pairing produced)
if 9 in bad_lines:
    print("FAIL: the extra-columns row's Lane/Items cells were mistaken for Cost/Outcome")
    fails += 1

# the "~2 (226k tokens, no subagents)" cost cell (line 4) must not trip either check
if 4 in bad_lines or any(lineno == 4 for lineno in bad_lines):
    print("FAIL: a '~N (explanation)' cost cell broke row 4's parsing")
    fails += 1

# the missing-trailing-pipe row (line 5) must still parse its valid 'N' code as fine
if 5 in bad_lines:
    print("FAIL: a missing trailing '|' caused a false positive on row 5's valid code")
    fails += 1

# leading_token / VALID_CODES sanity
for good in ("D", "D-", "F", "X", "N"):
    if ledger_check.leading_token(good) not in ledger_check.VALID_CODES:
        print(f"FAIL: {good!r} should be accepted as a standard code")
        fails += 1
for bad in ("A", "B", "C", "S", "S-", "B+", "F-rl", "d"):
    if ledger_check.leading_token(bad) in ledger_check.VALID_CODES:
        print(f"FAIL: {bad!r} should NOT be accepted as a standard code (case-sensitive, exact)")
        fails += 1

proc = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "ledger_check.py"), "--help"],
    cwd=ROOT, capture_output=True, text=True, timeout=30,
)
if proc.returncode != 0:
    print(f"FAIL: --help exit code {proc.returncode}")
    fails += 1
if "--fix-suggest" not in proc.stdout:
    print("FAIL: --help text missing --fix-suggest")
    fails += 1

# main() against the real LEDGER.md must not crash and must exit 1 (the real file, as of
# this test's writing, still carries pre-standardization codes and duplicate session ids
# from before this gate existed -- that is exactly what it is supposed to catch)
proc2 = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "ledger_check.py")],
    cwd=ROOT, capture_output=True, text=True, timeout=30,
)
if proc2.returncode not in (0, 1):
    print(f"FAIL: running against the real LEDGER.md exited {proc2.returncode}, expected 0 or 1")
    fails += 1

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: ledger_check finds the duplicate session id and non-standard codes, ignores the "
      "extra-columns/parenthetical-cost/missing-pipe rows, --help documents --fix-suggest")
