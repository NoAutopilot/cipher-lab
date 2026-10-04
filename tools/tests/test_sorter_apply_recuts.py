#!/usr/bin/env python3
"""Offline test for tools/sorter_apply_recuts.py and sign_sorter_apply.py's recuts.tsv export (SORTER-NUDGE, 4 Oct 2026).
Run: python3 tools/tests/test_sorter_apply_recuts.py"""
import csv, json, os, sys, tempfile
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from PIL import Image, ImageDraw
import sign_sorter_apply as sa
import sorter_apply_recuts as ar

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

d = Path(tempfile.mkdtemp()); (d / 'pages').mkdir(); (d / 'db' / 'recuts').mkdir(parents=True)
im = Image.new('L', (200, 80), 250); g = ImageDraw.Draw(im); g.rectangle((40, 30, 60, 60), fill=0); g.rectangle((100, 30, 120, 60), fill=0)
im.save(d / 'pages' / 'L01.png')
(d / 'signs.tsv').write_text('sid\tpage\tx\ty\tw\th\nL01_01\tL01\t40\t30\t40\t30\nL01_02\tL01\t100\t30\t20\t30\nL01_03\tL01\t150\t30\t20\t30\n')
(d / 'labels.tsv').write_text('sid\tsign\nL01_01\tA\nL01_02\tA\nL01_03\tB\n')
docs = {'L01_01': {'sid': 'L01_01', 'page': 'L01', 'x': 40, 'y': 30, 'w': 21, 'h': 31, 'old': [40, 30, 40, 30], 'at': '2026-10-04T19:00:00Z'},
        'L01_03': {'sid': 'L01_03', 'page': 'L01', 'x': 152, 'y': 30, 'w': 18, 'h': 30, 'old': [150, 31, 20, 30], 'at': '2026-10-04T19:01:00Z'},
        'bad': {'sid': 'bad', 'x': 'x'}}
for k, v in docs.items():
    (d / 'db' / 'recuts' / (k + '.json')).write_text(json.dumps(v))
sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(d / 'db'), '--out', str(d / 'settled.tsv'), '--summary', str(d / 'summary.json')])
rows = list(csv.DictReader(open(d / 'recuts.tsv'), delimiter='\t'))
check('export: recuts.tsv beside --out, malformed doc dropped', [r['tile'] for r in rows] == ['L01_01', 'L01_03'])
check('export: columns and values', list(rows[0]) == sa.RECUT_COLS and [rows[0][k] for k in ('old_w', 'new_w', 'new_h')] == ['40', '21', '31'])
check('export: summary counts recuts, statuses unchanged', json.load(open(d / 'summary.json'))['recuts'] == 2
      and {r['status'] for r in csv.DictReader(open(d / 'settled.tsv'), delimiter='\t')} == {'kept'})
nodb = Path(tempfile.mkdtemp())
sa.main(['--labels', str(d / 'labels.tsv'), '--db', str(nodb), '--out', str(nodb / 's.tsv')])
check('export: no recuts saved, no file', not (nodb / 'recuts.tsv').exists())

rc = ar.main(['--recuts', str(d / 'recuts.tsv'), '--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles')])
S = {r['sid']: r for r in csv.DictReader(open(d / 'signs.tsv'), delimiter='\t')}
check('apply: stale row (signs.tsv moved since) skipped, exit 2', rc == 2 and S['L01_03']['x'] == '150')
check('apply: signs.tsv updated to the new box', [S['L01_01'][k] for k in 'xywh'] == ['40', '30', '21', '31'] and S['L01_02']['x'] == '100')
t, o = d / 'tiles' / 'L01_01.jpg', d / 'tiles' / 'L01_01.orig.jpg'
check('apply: new crop and old crop kept', t.exists() and o.exists() and Image.open(t).width == 31 and Image.open(o).width == 50)
orig = o.read_bytes()
rc2 = ar.main(['--recuts', str(d / 'recuts.tsv'), '--signs', str(d / 'signs.tsv'), '--pages', str(d / 'pages'), '--tiles', str(d / 'tiles'), '--force'])
S2 = {r['sid']: r for r in csv.DictReader(open(d / 'signs.tsv'), delimiter='\t')}
check('apply again: idempotent, .orig never overwritten; --force takes the stale row', rc2 == 0 and o.read_bytes() == orig and S2['L01_03']['x'] == '152'
      and [S2['L01_01'][k] for k in 'xywh'] == ['40', '30', '21', '31'])
print('ALL PASS' if not fails else '%d FAILED' % fails); sys.exit(1 if fails else 0)
