#!/usr/bin/env python3
"""D1411-P6b crop step (copy of d1411p5/cut_halves.py): cut each p.6 numeral line (d1411p6/lines.tsv) of IMG_R1411_I6600_P6.png (sha1 0f597628..., not committed)
into two half-line crops split at the least-inked column near the middle, each half at its own centre (the lines slope),
`top` px above and `bot` px below, upscaled 2x LANCZOS (prereg PREREG-D1411P6.md: half-lines at 2x, each < 2500 px wide).

  python3 d1411p6/cut_halves.py IMAGE OUTDIR      -> OUTDIR/<line>_a.jpg, <line>_b.jpg and OUTDIR/boxes.tsv
"""
import csv, hashlib, os, sys
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
img, out = sys.argv[1], sys.argv[2]
assert hashlib.sha1(open(img, "rb").read()).hexdigest().startswith("0f597628"), "not the p.6 image"
os.makedirs(out, exist_ok=True)
im = Image.open(img).convert("L")
a = np.asarray(im).astype(float); bg = np.asarray(im.filter(ImageFilter.BoxBlur(40))).astype(float)
ink = a < bg - 35
boxes = []
for r in csv.DictReader(open(os.path.join(HERE, "lines.tsv")), delimiter="\t"):
    x0, x1, ya, yb, top, bot = (int(r[k]) for k in ("x0", "x1", "ya", "yb", "top", "bot"))
    mid = (x0 + x1) // 2; ym = (ya + yb) // 2
    col = ink[ym - 30:ym + 30, mid - 160:mid + 160].sum(0)
    col = np.convolve(col, np.ones(9) / 9, "same")
    gap = mid - 160 + int(np.argmin(col[10:-10])) + 10
    for half, (bx0, bx1, yc) in (("a", (x0, gap, ya)), ("b", (gap, x1, yb))):
        box = (bx0, yc - top, bx1, yc + bot)
        c = im.crop(box); c = c.resize((c.size[0] * 2, c.size[1] * 2), Image.LANCZOS)
        assert c.size[0] < 2500
        name = f"{r['line']}_{half}.jpg"; c.save(os.path.join(out, name), quality=90)
        boxes.append([name, *box])
with open(os.path.join(out, "boxes.tsv"), "w") as f:
    f.write("crop\tx0\ty0\tx1\ty1\n"); f.writelines("\t".join(map(str, b)) + "\n" for b in boxes)
print(len(boxes), "crops")
