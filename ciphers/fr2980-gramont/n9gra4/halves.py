#!/usr/bin/env python3
"""N9-GRA4 (copy of n8gra3/halves.py, prefix f18rB only): cut non-overlapping a/b halves from tools/iiif_lines.py's s1/s2 crops (which overlap by ~1,900 px when the
region is only a little wider than --max-width). The cut is the emptiest column (least ink in the strip's middle rows)
within +-200 px of the line's native midpoint, taken on s1; b starts at the same native x on s2. Writes
images/fr3040_f18/<line>_a.jpg / _b.jpg and n9gra4/halves.tsv (crop, native x0, cut x, x1)."""
import json, re
from pathlib import Path
import numpy as np
from PIL import Image
D = Path(__file__).resolve().parent.parent / "images" / "fr3040_f18"
m = {e["crop"]: e for e in json.load(open(D / "manifest.json"))["iiif_lines"]}
rows = ["line\tx0\tcut\tx1"]
for s1 in sorted(k for k in m if re.match(r"f18rB_L\d\d_s1\.jpg$", k)):
    s2 = s1.replace("_s1", "_s2"); line = s1[:-7]
    b1, b2 = m[s1]["box"], m[s2]["box"]
    x0, x1 = b1[0], b2[2]; mid = (x0 + x1) // 2
    A = np.asarray(Image.open(D / s1).convert("L"), dtype=float)
    h = A.shape[0]; core = A[h // 4: 3 * h // 4]
    ink = (core < 150).sum(0)
    lo, hi = mid - 200 - x0, mid + 200 - x0
    win = np.convolve(ink, np.ones(9), "same")
    cut = x0 + lo + int(np.argmin(win[lo:hi]))
    Image.open(D / s1).crop((0, 0, cut - x0, h)).save(D / f"{line}_a.jpg", quality=90)
    I2 = Image.open(D / s2); I2.crop((cut - b2[0], 0, I2.width, I2.height)).save(D / f"{line}_b.jpg", quality=90)
    rows.append(f"{line}\t{x0}\t{cut}\t{x1}")
(Path(__file__).resolve().parent / "halves.tsv").write_text("\n".join(rows) + "\n")
print(len(rows) - 1, "lines")
