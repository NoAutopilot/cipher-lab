#!/usr/bin/env python3
"""Offline test for tools/ledger_check.py's --over-cap-severity mode (RETRO-2026-10-26 P2): three
synthetic D- rows (ratio 1.05x -> near-cap, 1.71x -> real miss, no ratio -> unparsed), plus a non-D-
row that must not be counted at all. Run: python3 tools/tests/test_ledger_check_severity.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import ledger_check  # noqa: E402

SAMPLE = [
    "| Date | Role | Model | Session | Cost | Outcome | Lesson |\n",
    "|---|---|---|---|---|---|---|\n",
    # near-cap: ratio under the 1.3 threshold
    "| 20 Oct | NEAR-CAP-X (account 4, worker) | Sonnet | session_01NEARCAP0000000000000 | 4.2 | D- | "
    "ran 1.05x its USD 4 cap; cost USD 4.20 by get_session.\n",
    # real miss: ratio at or above the 1.3 threshold
    "| 20 Oct | REAL-MISS-X (account 4, worker) | Opus | session_01REALMISS000000000000 | 5.14 | D- | "
    "ran 1.71x its USD 3 cap (box 30, done in 19 min); a browser-fetch pricing miss.\n",
    # unparsed: D- outcome but no "<N>x" ratio anywhere in the Lesson cell
    "| 20 Oct | UNPARSED-X (account 4, worker) | Sonnet | session_01UNPARSED00000000000 | 6.0 | D- | "
    "ran over its cap; exact ratio not recorded this time.\n",
    # not D- at all: must never appear in any of the three buckets
    "| 20 Oct | CLEAN-D (account 4, worker) | Sonnet | session_01CLEAND0000000000000 | 2.0 | D | "
    "finished at 0.9x its USD 2 cap, well inside budget.\n",
]

fails = 0


def fail(msg):
    global fails
    print(f"FAIL: {msg}")
    fails += 1


near, real, unparsed = ledger_check.over_cap_severity(SAMPLE, 1)

near_lines = {lineno for lineno, _ in near}
real_lines = {lineno for lineno, _ in real}

if near_lines != {3}:
    fail(f"expected near-cap on line 3 only, got {near_lines}")
elif abs(near[0][1] - 1.05) > 1e-9:
    fail(f"expected near-cap ratio 1.05, got {near[0][1]}")

if real_lines != {4}:
    fail(f"expected real-miss on line 4 only, got {real_lines}")
elif abs(real[0][1] - 1.71) > 1e-9:
    fail(f"expected real-miss ratio 1.71, got {real[0][1]}")

if unparsed != [5]:
    fail(f"expected unparsed on line 5 only, got {unparsed}")

# the clean D row (line 6) must not appear in any bucket
all_lines = near_lines | real_lines | set(unparsed)
if 6 in all_lines:
    fail(f"the non-D- row (line 6) must never appear in any severity bucket, got {all_lines}")

# --help documents the new flag
help_r = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "ledger_check.py"), "--help"],
    capture_output=True, text=True, timeout=30,
)
if help_r.returncode != 0 or "--over-cap-severity" not in help_r.stdout:
    fail(f"--help failed or missing --over-cap-severity: rc={help_r.returncode}")

# CLI always exits 0 against the real LEDGER.md, whatever it finds
proc = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "ledger_check.py"), "--over-cap-severity", "1"],
    cwd=ROOT, capture_output=True, text=True, timeout=60,
)
if proc.returncode != 0:
    fail(f"--over-cap-severity must always exit 0, got rc={proc.returncode}: {proc.stdout}\n{proc.stderr}")
if "near-cap" not in proc.stdout or "real miss" not in proc.stdout:
    fail(f"--over-cap-severity CLI output missing a bucket header: {proc.stdout}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: ledger_check --over-cap-severity splits D- rows into near-cap/real-miss by their Lesson "
      "cell's own ratio, lists unparsed rows, excludes non-D- rows, and always exits 0")
