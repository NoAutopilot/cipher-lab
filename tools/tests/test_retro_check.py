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

# (e) exception review (owner, 16 Oct 2026): an X row, a no-repository death or 3+ rows at 2x cap since the last review
with tempfile.TemporaryDirectory() as td:
    open(os.path.join(td, "RETRO-2026-10-12.md"), "w").write(RETRO)
    open(os.path.join(td, "LEDGER.md"), "w").write("| Date | Role | Model | Cost | Outcome | Lesson |\n|---|---|---|---|---|---|\n"
        "| 14 Oct 2026 | x | session_01A | account-1 | Opus 5.5 | 3.0 | X | over-claimed and corrected |\n"
        "| 14 Oct 2026 | y | session_01B | account-1 | Opus 5.5 | 9.0 | D | 2.3x the 4 cap |\n"
        "| 14 Oct 2026 | z | session_01C | account-1 | Opus 5.5 | 8.0 | D | 2.0x the 4 cap |\n"
        "| 14 Oct 2026 | w | session_01D | account-1 | Opus 5.5 | 8.5 | D | 2.1x the 4 cap |\n"
        "| 11 Oct 2026 | old | session_01E | account-1 | Opus 5.5 | 8.5 | X | before the window |\n")
    reg = os.path.join(td, "reg.tsv")
    open(reg, "w").write(HDR + "RETRO-2026-10-12\tP1\tFix\tapplied\ttools/x.py\t2026-10-13\tx\nRETRO-2026-10-12\tP2\tAnother\tdeclined\twhy\t2026-10-13\tx\n")
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), NOW, 7, 8, datetime.date(2026, 9, 28))
    e = [f for f in findings if f.startswith("(e)")]
    if not e or "over_claim_X rows [3]" not in e[0] or "over_2x_cap rows [4, 5, 6]" not in e[0] or "7" in e[0].split("over_claim_X rows")[1].split(";")[0]:
        print(f"FAIL: exception review not triggered correctly: {findings}"); fails += 1
    # an EXC row dated after the X row clears it
    open(reg, "a").write("EXC-2026-10-15\tEXC1\texception review of the 14 Oct X row\tapplied\tdone\t2026-10-15\tx\n")
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), NOW, 7, 8, datetime.date(2026, 9, 28))
    if any(f.startswith("(e)") for f in findings):
        print(f"FAIL: a registered exception review did not clear the trigger: {findings}"); fails += 1
# gate_found_blind (EXC-2026-10-16 fix C): must catch a gate that was blind; must not block "blind" as a next step's adjective
# (ledger row 4542: the decoy gate worked, the false positive triggered the first exception review); and all rows are printed.
with tempfile.TemporaryDirectory() as td:
    open(os.path.join(td, "RETRO-2026-10-12.md"), "w").write(RETRO)
    open(os.path.join(td, "LEDGER.md"), "w").write("| Date | Role | Model | Cost | Outcome | Lesson |\n|---|---|---|---|---|---|\n"
        "| 14 Oct 2026 | a | session_01A | account-1 | Opus 5.5 | 3.0 | D | decoy gate FAIL 8/12 against 10/12, nothing applied; next a blind single-crop read |\n"
        "| 14 Oct 2026 | b | session_01B | account-1 | Opus 5.5 | 3.0 | D | ledger_check.py was blind to every row after a blank line |\n"
        "| 14 Oct 2026 | c | session_01C | account-1 | Opus 5.5 | 3.0 | D | the intake check silently skipped the premise section |\n")
    hits = rc.critical_since(os.path.join(td, "LEDGER.md"), datetime.date(2026, 10, 12))
    if hits["gate_found_blind"] != [4, 5]:
        print(f"FAIL: gate_found_blind should hit rows 4 and 5 only, got {hits['gate_found_blind']}"); fails += 1
    open(os.path.join(td, "LEDGER.md"), "a").write("".join(
        f"| 14 Oct 2026 | o{i} | session_01{i} | account-1 | Opus 5.5 | 9.0 | D | {2 + i / 10:.1f}x the 4 cap |\n" for i in range(8)))
    reg = os.path.join(td, "reg.tsv")
    open(reg, "w").write(HDR + "RETRO-2026-10-12\tP1\tFix\tapplied\ttools/x.py\t2026-10-13\tx\nRETRO-2026-10-12\tP2\tAnother\tdeclined\twhy\t2026-10-13\tx\n")
    findings, info = rc.run(reg, td, os.path.join(td, "LEDGER.md"), NOW, 7, 8, datetime.date(2026, 9, 28))
    e = [f for f in findings if f.startswith("(e)")]
    if not e or "over_2x_cap rows [6, 7, 8, 9, 10, 11, 12, 13]" not in e[0]:
        print(f"FAIL: all over-2x rows should be listed (no [:6] cut): {e}"); fails += 1
# Same-day re-trigger (owner, 16 Oct 2026, measurement integrity): rows an EXC row lists, and rows at or before the review's
# own ledger row, never re-fire; a critical row appended after the review does.
with tempfile.TemporaryDirectory() as td:
    open(os.path.join(td, "RETRO-2026-10-12.md"), "w").write(RETRO)
    lp = os.path.join(td, "LEDGER.md")
    open(lp, "w").write("| Date | Role | Model | Cost | Outcome | Lesson |\n|---|---|---|---|---|---|\n"
        "| 16 Oct 2026 | x | session_01A | account-1 | Opus 5.5 | 3.0 | X | over-claimed and corrected |\n"
        "| 16 Oct 2026 | y | session_01B | account-1 | Opus 5.5 | 9.0 | D | 2.3x the 4 cap |\n"
        "| 16 Oct 2026 | z | session_01C | account-1 | Opus 5.5 | 8.0 | D | 2.0x the 4 cap |\n"
        "| 16 Oct 2026 | w | session_01D | account-1 | Opus 5.5 | 8.5 | D | 2.1x the 4 cap |\n"
        "| 16 Oct 2026 | EXC-2026-10-16 exception review worker | session_01E | account-1 | Opus 5.5 | 1.9 | D | reviewed rows 3-6 |\n")
    reg = os.path.join(td, "reg.tsv")
    open(reg, "w").write(HDR + "RETRO-2026-10-12\tP1\tFix\tapplied\ttools/x.py\t2026-10-13\tx\nRETRO-2026-10-12\tP2\tAnother\tdeclined\twhy\t2026-10-13\tx\n"
                         "EXC-2026-10-16\tEXC1\texception review of rows 3, 4, 5, 6\tapplied\tdone\t2026-10-16\tx\n")
    findings, info = rc.run(reg, td, lp, NOW, 7, 8, datetime.date(2026, 9, 28))
    if any(f.startswith("(e)") for f in findings):
        print(f"FAIL: a same-day review re-fired on the rows it reviewed: {findings}"); fails += 1
    open(lp, "a").write("| 16 Oct 2026 | v | session_01F | account-1 | Opus 5.5 | 3.0 | X | a new over-claim after the review |\n")
    findings, info = rc.run(reg, td, lp, NOW, 7, 8, datetime.date(2026, 9, 28))
    e = [f for f in findings if f.startswith("(e)")]
    if not e or "over_claim_X rows [8]" not in e[0] or "over_2x_cap" in e[0]:
        print(f"FAIL: a critical row appended after the review must fire alone: {findings}"); fails += 1
if fails:
    print(f"{fails} failure(s) in the exception-review checks"); sys.exit(1)
print("ok: exception review triggers on an X row / 3+ rows at 2x cap since the last review and clears after an EXC row")
