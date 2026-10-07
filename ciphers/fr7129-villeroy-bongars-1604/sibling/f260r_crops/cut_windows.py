#!/usr/bin/env python3
"""Cut each p260 band (gloss row + cipher row) into ~520 px windows, 80 px overlap, upscaled 2x (D4-VILL2, 7 Oct 2026).
A red tick at the top of each window (after the first) marks where the previous window ended: signs left of it were in
the previous window. Reads f260r_crops/manifest.json band boxes and the src_*.jpg; writes f260r_crops/win/w<LL>_<kk>.jpg."""
import json
from pathlib import Path
from PIL import Image, ImageDraw
D = Path(__file__).resolve().parent
m = json.load(open(D / "manifest.json"))
bands = {}
for e in m["iiif_lines"]:
    if e["crop"].startswith("p260_L"):
        b = e["box"]; bands.setdefault(e["band"], [9999, b[1], 0, b[3]])
        bands[e["band"]][0] = min(bands[e["band"]][0], b[0]); bands[e["band"]][2] = max(bands[e["band"]][2], b[2])
src = Image.open(D / m["iiif_lines"][0]["source_file"]).convert("RGB")
out = D / "win"; out.mkdir(exist_ok=True)
W, OV, X0 = 520, 80, 200
for n, (x0, y0, x1, y1) in sorted(bands.items()):
    k, x = 0, X0
    while x < x1 - OV:
        k += 1
        c = src.crop((x, y0, min(x + W, x1), y1)); c = c.resize((c.size[0] * 2, c.size[1] * 2))
        if k > 1:
            ImageDraw.Draw(c).rectangle((2 * OV - 3, 0, 2 * OV + 3, 18), fill=(220, 0, 0))
        c.save(out / f"w{n:02d}_{k:02d}.jpg", quality=85)
        x += W - OV
    print(f"L{n:02d}: {k} windows")
