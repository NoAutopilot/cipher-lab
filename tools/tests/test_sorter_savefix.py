#!/usr/bin/env python3
"""Offline test for sign-sorter template 2026-10-20.1, the save state machine (SORTER-SAVEFIX, 20 Oct 2026; incident:
ciphers/fr16104-vivonne-spain-1572/tx/ksplit/sorter/SAVE-INCIDENT-2026-10-20.md -- the owner's Vivonne blind sort was mostly lost).

Static half (always runs): tools/sign_sorter/template.html carries the 2026-10-20.1 marker; every write goes through commitDoc's
read-back (`.get()`), a refused write is re-scheduled (no "retry once, then drop"), at most WMAX writes in flight; the banner
#saveBan and the recovery box #recover exist; nothing writes the old 'sorter:all' key any more (it is read, for recovery only).
Browser half (tools/sign_sorter/browser_tests/test_save.js, headless Chromium against mock_db.js, on make_fixtures.py's plain.html):
connecting -> held -> pumped (read-back, "All changes saved"); refused -> visible "NOT saved" + retry -> lands by itself; an
unconfirmed read-back is not "saved"; a burst keeps <= 2 in flight; this-browser-only mode is labelled and "Recover my sort from
this browser" brings it into storage on confirm (also an older page's 'sorter:all' copy, and a journal of refused writes), never
over a differing stored document unless ticked.
Must catch: a writer that resolves without a read-back; a failure that clears itself silently; a local-only session never offered
back. Must NOT block: a machine with no node/playwright/Chromium -- the browser half prints SKIP (and why), the static half runs.
Run: python3 tools/tests/test_sorter_savefix.py
"""
import os, re, shutil, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
BT = ROOT / 'tools' / 'sign_sorter' / 'browser_tests'
fails = 0
def check(name, ok, extra=''):
    global fails
    print('PASS' if ok else 'FAIL', name, extra); fails += not ok

t = (ROOT / 'tools' / 'sign_sorter' / 'template.html').read_text()
check('template marker 2026-10-20.1', 'content="2026-10-20.1"' in t)
check('every write is read back', 'await w.ref.get()' in t and "code: 'unconfirmed'" in t)
check('a refused write is re-scheduled, not dropped', 'schedule(path)' in t and 'function schedule(path)' in t)
check('at most WMAX writes in flight', re.search(r'WMAX = \d', t) is not None and 'wactive >= WMAX' in t)
check('banner and recovery box present', 'id="saveBan"' in t and 'id="recover"' in t and 'Recover my sort from this browser' in t)
check("the old 'sorter:all' key is never written", "setItem('sorter:all'" not in t and re.search(r'setItem\(LEGACY\s*,', t) is None)

node, exe = shutil.which('node'), os.environ.get('PW_EXE', '/opt/pw-browsers/chromium')
if not node or not os.path.exists(exe):
    print('SKIP browser half: node or Chromium missing')
else:
    with tempfile.TemporaryDirectory() as d:
        subprocess.run([sys.executable, str(BT / 'make_fixtures.py'), d], capture_output=True, text=True)   # region fixtures need scipy; plain.html does not
        if not os.path.exists(os.path.join(d, 'plain.html')):
            print('SKIP browser half: make_fixtures.py built no plain.html')
        else:
            env = dict(os.environ, PW_EXE=exe)
            env.setdefault('NODE_PATH', subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip())
            r = subprocess.run([node, 'test_save.js', os.path.join(d, 'plain.html')], cwd=BT, capture_output=True, text=True, env=env, timeout=600)
            out = r.stdout + r.stderr
            if "Cannot find module 'playwright'" in out:
                print('SKIP browser half: playwright not installed')
            else:
                print(out.strip()); check('browser half (test_save.js)', r.returncode == 0)
print('ALL PASS' if not fails else '%d FAILED' % fails); sys.exit(1 if fails else 0)
