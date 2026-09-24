#!/usr/bin/env python3
"""Offline smoke test for tools/decode_browser_login.js: no network, no credentials, no node_modules resolution
beyond what --help needs. Confirms the usage text advertises --fetch/--fetch-page/--delay and that invoking with
too few arguments exits 2 without touching Playwright (which would require DECODE_USER/DECODE_PASS and network).
Run: python3 tools/tests/test_decode_browser_login_help.py"""
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCRIPT = os.path.join(ROOT, 'tools', 'decode_browser_login.js')

env = dict(os.environ)
env.pop('DECODE_USER', None)
env.pop('DECODE_PASS', None)
node_root = subprocess.run(['npm', 'root', '-g'], cwd=ROOT, capture_output=True, text=True, timeout=30).stdout.strip()
if node_root:
    env['NODE_PATH'] = node_root

proc = subprocess.run(['node', SCRIPT, '--help'], cwd=ROOT, env=env, capture_output=True, text=True, timeout=30)

fails = 0
if proc.returncode != 2:
    print(f'FAIL: exit code {proc.returncode}, expected 2')
    fails += 1
usage = proc.stderr
for token in ('--fetch', '--fetch-page', '--delay', 'RECORD_ID', 'OUT_DIR'):
    if token not in usage:
        print(f'FAIL: usage text missing {token!r}')
        fails += 1

if fails:
    print(f'{fails} failure(s)')
    sys.exit(1)
print('ok: decode_browser_login.js --help exits 2 with usage mentioning --fetch/--fetch-page/--delay')
