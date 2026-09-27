#!/usr/bin/env python3
"""Offline test for tools/ledger_check.py's --split mode (RETRO-2026-09-27x P5) and the always-on
shifted-outcome check. Builds a small in-memory LEDGER.md-shaped sample with: a solving row, an
acquisition row, a validation row, two parent self-ledger rows bracketing them (one under, one over
the one-third line), an unmatched row, a [bucket:V] override, and the row-1184 shifted-outcome shape
(placeholder cost, resolved number in Outcome, the real code stranded in Lesson).
Run: python3 tools/tests/test_ledger_check_split.py"""
import contextlib
import io
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ledger_check  # noqa: E402

SAMPLE = [
    "| Date | Role | Model | Session | Cost | Outcome | Lesson |\n",
    "|---|---|---|---|---|---|---|\n",
    # parent 1's tenure starts here
    "| 27 Sep | Transcription: known-plaintext key re-derivation | Sonnet | session_01AAAA | 5.0 | D | S bucket |\n",
    "| 27 Sep | Scout: intake fetch of a folio image | Sonnet | session_01BBBB | 3.0 | D | A bucket |\n",
    "| 27 Sep | Verifier: check-solved audit | Sonnet | session_01CCCC | 2.0 | D | V bucket |\n",
    "| 27 Sep | Something with no matching keyword at all | Sonnet | session_01DDDD | 1.0 | D | unmatched |\n",
    "| 27 Sep | A row tagged by hand [bucket:V] | Sonnet | session_01EEEE | 4.0 | D | override |\n",
    "| 27 Sep | parent 7x (Orchestrator 1): hand-over | Fable | session_01PARENT1 | 4.0 | D | own cost 4.0 vs workers 15.0 |\n",
    # parent 2's tenure: one row, small worker spend relative to its own cost -> over a third
    "| 27 Sep | Scout: intake fetch of another folio image | Sonnet | session_01FFFF | 1.0 | D | A bucket 2 |\n",
    "| 27 Sep | parent 7y (Orchestrator 2): hand-over | Fable | session_01PARENT2 | 5.0 | D | own cost 5.0 vs workers 1.0 |\n",
    # the row-1184 shifted-outcome shape: placeholder cost, resolved number as Outcome, real code
    # stranded at the start of what should be the Lesson cell
    "| 27 Sep | Solver: shifted-outcome fixture row | Sonnet | session_01GGGG | parent's get_session | "
    "5.70 (parent get_session at archive) | D (1.1x cap 5; some lesson text) |\n",
]

fails = 0


def fail(msg):
    global fails
    print(f"FAIL: {msg}")
    fails += 1


# --- bucket classification ---
rules = ledger_check.load_effort_roles()
checks = {
    "Transcription: known-plaintext key re-derivation": "S",
    "Scout: intake fetch of a folio image": "A",
    "Verifier: check-solved audit": "V",
    "Something with no matching keyword at all": None,
    "A row tagged by hand [bucket:V]": "V",
    "parent 7x (Orchestrator 1): hand-over": "C",
}
for role, expected in checks.items():
    got = ledger_check.classify_bucket(role, rules)
    if got != expected:
        fail(f"classify_bucket({role!r}) = {got!r}, expected {expected!r}")

# --- shifted-outcome check: only the fixture row, not the well-formed ones ---
shifted = ledger_check.find_shifted_outcome_rows(SAMPLE)
shifted_lines = {lineno for lineno, _, _ in shifted}
if shifted_lines != {11}:
    fail(f"find_shifted_outcome_rows found lines {shifted_lines}, expected {{11}} (0-indexed SAMPLE, 1-based lineno)")

# --- --split output, via the module's own print_split (captured) ---
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ledger_check.print_split(SAMPLE, 1)
out = buf.getvalue()

if "S (Solving" not in out or "A (Acquisition" not in out or "V (Validation" not in out or "C (Coordination" not in out:
    fail(f"--split output missing a bucket header: {out}")
if "Something with no matching keyword at all" not in out:
    fail("--split output did not list the unmatched row")
if "own 4.00 vs workers 15.00" not in out.replace("15.0 ", "15.00 ") and "workers 15.00" not in out:
    fail(f"--split output did not compute parent 7x's tenure worker spend correctly: {out}")
if "own 5.00 vs workers 1.00" not in out and "workers 1.00" not in out:
    fail(f"--split output did not compute parent 7y's tenure worker spend correctly: {out}")
if "OVER A THIRD" not in out:
    fail(f"--split output did not flag parent 7y as over a third: {out}")

help_r = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "ledger_check.py"), "--help"],
    capture_output=True, text=True, timeout=30,
)
if help_r.returncode != 0 or "--split" not in help_r.stdout:
    fail(f"--help failed or missing --split: rc={help_r.returncode}")

# --split against the real LEDGER.md must not crash (the placeholder rows RETRO-2026-09-27x P5 named
# are already fixed, so this must find no shifted-outcome rows for lines 1158+)
proc = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "ledger_check.py"), "--split", "1158"],
    cwd=ROOT, capture_output=True, text=True, timeout=30,
)
if "line 1184" in proc.stdout or "line 1186" in proc.stdout or "line 1187" in proc.stdout:
    fail(f"--split still reports the RETRO-2026-09-27x P5 rows as shifted after the fix: {proc.stdout}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: ledger_check --split classifies buckets, honors [bucket:X] overrides, computes parent-vs-"
      "worker spend per tenure, and the always-on shifted-outcome check finds only the fixture's "
      "row-1184-shaped line")
