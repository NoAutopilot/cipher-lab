#!/usr/bin/env python3
"""TXE2-BOXES (PREREG-txeng2-5 P1, 9 Oct 2026): one per-sign box per feed focus tile, in the sign sorter's input format.
Read-free and value-blind: no reader, no truth file, no value; the only things taken from the line read (passZ) are the
tile's line and position and each line's position COUNT. Writes, per unit (f152r, spinelli) in benchmark-tx/txeng2/boxes/:
  <unit>/signs.tsv   sid, page, x, y, w, h (tools/sign_sorter.py --signs; page = an image in <unit>/pages.txt's dir)
  <unit>/labels.tsv  sid, sign, family -- every tile in ONE neutral pile "unsorted" (no top-1 label, no machine pick)
  <unit>/focus.tsv   the rows of benchmark-tx/txeng2/feed/<unit>_focus.tsv whose tile is boxed (the question; no value)
  <unit>/boxes.tsv   per tile: tile, line, pos, box_k, source crop, x, y, w, h, mapping, overlay_check, note
  overlays/<unit>_<line>.jpg  every candidate box of the line numbered, focus boxes thick (the check image)
f152r: atlas boxes (ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv, page f152r, 218 boxes; default glyph_atlas segment)
mapped by line and order: atlas line 3/4/5 = passZ L02/L03/L04 (atlas lines 1-2 hold the plain text and L01); dropped
before ordering: edge specks (w < 10 px at the region edges) and boxes whose height is under 0.65 x the page median sign
height and whose x-range overlaps a taller neighbour box (a stroke fragment or tick over/under a sign). L04's last position is end-anchored on the
last box before the plain text resumes (the counts differ on L04; see the note column).
spinelli: benchmark-tx/txeng2/boxes/spin_join.py on a glyph_atlas segment run (default mode, --median-h 55) of the
confirm line crops; mapped by order only; overlay_check is filled in by eye on the overlay (box covers one whole sign,
line box count = positions) in overlay_checks.tsv, never from a value.
  python3 benchmark-tx/txeng2/boxes/build_boxes.py  (after: sh benchmark-tx/txeng2/boxes/build.sh)"""
import csv, os, shutil
from PIL import Image, ImageDraw
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
B = os.path.join(ROOT, 'benchmark-tx/txeng2/boxes'); FEED = os.path.join(ROOT, 'benchmark-tx/txeng2/feed')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
checks = {r['tile']: r for r in rd(os.path.join(B, 'overlay_checks.tsv'))} if os.path.exists(os.path.join(B, 'overlay_checks.tsv')) else {}
os.makedirs(os.path.join(B, 'overlays'), exist_ok=True)

def focus(unit):
    return [l.rstrip('\n').split('\t') for l in open(os.path.join(FEED, unit + '_focus.tsv')) if l.strip()]

def write_unit(unit, rows, pages_dir):
    d = os.path.join(B, unit); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'pages.txt'), 'w').write(pages_dir + '\n')
    with open(os.path.join(d, 'boxes.tsv'), 'w') as f:
        f.write('tile\tline\tpos\tbox_k\tsource\tx\ty\tw\th\tmapping\toverlay_check\tnote\n')
        for r in rows:
            c = checks.get(r['tile'], {})
            f.write('\t'.join(str(r[k]) for k in ('tile', 'line', 'pos', 'k', 'source', 'x', 'y', 'w', 'h', 'mapping'))
                    + '\t' + c.get('overlay_check', 'unchecked') + '\t' + c.get('note', '') + '\n')
    ok = [r for r in rows if checks.get(r['tile'], {}).get('overlay_check') == 'yes']
    okt = {r['tile'] for r in ok}
    with open(os.path.join(d, 'focus.tsv'), 'w') as f:
        f.writelines('\t'.join(q) + '\n' for q in focus(unit) if q[0] in okt)
    with open(os.path.join(d, 'signs.tsv'), 'w') as f, open(os.path.join(d, 'labels.tsv'), 'w') as g:
        f.write('sid\tpage\tx\ty\tw\th\n'); g.write('sid\tsign\tfamily\n')
        for r in ok:
            f.write('\t'.join(str(r[k]) for k in ('tile', 'page', 'x', 'y', 'w', 'h')) + '\n')
            g.write(f"{r['tile']}\tunsorted\tunsorted\n")
    print(unit, 'tiles listed', len(rows), 'boxed (overlay yes)', len(ok))

def overlay(name, img_path, cands, focus_k, crop_box=None):
    im = Image.open(img_path).convert('RGB'); dr = ImageDraw.Draw(im)
    for k, (x, y, w, h) in cands:
        thick = k in focus_k
        dr.rectangle([x, y, x + w, y + h], outline=(0, 70, 170) if not thick else (230, 120, 0), width=5 if thick else 2)
        dr.text((x + 2, y + h + 2), str(k) + (' <' + focus_k[k] + '>' if thick else ''), fill=(120, 0, 90))
    if crop_box: im = im.crop(crop_box)
    if im.width > 2400: im = im.resize((2400, int(im.height * 2400 / im.width)))
    im.save(os.path.join(B, 'overlays', name + '.jpg'), quality=70)

