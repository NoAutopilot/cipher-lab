#!/usr/bin/env python3
"""Offline test for tools/spawn_args.py (16 Oct 2026). Run: python3 tools/tests/test_spawn_args.py
Must catch: a create_session argument object with no source_url (the 25 Sept and 12 Oct 2026 failure, 8
sessions spawned with no repository), a title not starting with LIVE. Must not block: a complete object; a
--job call for a queued row."""
import json
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import spawn_args  # noqa: E402

fails = 0

# 1. the original failure: no source_url
bad = {"model": "claude-opus-5-5", "prompt": "Read the brief", "title": "LIVE X worker", "source_revision": "main"}
p = spawn_args.check_args(bad)
if not any("source_url" in x for x in p):
    print("FAIL: an argument object without source_url was not refused"); fails += 1

# 2. wrong repository
bad2 = dict(bad, source_url="https://github.com/someone/else")
if not any("source_url" in x for x in spawn_args.check_args(bad2)):
    print("FAIL: a foreign source_url was not refused"); fails += 1

# 3. title not LIVE
bad3 = dict(bad, source_url=spawn_args.SOURCE_URL, title="X worker")
if not any("LIVE" in x for x in spawn_args.check_args(bad3)):
    print("FAIL: a title without LIVE was not refused"); fails += 1

# 4. complete object passes
good = dict(bad, source_url=spawn_args.SOURCE_URL)
if spawn_args.check_args(good):
    print(f"FAIL: a complete object was refused: {spawn_args.check_args(good)}"); fails += 1

# 5. the builder from a queue row always includes source_url and a LIVE title
with tempfile.TemporaryDirectory() as td:
    q = os.path.join(td, "WORK-QUEUE.tsv")
    with open(q, "w") as f:
        f.write("job_id\taccount\tbrief\tmodel\tcap_usd\tbox_min\tstatus\tadded\tnote\n")
        f.write("TEST-JOB\taccount-2\t.claude/briefs/runs/x.md\tOpus 5.5\t4\t60\tqueued\t2026-10-16 03:00\tnote\n")
    proc = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "spawn_args.py"), "--job", "TEST-JOB", "--queue", q],
                          capture_output=True, text=True, cwd=ROOT, timeout=30)
    if proc.returncode != 0:
        print(f"FAIL: --job exited {proc.returncode}: {proc.stderr}"); fails += 1
    else:
        obj = json.loads(proc.stdout)
        if obj.get("source_url") != spawn_args.SOURCE_URL or obj.get("source_revision") != "main":
            print("FAIL: --job output lacks the repository source"); fails += 1
        if obj.get("model") != "claude-opus-5-5":
            print(f"FAIL: model id mapping wrong: {obj.get('model')}"); fails += 1
        if not obj.get("title", "").startswith("LIVE") or ".claude/briefs/runs/x.md" not in obj.get("prompt", ""):
            print("FAIL: title/prompt conventions not met"); fails += 1
    # 6. --check on a saved bad object exits 1, on a good one 0
    bpath = os.path.join(td, "bad.json"); json.dump(bad, open(bpath, "w"))
    gpath = os.path.join(td, "good.json"); json.dump(good, open(gpath, "w"))
    rb = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "spawn_args.py"), "--check", bpath], capture_output=True, text=True, cwd=ROOT)
    rg = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "spawn_args.py"), "--check", gpath], capture_output=True, text=True, cwd=ROOT)
    if rb.returncode != 1 or rg.returncode != 0:
        print(f"FAIL: --check exit codes bad={rb.returncode} good={rg.returncode}"); fails += 1

if fails:
    print(f"{fails} failure(s)"); sys.exit(1)
print("ok: spawn_args refuses a call without source_url or a LIVE title, builds a complete call from a queue row")
