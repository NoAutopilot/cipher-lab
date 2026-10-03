"""Zoom each f.30 'eh'/CROSS glyph from its strip (crops/f30_split/<line>_<pos>_<sign>.jpg, made by
split_shapes_crops.py) at 3x, using the glyph centre read by eye on the strips (A2-GRA3, 3 Oct 2026; GX below, pixels
in the strip). Writes crops/f30_split/zoom_eh.jpg and zoom_cross.jpg, one labelled cell per occurrence.
  python3 split_shapes_zoom.py"""
import os, sys
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(H, 'crops', 'f30_split')
if '--help' in sys.argv: print(__doc__); sys.exit()
GX = {'f30r_L01_31': 270, 'f30r_L03_9': 320, 'f30r_L04_6': 335, 'f30r_L04_16': 290, 'f30r_L04_36': 190,
      'f30r_L05_12': 265, 'f30r_L06_8': 350, 'f30r_L06_32': 175, 'f30r_L08_15': 300, 'f30r_L10_7': 375,
      'f30r_L13_8': 345, 'f30r_L13_24': 185, 'f30r_L14_26': 130, 'f30r_L17_11': 350, 'f30r_L17_21': 240,
      'f30r_L26_34': 95, 'f30r_L30_3': 440, 'f30r_L31_25': 260, 'f30r_L34_32': 235, 'f30r_L35_26': 205,
      'f30v_L02_28': 290, 'f30v_L17_18': 270,
      'f30r_L03_30': 210, 'f30r_L03_36': 180, 'f30r_L07_3': 350, 'f30r_L08_28': 245, 'f30r_L11_2': 310,
      'f30r_L12_0': 150, 'f30r_L21_12': 300, 'f30r_L33_15': 325}
for sign, name in (('eh', 'zoom_eh.jpg'), ('CROSS', 'zoom_cross.jpg')):
    cells = []
    for k, gx in GX.items():
        f = os.path.join(D, f'{k}_{sign}.jpg')
        if not os.path.exists(f): continue
        im = Image.open(f); g = im.crop((max(0, gx - 50), 24, gx + 50, im.height)).resize((300, (im.height - 24) * 3))
        c = Image.new('RGB', (300, g.height + 22), 'white'); c.paste(g, (0, 22))
        ImageDraw.Draw(c).text((4, 4), k, fill=(200, 0, 0)); cells.append(c)
    cols = 4; rws = (len(cells) + cols - 1) // cols; ch = max(c.height for c in cells)
    sh = Image.new('RGB', (cols * 306, rws * (ch + 6)), 'gray')
    for i, c in enumerate(cells): sh.paste(c, ((i % cols) * 306, (i // cols) * (ch + 6)))
    sh.save(os.path.join(D, name), quality=85); print(name, sh.size)
