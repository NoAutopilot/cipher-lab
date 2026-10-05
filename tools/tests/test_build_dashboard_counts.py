#!/usr/bin/env python3
"""Offline test for tools/build_dashboard.py's headline counts (27 Sept 2026, BOARD-COUNTS, CODEX-REVIEW-2026-09-27.md
s.1-2): the strip counts documents from explicit per-row fields, not rows from grade text. Fixture rows:
  A  N4 plaintext, two audits, recovered passages, two documents          -> 2 recovered-passage documents
  B  N4 plaintext but audit_status "one audit"                           -> not counted (the old rule counted any N4)
  C  key to a text already in print, mapping N3, two audits              -> not a reading; counted in the third chip
  D  a second row naming one of A's documents                            -> the document is counted once
  E  completed reading, N3, two audits                                   -> 1 completed reading
  F  catalogue contribution with one audit                               -> 1 contribution
Run: python3 tools/tests/test_build_dashboard_counts.py"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def row(title, kind, grade, **f):
    r = {"title": title, "kind": kind, "grade": grade, "date": "27 Sept 2026", "line": "x",
         "link": "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/" + title.lower()}
    r.update(f)
    return r


RESULTS = [
    row("A", "recovery", "N4", document_id="doc A1", documents=["doc A1", "doc A2"], claim_scope="recovered-passages",
        plaintext_novelty="N4", mapping_novelty="N4", audit_status="two audits", key="ours", depth="D3"),
    row("B", "solve", "N4 (no prior decipherment located)", document_id="doc B", claim_scope="recovered-passages",
        plaintext_novelty="N4", mapping_novelty="N4", audit_status="one audit"),
    row("C", "contribution", "key N3; text N1", document_id="doc C", claim_scope="key-to-known-text",
        plaintext_novelty="N1", mapping_novelty="N3", audit_status="two audits", key="ours"),
    row("D", "recovery", "N3", document_id="doc A2", claim_scope="recovered-passages",
        plaintext_novelty="N3", mapping_novelty="N3", audit_status="two audits", depth="D2"),
    row("E", "solve", "N3", document_id="doc E", claim_scope="completed-reading",
        plaintext_novelty="N3", mapping_novelty="N3", audit_status="two audits", depth="D2"),
    row("F", "contribution", "N0", document_id="doc F", claim_scope="catalogue-contribution",
        plaintext_novelty="N0", mapping_novelty="N0", audit_status="one audit"),
]

STATUS = {"updated": "27 Sept 2026", "headline": "test",
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
    want = {"documents with recovered passages": 2, "completed readings": 1,
            "keys or mappings to text already in print": 1, "catalogue contributions and corrections": 1,
            "with our own key and no earlier decipherment found": 2}
    for label, n in want.items():
        m = re.search(r"<b>(\d+)</b> " + re.escape(label), page)
        got = int(m.group(1)) if m else None
        ok = got == n
        fails += not ok
        print(("ok  " if ok else "FAIL") + f": {label}: {got} (want {n})")
    for bad in ("everywhere looked",):
        if bad in page:
            print(f"FAIL: page still says '{bad}'")
            fails += 1
    if "principal sources searched" not in page:
        print("FAIL: N4 label 'principal sources searched' missing")
        fails += 1
    if "warning: no audit_status" in proc.stderr:
        print("FAIL: heuristic warning printed for rows that carry audit_status")
        fails += 1
print("PASS" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
