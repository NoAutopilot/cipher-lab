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
    (d / 'bad.html').write_text('<html>no data</html>')
    check('page with no DATA line refused (exit 2)', rr.main([str(d / 'bad.html'), '--out', str(d / 'x.html')]) == 2)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
