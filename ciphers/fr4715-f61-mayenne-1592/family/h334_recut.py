#!/usr/bin/env python3
"""H334 (runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ, 29 Sept 2026), script-only: re-cut the four f.106r crops whose cipher row left the band in
H332's cut (both sign readers reported it; the --local 18 --slope -0.028 window sat 40-50 px above the row at the right end, where the rows
flatten). Centres (native y) set by eye from a ruled strip of x 3600-4650 (rows at the right edge: L07 1300, L08 1400, L09 1506, L10 1612,
L11 1719, L12 1819); every other crop of sheets/f106r_b keeps H332's box. Same geometry (up 78, down 42, x3, overlap ticks). Writes the four crops
over sheets/f106r_b/ and the boxes into sheets/f106r_b_bands.json (key 'recut_h334').   python3 h334_recut.py [--check]"""
import json, os, sys
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); J = f"{HERE}/sheets/f106r_b_bands.json"; bj = json.load(open(J))
FIX = {"f106r_L08_s7.jpg": 1400, "f106r_L09_s6.jpg": 1504, "f106r_L09_s7.jpg": 1506, "f106r_L10_s7.jpg": 1612}
up, down, sc, ov = 78, 42, 3.0, 60
new = {}
for name, cy in FIX.items():
    x0, _, x1, _ = bj["boxes"][name]; new[name] = [x0, cy - up, x1, cy + down]
if "--check" in sys.argv:
    ok = bj.get("recut_h334") == new; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
im = Image.open(f"{HERE}/images/3983_f106r.jpg").convert("L")
for name, (x0, y0, x1, y1) in new.items():
    c = im.crop((x0, y0, x1, y1)).convert("RGB"); c = c.resize((int(c.width * sc), int(c.height * sc)), Image.LANCZOS); d = ImageDraw.Draw(c)
    d.line((int(ov * sc), 0, int(ov * sc), 12), fill=(255, 0, 0), width=3)
    if x1 < 1540 + 3060: d.line((c.width - int(ov * sc), 0, c.width - int(ov * sc), 12), fill=(255, 0, 0), width=3)
    c.save(f"{HERE}/sheets/f106r_b/{name}", quality=90); print(name, [x0, y0, x1, y1], "was", bj["boxes"][name])
bj["recut_h334"] = new; json.dump(bj, open(J, "w"), indent=1)
