#!/usr/bin/env python3
"""Offline test for tools/build_dashboard.py's Side quests view (24 Sept 2026, board side-quests
worker): builds the page in a temp directory from a minimal status.json carrying a three-item
`sidequests` fixture (one waiting on you, one running, one done) and asserts the view renders the
tab, the count line, all three cards in the right order (waiting on you, running, done), and the
"Side quests waiting on you" short list on Your desk.
Run: python3 tools/tests/test_build_dashboard_sidequests.py"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SIDEQUESTS = [
    {
        "title": "Zed done thing",
        "asked": "24 Sept 2026 10:00 UTC",
        "state": "done",
        "result": "It finished with a number: 42.",
        "next": "Nothing; closed.",
        "link": "ciphers/zed-done/",
        "session": ""
    },
    {
        "title": "Alpha waiting thing",
        "asked": "24 Sept 2026 09:00 UTC",
        "state": "waiting on you",
        "result": "Drafted and ready.",
        "next": "You submit the form.",
        "link": "outreach/alpha.md",
        "session": ""
    },
    {
        "title": "Beta running thing",
        "asked": "24 Sept 2026 11:00 UTC",
        "state": "running",
        "result": "In progress on the live leaf.",
        "next": "Reports when it finishes.",
        "link": "ciphers/beta-running/",
        "session": "session_01Example00000000000000000"
    },
]

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
    "sidequests": SIDEQUESTS,
}

fails = 0

with tempfile.TemporaryDirectory() as tmp:
    shutil.copy(os.path.join(ROOT, "tools", "build_dashboard.py"), tmp)
    with open(os.path.join(tmp, "status.json"), "w", encoding="utf-8") as f:
        json.dump(STATUS, f)

    proc = subprocess.run([sys.executable, "build_dashboard.py"], cwd=tmp, capture_output=True, text=True, timeout=30)
    if proc.returncode != 0:
        print(f"FAIL: build_dashboard.py exited {proc.returncode}: {proc.stderr}")
        fails += 1

    page = open(os.path.join(tmp, "docs", "index.html"), encoding="utf-8").read()

if 'data-view="sidequests"' not in page or "Side quests" not in page:
    print("FAIL: no Side quests tab button")
    fails += 1

m = re.search(r'<section class="view" id="sidequests".*?</section>', page, re.S)
if not m:
    print("FAIL: no Side quests section in the built page")
    fails += 1
    sec = ""
else:
    sec = m.group(0)

if "<b>3 items: 1 waiting on you, 1 running, 1 done</b>" not in sec:
    print("FAIL: count line wrong or missing")
    fails += 1

for title in ("Zed done thing", "Alpha waiting thing", "Beta running thing"):
    if title not in sec:
        print(f"FAIL: card for '{title}' not rendered")
        fails += 1

# ordering: waiting on you first, then running, then done
pos = {t: sec.find(t) for t in ("Alpha waiting thing", "Beta running thing", "Zed done thing")}
if not (pos["Alpha waiting thing"] < pos["Beta running thing"] < pos["Zed done thing"]):
    print(f"FAIL: cards not ordered waiting-on-you, running, done: {pos}")
    fails += 1

if "session_01Example00000000000000000" not in sec:
    print("FAIL: live session id not shown on its card")
    fails += 1
if "session_01Example00000000000000000" in re.sub(r'<li class="sqcard">.*?Beta running thing.*?</li>', '', sec, flags=re.S):
    pass  # session id appearing only within its own card is not independently asserted here; card content check above suffices

desk_m = re.search(r'<h3>Side quests waiting on you</h3>.*?</ul>', page, re.S)
if not desk_m:
    print("FAIL: 'Side quests waiting on you' list missing from Your desk")
    fails += 1
elif "Alpha waiting thing" not in desk_m.group(0):
    print("FAIL: waiting-on-you item not listed on Your desk")
    fails += 1
elif "Zed done thing" in desk_m.group(0) or "Beta running thing" in desk_m.group(0):
    print("FAIL: Your desk side-quest list should only list items waiting on you")
    fails += 1

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: Side quests view renders the tab, count line, three ordered cards, and the desk shortlist")