# ---- f152r
A = [r for r in rd(os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv')) if r['page'] == 'f152r']
IMG = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/harvest/f152r/src_ark_12148_btv1b9060248g_f154_4350_3700_3800_580.jpg')
MED = 51.0  # atlas/pages.json median_h for f152r
LINEMAP = {'f152r_L02': '3', 'f152r_L03': '4', 'f152r_L04': '5'}
def f152r_order(al):
    bs = sorted([r for r in A if r['line'] == al], key=lambda r: int(r['x']))
    out = []
    for r in bs:
        x, y, w, h = (int(r[k]) for k in 'xywh')
        if w < 10 and (x < 50 or x > 3550): continue                    # edge speck
        frag = h < 0.65 * MED and any(o is not r and int(o['h']) > h and int(o['x']) < x + w and x < int(o['x']) + int(o['w'])
                                      for o in bs)
        if frag: continue                                               # fragment above/below a neighbour box
        out.append(r)
    return out
rows = []
for tile, _q in focus('f152r'):
    line, pos = tile.rsplit('_', 1)[0], int(tile.rsplit('_', 1)[1])
    seq = f152r_order(LINEMAP[line])
    if line == 'f152r_L04':  # end-anchored: last box before the plain text that ends the line (x < 2620)
        seq = [r for r in seq if int(r['x']) + int(r['w']) <= 2620]; idx = len(seq) - 1 - (25 - pos); mp = f'end-anchored ({len(seq)} boxes / 25 positions)'
    else:
        idx = pos - 1; mp = f'order ({len(seq)} boxes / {sum(1 for r in rd(os.path.join(ROOT, "benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv")) if r["line"] == line)} positions)'
    r = seq[idx]
    rows.append(dict(tile=tile, line=line, pos=pos, k=r['sid'], source=os.path.relpath(IMG, ROOT), page='f152r',
                     x=r['x'], y=r['y'], w=r['w'], h=r['h'], mapping=mp))
for line, al in LINEMAP.items():
    seq = f152r_order(al); fk = {int(r['pos']): t['tile'].rsplit('_', 1)[1] for t in rows if t['line'] == line for r in seq if r['sid'] == t['k']}
    ys = [int(r['y']) for r in seq]
    overlay('f152r_' + line.split('_')[1], IMG, [(int(r['pos']), tuple(int(r[k]) for k in 'xywh')) for r in seq], fk,
            (0, max(0, min(ys) - 30), 3800, min(580, max(int(r['y']) + int(r['h']) for r in seq) + 30)))
write_unit('f152r', rows, 'ciphers/nevers-birago-fr3251-1572/atlas/pages.json')

# ---- spinelli
S = rd(os.path.join(B, 'spinelli_lineboxes.tsv'))
npos = {}
for r in rd(os.path.join(ROOT, 'benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv')): npos[r['line']] = npos.get(r['line'], 0) + 1
rows = []
for tile, _q in focus('spinelli'):
    line, pos = tile.rsplit('_', 1)[0], int(tile.rsplit('_', 1)[1])
    seq = [r for r in S if r['line'] == line]
    r = seq[pos - 1] if pos <= len(seq) else None
    mp = f'order ({len(seq)} boxes / {npos[line]} positions)'
    if r is None:
        rows.append(dict(tile=tile, line=line, pos=pos, k='', source='', page='', x='', y='', w='', h='', mapping=mp)); continue
    u = checks.get(tile, {}).get('union_k')
    if u:  # a mark box the overlay check unions into the tile box (overlay_checks.tsv union_k)
        m = next(q for q in seq if q['k'] == u); x0 = min(int(r['x']), int(m['x'])); y0 = min(int(r['y']), int(m['y']))
        x1 = max(int(r['x']) + int(r['w']), int(m['x']) + int(m['w'])); y1 = max(int(r['y']) + int(r['h']), int(m['y']) + int(m['h']))
        r = dict(r, x=x0, y=y0, w=x1 - x0, h=y1 - y0, k=r['k'] + '+' + u)
    rows.append(dict(tile=tile, line=line, pos=pos, k=r['k'], source=r['crop'], page=os.path.basename(r['crop'])[:-4],
                     x=r['x'], y=r['y'], w=r['w'], h=r['h'], mapping=mp))
for crop in sorted({r['crop'] for r in S if r['line'] in {t['line'] for t in rows}}):
    cands = [(int(r['k']), tuple(int(r[k]) for k in 'xywh')) for r in S if r['crop'] == crop]
    fk = {int(str(t['k']).split('+')[0]): str(t['pos']) for t in rows if t['source'] == crop}
    overlay('spinelli_' + os.path.basename(crop)[:-4], os.path.join(ROOT, crop), cands, fk)
write_unit('spinelli', rows, 'benchmark-tx/txeng/confirm/crops')
