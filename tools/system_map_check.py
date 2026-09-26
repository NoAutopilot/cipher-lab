#!/usr/bin/env python3
"""Check that SYSTEM.md, the current-state map, mentions every part of the machine (CLAUDE.md Usage 8a, rules become
tools; SYSTEM-MAP for parent 7h, 26 Sept 2026, at the owner's ask: "sometimes we add something and then it's lost in the
ether and our other agent account can't see it").

    python3 tools/system_map_check.py [--root DIR] [--map FILE] [--quiet]

A name counts as mentioned when it appears anywhere in SYSTEM.md's text (a tool by its basename, e.g. `room.py`; a
register by its path, e.g. `hub-seed/ASSIGNMENTS.md`). Required names:

  - every tools/*.py except tests (tools/tests/ is not scanned);
  - every tools/*_runner*_prompt.md and tools/*_runner_brief.md (the ChatGPT and Desktop runner prompts);
  - every *.tsv at the repository root (the queues and root registers);
  - the fixed register list REGISTERS below;
  - every tools/<name>.py named in CLAUDE.md's Usage 8a paragraph (the gate precedents).

Exit 0 and one summary line when all are present; exit 1 with one "MISSING <kind>: <name>" line per absent name;
exit 2 when SYSTEM.md itself is missing. Offline; reads files only. Test: tools/tests/test_system_map_check.py.
Run it at every parent check-in (parent.md duty 3a) and before pushing any change that adds a tool, gate, loop,
register or runner; the fix for a MISSING line is a row in SYSTEM.md in the same commit.
"""
import argparse
import glob
import os
import re
import sys

REGISTERS = [
    "status.json", "NEAR.md", "ASKS.md", "KEYS.md", "KEYS-STATUS.md", "CONTRIBUTIONS.md", "CITATIONS.md",
    "LEDGER.md", "ROOM.md", "STATUS.md", "hub-seed/ASSIGNMENTS.md", "hub-seed/SUCCESSOR-PROMPT.md", "UPDATES.md",
    "SECOND-OPINIONS-QUEUE.tsv", "JSTOR-QUEUE.tsv", "LOCAL-QUEUE.tsv", "QUEUE.md", "BUDGETS.md", "specs/",
    "ciphers/", "outreach/",
]


def usage_8a_tools(claude_text):
    """tools/<name>.py basenames named in CLAUDE.md's item 8a (up to the next numbered item)."""
    m = re.search(r"^8a\.(.*?)(?=^\d+[a-z]?\. |^## |\Z)", claude_text, re.S | re.M)
    if not m:
        return []
    seen = []
    for name in re.findall(r"tools/([A-Za-z0-9_]+\.py)", m.group(1)):
        if name not in seen:
            seen.append(name)
    return seen


def required(root):
    """[(kind, name)] every name SYSTEM.md must mention."""
    req = []
    for p in sorted(glob.glob(os.path.join(root, "tools", "*.py"))):
        req.append(("tool", os.path.basename(p)))
    runners = set(glob.glob(os.path.join(root, "tools", "*_runner*_prompt.md")))
    runners |= set(glob.glob(os.path.join(root, "tools", "*_runner_brief.md")))
    for p in sorted(runners):
        req.append(("runner", os.path.basename(p)))
    for p in sorted(glob.glob(os.path.join(root, "*.tsv"))):
        req.append(("queue/tsv", os.path.basename(p)))
    for r in REGISTERS:
        req.append(("register", r))
    cpath = os.path.join(root, "CLAUDE.md")
    if os.path.exists(cpath):
        with open(cpath, encoding="utf-8") as f:
            for name in usage_8a_tools(f.read()):
                req.append(("8a gate", name))
    out, seen = [], set()
    for kind, name in req:
        if name not in seen:
            seen.add(name)
            out.append((kind, name))
    return out


def missing(root, map_text):
    return [(k, n) for k, n in required(root) if n not in map_text]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    help="repository root (default: this script's repository)")
    ap.add_argument("--map", default=None, help="map file (default: ROOT/SYSTEM.md)")
    ap.add_argument("--quiet", action="store_true", help="print only MISSING lines")
    a = ap.parse_args(argv)
    mpath = a.map or os.path.join(a.root, "SYSTEM.md")
    if not os.path.exists(mpath):
        print(f"system_map_check: {mpath} not found -- SYSTEM.md is the current-state map (CLAUDE.md Usage 8a)")
        return 2
    with open(mpath, encoding="utf-8") as f:
        text = f.read()
    req = required(a.root)
    miss = missing(a.root, text)
    for kind, name in miss:
        print(f"MISSING {kind}: {name}")
    if miss:
        print(f"system_map_check: FAIL -- {len(miss)} of {len(req)} names absent from SYSTEM.md; "
              "add a row for each in the same commit")
        return 1
    if not a.quiet:
        print(f"system_map_check: ok -- all {len(req)} names present in SYSTEM.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
