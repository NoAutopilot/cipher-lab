#!/usr/bin/env python3
"""SIG-B228: cut shape tiles from the native source regions on disk (no network). Centres located by eye on gridded copies.
Writes b167228/sig_tiles/T??.png (blind ids), E??.png (labelled f.229 exemplars), key_private.tsv (tile -> shape, for scoring only),
and the two sheets given to the blind readers. Usage: python3 b167228/sig_tiles.py (from the target folder)"""
import random
from PIL import Image, ImageDraw
C = 'images/crops/'
VB = C + 'src_ark_12148_btv1b90015040_f240_850_3560_3200_1340.jpg'
VA = C + 'src_ark_12148_btv1b90015040_f240_850_1250_3200_480.jpg'
RA = C + 'src_ark_12148_btv1b90015040_f239_4250_2150_3450_560.jpg'
RB = C + 'src_ark_12148_btv1b90015040_f239_4200_4150_3500_500.jpg'
VBY = {1: 120, 2: 264, 3: 424, 4: 592, 5: 752, 6: 920, 7: 1088}
# (shape, where, source, x, y)
TARGET = [('q', 'v_b_L01', VB, 1287, VBY[1]), ('q', 'v_b_L02a', VB, 925, VBY[2]), ('q', 'v_b_L02b', VB, 2045, VBY[2]),
          ('q', 'v_b_L04a', VB, 918, VBY[4]), ('q', 'v_b_L04b', VB, 1960, VBY[4]), ('q', 'v_b_L07', VB, 480, VBY[7]),
          ('ll', 'v_a_L01', VA, 1420, 152), ('ll', 'v_b_L01', VB, 2205, VBY[1]), ('ll', 'v_b_L05', VB, 1215, VBY[5]),
          ('ll', 'v_b_L06', VB, 1025, VBY[6]),
          ('g+', 'v_b_L01', VB, 2410, VBY[1]), ('g+', 'v_b_L03', VB, 385, VBY[3]), ('g+', 'v_b_L05', VB, 1426, VBY[5]),
          ('ll|u4', 'r_a_L02', RA, 1375, 303), ('v', 'r_a_L02', RA, 1700, 303), ('ff', 'r_a_L02', RA, 1925, 303),
          ('ff', 'r_b_L02', RB, 2530, 359), ('wave', 'r_b_L02', RB, 1310, 359)]
DECOY = [('DECOY:hook=s', 'v_b_L02', VB, 1035, VBY[2]), ('DECOY:gam=u', 'v_b_L02', VB, 1630, VBY[2]),
         ('DECOY:y+=r', 'v_b_L02', VB, 1713, VBY[2])]
L4, L5, L6 = C + 'b170f229r_L04.jpg', C + 'b170f229r_L05.jpg', C + 'b170f229r_L06.jpg'
EXEMPLAR = [('s', 'hook', L4, 733), ('n', 'h', L4, 219), ('r', 'y+', L4, 1444), ('a', '4u', L4, 1594), ('c', '9', L4, 1825),
            ('m', 'm4', L4, 2068), ('u', 'gam', L5, 294), ('p', 'mm', L5, 756), ('e', "w'", L5, 990), ('t', 'u4', L5, 1110),
            ('l', 'n', L6, 600)]
W, H = 150, 210
def tile(src, x, y=None):
    im = Image.open(src).convert('L')
    if y is None:
        return im.crop((x - W // 2, 0, x + W // 2, im.size[1])).resize((W, H))
    return im.crop((x - W // 2, y - 90, x + W // 2, y + 120))
if __name__ == '__main__':
    items = TARGET + DECOY
    rnd = random.Random(20261008)
    order = list(range(len(items))); rnd.shuffle(order)
    key = ['tile\tshape\twhere\tx\ty']
    tiles = []
    for n, i in enumerate(order, 1):
        s, w, src, x, y = items[i]
        t = tile(src, x, y); t.save(f'b167228/sig_tiles/T{n:02d}.png'); tiles.append((f'T{n:02d}', t))
        key.append(f'T{n:02d}\t{s}\t{w}\t{x}\t{y}')
    open('b167228/sig_tiles/key_private.tsv', 'w').write('\n'.join(key) + '\n')
    def sheet(lst, path, cols=6):
        rows = (len(lst) + cols - 1) // cols
        out = Image.new('L', (cols * (W + 10), rows * (H + 40)), 255); d = ImageDraw.Draw(out)
        for k, (lab, t) in enumerate(lst):
            cx, cy = (k % cols) * (W + 10), (k // cols) * (H + 40)
            out.paste(t, (cx, cy + 30)); d.text((cx + 5, cy + 5), lab, fill=0)
            d.rectangle([cx, cy + 30, cx + W - 1, cy + 30 + H - 1], outline=128)
        out.save(path)
    sheet(tiles, 'b167228/sig_tiles/sheet_unknown.png')
    ex = []
    for let, shape, src, x in EXEMPLAR:
        t = tile(src, x); ex.append((f'E-{let}', t))
    sheet(ex, 'b167228/sig_tiles/sheet_f229_exemplars.png')
    tb = Image.open('images/louisxiii_davaux.png').convert('L').crop((0, 0, 440, 150))
    tb.resize((tb.size[0] * 3, tb.size[1] * 3), Image.LANCZOS).save('b167228/sig_tiles/sheet_tomokiyo_block.png')
    print(len(tiles), 'unknown tiles,', len(ex), 'f229 exemplars')
