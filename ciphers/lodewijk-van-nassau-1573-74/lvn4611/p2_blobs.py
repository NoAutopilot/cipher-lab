"""LVN-4611P2 (15 Oct 2026): number the ink runs on each deskewed physical line crop of WVO 4611 p2 (tools/iiif_lines.py --image
<p2 300-dpi png> --region 250,140,2200,3000 --prefix p2 --deskew --centres <lvn4611/p2_centres.txt>), for placement by eye.
usage: python3 p2_blobs.py LINES_DIR OUT_PREFIX [GAP]   writes OUT_PREFIX_seg.json and numbered strip sheets OUT_PREFIX_<k>.jpg (scratch only)."""
import sys, json, glob, os
import numpy as np
from PIL import Image, ImageDraw
d, out = sys.argv[1:3]; GAP = int(sys.argv[3]) if len(sys.argv) > 3 else 9
seg = {}; strips = []
for f in sorted(glob.glob(os.path.join(d, 'p2_L*.jpg'))):
    ln = os.path.basename(f)[3:6].replace('L', 'K')
    pim = Image.open(f).convert('L'); im = np.array(pim); h = im.shape[0]
    band = im[int(h * .25):int(h * .8)] < 150
    col = band.sum(0); on = col >= 2
    m = []; a = None
    for x, v in enumerate(on):
        if v and a is None: a = x
        if not v and a is not None: m.append([a, x]); a = None
    mm = []
    for a, b in m:
        if mm and a - mm[-1][1] < GAP: mm[-1][1] = b
        else: mm.append([a, b])
    mm = [(a, b) for a, b in mm if b - a >= 14 and col[a:b].sum() > 150]
    seg[ln] = [[int(a), int(b)] for a, b in mm]
    s2 = Image.new('RGB', (pim.width, h + 18), 'white'); s2.paste(pim.convert('RGB'), (0, 18)); dr = ImageDraw.Draw(s2)
    for i, (a, b) in enumerate(mm):
        dr.line([(a, 16), (b, 16)], fill=(0, 90, 200), width=3); dr.text(((a + b) // 2 - 6, 2), str(i + 1), fill=(200, 40, 0))
    strips.append((ln, s2))
json.dump(seg, open(out + '_seg.json', 'w'))
k = 0
for i in range(0, len(strips), 3):
    ims = []
    for ln, s in strips[i:i + 3]:
        mid = (s.width + 1) // 2
        for half in (s.crop((0, 0, mid + 30, s.height)), s.crop((mid - 30, 0, s.width, s.height))):
            t = Image.new('RGB', (half.width, half.height + 14), 'white'); t.paste(half, (0, 14)); ImageDraw.Draw(t).text((2, 1), ln, fill=(0, 120, 0)); ims.append(t)
    o = Image.new('RGB', (max(x.width for x in ims), sum(x.height for x in ims)), 'white'); y = 0
    for x in ims: o.paste(x, (0, y)); y += x.height
    o.save(f'{out}_{k}.jpg', quality=82); k += 1
print(k, {l: len(v) for l, v in seg.items()})
