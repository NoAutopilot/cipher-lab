#!/usr/bin/env python3
"""R14-OLDF (6 Oct 2026): per-token crops of the 14 M/I-graded B/C1 tokens, cut from the leaves on disk (no network).
Boxes (adjusted once after a contact-sheet check) are in the coordinates of the A2-OLD regions (B: scan 002 region 3300,2300,1680,1200 at native scale;
C1: scan 006 region 200,120,2420,760, boxes read on a 2000-px view and scaled x1.21). Output: 3x upscaled crops
images/crops_R14OLDF/<id>.png plus a 1x copy. Re-run: python3 scripts/token_crops_R14OLDF.py"""
from PIL import Image
B = ("images/002_8de1649f-efac-4956-9dbf-253653e2c7e7.jpg", (3300, 2300), 1.0)
C = ("images/006_d027ee45-9cd0-44db-82cd-45ed3575eecb.jpg", (200, 120), 1.21)
BOX = {  # id: (leaf, (x0,y0,x1,y1) in region view coords)
 "B28": (B, (825, 240, 915, 345)), "B29": (B, (890, 240, 1210, 360)), "B31": (B, (1375, 230, 1625, 340)),
 "B37": (B, (970, 335, 1200, 435)), "B57": (B, (65, 645, 270, 775)), "B64": (B, (1482, 635, 1645, 735)),
 "C1_03": (C, (812, 45, 880, 140)), "C1_05": (C, (955, 40, 1210, 140)), "C1_21": (C, (795, 215, 1150, 350)),
 "C1_29": (C, (825, 345, 965, 455)), "C1_30": (C, (975, 350, 1130, 430)), "C1_31": (C, (1155, 335, 1410, 455)),
 "C1_36": (C, (460, 465, 610, 585)), "C1_44": (C, (440, 540, 640, 690)),
}
cache = {}
for k, ((f, (ox, oy), s), (x0, y0, x1, y1)) in BOX.items():
    im = cache.setdefault(f, Image.open(f))
    c = im.crop((ox + int(x0 * s), oy + int(y0 * s), ox + int(x1 * s), oy + int(y1 * s)))
    c.save(f"images/crops_R14OLDF/{k}_1x.png")
    c.resize((c.width * 3, c.height * 3), Image.LANCZOS).save(f"images/crops_R14OLDF/{k}.png")
    print(k, c.size)
