#!/usr/bin/env python3
"""Offline test for tools/decode_browser_login.js's guessFullsizeName() and scanFilesrvLinks() helpers, added
24 Sept 2026 (LANE N2 dcB, DECODE full-size image access test). No network, no credentials: require.main !==
module skips the login IIFE entirely.
Run: python3 tools/tests/test_decode_browser_login_guessfullsize.py"""
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


node_src = r"""
const { guessFullsizeName, scanFilesrvLinks } = require(%r);
const out = {};
out.thumb = guessFullsizeName('TH_IMG_R1162_I5837_P1.png');
out.notThumb = guessFullsizeName('DOC_8725_2024-Oct-12-01-36-20_15694.txt');

const html = '<img src="/decrypt-custom/filesrv/?file=TH_IMG_R8725_I40320_P1.jpg" alt="IMG_R8725_I40320_P1.jpg">'
  + '<a href="/decrypt-custom/filesrv/?file=DOC_8725_1.jpg">doc</a>';
const seen = new Set();
const queue = [];
scanFilesrvLinks(html, queue, seen, 10, true);
out.withGuess = queue.slice();

const seen2 = new Set();
const queue2 = [];
scanFilesrvLinks(html, queue2, seen2, 10, false);
out.withoutGuess = queue2.slice();

const seenCap = new Set();
const queueCap = [];
scanFilesrvLinks(html, queueCap, seenCap, 1, true);
out.capped = queueCap.slice();

console.log(JSON.stringify(out));
""" % (SCRIPT,)

proc = subprocess.run(['node', '-e', node_src], cwd=ROOT, capture_output=True, text=True, timeout=30)
if proc.returncode != 0:
    fail(f'node -e exited {proc.returncode}: {proc.stderr}')
else:
    out = json.loads(proc.stdout)
    if out['thumb'] != 'IMG_R1162_I5837_P1.png':
        fail(f"guessFullsizeName should strip TH_ prefix: {out['thumb']!r}")
    if out['notThumb'] is not None:
        fail(f"guessFullsizeName should return null for a non-TH_ name: {out['notThumb']!r}")
    with_guess = out['withGuess']
    if not any('file=IMG_R8725_I40320_P1.jpg' in u for u in with_guess):
        fail(f'--guess-fullsize should queue the un-prefixed full-size guess: {with_guess}')
    if not any('file=TH_IMG_R8725_I40320_P1.jpg' in u for u in with_guess):
        fail(f'the original thumbnail link should still be queued: {with_guess}')
    if not any('file=DOC_8725_1.jpg' in u for u in with_guess):
        fail(f'a non-TH_ filesrv link should still be queued unchanged: {with_guess}')
    without_guess = out['withoutGuess']
    if any('IMG_R8725_I40320_P1.jpg' == u.split('file=')[-1] for u in without_guess):
        fail(f'without --guess-fullsize, no un-prefixed guess should be queued: {without_guess}')
    if len(out['capped']) != 1:
        fail(f'maxFiles=1 should cap the queue at one entry: {out["capped"]}')

if fails:
    print(f'{fails} failure(s)')
    sys.exit(1)
print('ok')
