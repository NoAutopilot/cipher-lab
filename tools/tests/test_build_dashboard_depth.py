#!/usr/bin/env python3
"""Offline test for tools/build_dashboard.py's depth gate (BOARD-DEPTH, 5 Oct 2026; CLAUDE.md rule 4a: a unique solve
is N3+ AND D2+). Every fixture row is N3+, two audits, recovered passages:
  A  depth D2                -> counted in the headline
  B  depth D1                -> not counted; one "fragments read"
  C  no depth field          -> neither; held out and named
  D  depth D4                -> counted
Must NOT block: a D2+ row (A, D) still counts. Run: python3 tools/tests/test_build_dashboard_depth.py"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def row(title, **f):
    r = {"title": title, "kind": "recovery", "grade": "N3", "date": "5 Oct 2026", "line": "x",
         "link": "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/" + title.lower(),
         "document_id": "doc " + title, "claim_scope": "recovered-passages", "plaintext_novelty": "N3",
         "mapping_novelty": "N3", "audit_status": "two audits"}
    r.update(f)
    return r


RESULTS = [row("A", depth="D2"), row("B", depth="D1"), row("Cnodepth"), row("D", depth="D4")]
STATUS = {"updated": "5 Oct 2026", "headline": "test",
          "stages": ["Identified", "Verified unsolved", "Ciphertext in hand", "Key source located", "Request sent",
                     "Copies received", "Transcribed", "Reading attempted", "Novelty verified", "Solved"],
          "targets": [], "workers": [], "queue": [], "log": [], "results": RESULTS, "lanes": []}

fails = 0
with tempfile.TemporaryDirectory() as tmp:
    shutil.copy(os.path.join(ROOT, "tools", "build_dashboard.py"), tmp)
    with open(os.path.join(tmp, "status.json"), "w", encoding="utf-8") as f:
        json.dump(STATUS, f)
    proc = subprocess.run([sys.executable, "build_dashboard.py"], cwd=tmp, capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        print(f"FAIL: build_dashboard.py exited {proc.returncode}: {proc.stderr}")
        sys.exit(1)
    page = open(os.path.join(tmp, "dashboard.html"), encoding="utf-8").read()
    want = {"documents with recovered passages": 2, "fragments read": 1, "held out until a verifier sets depth": 1}
    for label, n in want.items():
        m = re.search(r"<b>(\d+)</b> " + re.escape(label), page)
        got = int(m.group(1)) if m else None
        ok = got == n
        fails += not ok
        print(("ok  " if ok else "FAIL") + f": {label}: {got} (want {n})")
    if "Cnodepth" not in proc.stderr:
        print("FAIL: held-out row not named on stderr")
        fails += 1
print("PASS" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
