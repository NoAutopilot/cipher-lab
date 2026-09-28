#!/usr/bin/env python3
"""H31: contact sheets from a NARA whole-reel PDF (catalog.archives.gov medialz), for a blind sweep by a vision reader.
usage: h31_sheets.py REEL.pdf OUTDIR PREFIX first_page last_page cols rows frame_width
PDF page index i corresponds to microfilm frame i+1 (checked on M30 reel 11: page 64 == IIIF frame 0065). Each cell
is labelled with its frame number; a sheet holds cols x rows frames."""
import sys, os, pymupdf
from PIL import Image, ImageDraw
pdf, out, prefix = sys.argv[1], sys.argv[2], sys.argv[3]
a, b, cols, rows, fw = map(int, sys.argv[4:9])
os.makedirs(out, exist_ok=True)
d = pymupdf.open(pdf)
per = cols * rows
frames = list(range(a, b + 1))
n = 0
for s in range(0, len(frames), per):
    chunk = frames[s:s + per]
    imgs = []
    for fr in chunk:
        p = d[fr - 1]; z = fw / p.rect.width
        pix = p.get_pixmap(matrix=pymupdf.Matrix(z, z))
        im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        dr = ImageDraw.Draw(im); dr.rectangle((0, 0, 110, 26), fill=(255, 255, 0)); dr.text((4, 6), f"fr {fr:04d}", fill=(0, 0, 0))
        imgs.append(im)
    ch = max(i.size[1] for i in imgs)
    sheet = Image.new('RGB', (cols * fw + (cols - 1) * 8, rows * ch + (rows - 1) * 8), (120, 120, 120))
    for k, im in enumerate(imgs):
        sheet.paste(im, ((k % cols) * (fw + 8), (k // cols) * (ch + 8)))
    f = f"{prefix}_{chunk[0]:04d}-{chunk[-1]:04d}.jpg"
    sheet.save(os.path.join(out, f), quality=80); n += 1
print(prefix, 'sheets', n, 'frames', frames[0], '-', frames[-1], 'cell', fw)
