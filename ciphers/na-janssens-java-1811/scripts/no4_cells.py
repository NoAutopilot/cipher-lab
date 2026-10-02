#!/usr/bin/env python3
"""GAPS9 (2 Oct 2026): per-cell native-resolution crops of the No.4 gloss table's doubtful cells.

Selects the cells GAPS8 marked uncertain in no4/no4_merge.tsv plus every No.4 cell whose code sits in a
conflicts.tsv row naming a no4 page; cuts each from the native IIIF pages in images/crops_no4_native/ on a
5-column grid (row centres from tools/iiif_lines.py --dry-run, eye-checked on an overlay); writes
no4/gaps9_cells.tsv (id -> leaf, order) and labelled contact sheets images/crops_no4_native/sheet_NN.jpg that show
only a cell id, never the current code or gloss (blind passes). Usage: python3 scripts/no4_cells.py
"""
import csv, os
from PIL import Image, ImageDraw, ImageFont
D = 'images/crops_no4_native/'
P = {
 'no4-205R': ('205_native.jpg', 0, 2462, [(168,324),(458,582),(712,843),(970,1097),(1236,1362),(1482,1629),(1743,1882),(1995,2131),(2245,2389),(2529,2664),(2794,2914),(3039,3166)]),
 'no4-206L': ('206_native.jpg', 0, 2435, [(306,421),(561,689),(820,959),(1086,1212),(1357,1487),(1609,1767),(1896,2015),(2161,2306),(2441,2568),(2701,2836),(2966,3114),(3233,3374)]),
 'no4-206R': ('206_native.jpg', 2435, 2436, [(300,419),(563,689),(826,958),(1095,1234),(1388,1518),(1639,1790),(1906,2044),(2176,2310),(2441,2573),(2717,2849),(2989,3117),(3246,3388)]),
 'no4-207L': ('207_native.jpg', 0, 2479, [(314,445),(555,669),(785,900),(1021,1148),(1265,1378),(1505,1622),(1759,1883),(1994,2125),(2242,2357)]),
}
merge = list(csv.DictReader(open('no4/no4_merge.tsv'), delimiter='\t'))
conf_codes = {r['code'] for r in csv.DictReader(open('conflicts.tsv'), delimiter='\t') if 'no4' in r['variants']}
sel = [r for r in merge if 'uncertain' in r['note'] or r['code'] in conf_codes]
imgs = {}
cells = []
for i, r in enumerate(sel, 1):
    f, xo, w, rows = P[r['leaf']]
    if f not in imgs: imgs[f] = Image.open(D + f).convert('L')
    o = int(r['order']) - 1; row, col = divmod(o, 5)
    c, g = rows[row]; cw = w / 5
    box = (int(xo + col*cw - 0.12*cw), max(0, c - 120), int(xo + (col+1)*cw + 0.12*cw), g + 120)
    cells.append((i, r, imgs[f].crop(box)))
with open('no4/gaps9_cells.tsv', 'w') as fh:
    fh.write('id\tleaf\torder\treason\n')
    for i, r, _ in cells:
        why = ('uncertain' if 'uncertain' in r['note'] else '') + ('+conflict' if r['code'] in conf_codes else '')
        fh.write(f'{i}\t{r["leaf"]}\t{r["order"]}\t{why.strip("+")}\n')
font = ImageFont.load_default(size=40) if hasattr(ImageFont, 'load_default') else None
per = 12
for s in range(0, len(cells), per):
    chunk = cells[s:s+per]; cw, ch = 700, 460
    sheet = Image.new('L', (cw*3, ch*4), 255); d = ImageDraw.Draw(sheet)
    for k, (i, r, im) in enumerate(chunk):
        im = im.copy(); im.thumbnail((cw-20, ch-70))
        x, y = (k % 3)*cw, (k // 3)*ch
        d.rectangle((x, y, x+cw-1, y+ch-1), outline=0, width=3)
        d.text((x+10, y+8), f'#{i}', fill=0, font=font)
        sheet.paste(im, (x+10, y+60))
    sheet.save(D + f'sheet_{s//per+1:02d}.jpg', quality=85)
print(len(cells), 'cells,', (len(cells)+per-1)//per, 'sheets; conflict codes', len(conf_codes))
