#!/usr/bin/env python3
"""Regenerate the H18 line sheets (campaign step H18, 28 Sept 2026) from the frames in images/: five line crops per
sheet, each line box from the page's crops_* manifest widened to reach into the gutter and given 55 px of top margin.
Page 4 uses tools/iiif_lines.py --image on M34-014-0033.jpg (region 0,0,1944,3264, --top-margin 55, distance 100,
prominence 15) and stacks four crops per sheet. The sheets are not committed (images/ is at the 30 MB line); run this
from the target folder to rebuild them: python3 images/crops_h18/regen_sheets.py
"""
import json, subprocess, sys, glob
from pathlib import Path
from PIL import Image
T = Path(__file__).resolve().parents[2]; D = T/'images'; OUT = D/'crops_h18'
def boxes(d): return [e['box'] for e in json.load(open(D/d/'manifest.json'))['iiif_lines']]
jobs = {'p1_w30': ('M34-014-0030.jpg', 40, 2096, boxes('crops_0030')[3:]),
        'p2_w31': ('M34-014-0031.jpg', 40, 1990, boxes('crops_0031L')), 'p3_w31': ('M34-014-0031.jpg', 1880, 3968, boxes('crops_0031R')),
        'p2_w32': ('M34-014-0032.jpg', 40, 1990, boxes('crops_0032L')), 'p3_w32': ('M34-014-0032.jpg', 1880, 3968, boxes('crops_0032R'))}
def stack(name, crops, per):
    files = []
    for k in range(0, len(crops), per):
        part = crops[k:k+per]; w = max(c.size[0] for c in part); h = sum(c.size[1]+12 for c in part)
        sh = Image.new('L', (w, h), 255); y = 0
        for c in part: sh.paste(c.convert('L'), (0, y)); y += c.size[1]+12
        fn = f'{name}_s{k//per+1}.jpg'; sh.save(OUT/fn, quality=88); files.append(fn)
    return files
for name, (f, x0, x1, bx) in jobs.items():
    im = Image.open(D/f); H = im.size[1]
    stack(name, [im.crop((x0, max(0, b[1]-55), x1, min(H, b[3]+15))) for b in bx], 5)
tmp = OUT/'_p4'; tmp.mkdir(exist_ok=True)
subprocess.run([sys.executable, str(T.parents[1]/'tools/iiif_lines.py'), '--image', str(D/'M34-014-0033.jpg'), '--out', str(tmp), '--region', '0,0,1944,3264', '--prefix', 'f0033', '--top-margin', '55', '--distance', '100', '--prominence', '15'], check=True)
stack('p4_w33', [Image.open(p) for p in sorted(glob.glob(str(tmp/'f0033_L*.jpg')))], 4)
print('sheets rebuilt in', OUT)
