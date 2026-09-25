#!/usr/bin/env python3
"""Request a credential: one command files the KEYS.md row, the ASKS.md row for the owner's desk and the ROOM.md flag.

Usage:
  tools/key_request.py NAME --purpose "what it is for" --tool tools/x.py [--by "LANE R8 worker X"] [--no-push]

The owner adds the variable in both accounts' environment settings; the next fresh session on each account announces
it (tools/key_probe.py --sync from tools/room.py --start). Never pass or print a value. Exit 2 if NAME already has a row.
"""
import argparse
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name"); ap.add_argument("--purpose", required=True); ap.add_argument("--tool", required=True)
    ap.add_argument("--by", default="a session"); ap.add_argument("--no-push", action="store_true")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[A-Z][A-Z0-9_]{2,}", a.name):
        print("NAME must be an UPPER_CASE environment variable name"); return 1
    keys = os.path.join(ROOT, "KEYS.md"); asks = os.path.join(ROOT, "ASKS.md")
    if re.search(rf"^\| {re.escape(a.name)} \|", open(keys, encoding="utf-8").read(), flags=re.M):
        print(f"{a.name} already has a KEYS.md row"); return 2
    day = time.strftime("%-d %b %Y", time.gmtime()).replace("Sep ", "Sept ")
    nums = [int(x) for x in re.findall(r"^\| (\d+) \|", open(asks, encoding="utf-8").read(), flags=re.M)]
    n = (max(nums) + 1) if nums else 1
    with open(keys, "a", encoding="utf-8") as f:
        f.write(f"| {a.name} | {a.purpose} | {a.tool} | {a.by}, {day}, ASKS {n} | requested | |\n")
    with open(asks, "a", encoding="utf-8") as f:
        f.write(f"| {n} | {day} | cipher-lab | Key request ({a.by}): please add `{a.name}` ({a.purpose}; read by {a.tool}) "
                f"to the environment settings of BOTH accounts. KEYS.md row `requested`; the next fresh session on each "
                f"account announces it in ROOM.md when it appears. Never paste the value into chat. | open |\n")
    print(f"KEYS.md row and ASKS.md row {n} written for {a.name}")
    if a.no_push:
        return 0
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "room.py"), a.by,
                        f"flag: key request {a.name} ({a.purpose}) -- KEYS.md requested, ASKS {n}; owner adds it on both accounts"],
                       cwd=ROOT)
    if r.returncode == 0:
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "room.py"), "--push", "KEYS.md", "ASKS.md"], cwd=ROOT)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
