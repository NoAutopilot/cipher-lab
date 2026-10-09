#!/usr/bin/env python3
"""atlas_v5 (TXE2-BASE-SPIN2, PREREG-txeng2-9 B2, 9 Oct 2026): atlas_v4 plus three rows drawn from Domnina 2016's published key.

The three shapes the B1 readers marked NEW (circle-on-stem, long-s-crossbar, looped-H) were looked up in Domnina 2016
Ill. 1 (sources/domnina-2015-2016/p27_2016_plate_key_letter_decipherment.jpg, cropped to
benchmark-tx/txeng2/basespin2/lookup/domnina2016_ill1_table.png) by one blind Opus subagent that saw only that table image
and the three shape names (benchmark-tx/txeng2/basespin2/lookup/lookup.tsv). Each new row carries ONE exemplar: the
published drawing itself, cut from the table at the subagent's box and fitted into a 72 px tile. No tile comes from the
manuscript, so no tile was chosen through any eval position. Row names are the published cells, in the v7 KEY_* style:
  KEY_G1    Domnina 2016 cell G, sign 1    (circle-on-stem; lookup M)
  KEY_U_V2  Domnina 2016 cell U/V, sign 2  (long-s-crossbar; lookup H)
  KEY_SS    Domnina 2016 cell SS, sign 1   (looped-H; lookup H)
atlas_v4.png/tsv are left untouched.

    python3 build_atlas_v5.py           # writes atlas_v5.png, atlas_v5.tsv
    python3 build_atlas_v5.py --check   # exit 1 if the committed atlas_v5.* differ from a rebuild
"""
import csv, hashlib, io, os, sys
from PIL import Image, ImageDraw, ImageFont
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TABLE = os.path.join(ROOT, 'benchmark-tx', 'txeng2', 'basespin2', 'lookup', 'domnina2016_ill1_table.png')
CELL = 72
NEW = [  # code, box in TABLE (x0,y0,x1,y1), desc
    ('KEY_G1', (236, 2049, 292, 2174), 'published key cell G sign 1 (Domnina 2016 Ill. 1): loop on a vertical stem, foot turned left'),
    ('KEY_U_V2', (831, 1283, 903, 1406), 'published key cell U/V sign 2 (Domnina 2016 Ill. 1): tall long s / f with a crossbar and a left foot'),
    ('KEY_SS', (1170, 1814, 1266, 1929), 'published key cell SS sign 1 (Domnina 2016 Ill. 1): large looped H-like flourish'),
]


def tile_of(table, box):
    g = table.crop(box).convert('L')
    s = (CELL - 6) / max(g.size)
    g = g.resize((max(1, round(g.size[0] * s)), max(1, round(g.size[1] * s))), Image.LANCZOS)
    t = Image.new('L', (CELL, CELL), 255)
    t.paste(g, ((CELL - g.size[0]) // 2, (CELL - g.size[1]) // 2))
    return t


def build():
    v4 = Image.open(os.path.join(HERE, 'atlas_v4.png')).convert('L')
    rows = list(csv.DictReader(open(os.path.join(HERE, 'atlas_v4.tsv')), delimiter='\t'))
    table = Image.open(TABLE)
    out = Image.new('L', (v4.size[0], v4.size[1] + CELL * len(NEW)), 255)
    out.paste(v4, (0, 0))
    trows = list(rows)
    for j, (code, box, desc) in enumerate(NEW):
        y = v4.size[1] + j * CELL
        strip = Image.new('L', (2 * CELL, CELL), 255)
        d = ImageDraw.Draw(strip)
        d.text((4, 14), code, fill=0, font=ImageFont.truetype(FONT, 17))
        d.text((4, 44), 'print', fill=0, font=ImageFont.truetype(MONO, 13))
        out.paste(strip, (0, y))
        out.paste(tile_of(table, box), (2 * CELL, y))
        for x in range(out.size[0]):
            out.putpixel((x, y + CELL - 1), 190)
        trows.append({'code': code, 'desc': desc, 'count': '0', 'pages': 'print',
                      'exemplars': 'domnina2016_ill1:%d,%d,%d,%d' % box, 'marks_seen': ''})
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(rows[0].keys()), delimiter='\t', lineterminator='\n')
    w.writeheader(); w.writerows(trows)
    png = io.BytesIO(); out.save(png, format='PNG', optimize=False)
    return png.getvalue(), buf.getvalue()


if __name__ == '__main__':
    png, tsv = build()
    pp, tp = os.path.join(HERE, 'atlas_v5.png'), os.path.join(HERE, 'atlas_v5.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(pp) and open(pp, 'rb').read() == png and open(tp).read() == tsv
        print('atlas_v5:', 'ok' if ok else 'STALE', hashlib.sha256(png).hexdigest()); sys.exit(0 if ok else 1)
    open(pp, 'wb').write(png); open(tp, 'w').write(tsv)
    print('atlas_v5.png sha256', hashlib.sha256(png).hexdigest())
