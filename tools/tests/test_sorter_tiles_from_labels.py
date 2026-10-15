#!/usr/bin/env python3
"""Offline test of SORTER-STEP1-INK63 (15 Oct 2026): tools/sign_sorter.py --tiles-from PAGE.html --labels L.tsv (no --piles-from).
Catches: tiles that survive only inside a committed sorter page (no crop on disk) dropped from a new page; a sid in no page silently
lost when --signs/--pages can cut it. Must NOT change: the piles are exactly --labels (no pile invented or merged); a tile reused from a
page keeps that page's image bytes; a sid in neither source is skipped and counted; with --piles-from the old path is untouched. Also tools/sorter_preflight.py --step1 (check 2 inverted:
the question box must be empty on a step-1 page; the default still fails an empty box)."""
import json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
from PIL import Image, ImageDraw

fails = 0
def check(name, ok, extra=''):
    global fails
    print('PASS' if ok else 'FAIL', name, extra if not ok else ''); fails += not ok

def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True); open(path, 'w').write(text); return path

def run(*args):
    return subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'sign_sorter.py'), *args, '--no-preflight'],
                          capture_output=True, text=True)

d = tempfile.mkdtemp(prefix='tiles_from_labels_')
for name, shape in (('A', 'ellipse'), ('B', 'rectangle')):
    os.makedirs(os.path.join(d, name, 'pages'))
    im = Image.new('L', (400, 80), 255); g = ImageDraw.Draw(im); rows = ['sid\tpage\tx\ty\tw\th']
    for i in range(5):
        x = 20 + i * 70; getattr(g, shape)((x, 22, x + 30, 58), outline=0, width=4)
        rows.append(f'{name}_{i}\tL{name}\t{x - 2}\t16\t36\t48')
    im.save(os.path.join(d, name, 'pages', f'L{name}.png'))
    w(os.path.join(d, name, 'signs.tsv'), '\n'.join(rows) + '\n')
# page 1 holds the A tiles only (built the ordinary way, JPEG tiles at half page scale, as the Vivonne pages)
w(os.path.join(d, 'labA.tsv'), 'sid\tsign\n' + ''.join(f'A_{i}\tq\n' for i in range(5)))
r = run('--signs', os.path.join(d, 'A', 'signs.tsv'), '--labels', os.path.join(d, 'labA.tsv'), '--pages', os.path.join(d, 'A', 'pages'),
        '--tile-quality', '85', '--page-scale', '0.5', '--title', 't', '--out', os.path.join(d, 'p1.html'), '--data-out', os.path.join(d, 'p1.json'))
check('fixture page builds', r.returncode == 0, r.stderr[-400:])
p1 = {it['sid']: it['img'] for p in json.load(open(os.path.join(d, 'p1.json')))['piles'] for it in p['items']}
# new page: blind shape piles over A tiles (from page 1) and B tiles (cut from disk), plus one sid in neither source
w(os.path.join(d, 'lab.tsv'), 'sid\tsign\tfamily\n' + 'A_0\tshape 01\tshapes\nA_1\tshape 01\tshapes\nA_2\tshape 02\tshapes\n'
  'B_0\tshape 02\tshapes\nB_1\tshape 03\tshapes\nB_2\tshape 03\tshapes\nB_3\tshape 03\tshapes\nZ_9\tshape 03\tshapes\n')
r = run('--tiles-from', os.path.join(d, 'p1.html'), '--signs', os.path.join(d, 'B', 'signs.tsv'), '--pages', os.path.join(d, 'B', 'pages'),
        '--labels', os.path.join(d, 'lab.tsv'), '--seed-shape', '--title', 't', '--out', os.path.join(d, 'p2.html'), '--data-out', os.path.join(d, 'p2.json'))
check('tiles-from + labels builds', r.returncode == 0, r.stderr[-400:])
check('report counts disk cuts and skips', '7 tiles in 3 piles (4 cut from --signs/--pages), 1 skipped' in r.stdout, r.stdout)
dd = json.load(open(os.path.join(d, 'p2.json')))
piles = {p['id']: sorted(it['sid'] for it in p['items']) for p in dd['piles']}
check('piles are exactly --labels', piles == {'shape 01': ['A_0', 'A_1'], 'shape 02': ['A_2', 'B_0'], 'shape 03': ['B_1', 'B_2', 'B_3']}, piles)
check('a reused tile keeps its page bytes', all(it['img'] == p1[it['sid']] for p in dd['piles'] for it in p['items'] if it['sid'] in p1))
check('both line images embedded', set(dd['pages']) == {'LA', 'LB'}, list(dd['pages']))
check('one tile format and scale', dd['tileMime'] == 'image/jpeg' and dd['pageScale'] == 0.5, (dd['tileMime'], dd['pageScale']))
check('oddness on every tile', all('d' in it for p in dd['piles'] for it in p['items']))
check('blind page', dd.get('mode') == 'blind')
r = run('--tiles-from', os.path.join(d, 'p1.html'), '--title', 't', '--out', os.path.join(d, 'p3.html'))
check('--tiles-from without --labels or --piles-from is refused', r.returncode != 0 and '--labels' in r.stderr, r.stderr[-300:])
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sorter_preflight as pf
ok, line = pf.check_answerable(dd, step1=True)
check('preflight --step1: a page with no questions and >= 2 named piles passes', ok, line)
ok, line = pf.check_answerable(dd)
check('preflight without --step1: the same page still fails (focus box empty)', not ok and 'focus box empty' in line, line)
dq = dict(dd, focus=[{'sid': 'A_0', 'q': 'which pile?'}])
ok, line = pf.check_answerable(dq, step1=True)
check('preflight --step1: a step-1 page carrying a question fails', not ok and 'asks none' in line, line)
print('ALL PASS' if not fails else f'{fails} FAILED'); sys.exit(1 if fails else 0)
