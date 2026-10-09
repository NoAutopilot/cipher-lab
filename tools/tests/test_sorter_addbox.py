#!/usr/bin/env python3
"""Offline test for the sign sorter's added boxes (MQS-SORTER-BOX, 9 Oct 2026): sign_sorter_apply.py's added.tsv export and
sorter_apply_recuts.py --added. Catches: a split's rest and a missed sign reaching signs.tsv and the tiles folder. Must NOT: give
an added box a label, keep a doc whose from tile is unknown, or move an existing tile on a re-run.
Page side: tools/sign_sorter/browser_tests/test_addbox.js. Run: python3 tools/tests/test_sorter_addbox.py"""
import csv, json, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from PIL import Image, ImageDraw
import sign_sorter_apply as sa
import sorter_apply_recuts as ar

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

d = Path(tempfile.mkdtemp()); (d / 'pages').mkdir()
for c in ('recuts', 'added'):
    (d / 'db' / c).mkdir(parents=True)
im = Image.new('L', (240, 80), 250); g = ImageDraw.Draw(im)
for x0 in (40, 70, 130, 180):   # four signs; the machine cut 40-90 as one box (two signs) and missed the one at 180
    g.rectangle((x0, 30, x0 + 18, 60), fill=0)
im.save(d / 'pages' / 'L01.png')
(d / 'signs.tsv').write_text('sid\tpage\tline\tpos\tx\ty\tw\th\nL01_01\tL01\tL01\t1\t40\t30\t49\t31\nL01_02\tL01\tL01\t2\t130\t30\t19\t31\n')
(d / 'labels.tsv').write_text('sid\tsign\nL01_01\tA\nL01_02\tB\n')
docs = {'recuts/L01_01': {'sid': 'L01_01', 'page': 'L01', 'x': 40, 'y': 30, 'w': 19, 'h': 31, 'old': [40, 30, 49, 31], 'at': 't',
                          'quad': [[40, 30], [59, 30], [59, 61], [40, 61]], 'mask': []},
        'added/L01_01_43_1': {'id': 'L01_01+1', 'from': 'L01_01', 'kind': 'split', 'page': 'L01', 'x': 59, 'y': 30, 'w': 30, 'h': 31,
                              'quad': [[59, 30], [89, 30], [89, 61], [59, 61]], 'mask': [], 'at': 't'},
        'added/L01_02_43_1': {'id': 'L01_02+1', 'from': 'L01_02', 'kind': 'missed', 'page': 'L01', 'x': 179, 'y': 29, 'w': 21, 'h': 32,
                              'quad': [[179, 29], [200, 29], [200, 61], [179, 61]], 'mask': [], 'at': 't'},
        'added/other': {'id': 'Z9+1', 'from': 'Z9', 'kind': 'missed', 'x': 1, 'y': 1, 'w': 5, 'h': 5}}
for k, v in docs.items():
    (d / 'db' / (k + '.json')).write_text(json.dumps(v))
sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(d / 'db'), '--out', str(d / 'settled.tsv'), '--summary', str(d / 'summary.json')])
A = list(csv.DictReader(open(d / 'added.tsv'), delimiter='\t')); S0 = json.load(open(d / 'summary.json'))
check('export: added.tsv beside --out, unknown from tile dropped and counted', [r['id'] for r in A] == ['L01_01+1', 'L01_02+1']
      and S0['added'] == 2 and S0['added_dropped'] == 1)
check('export: kind and box from the quad', A[0]['kind'] == 'split' and [A[0][k] for k in 'xywh'] == ['59', '30', '30', '31'] and A[1]['kind'] == 'missed')
check('must not: added boxes get no row (no label) in the settled labels', [r['sid'] for r in csv.DictReader(open(d / 'settled.tsv'), delimiter='\t')] == ['L01_01', 'L01_02'])
nodb = Path(tempfile.mkdtemp())
sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(nodb), '--out', str(nodb / 's.tsv')])
check('export: nothing added, no added.tsv', not (nodb / 'added.tsv').exists())

rc = ar.main(['--recuts', str(d / 'recuts.tsv'), '--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles'),
              '--added', str(d / 'added.tsv')])
S = {r['sid']: r for r in csv.DictReader(open(d / 'signs.tsv'), delimiter='\t')}
check('apply: exit 0, recut then two rows appended', rc == 0 and list(S) == ['L01_01', 'L01_02', 'L01_01+1', 'L01_02+1'])
check('apply: kept part is the recut box', [S['L01_01'][k] for k in 'xywh'] == ['40', '30', '19', '31'])
check('apply: added row copies page/line/pos from its from tile, box from added.tsv',
      [S['L01_01+1'][k] for k in ('page', 'line', 'pos', 'x', 'w')] == ['L01', 'L01', '1', '59', '30'] and S['L01_02+1']['x'] == '179')
for aid, x0 in (('L01_01+1', 70), ('L01_02+1', 180)):
    t = Image.open(d / 'tiles' / (aid + '.jpg')).convert('L')
    check('apply: tile %s cut and holds its sign\'s ink' % aid, t.size[0] > 20 and t.getextrema()[0] < 60)
before = (d / 'signs.tsv').read_text()
rc2 = ar.main(['--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles'), '--added', str(d / 'added.tsv')])
check('re-run (added only): already applied, signs.tsv unchanged', rc2 == 0 and (d / 'signs.tsv').read_text() == before)
A2 = d / 'added2.tsv'; A2.write_text(open(d / 'added.tsv').read().replace('\t179\t29\t', '\t150\t29\t'))
rc3 = ar.main(['--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles'), '--added', str(A2)])
S3 = {r['sid']: r for r in csv.DictReader(open(d / 'signs.tsv'), delimiter='\t')}
check('must not: an added id already in signs.tsv at another box is skipped (exit 2), not moved', rc3 == 2 and S3['L01_02+1']['x'] == '179')
print('FAILS', fails); sys.exit(1 if fails else 0)
