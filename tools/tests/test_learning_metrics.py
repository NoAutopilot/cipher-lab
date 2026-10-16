#!/usr/bin/env python3
"""Offline test for tools/learning_metrics.py (16 Oct 2026). Run: python3 tools/tests/test_learning_metrics.py
Must catch: an over-cap row (ratio > 1), a no-repository row, a non-test row, a target with 3 N rows, an applied-with-test
register row, and one N3/D2 result dated in the window; must not count rows outside the window, a ratio under 1, or an
orchestrator's own cost as worker spend."""
import datetime
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import learning_metrics as lm  # noqa: E402

LEDGER = """| Date | Role | Model | Cost | Outcome | Lesson |
|---|---|---|---|---|---|
| 10 Oct 2026 | HAR-41R harley-287-1587 f.41r (LANE X, account 1) | session_01A | account-1 | Opus 5.5 | 9.45 | D | 2.10x the 4.5 cap |
| 10 Oct 2026 | MQS-SHEETS A1 | session_01B | account-1 | Opus 5.5 | 0.30 | F | orchestrator's create_session omitted source_url |
| 11 Oct 2026 | OBRED-1 oldenbarnevelt-brederode-1605 screen | session_01C | account-2 | Opus 5.5 | 3.0 | N | no block |
| 11 Oct 2026 | OBRED-2 oldenbarnevelt-brederode-1605 screen | session_01D | account-2 | Opus 5.5 | 3.0 | N | no block |
| 12 Oct 2026 | OBRED-3 oldenbarnevelt-brederode-1605 screen | session_01E | account-2 | Opus 5.5 | 3.0 | N | control FAIL, non-test |
| 12 Oct 2026 | GOOD-1 some-target-1600 read | session_01F | account-2 | Opus 5.5 | 2.0 | D | under cap 0.8x the 2.5 cap |
| 12 Oct 2026 | LANE DEFAULT-account-2 orchestrator (account 2) | session_01G | account-2 | Opus 5.5 | 20.0 | D | lane self row |
| 20 Oct 2026 | LATE-1 some-target-1600 read | session_01H | account-2 | Opus 5.5 | 5.0 | D | 3x the cap -- outside the window |
"""
REG = "retro\tproposal\tasks_for\tstatus\tevidence\tdecided_on\tby\nRETRO-X\tP1\ta\tapplied\ttools/x.py + tools/tests/test_x.py\t2026-10-12\tme\nRETRO-X\tP2\tb\topen\t\t2026-10-12\tme\nRETRO-X\tP3\tc\tapplied\tprose\t2026-10-30\tme\n"
STATUS = {"results": [
    {"title": "in-window solve", "plaintext_novelty": "N4", "depth": "D2", "depth_date": "11 Oct 2026", "key": "period"},
    {"title": "out-of-window", "plaintext_novelty": "N3", "depth": "D3", "depth_date": "1 Oct 2026"},
    {"title": "not deep enough", "plaintext_novelty": "N4", "depth": "D1", "depth_date": "11 Oct 2026"},
]}
fails = 0
with tempfile.TemporaryDirectory() as td:
    lp = os.path.join(td, "LEDGER.md"); open(lp, "w").write(LEDGER)
    rp = os.path.join(td, "reg.tsv"); open(rp, "w").write(REG)
    sp = os.path.join(td, "status.json"); json.dump(STATUS, open(sp, "w"))
    m = lm.compute(lm.load_rows(lp), lm.load_results(sp), lm.load_register(rp), datetime.date(2026, 10, 9), datetime.date(2026, 10, 15))
    chk = [
        (m["rows"] == 7, f"rows {m['rows']} != 7"),
        (abs(m["worker_usd"] - 20.75) < 0.01, f"worker_usd {m['worker_usd']} != 20.75 (orchestrator row excluded)"),
        (m["operational"]["over_cap"]["rows"] == 1, f"over_cap {m['operational']['over_cap']}"),
        (m["operational"]["no_repository"]["rows"] == 1, "no_repository not counted"),
        (m["repeated_approaches"]["rows"] == 1, f"repeat rows {m['repeated_approaches']['rows']}"),
        (m["repeated_approaches"]["targets_with_3plus_N"] == 1, f"3+N targets {m['repeated_approaches']}"),
        (m["retro_proposals"]["applied"] == 1 and m["retro_proposals"]["applied_with_test"] == 1 and m["retro_proposals"]["open"] == 1, f"register {m['retro_proposals']}"),
        (m["solves"]["n3_d2_new"] == 1 and m["solves"]["usd_per_solve"] == 20.75, f"solves {m['solves']}"),
        (m["solves"]["ours_key"] == 0 and m["solves"]["usd_per_ours_key_solve"] == "no solve with our own key", f"key split {m['solves']}"),
    ]
    for ok, msg in chk:
        if not ok:
            print("FAIL:", msg); fails += 1
    m2 = lm.compute(lm.load_rows(lp), lm.load_results(sp), lm.load_register(rp), datetime.date(2026, 11, 1), datetime.date(2026, 11, 7))
    if m2["solves"]["usd_per_solve"] != "no solve":
        print("FAIL: an empty window must say 'no solve', not a rate"); fails += 1
if fails:
    print(f"{fails} failure(s)"); sys.exit(1)
print("ok: learning_metrics counts the repeat shapes, register decisions and N3+/D2+ solves inside the window only, and never claims a rate without a solve")
