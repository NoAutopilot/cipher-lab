#!/usr/bin/env python3
"""Offline test for tools/retro_check.py (16 Oct 2026). Run: python3 tools/tests/test_retro_check.py
Must catch: an OPEN proposal older than the window (the 28 P3 -> 10-05 P2 -> 10-12 P4 shape); a proposal in a
RETRO file with no register row; a lapsed weekly cadence. Must not block: a register where every proposal is
applied/declined and the newest RETRO is recent."""
import datetime
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import retro_check as rc  # noqa: E402

HDR = "retro\tproposal\tasks_for\tstatus\tevidence\tdecided_on\tby\n"
RETRO = "# retro\n\n## 5. Proposed changes\n\n**P1. Fix the thing.**\nbody\n\n**P2. Another.**\nbody\n"
fails = 0
NOW = datetime.date(2026, 10, 16)

with tempfile.TemporaryDirectory() as td:
    open(os.path.join(td, "RETRO-2026-10-12.md"), "w").write(RETRO)
    open(os.path.join(td, "LEDGER.md"), "w").write("| Date | Role | Model | Cost | Outcome | Lesson |\n|---|---|---|---|---|---|\n| 14 Oct 2026 | x | Opus 5.5 | 3.0 | D | l |\n")
    # 1. an open proposal older than 7 days, and P2 unregistered
    reg = os.path.join(td, "reg.tsv")
    open(reg, "w").write(HDR + "RETRO-2026-10-12\tP1\tFix the thing\topen\t\t2026-10-01\tx\n")
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), NOW, 7, 8, datetime.date(2026, 9, 28))
    if not any(f.startswith("(a) OPEN") and "P1" in f for f in findings):
        print(f"FAIL: stale open proposal not flagged: {findings}"); fails += 1
    if not any("unregistered" in f and "P2" in f for f in findings):
        print(f"FAIL: unregistered P2 not flagged: {findings}"); fails += 1
    if not any(i.startswith("(d)") and "1 LEDGER.md rows" in i for i in info):
        print(f"FAIL: ledger-since count wrong: {info}"); fails += 1
    # 2. clean register, recent retro -> no findings
    open(reg, "w").write(HDR + "RETRO-2026-10-12\tP1\tFix\tapplied\ttools/x.py\t2026-10-13\tx\nRETRO-2026-10-12\tP2\tAnother\tdeclined\twhy\t2026-10-13\tx\n")
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), NOW, 7, 8, datetime.date(2026, 9, 28))
    if findings:
        print(f"FAIL: clean register flagged: {findings}"); fails += 1
    # 3. lapsed cadence
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), datetime.date(2026, 10, 25), 7, 8, datetime.date(2026, 9, 28))
    if not any(f.startswith("(c)") for f in findings):
        print(f"FAIL: lapsed cadence not flagged: {findings}"); fails += 1
    # 4. an open proposal inside the window is not flagged
    open(reg, "w").write(HDR + "RETRO-2026-10-12\tP1\tFix\topen\t\t2026-10-14\tx\nRETRO-2026-10-12\tP2\tAnother\tdeclined\twhy\t2026-10-13\tx\n")
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), NOW, 7, 8, datetime.date(2026, 9, 28))
    if any(f.startswith("(a)") for f in findings):
        print(f"FAIL: a 2-day-old open proposal was flagged: {findings}"); fails += 1

if fails:
    print(f"{fails} failure(s)"); sys.exit(1)
print("ok: retro_check flags stale open proposals, unregistered proposals and a lapsed cadence, and passes a clean register")
