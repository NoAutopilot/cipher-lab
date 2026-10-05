#!/usr/bin/env python3
"""Offline test for tools/progress_metrics.py (METRICS, 5 Oct 2026): a small LEDGER.md-shaped sample
covering the real file's layouts (6-cell, Session column, account+model columns, "~N (note)" cost,
no trailing pipe, prose cost, orchestrator row) and a status.json sample, checked against hand-computed
weekly figures. Run: python3 tools/tests/test_progress_metrics.py"""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import progress_metrics as pm  # noqa: E402

LEDGER = """| Date | Role | Model | Cost | Outcome | Lesson |
|---|---|---|---|---|---|
| 22 Sept | Scout: round 1 | Sonnet | ~2 (226k tokens) | D | x |
| 24 Sep | Scout round 2 | Sonnet | session_01AAA | 4.00 | D- | y |
| 24 Sep | LANE N orchestrator: nominations | Opus | 99.00 | D | orchestrator, own column |
| 25 Sep | Verifier: x | Opus | session_01BBB | 3.00 | F | no trailing pipe
| 25 Sep | Verifier: y | Opus | not visible from account 3 | D | prose cost skipped |
| 3 Oct 2026 | CLOSER-50 (account-4) | session_01CCC | account-4 | Opus 5.5 | 1.31 | D | z |
| 3 Oct 2026 | CLOSER-51 | session_01DDD | account-4 | Opus 5.5 | 2.69 | N | clean negative |
| 4 Oct 2026 | odd row | Sonnet | 1.00 | B | non-standard code |
| someday | broken | Sonnet | 1.00 | D | no date |
"""
STATUS = {"results": [
    {"date": "24 Sept 2026", "depth": "D2"},
    {"date": "25 Sept 2026", "depth": "D3"},
    {"date": "25 Sept 2026", "depth": "D1"},
    {"date": "2 Oct 2026", "depth": "D4", "superseded_by": "x"},
    {"date": "2 Oct 2026", "depth": "D2"},
], "targets": [{"depth": "D2"}]}


def main():
    with tempfile.TemporaryDirectory() as d:
        lp, sp = os.path.join(d, "L.md"), os.path.join(d, "s.json")
        open(lp, "w").write(LEDGER)
        json.dump(STATUS, open(sp, "w"))
        rows, skipped = pm.load_ledger(lp)
        assert skipped["date"] == 1, skipped
        assert skipped["cost"] == 1, skipped
        assert skipped["outcome"] == 1, skipped  # code B
        res, rskip = pm.load_results(sp)
        assert len(res) == 3 and rskip == 1, (res, rskip)
        t = {r["week"]: r for r in pm.compute(rows, res)}
        w39, w40 = t["2026-W39"], t["2026-W40"]
        assert w39["spend"] == 9.0 and w39["orch_spend"] == 99.0, w39
        assert w39["d_denom"] == 4 and w39["share_d"] == 0.5, w39  # D, D-, F, D(prose cost)
        assert w39["d2_new"] == 2 and w39["usd_per_d2"] == 4.5, w39
        assert w40["spend"] == 5.0 and w40["d2_new"] == 1 and w40["share_d"] == 1.0, w40
        assert "CLOSER 2.00 (n=2)" in w40["median_by_role"], w40
        out = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "progress_metrics.py"),
                              "--ledger", lp, "--status", sp, "--tsv"], capture_output=True, text=True)
        assert out.returncode == 0 and out.stdout.splitlines()[0].startswith("week\t"), out
        assert "skipped" in out.stderr
    h = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "progress_metrics.py"), "--help"],
                       capture_output=True, text=True)
    assert "--tsv" in h.stdout
    print("ok test_progress_metrics")


if __name__ == "__main__":
    main()
