#!/usr/bin/env python3
"""Offline test for tools/build_dashboard.py's Hall of fame view (24 Sept 2026, board hall-of-fame
worker): builds the page in a temp directory from a minimal status.json, a two-row CITATIONS.md
fixture and a one-row CONTRIBUTIONS.md fixture, and asserts the view renders both citation cards
(who, where as a link, what as a link, the quote), the count line, and the pending row.
Run: python3 tools/tests/test_build_dashboard_fame.py"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

STATUS = {
    "updated": "24 Sept 2026",
    "headline": "test",
    "stages": ["Identified", "Verified unsolved", "Ciphertext in hand", "Key source located",
               "Request sent", "Copies received", "Transcribed", "Reading attempted",
               "Novelty verified", "Solved"],
    "targets": [],
    "workers": [],
    "queue": [],
    "log": [],
    "results": [],
    "lanes": [],
}

CITATIONS = """# Citations

| Date | Who | Where | What of ours | How | Quote | Evidence |
|---|---|---|---|---|---|---|
| 1 Jan 2027 | A. Example | [page](https://example.org/a) | [ciphers/foo](https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/foo) | credit and link | "a first quote" | `sources/example/a.htm` |
| 2 Jan 2027 | B. Example | [page](https://example.org/b) | [ciphers/bar](https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/bar) | co-authorship | "a second quote" | `sources/example/b.htm` |
"""

CONTRIBUTIONS = """# Contributions handed on

| Date | Item | Class (AUDIT.md) | Found-solved grade (README) | Recipient | Channel | What was offered | Status |
|---|---|---|---|---|---|---|---|
| 1 Jan 2027 | Foo reading | N4 | not found-solved | Some Institute | email | a reading | sent by the person, 1 Jan 2027; reply pending |
"""

fails = 0

with tempfile.TemporaryDirectory() as tmp:
    shutil.copy(os.path.join(ROOT, "tools", "build_dashboard.py"), tmp)
    with open(os.path.join(tmp, "status.json"), "w", encoding="utf-8") as f:
        json.dump(STATUS, f)
    with open(os.path.join(tmp, "CITATIONS.md"), "w", encoding="utf-8") as f:
        f.write(CITATIONS)
    with open(os.path.join(tmp, "CONTRIBUTIONS.md"), "w", encoding="utf-8") as f:
        f.write(CONTRIBUTIONS)

    proc = subprocess.run([sys.executable, "build_dashboard.py"], cwd=tmp, capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        print(f"FAIL: build_dashboard.py exited {proc.returncode}: {proc.stderr}")
        fails += 1

    page = open(os.path.join(tmp, "docs", "index.html"), encoding="utf-8").read()

m = re.search(r'<section class="view" id="fame".*?</section>', page, re.S)
if not m:
    print("FAIL: no Hall of fame section in the built page")
    fails += 1
    sec = ""
else:
    sec = m.group(0)

if 'data-view="fame"' not in page or "Hall of fame" not in page:
    print("FAIL: no Hall of fame tab button")
    fails += 1
if "<b>2</b> public citations" not in sec:
    print("FAIL: citation count is not 2")
    fails += 1
if "A. Example" not in sec or "B. Example" not in sec:
    print("FAIL: both citation cards not rendered")
    fails += 1
if 'href="https://example.org/a"' not in sec or 'href="https://example.org/b"' not in sec:
    print("FAIL: citation 'where' links not rendered")
    fails += 1
if 'href="https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/foo"' not in sec:
    print("FAIL: citation 'what' link not rendered")
    fails += 1
if "a first quote" not in sec or "a second quote" not in sec:
    print("FAIL: citation quotes not rendered")
    fails += 1
if "Some Institute" not in sec:
    print("FAIL: pending contribution row not rendered")
    fails += 1

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: Hall of fame view renders two citation cards, the count, and the pending row")
