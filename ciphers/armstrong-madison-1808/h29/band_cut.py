#!/usr/bin/env python3
"""H29 fixed-pitch band cutter for pages whose interlinear glosses flatten the row ink profile (tools/iiif_lines.py
found 20-23 of about 27 lines on Monroe reel 3 frame 0742 at every prominence tried). Each crop is a window of
about 2.3 line pitches; the TARGET line sits between two red guide lines, so every line of the page is the target of
exactly one crop and a reader transcribes only what lies between the guides (plus the gloss just above each group).
usage: band_cut.py IMAGE OUTDIR PREFIX x0 y0 x1 y1 first_centre pitch n_lines [--half H] [--scale S]"""
import sys, json, os
from PIL import Image, ImageDraw
a = sys.argv[1:]
img, out, prefix = a[0], a[1], a[2]
x0, y0, x1, y1, c0, pitch, n = map(float, a[3:10])
half = float(a[a.index('--half') + 1]) if '--half' in a else pitch * 0.5
scale = float(a[a.index('--scale') + 1]) if '--scale' in a else 1.0  # H32: upscale crops of low-resolution microfilm
im = Image.open(img); os.makedirs(out, exist_ok=True)
man = []
dbg = im.convert('RGB'); dd = ImageDraw.Draw(dbg)
for i in range(int(n)):
    c = y0 + c0 + i * pitch
    top, bot = c - half, c + half
    ya, yb = max(0, int(top - pitch * 0.9)), min(im.size[1], int(bot + pitch * 0.5))
    crop = im.crop((int(x0), ya, int(x1), yb)).convert('RGB')
    if scale != 1.0:
        crop = crop.resize((int(crop.size[0] * scale), int(crop.size[1] * scale)), Image.LANCZOS)
    d = ImageDraw.Draw(crop)
    for yy in ((top - ya) * scale, (bot - ya) * scale):
        d.line((0, yy, crop.size[0], yy), fill=(255, 0, 0), width=3)
    f = f"{prefix}_L{i + 1:02d}.jpg"; crop.save(os.path.join(out, f), quality=88)
    man.append({"file": f, "line": i + 1, "region_xyxy": [int(x0), ya, int(x1), yb], "target_band_y": [int(top), int(bot)]})
    dd.line((x0, top, x1, top), fill=(255, 0, 0), width=3); dd.line((x0, bot, x1, bot), fill=(0, 0, 255), width=3); dd.text((x0 + 5, c - 10), str(i + 1), fill=(255, 0, 0))
dbg.crop((int(x0), int(y0), int(x1), int(y1))).resize((1000, int((y1 - y0) * 1000 / (x1 - x0)))).save(os.path.join(out, f"{prefix}_bands_debug.jpg"), quality=80)
json.dump(man, open(os.path.join(out, f"{prefix}_manifest.json"), 'w'), indent=0)
print(prefix, 'crops', len(man), 'pitch', pitch, 'first centre', c0)
