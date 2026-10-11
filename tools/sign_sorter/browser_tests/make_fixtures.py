#!/usr/bin/env python3
"""Build the synthetic sign-sorter pages the browser tests run on (QA pass, 3 Oct 2026).

  python3 tools/sign_sorter/browser_tests/make_fixtures.py OUT_DIR

Writes OUT_DIR/plain.html (two pages, piles X / X-DOT / Y in family X and Z in family Z, 8 "Check these first" tiles on
both pages, so test_qa.js has a cross-page step) and OUT_DIR/cluster.html (the same plus --auto-clusters and a
--rank-confusion box, which test_cluster_rank.js needs) and OUT_DIR/refs.html (plain + --refs, for test_refs.js) and OUT_DIR/region.html (SORTER-PAGEVIEW: a sloped three-line region cut by
tools/sorter_recut.py into deskewed strips r_L01-r_L03, built with --region, for test_pageview.js). Shapes are drawn with PIL; no real manuscript is used.
Template 2026-10-09.1: plain, refs and cluster are built with --no-focus-to-tray (the in-pile layout the older tests drive);
OUT_DIR/tray.html is plain on the default (the focus tiles start in the "Taken out" tray), for test_focus_tray.js, with tray_rank.html
(a "Most useful first" box with tiles of its own), tray_rank_in.html (a rank box that only repeats the focus tiles) and cluster_tray.html
(--auto-clusters on the default) and tray_key.html (the default plus --key box: the box-check key, template 2026-10-09.6)."""
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
subprocess.run(base + ['--no-focus-to-tray', '--out', str(out / 'plain.html')], check=True)
subprocess.run(base + ['--out', str(out / 'tray.html')], check=True)   # default: questions start in the tray (test_focus_tray.js)
(out / 'refs.tsv').write_text('sid\np1_01\np1_07\np2_03\n')   # two X, one Y: earlier-pick tiles with a green check, correctable (test_refs.js)
subprocess.run(base + ['--no-focus-to-tray', '--refs', str(out / 'refs.tsv'), '--out', str(out / 'refs.html')], check=True)
subprocess.run(base + ['--no-focus-to-tray', '--auto-clusters', '2', '--rank-confusion', str(out / 'confusion.tsv'), '--out', str(out / 'cluster.html')], check=True)
(out / 'rank.tsv').write_text('sid\tscore\talt\twhy\np1_01\t9\tY\tX or Y?\np1_02\t5\tX\tY or X?\np2_04\t3\tZ\tX or Z?\n')   # two tiles outside the focus list
subprocess.run(base + ['--rank', str(out / 'rank.tsv'), '--out', str(out / 'tray_rank.html')], check=True)   # tray + a "Most useful first" box
(out / 'rank_in.tsv').write_text('sid\tscore\talt\twhy\np1_02\t9\tX\tY or X?\np1_05\t5\tY\tX or Y?\n')   # every rank tile also a focus tile
subprocess.run(base + ['--rank', str(out / 'rank_in.tsv'), '--out', str(out / 'tray_rank_in.html')], check=True)   # tray: the rank box is not shown
subprocess.run(base + ['--auto-clusters', '2', '--out', str(out / 'cluster_tray.html')], check=True)   # tray + provisional shape groups (cluster offer)
subprocess.run(base + ['--key', 'box', '--out', str(out / 'tray_key.html')], check=True)   # tray + the box-check key (template 2026-10-09.6, test_s2_fix.js)

# region.html (SORTER-PAGEVIEW, 4 Oct 2026): three sloped lines on one region image, recut into deskewed strips, "Whole page" view
sys.path.insert(0, str(ROOT / 'tools')); import numpy as np, sorter_recut as sr
RW, RH, RP, SL = 1300, 520, 120, 0.06
reg = Image.new('L', (RW, RH), 245); g = ImageDraw.Draw(reg); rows = ['X Y Z X X-DOT Y X Z X Y X Z X Y X Z X Y X Z X Y X X'.split()[:22]] * 3
traces, cols, cents = [], [], []
for n, row in enumerate(rows):
    base = 110 + n * RP; xs = []
    for i, sg in enumerate(row):
        x = 40 + 56 * i; shapes[sg](g, x, int(base + SL * x) - 15); xs.append(x + 10)
    traces.append(np.array([base + SL * x for x in range(RW)], float)); cols.append([(sg, 'Z' if sg == 'Z' else 'X') for sg in row]); cents.append(xs)
g.line((0, 300, RW, 300 + SL * RW), fill=120, width=1)   # a long ruled stroke between lines 2 and 3 (shows on the page, not in a strip)
rd = out / 'region'; rd.mkdir(exist_ok=True); reg.save(rd / 'region.png')
sr.run(np.array(reg), traces, ['r_L01', 'r_L02', 'r_L03'], cols, cents, rd, rd / 'pages', sr.Cfg(pitch=RP, half=60, nclu=4, clear=20),
       region_image=str(rd / 'region.png'))
subprocess.run([sys.executable, str(ROOT / 'tools' / 'sign_sorter.py'), '--signs', str(rd / 'signs.tsv'), '--labels', str(rd / 'labels.tsv'),
                '--pages', str(rd / 'pages'), '--region', str(rd / 'region.json'), '--title', 'Fixture region sorter', '--lede', 'Synthetic region.',
                '--out', str(out / 'region.html')], check=True)
