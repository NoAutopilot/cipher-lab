#!/usr/bin/env python3
"""Offline test for the box-check key, a sign-sorter page option (template 2026-10-09.6; owner, 10 Oct 2026, on a box-check
page: "add a simple key at the top explaining what to do in different situations with examples").

tools/sign_sorter.py --key box bakes `"key": "box"` into the page's `const OPTS = {...};` line (outside DATA); a build without
--key carries no key in OPTS and DATA is the same byte for byte. The template holds the key block itself ("What to do: a key",
`<details id="boxKey" ... hidden>`, shown by the page script only when OPTS.key is 'box' and removed otherwise); its drawings are
neutral shapes and tell the machine's box from the fixed box by outline (solid vs dashed), never by colour alone; its fold state
is kept in localStorage behind try/catch. tools/sorter_rerender.py keeping or adding the key is tested in test_sorter_rerender.py.
Must NOT: add a key to a page built without --key; accept an unknown key. Run: python3 tools/tests/test_sign_sorter_key.py"""
import json, re, subprocess, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss, sorter_rerender as rr
from PIL import Image

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

tpl = (ROOT / 'tools' / 'sign_sorter' / 'template.html').read_text()
with tempfile.TemporaryDirectory() as d:
    d = Path(d); (d / 'pages').mkdir()
    Image.new('L', (60, 40), 255).save(d / 'pages' / 'p1.png')
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\ns1\tp1\t5\t5\t10\t20\ns2\tp1\t30\t5\t10\t20\n')
    (d / 'labels.tsv').write_text('sid\tsign\tfamily\ns1\tA\tA\ns2\tB\tB\n')
    base = [sys.executable, str(ROOT / 'tools' / 'sign_sorter.py'), '--signs', str(d / 'signs.tsv'), '--labels', str(d / 'labels.tsv'),
            '--pages', str(d / 'pages'), '--title', 'Key test', '--no-preflight']
    r0 = subprocess.run(base + ['--out', str(d / 'plain.html')], capture_output=True, text=True)
    r1 = subprocess.run(base + ['--out', str(d / 'key.html'), '--key', 'box'], capture_output=True, text=True)
    r2 = subprocess.run(base + ['--out', str(d / 'bad.html'), '--key', 'nope'], capture_output=True, text=True)
    plain, key = (d / 'plain.html').read_text(), (d / 'key.html').read_text()
    check('both builds exit 0', r0.returncode == 0 and r1.returncode == 0)
    check('--key box: OPTS carries key box', rr.page_opts(key) == {'focusToTray': True, 'key': 'box'})
    check('no --key: OPTS carries no key (a build without the flag shows no key)', rr.page_opts(plain) == {'focusToTray': True})
    check('the two builds carry the same DATA', rr.extract(plain)[0] == rr.extract(key)[0])
    check('an unknown --key is refused by the CLI (exit 2)', r2.returncode == 2 and 'invalid choice' in r2.stderr)
    try:
        ss.render(rr.extract(plain)[0], 'x', 'y', key='nope'); bad = False
    except ValueError:
        bad = True
    check('render(key=...) refuses an unknown key', bad)

# the template's key block and its script
m = re.search(r'<details id="boxKey"[^>]*>(.*?)</details>', tpl, re.S)
check('the template holds the key block once, hidden until the page script shows it', bool(m) and tpl.count('<details id="boxKey"') == 1
      and re.search(r'<details id="boxKey"[^>]*\bhidden\b', tpl) is not None)
blk = m.group(1) if m else ''
cases = ['One sign, the box fits it', 'Two signs in one box', 'One sign cut into two boxes', 'The box cuts off part of the sign',
         'stain', 'A sign with no box', 'A dot or tick', 'Not sure']
check('it has a row for each case (one sign fits / two in one box / one cut in two / box cuts the sign / stain or shadow / no box / dot or tick / not sure)',
      all(c in blk for c in cases) and blk.count('<tr>') == len(cases))
check('and a step-2 line naming its "Fix the cut" (the button template 2026-10-09.6 adds to step 2)', 'Step 2' in blk and 'Fix the cut' in blk and 'id="s2Fix"' in tpl)
svgs = re.findall(r'<svg.*?</svg>', blk, re.S)
befaft = [s for s in svgs if 'translate(' in s]
check('the drawings are inline shapes (no image, no real sign), one per row', len(svgs) == len(cases) and '<img' not in blk)
check('every before/after drawing tells the boxes apart by outline: a solid box before, a dashed one after (not by colour alone)',
      befaft and all(re.search(r'<rect(?![^>]*dasharray)[^>]*/>', s.split('translate(')[0]) and 'stroke-dasharray' in s.split('translate(')[1] for s in befaft)
      and len({c for s in svgs for c in re.findall(r'stroke="(#[0-9A-Fa-f]{6})"', s)}) <= 1)
check('the legend says so in words', 'solid outline' in blk and 'dashed' in blk)
text = re.sub(r'<[^>]+>', ' ', blk)
check('no person-facing colour word in the key (owner is red-green colour-blind)', not re.search(r'\b(red|green|orange|blue)\b', text, re.I))
js = re.search(r"\(function\(\)\{ const k = document.getElementById\('boxKey'\);.*?\}\)\(\);", tpl, re.S)
check('the page script shows it only for OPTS.key box and removes it otherwise', bool(js) and "OPTS.key === 'box'" in js.group(0) and 'k.remove()' in js.group(0))
check('its fold state is remembered per browser, every localStorage call inside try/catch',
      bool(js) and js.group(0).count('localStorage') == 2 and js.group(0).count('try {') == 2)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
