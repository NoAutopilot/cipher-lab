#!/usr/bin/env python3
"""Offline test for tools/decode_list.py: no network. Parses a saved two-row
fixture (tools/tests/fixtures/decode_recordslist_sample.html, trimmed from a
real de-crypt.org RecordsList?...&cmd=search response fetched 24 Sept 2026)
and checks field extraction plus --help exits cleanly without touching the
network or DECODE_USER/DECODE_PASS.
Run: python3 tools/tests/test_decode_list.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import decode_list as dl  # noqa: E402

FIXTURE = os.path.join(ROOT, "tools", "tests", "fixtures", "decode_recordslist_sample.html")

fails = 0
html = open(FIXTURE, encoding="utf-8").read()

total = dl.pager_total(html)
if total != 801:
    print(f"FAIL: pager_total = {total}, expected 801")
    fails += 1

rows = dl.parse_rows(html, source_page=1)
if len(rows) != 2:
    print(f"FAIL: parsed {len(rows)} rows, expected 2")
    fails += 1
else:
    r0 = rows[0]
    checks = {
        "id": "10181",
        "status": "Non-decrypted",
        "record_type": "Cipher",
        "city": "Barcelona",
        "date_range": "1718 -",
        "number_of_pages": "4",
    }
    for k, v in checks.items():
        if r0.get(k) != v:
            print(f"FAIL: row0[{k!r}] = {r0.get(k)!r}, expected {v!r}")
            fails += 1
    r1 = rows[1]
    if r1.get("plaintext_lang") != "" or r1.get("cleartext_lang") != "Spanish":
        print(f"FAIL: row1 language fields wrong: {r1.get('cleartext_lang')!r}/{r1.get('plaintext_lang')!r}")
        fails += 1

env = dict(os.environ)
env.pop("DECODE_USER", None)
env.pop("DECODE_PASS", None)
proc = subprocess.run(
    [sys.executable, os.path.join(ROOT, "tools", "decode_list.py"), "--help"],
    cwd=ROOT, env=env, capture_output=True, text=True, timeout=30,
)
if proc.returncode != 0:
    print(f"FAIL: --help exit code {proc.returncode}")
    fails += 1
for token in ("--status", "--record-type", "--recperpage", "--max-requests"):
    if token not in proc.stdout:
        print(f"FAIL: --help text missing {token!r}")
        fails += 1

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: decode_list.py parses the sample RecordsList rows and --help works offline")
