#!/usr/bin/env python3
"""MONL-KING3 (20 Oct 2026): cut f.133 (c258) L11-L25 line crops from the native page fetched by regen_monlking3.sh.
tools/iiif_lines.py's peak finder split this region irregularly (pitch 53-67, two lines merged at 90 px distance), so the bands
are placed here from the deskewed row-ink profile (rotation -2.0 deg about the region centre; peaks >= 50 px apart, pitch 102-112):
L10 at profile peak 0 (anchor, matches king2's L10 ending '//'), L11-L25 the next 15 peaks. Each band is 180 px tall and cut into
segment 1 (region x 0-1700) and segment 2 (x 1400-2350, stopping at the gutter so the facing leaf is excluded), 300 px overlap, the king2 prompt's convention."""
import sys, json
import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw
HERE = Path(__file__).resolve().parent
SRC = HERE / "images/scratchking2/src_image_v3_ark_12148_btv1b9060724s_f258_full.jpg"
OUT = HERE / "images/scratchking3"; (OUT / "crops").mkdir(parents=True, exist_ok=True)
X0, Y0, W, H, ANG = 1150, 1750, 2550, 1850, -2.0
reg = Image.open(SRC).convert("L").crop((X0, Y0, X0 + W, Y0 + H)).rotate(ANG, resample=Image.BILINEAR, fillcolor=255)
ink = (255 - np.asarray(reg, dtype=float))[:, 200:2300].sum(1)
s = np.convolve(ink, np.ones(31) / 31, "same")
pk = [y for y in range(1, H - 1) if s[y] >= s[y - 1] and s[y] > s[y + 1] and s[y] == s[max(0, y - 50):y + 50].max()]
lines = {f"L{10 + i:02d}": y for i, y in enumerate(pk[:16])}
dbg = reg.convert("RGB"); d = ImageDraw.Draw(dbg)
man = {}
for name, y in lines.items():
    d.line((0, y - 90, W, y - 90), fill=(0, 0, 200), width=2); d.text((5, y - 88), name, fill=(0, 0, 200))
    if name == "L10": continue
    band = reg.crop((0, y - 90, W, y + 90))
    band.crop((0, 0, 1700, 180)).save(OUT / f"crops/c258_{name}_s1.jpg", quality=92)
    band.crop((1400, 0, 2350, 180)).save(OUT / f"crops/c258_{name}_s2.jpg", quality=92)
    man[name] = {"profile_y": int(y), "native_y_centre_at_region_centre": int(Y0 + y)}
dbg.resize((W // 2, H // 2)).save(OUT / "c258_king3_bands_debug.jpg", quality=85)
(OUT / "manifest.json").write_text(json.dumps({"source": str(SRC.name), "region": [X0, Y0, W, H], "rotate": ANG, "lines": man}, indent=1) + "\n")
print({k: int(v) for k, v in lines.items()})
