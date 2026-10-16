#!/usr/bin/env python3
"""Offline test for tools/experiment_log.py (16 Oct 2026). Run: python3 tools/tests/test_experiment_log.py
Must catch: a new PREREG with no Decision block; one whose Decision word is not continue/change/stop; a finished run
whose Observed/Decision/Lesson still read <pending>. Must not block: a pre-cutoff PREREG (warn only); a complete block;
a pending block before the run."""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import experiment_log as el  # noqa: E402

fails = 0
NEW = "# PREREG X, written 16 Oct 2026 by date -u\n\n## Material\nstuff\n"
OLD = "# PREREG Y, written 1 Oct 2026\n\n## Material\nstuff\n"
BLOCK_PENDING = "\n## Decision\nBelief: the f-sign splits by the ascender\nWould change it: recall under 0.80 at N_f 18\nObserved: <pending>\nDecision: <pending>\nLesson: <pending>\n"
BLOCK_DONE = "\n## Decision\nBelief: the f-sign splits by the ascender\nWould change it: recall under 0.80 at N_f 18\nObserved: recall 0.833 / precision 0.750 vs null 0.400\nDecision: stop -- applying it blind shortens the best run; owner questions instead\nLesson: a 75%-precision split hurts a run-length statistic; use it as questions, not a key row\n"
BLOCK_BAD = BLOCK_DONE.replace("Decision: stop --", "Decision: maybe --")

with tempfile.TemporaryDirectory() as td:
    def w(name, text):
        p = os.path.join(td, name); open(p, "w").write(text); return p
    cases = [
        (w("PREREG-A.md", NEW), False, "fail"),                 # new, no block
        (w("PREREG-B.md", OLD), False, "warn"),                 # old, no block: warn only
        (w("PREREG-C.md", NEW + BLOCK_PENDING), False, "ok"),   # before the run
        (w("PREREG-D.md", NEW + BLOCK_PENDING), True, "fail"),  # after the run, still pending
        (w("PREREG-E.md", NEW + BLOCK_DONE), True, "ok"),       # complete
        (w("PREREG-F.md", NEW + BLOCK_BAD), True, "fail"),      # bad decision word
    ]
    for path, done, want in cases:
        level, msg = el.check_file(path, done)
        if level != want:
            print(f"FAIL: {os.path.basename(path)} done={done}: want {want}, got {level} ({msg})"); fails += 1
    # index: a target folder with a decided PREREG and a HYPOTHESES family row
    cd = os.path.join(td, "ciphers", "t1"); os.makedirs(cd)
    open(os.path.join(cd, "PREREG-E.md"), "w").write(NEW + BLOCK_DONE)
    open(os.path.join(cd, "HYPOTHESES.md"), "w").write("| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |\n|---|---|---|---|---|---|---|---|---|\n| 28 Sept 2026 00:32 | wordcode | N=522 K=38 | 1 | 0.852 (0.808-0.904) | -1231 | FAIL | no | retired |\n")
    rows = el.index_rows(os.path.join(td, "ciphers"))
    if len(rows) != 2 or rows[0]["decision"][:4] != "stop" or rows[1]["instrument"] != "wordcode" or rows[1]["n"] != "522" or rows[1]["decision"] != "stop":
        print(f"FAIL: index rows wrong: {rows}"); fails += 1

if fails:
    print(f"{fails} failure(s)"); sys.exit(1)
print("ok: experiment_log checks the Decision block (new fail / old warn / pending before, not after) and indexes PREREG decisions with HYPOTHESES family rows")
