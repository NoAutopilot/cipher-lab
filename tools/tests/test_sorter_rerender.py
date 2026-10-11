#!/usr/bin/env python3
"""Offline test for tools/sorter_rerender.py: build a tiny sorter page, render it on an OLD-style shell (only the
`const DATA = ...;` line, <title> and lede kept), re-render it, and check the data, title and lede survive byte for
byte and the new page carries the current template's "Fix the cut". Must NOT accept a page with no DATA line.
Run: python3 tools/tests/test_sorter_rerender.py"""
import json, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss, sorter_rerender as rr
from PIL import Image

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

with tempfile.TemporaryDirectory() as d:
    d = Path(d); (d / 'pages').mkdir()
    Image.new('L', (60, 40), 255).save(d / 'pages' / 'p1.png')
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\ns1\tp1\t5\t5\t10\t20\ns2\tp1\t30\t5\t10\t20\n')
    (d / 'labels.tsv').write_text("sid\tsign\tfamily\ns1\tA\tA\ns2\t0'\t0\n")
    data = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'))
    data['focus'] = [{'sid': 's2', 'q': 'A or 0\'? </script>'}]
    old = ('<!doctype html><title>Old &amp; Sorter</title><p class="lede">Lede &lt;x&gt;</p>\n<script>\nconst DATA = '
           + json.dumps(data).replace('</', '<\\/') + ';\n</script>')
    (d / 'old.html').write_text(old)
    rc = rr.main([str(d / 'old.html'), '--out', str(d / 'new.html')])
    new = (d / 'new.html').read_text()
    got = rr.extract(new)
    check('exit 0', rc == 0)
    check('data carried over unchanged', got and got[0] == {k: v for k, v in data.items() if not k.startswith('_')})
    check('title and lede unescaped once, re-escaped once', got and got[1] == 'Old & Sorter' and got[2] == 'Lede <x>')
    check('new page has Fix the cut', 'Fix the cut' in new)
    # template 2026-10-09.1: --focus-to-tray is a page option outside DATA, on by default
    check('default re-render: focus-to-tray on', 'const OPTS = {"focusToTray": true};' in new)
    rc = rr.main([str(d / 'old.html'), '--out', str(d / 'off.html'), '--no-focus-to-tray'])
    off = (d / 'off.html').read_text(); got_off = rr.extract(off)
    check('--no-focus-to-tray: option off, DATA still carried over unchanged', rc == 0 and 'const OPTS = {"focusToTray": false};' in off
          and got_off and got_off[0] == got[0])
    rc = rr.main([str(d / 'off.html'), '--out', str(d / 'keep.html')])   # a new-template page re-renders too (its OPTS line is not DATA)
    check('re-rendering a new-template page with no flag: DATA unchanged, its own option carried over (off stays off)',
          rc == 0 and rr.extract((d / 'keep.html').read_text())[0] == got[0] and 'const OPTS = {"focusToTray": false};' in (d / 'keep.html').read_text())
    rc = rr.main([str(d / 'off.html'), '--out', str(d / 'on.html'), '--focus-to-tray'])
    check('...and the flag still overrides it', rc == 0 and 'const OPTS = {"focusToTray": true};' in (d / 'on.html').read_text())
    check('page_opts: reads the OPTS line, None for a page without one', rr.page_opts(off) == {'focusToTray': False} and rr.page_opts('<html>') is None)
    # template 2026-10-09.6: the box-check key is a page option too (OPTS.key = 'box'), set by --key box, kept on a re-render
    rc = rr.main([str(d / 'old.html'), '--out', str(d / 'key.html'), '--key', 'box'])
    key = (d / 'key.html').read_text()
    check('--key box: a page built without the key gains it (OPTS key box), DATA unchanged',
          rc == 0 and rr.page_opts(key) == {'focusToTray': True, 'key': 'box'} and rr.extract(key)[0] == got[0])
    rc = rr.main([str(d / 'key.html'), '--out', str(d / 'key2.html')])
    check('re-rendering a key page with no flag keeps the key', rc == 0 and rr.page_opts((d / 'key2.html').read_text()).get('key') == 'box')
    rc = rr.main([str(d / 'key.html'), '--out', str(d / 'key3.html'), '--no-focus-to-tray'])
    check('...and keeps it when only the other option changes', rc == 0 and rr.page_opts((d / 'key3.html').read_text()) == {'focusToTray': False, 'key': 'box'})
    rc = rr.main([str(d / 'key.html'), '--out', str(d / 'nokey.html'), '--key', 'none'])
    check('--key none takes it off (no key in OPTS)', rc == 0 and 'key' not in rr.page_opts((d / 'nokey.html').read_text()))
    rc = rr.main([str(d / 'nokey.html'), '--out', str(d / 'nokey2.html')])
    check('a page without the key re-renders without it (must not add a key nobody asked for)', rc == 0 and 'key' not in rr.page_opts((d / 'nokey2.html').read_text()))
    # a page hand-patched by the 10 Oct 2026 scratch script box_key.py: its <style id="boxKeyCss"> block marks it; the re-render keeps the key
    (d / 'patched.html').write_text(old.replace('</p>\n<script>', '</p><style id="boxKeyCss">#boxKey{}</style><details id="boxKey" open></details>\n<script>'))
    rc = rr.main([str(d / 'patched.html'), '--out', str(d / 'patched2.html')])
    p2 = (d / 'patched2.html').read_text()
    check('a box_key.py-patched page (no OPTS line) keeps its key on the re-render, and the old patch block is not carried over',
          rc == 0 and rr.page_opts(p2) == {'focusToTray': True, 'key': 'box'} and 'id="boxKeyCss"' not in p2 and p2.count('id="boxKey"') == 1)
    (d / 'bad.html').write_text('<html>no data</html>')
    check('page with no DATA line refused (exit 2)', rr.main([str(d / 'bad.html'), '--out', str(d / 'x.html')]) == 2)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
