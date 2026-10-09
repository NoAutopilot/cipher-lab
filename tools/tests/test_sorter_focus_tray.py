#!/usr/bin/env python3
"""Offline test for sign-sorter template 2026-10-09.1, "questions start in the tray" (owner, 9 Oct 2026, Harley 287).

Builds the synthetic fixtures (tools/sign_sorter/browser_tests/make_fixtures.py: no real manuscript) and checks:
 - static: tray.html carries OPTS.focusToTray true, plain.html (built --no-focus-to-tray) false, both on the current template
   marker (the preflight's template line passes);
 - browser (tools/sign_sorter/browser_tests/test_focus_tray.js, headless Chromium against mock_db.js, phone and desktop):
   the focus tiles start in the "Taken out" tray and the page lands on step 2, tile 1, its own pile the first card; one tap
   there is a keep (db 'checked'), not a move; nothing is written at load; a tile with a saved move or keep (db, or
   browser-only storage) is never re-trayed; all answered -> back on step 1; "Most useful first" tiles wait too;
   --no-focus-to-tray keeps the old layout.
Must NOT block: a machine with no node/playwright -- the browser half prints SKIP (and says why), the static half still runs.
Run: python3 tools/tests/test_sorter_focus_tray.py
"""
import os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sorter_preflight as pf

BT = ROOT / 'tools' / 'sign_sorter' / 'browser_tests'
fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

with tempfile.TemporaryDirectory() as d:
    r = subprocess.run([sys.executable, str(BT / 'make_fixtures.py'), d], capture_output=True, text=True)
    check('fixtures built', r.returncode == 0)
    tray, plain = (Path(d) / 'tray.html').read_text(), (Path(d) / 'plain.html').read_text()
    check('tray.html: focusToTray on (the default)', 'const OPTS = {"focusToTray": true};' in tray)
    check('plain.html: focusToTray off (--no-focus-to-tray)', 'const OPTS = {"focusToTray": false};' in plain)
    cur = pf.current_marker()
    check(f'both on the current template marker ({cur}) and the preflight template line passes',
          all(re.search(r'content="([^"]+)"', h.split('sign-sorter-template')[1]).group(1) == cur and pf.check_template(h)[0] for h in (tray, plain)))
    node = shutil.which('node')
    npm_root = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip() if shutil.which('npm') else ''
    exe = os.environ.get('PW_EXE', '/opt/pw-browsers/chromium')
    have = node and npm_root and (Path(npm_root) / 'playwright').exists() and os.path.exists(exe)
    if not have:
        print('SKIP browser half: needs node, a global playwright and Chromium at $PW_EXE (' + exe + ')')
    else:
        env = dict(os.environ, NODE_PATH=npm_root, PW_EXE=exe)
        r = subprocess.run([node, 'test_focus_tray.js', d], cwd=BT, env=env, capture_output=True, text=True, timeout=900)
        bad = [l for l in r.stdout.splitlines() if l.startswith('FAIL')]
        print(f'browser: {sum(l.startswith("PASS") for l in r.stdout.splitlines())} PASS, {len(bad)} FAIL (test_focus_tray.js)')
        for l in bad: print('  ' + l)
        check('browser behaviour (test_focus_tray.js)', r.returncode == 0 and not bad)
        if r.returncode and not bad: print(r.stderr[-2000:])
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
