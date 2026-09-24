#!/usr/bin/env python3
"""Offline test for tools/decode_browser_login.js's safeFilename() helper: no network, no credentials.
Regression case (24 Sept 2026): six --fetch-page DocumentsList URLs differing only by ?fk_id=N all
resolved to the same last-path-segment filename ("DocumentsList.html"), so five of six fetches in one
login silently overwrote each other on disk. Requiring the module (require.main !== module) must skip
the login IIFE entirely, so this needs no DECODE_USER/DECODE_PASS and makes no network call.
Run: python3 tools/tests/test_decode_browser_login_safefilename.py"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, 'tools', 'decode_browser_login.js')

fails = 0


def fail(msg):
    global fails
    print(f'FAIL: {msg}')
    fails += 1


cases = [
    "DocumentsList?showmaster=records&fk_id=1411",
    "DocumentsList?showmaster=records&fk_id=2678",
    "RecordsView/1411",
    "https://de-crypt.org/decrypt-custom/filesrv/?file=TH_IMG_R1411_I6595_P1.png",
]
node_src = (
    "const { safeFilename } = require(%r);"
    "console.log(JSON.stringify(%s.map(safeFilename)));"
) % (SCRIPT, json.dumps(cases))

proc = subprocess.run(['node', '-e', node_src], cwd=ROOT, capture_output=True, text=True, timeout=30)
if proc.returncode != 0:
    fail(f'node -e exited {proc.returncode}: {proc.stderr}')
else:
    names = json.loads(proc.stdout)
    if names[0] == names[1]:
        fail(f'two distinct fk_id URLs collided: {names[0]!r} == {names[1]!r}')
    if names[0] != 'DocumentsList_showmaster_records_fk_id_1411':
        fail(f'unexpected filename for query-distinguished URL: {names[0]!r}')
    if names[2] != '1411':
        fail(f'path-distinguished URL should be unaffected: {names[2]!r}')
    if names[3] != 'TH_IMG_R1411_I6595_P1.png':
        fail(f'?file= param should still win: {names[3]!r}')
    if len(set(names)) != len(names):
        fail(f'not all filenames distinct: {names}')

if fails:
    print(f'{fails} failure(s)')
    sys.exit(1)
print('ok')
