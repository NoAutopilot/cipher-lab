#!/usr/bin/env python3
"""Build the synthetic sign-sorter pages the browser tests run on (QA pass, 3 Oct 2026).

  python3 tools/sign_sorter/browser_tests/make_fixtures.py OUT_DIR

Writes OUT_DIR/plain.html (two pages, piles X / X-DOT / Y in family X and Z in family Z, 8 "Check these first" tiles on
both pages, so test_qa.js has a cross-page step) and OUT_DIR/cluster.html (the same plus --auto-clusters and a
--rank-confusion box, which test_cluster_rank.js needs) and OUT_DIR/refs.html (plain + --refs, for test_refs.js). Shapes are drawn with PIL; no real manuscript is used."""
import subprocess, sys
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[3]
out = Path(sys.argv[1]); (out / 'pages').mkdir(parents=True, exist_ok=True)
shapes = {'X': lambda g, x, y: (g.line((x, y, x + 20, y + 30), fill=0, width=3), g.line((x + 20, y, x, y + 30), fill=0, width=3)),
          'X-DOT': lambda g, x, y: (shapes['X'](g, x, y), g.ellipse((x + 8, y - 9, x + 13, y - 4), fill=0)),
          'Y': lambda g, x, y: (g.line((x, y, x + 10, y + 15), fill=0, width=3), g.line((x + 20, y, x + 10, y + 15), fill=0, width=3),
                                g.line((x + 10, y + 15, x + 10, y + 30), fill=0, width=3)),
          'Z': lambda g, x, y: (g.line((x, y, x + 20, y), fill=0, width=3), g.line((x + 20, y, x, y + 30), fill=0, width=3),
                                g.line((x, y + 30, x + 20, y + 30), fill=0, width=3))}
seq = {'p1': 'X Y X Z X X-DOT Y X X Z X Y'.split(), 'p2': 'X Z Y X X X-DOT Y Z X X Y X'.split()}
signs, labels = ['sid\tpage\tx\ty\tw\th'], ['sid\tsign\tfamily']
for page, row in seq.items():
    im = Image.new('L', (60 + 45 * len(row), 110), 250); g = ImageDraw.Draw(im)
    for i, s in enumerate(row):
        x, y = 30 + 45 * i, 40 + (i % 3) * 4
        shapes[s](g, x, y)
        sid = '%s_%02d' % (page, i + 1)
        signs.append('%s\t%s\t%d\t%d\t21\t31' % (sid, page, x, y)); labels.append('%s\t%s\t%s' % (sid, s, 'Z' if s == 'Z' else 'X'))
    im.save(out / 'pages' / (page + '.png'))
(out / 'signs.tsv').write_text('\n'.join(signs) + '\n'); (out / 'labels.tsv').write_text('\n'.join(labels) + '\n')
focus = ['p1_02', 'p1_05', 'p1_09', 'p2_02', 'p2_06', 'p2_09', 'p1_12', 'p2_12', 'p9_99']
(out / 'focus.tsv').write_text(''.join('%s\tL1.%s: reader A read X, reader B read Y; X or Y?\n' % (s, s[-2:]) for s in focus))
(out / 'confusion.tsv').write_text('label_a\tlabel_b\tn\nX\tY\t9\nX\tX-DOT\t4\nY\tZ\t2\n')
base = [sys.executable, str(ROOT / 'tools' / 'sign_sorter.py'), '--signs', str(out / 'signs.tsv'), '--labels', str(out / 'labels.tsv'),
        '--pages', str(out / 'pages'), '--focus', str(out / 'focus.tsv'), '--title', 'Fixture sorter', '--lede', 'Synthetic test page.']
subprocess.run(base + ['--out', str(out / 'plain.html')], check=True)
(out / 'refs.tsv').write_text('sid\np1_01\np1_07\np2_03\n')   # two X, one Y: locked reference tiles (test_refs.js)
subprocess.run(base + ['--refs', str(out / 'refs.tsv'), '--out', str(out / 'refs.html')], check=True)
subprocess.run(base + ['--auto-clusters', '2', '--rank-confusion', str(out / 'confusion.tsv'), '--out', str(out / 'cluster.html')], check=True)
