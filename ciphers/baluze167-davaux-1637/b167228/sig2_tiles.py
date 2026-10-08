#!/usr/bin/env python3
"""SIG-B228B: cut the u4/4u tiles and the 71-mark crops from the native source regions on disk (no network), per prereg_sig2.md.
Centres placed by eye on gridded copies (shape location only, no value judged). Tile geometry = b167228/sig_tiles.py tile().
Writes b167228/sig2/U?.png + sheet_unknown2.png (4 targets, 3 decoys, 2 anchors, shuffled), N?.png + sheet_marks.png (2 targets,
6 controls, shuffled), and key_private2.tsv (blind id -> role, for scoring only). Usage: python3 b167228/sig2_tiles.py (target folder)"""
import random, sys
sys.path.insert(0, 'b167228')
from PIL import Image, ImageDraw
from sig_tiles import tile, VA, VB, VBY, W, H
RB = 'images/crops/src_ark_12148_btv1b90015040_f239_4200_4150_3500_500.jpg'
SHAPES = [('target:u4|4u', 'v_a_L02_c4', VA, 660, 270), ('target:u4|4u', 'v_b_L01_c10', VB, 2290, VBY[1]),
          ('target:u4|4u', 'v_b_L05_c8', VB, 1305, VBY[5]), ('target:u4|4u', 'v_b_L06_c6', VB, 1220, VBY[6]),
          ('DECOY:h=n', 'v_b_L04', VB, 840, VBY[4]), ('DECOY:gam=u', 'v_b_L07', VB, 1150, VBY[7]),
          ('DECOY:y+=r', 'v_b_L07', VB, 1265, VBY[7]),
          ('ANCHOR:4u=a', 'v_a_L01_c5', VA, 780, 152), ('ANCHOR:u4=t', 'v_b_L04_c1', VB, 270, VBY[4])]
# mark crops: (role, where, src, x, y0, y1)
MARKS = [('target:71', 'v_a_L01_occ2', VA, 540, 30, 200), ('target:71', 'v_a_L01_occ5', VA, 1515, 30, 200),
         ('control:acute', 'r_b_L02 40', RB, 1060, 300, 440), ('control:acute', 'v_b_L04 90', VB, 400, VBY[4] - 120, VBY[4] + 50),
         ('control:acute', 'v_b_L02 44', VB, 1290, VBY[2] - 120, VBY[2] + 50), ('control:acute', 'v_b_L02 65', VB, 365, VBY[2] - 120, VBY[2] + 50),
         ('control:none', 'v_a_L01 16', VA, 1870, 30, 200), ('control:none', 'v_b_L02 13', VB, 2130, VBY[2] - 120, VBY[2] + 50)]
def sheet(lst, path, w, h, cols):
    rows = (len(lst) + cols - 1) // cols
    out = Image.new('L', (cols * (w + 10), rows * (h + 40)), 255); d = ImageDraw.Draw(out)
    for k, (lab, t) in enumerate(lst):
        cx, cy = (k % cols) * (w + 10), (k // cols) * (h + 40)
        out.paste(t, (cx, cy + 30)); d.text((cx + 5, cy + 5), lab, fill=0)
        d.rectangle([cx, cy + 30, cx + w - 1, cy + 30 + h - 1], outline=128)
    out.save(path)
if __name__ == '__main__':
    rnd = random.Random(202610082)
    key = ['id\trole\twhere\tx\ty']
    o = list(range(len(SHAPES))); rnd.shuffle(o); tl = []
    for n, i in enumerate(o, 1):
        r, w, src, x, y = SHAPES[i]; t = tile(src, x, y); t.save(f'b167228/sig2/U{n}.png'); tl.append((f'U{n}', t))
        key.append(f'U{n}\t{r}\t{w}\t{x}\t{y}')
    sheet(tl, 'b167228/sig2/sheet_unknown2.png', W, H, 5)
    o = list(range(len(MARKS))); rnd.shuffle(o); ml = []
    for n, i in enumerate(o, 1):
        r, w, src, x, y0, y1 = MARKS[i]
        t = Image.open(src).convert('L').crop((x - 90, y0, x + 90, y1)); t = t.resize((360, 2 * (y1 - y0)), Image.LANCZOS)
        t = t.crop((0, 0, 360, 340)) if t.size[1] > 340 else t
        canvas = Image.new('L', (360, 340), 255); canvas.paste(t, (0, 0)); canvas.save(f'b167228/sig2/N{n}.png'); ml.append((f'N{n}', canvas))
        key.append(f'N{n}\t{r}\t{w}\t{x}\t{y0}-{y1}')
    sheet(ml, 'b167228/sig2/sheet_marks.png', 360, 340, 4)
    open('b167228/sig2/key_private2.tsv', 'w').write('\n'.join(key) + '\n')
    print(len(tl), 'shape tiles,', len(ml), 'mark crops')
