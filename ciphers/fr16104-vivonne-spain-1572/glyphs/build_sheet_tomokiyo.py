#!/usr/bin/env python3
"""sheet_tomokiyo_v1 (TXE2-VIVSHEET, PREREG-txeng2-15 SH-VIV, 9 Oct 2026): a VALUE-BLIND exemplar sheet for the
Saint-Gouard (Jean de Vivonne) 1572-74 hand, cut from Tomokiyo's published key drawings on disk
(sources/cryptiana/web/henryiii_Vivonne*.png). Zero network.

One 72 px tile per committed transcription label (the single-sign token inventory of tx/SIGNS.md + tx/f102r_rec.tsv,
40 labels). Each tile is the drawn sign at the box an Opus subagent found by SHAPE ("looks like the token"), one call
per drawing (boxes_tomokiyo_v1.tsv is that input, verbatim). Tiles carry the committed TOKEN and the drawing's key
year only, never the printed value. Vivonne1 is the 1574 key (the hand's own period); a tile from another drawing is a
different Vivonne key (1580, 1588) and is marked with its year on the sheet and in the manifest. The sheet is used by
no reader in round 15 (a later declared baseline change only).

    python3 build_sheet_tomokiyo.py           # writes sheet_tomokiyo_v1.png, sheet_tomokiyo_v1.tsv
    python3 build_sheet_tomokiyo.py --check   # exit 1 if the committed sheet/manifest differ from a rebuild
"""
import csv, io, os, sys
from PIL import Image, ImageDraw, ImageFont
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
DRAW = os.path.join(ROOT, 'sources', 'cryptiana', 'web')
BOXES = os.path.join(HERE, 'boxes_tomokiyo_v1.tsv')
YEAR = {'henryiii_Vivonne1.png': '1574', 'henryiii_Vivonne2.png': '1580', 'henryiii_Vivonne3.png': '1580',
        'henryiii_Vivonne4.png': '1585', 'henryiii_Vivonne5.png': '1586-87', 'henryiii_Vivonne6.png': '1588'}
CELL, PAD, COLS, LAB = 72, 2, 8, 22


def tile_of(img, box):
    x0, y0, x1, y1 = box
    g = img.crop((x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD)).convert('L')
    s = (CELL - 6) / max(g.size)
    g = g.resize((max(1, round(g.size[0] * s)), max(1, round(g.size[1] * s))), Image.LANCZOS)
    t = Image.new('L', (CELL, CELL), 255)
    t.paste(g, ((CELL - g.size[0]) // 2, (CELL - g.size[1]) // 2))
    return t


def build():
    rows = list(csv.DictReader(open(BOXES, encoding='utf-8'), delimiter='\t'))
    n = len(rows)
    nrow = (n + COLS - 1) // COLS
    W, H = COLS * (CELL + 8) + 8, nrow * (CELL + LAB + 8) + 8
    out = Image.new('L', (W, H), 255)
    d = ImageDraw.Draw(out)
    big, small = ImageFont.truetype(FONT, 15), ImageFont.truetype(MONO, 11)
    cache, man = {}, []
    for i, r in enumerate(rows):
        dr = r['drawing']
        if dr not in cache:
            cache[dr] = Image.open(os.path.join(DRAW, dr)).convert('RGB')
        box = tuple(int(r[k]) for k in ('x0', 'y0', 'x1', 'y1'))
        x = 8 + (i % COLS) * (CELL + 8)
        y = 8 + (i // COLS) * (CELL + LAB + 8)
        d.text((x + 2, y + 2), r['token'], fill=0, font=big)
        yr = YEAR[dr]
        d.text((x + CELL - 6 * len(yr) - 8, y + 6), yr if yr == '1574' else yr + '*', fill=0, font=small)
        out.paste(tile_of(cache[dr], box), (x, y + LAB))
        d.rectangle((x - 1, y + LAB - 1, x + CELL, y + LAB + CELL), outline=150)
        man.append((f'{i + 1:02d}', r['token'], dr, yr, '%d,%d,%d,%d' % box, r['conf'], r['note']))
    tsv = io.StringIO()
    tsv.write('tile\ttoken\tdrawing\tkey_year\tbox\tconf\tnote\n')
    for m in man:
        tsv.write('\t'.join(m) + '\n')
    return out, tsv.getvalue()


def main():
    img, tsv = build()
    png, tp = os.path.join(HERE, 'sheet_tomokiyo_v1.png'), os.path.join(HERE, 'sheet_tomokiyo_v1.tsv')
    if '--check' in sys.argv:
        bad = []
        if open(tp, encoding='utf-8').read() != tsv:
            bad.append('tsv')
        if Image.open(png).convert("L").tobytes() != img.tobytes():
            bad.append('png')
        print('STALE: ' + ' '.join(bad) if bad else 'OK: sheet_tomokiyo_v1 matches a rebuild')
        sys.exit(1 if bad else 0)
    img.save(png, optimize=True)
    open(tp, 'w', encoding='utf-8').write(tsv)
    print('wrote', png, tp, len(tsv.splitlines()) - 1, 'tiles')


if __name__ == '__main__':
    main()
