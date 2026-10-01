#!/usr/bin/env python3
"""Offline test for tools/sign_sorter.py: a synthetic two-sign page, one sign with a mark above it.
Checks that the tile is cut around the mark (the Debosnys clipping lesson), piles and families come out,
oddness is computed, and the template placeholders are all filled. Run: python3 tools/tests/test_sign_sorter.py
(Browser click tests: tools/sign_sorter/browser_tests/*.js, run with node + playwright against a built page.)"""
import os, sys, tempfile
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sign_sorter as ss
from PIL import Image, ImageDraw

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

with tempfile.TemporaryDirectory() as d:
    d = Path(d); (d / 'pages').mkdir()
    im = Image.new('L', (200, 100), 255); g = ImageDraw.Draw(im)
    g.line((20, 40, 40, 70), fill=0, width=3); g.line((40, 40, 20, 70), fill=0, width=3)   # X at 20..40 x 40..70
    g.ellipse((28, 10, 33, 15), fill=0)                                                       # dot well above it
    g.line((100, 40, 120, 70), fill=0, width=3); g.line((120, 40, 100, 70), fill=0, width=3)
    im.save(d / 'pages' / 'p1.png')
    (d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\ns1\tp1\t20\t40\t21\t31\ns2\tp1\t100\t40\t21\t31\ns3\tp1\t300\t40\t5\t5\n')
    (d / 'labels.tsv').write_text('sid\tsign\tfamily\ns1\tX-DOT\tX\ns2\tX\tX\ns3\tX\tX\nmissing\tX\tX\n')
    (d / 'marks.tsv').write_text('mid\tpage\tx\ty\tw\th\tsid\nm1\tp1\t28\t5\t6\t6\ts1\n')
    data = ss.build(str(d / 'signs.tsv'), str(d / 'labels.tsv'), str(d / 'pages'), str(d / 'marks.tsv'))
    piles = {p['id']: p for p in data['piles']}
    check('two piles, family kept', set(piles) == {'X', 'X-DOT'} and piles['X-DOT']['family'] == 'X')
    s1 = piles['X-DOT']['items'][0]
    check('tile box grows to include the mark above', s1['b'][1] == 5 and s1['b'][3] == 66)
    check('missing sid and off-page box skipped (2 tiles, 2 skipped)', sum(len(p['items']) for p in data['piles']) == 2 and data['skipped'] == 2)
    check('oddness present', all('d' in it for p in data['piles'] for it in p['items']))
    check('page image embedded', 'p1' in data['pages'])
    html = ss.render(data, 'Test <Sorter>', 'Lede & more')
    check('placeholders filled and escaped', '__DATA__' not in html and '__TITLE__' not in html and '__LEDE__' not in html
          and 'Test &lt;Sorter&gt;' in html and 'Lede &amp; more' in html)
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)
