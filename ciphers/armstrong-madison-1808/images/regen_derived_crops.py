#!/usr/bin/env python3
"""Rebuild the derived crops of campaign steps H5 and H13 (27 Sept 2026) from the frames in images/ -- they are not
committed because images/ sits at its 30 MB line. Run from the target folder: python3 images/regen_derived_crops.py
H5  -> images/crops_0030_wide/f0030_L12w.jpg, L13w, L14w: frame 0030, x 40-2096, y bands (1590,1790) (1705,1920)
       (1835,2060), 2x Lanczos.
H13 -> images/crops_h13/h13_sheet_p1.jpg (frame 0030, x 40-2096, boxes y (1031,1150) (1150,1261) (1515,1632) (2021,2152)
       (2152,2276), each y0-55..y1+15), h13_sheet_p2.jpg (frame 0031, x 40-1990, boxes (656,803) (1221,1363) (1658,1812)
       (1971,2124) (2124,2265)), h13_sheet_p3.jpg (frame 0031, x 1900-3968, boxes (595,745) (875,1008) (1008,1159)),
       h13_sheet_p23b.jpg (frame 0031: x 40-1990 bands (1330,1530) (1790,1990) (2240,2440); x 1900-3968 bands (700,900)
       (1130,1330); each y0-40..y1), h13_zoom.jpg (3x: frame 0030 boxes (850,1000,1400,1150) (950,1120,1650,1270);
       frames 0031/0032 box (40,1930,700,2110) / (40,1970,700,2150)). Sheets stack crops with 12 px gaps (zoom: 20 px).
"""
from pathlib import Path
from PIL import Image
D = Path(__file__).resolve().parent
f30, f31, f32 = (Image.open(D/f'M34-014-00{n}.jpg') for n in (30, 31, 32))
def stack(crops, gap, out):
    w = max(c.size[0] for c in crops); h = sum(c.size[1]+gap for c in crops)
    sh = Image.new('L', (w, h), 255); y = 0
    for c in crops: sh.paste(c.convert('L'), (0, y)); y += c.size[1]+gap
    out.parent.mkdir(exist_ok=True); sh.save(out, quality=90)
(D/'crops_0030_wide').mkdir(exist_ok=True)
for name, (y0, y1) in {'L12w': (1590, 1790), 'L13w': (1705, 1920), 'L14w': (1835, 2060)}.items():
    c = f30.crop((40, y0, 2096, y1)); c.resize((c.size[0]*2, c.size[1]*2), Image.LANCZOS).save(D/'crops_0030_wide'/f'f0030_{name}.jpg', quality=92)
def band(fr, x0, x1, boxes, top=55, bot=15): return [fr.crop((x0, y0-top, x1, y1+bot)) for y0, y1 in boxes]
stack(band(f30, 40, 2096, [(1031,1150),(1150,1261),(1515,1632),(2021,2152),(2152,2276)]), 12, D/'crops_h13/h13_sheet_p1.jpg')
stack(band(f31, 40, 1990, [(656,803),(1221,1363),(1658,1812),(1971,2124),(2124,2265)]), 12, D/'crops_h13/h13_sheet_p2.jpg')
stack(band(f31, 1900, 3968, [(595,745),(875,1008),(1008,1159)]), 12, D/'crops_h13/h13_sheet_p3.jpg')
stack(band(f31, 40, 1990, [(1330,1530),(1790,1990),(2240,2440)], 40, 0) + band(f31, 1900, 3968, [(700,900),(1130,1330)], 40, 0), 12, D/'crops_h13/h13_sheet_p23b.jpg')
z = []
for fr, box in [(f30, (850,1000,1400,1150)), (f30, (950,1120,1650,1270)), (f31, (40,1930,700,2110)), (f32, (40,1970,700,2150))]:
    c = fr.crop(box); z.append(c.resize((c.size[0]*3, c.size[1]*3), Image.LANCZOS))
stack(z, 20, D/'crops_h13/h13_zoom.jpg'); print('derived crops rebuilt')
