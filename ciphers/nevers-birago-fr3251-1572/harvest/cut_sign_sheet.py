#!/usr/bin/env python3
"""Cut a value-blind sign sheet from Tomokiyo's NeversBirago.png (HARVEST-D2, 28 Sept 2026), the way HARVEST-A did for
the Ceppo-Nevers table: ink blobs in the letter grid (y 40-235) and the word-code row (y 300-350) are found by
connected components, assigned to the header column whose x-centre is nearest, relabelled T## by a seeded shuffle and
laid out on a grid with the letter headers removed. Writes sign_sheet_blind_1572.png (for readers) and
sign_id_map_1572.json (id -> value, never shown to a reader).
"""
import json, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
HERE = Path(__file__).resolve().parent
SRC = HERE.parents[2] / "sources/cryptiana/web/img/NeversBirago.png"
COLS = [("a", 20), ("b", 57), ("c", 93), ("d", 131), ("e", 168), ("f", 205), ("g", 243), ("h", 280), ("i", 318),
        ("l", 345), ("m", 382), ("n", 430), ("o", 469), ("p", 507), ("q", 545), ("r", 590), ("s", 622), ("t", 655),
        ("u", 693), ("x", 730), ("y", 770), ("z", 808), ("et", 890)]
WORDS = [("che", 100), ("per", 170), ("qual", 250), ("quello", 328), ("carmagnola", 470), ("turino", 592),
         ("bugonotti", 730)]
im = Image.open(SRC).convert("L"); W, H = im.size; px = im.load()
ink = [[px[x, y] < 140 for x in range(W)] for y in range(H)]


def blobs(y0, y1, min_px=12, join=6):
    seen = [[False] * W for _ in range(H)]; out = []
    for y in range(y0, y1):
        for x in range(W):
            if ink[y][x] and not seen[y][x]:
                st = [(x, y)]; seen[y][x] = True; pts = []
                while st:
                    cx, cy = st.pop(); pts.append((cx, cy))
                    for dx in range(-join, join + 1):
                        for dy in range(-join, join + 1):
                            nx, ny = cx + dx, cy + dy
                            if y0 <= ny < y1 and 0 <= nx < W and ink[ny][nx] and not seen[ny][nx]:
                                seen[ny][nx] = True; st.append((nx, ny))
                if len(pts) >= min_px:
                    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
                    out.append((min(xs), min(ys), max(xs), max(ys)))
    return out


cells = []
for (x0, y0, x1, y1) in blobs(40, 235):
    cx = (x0 + x1) / 2; col = min(COLS, key=lambda c: abs(c[1] - cx))
    cells.append({"value": col[0], "box": [x0 - 3, y0 - 3, x1 + 4, y1 + 4], "kind": "letter"})
for (x0, y0, x1, y1) in blobs(307, 352):
    if x1 - x0 > 60 and y1 - y0 < 8:  # the row underline, not a sign
        continue
    cx = (x0 + x1) / 2; col = min(WORDS, key=lambda c: abs(c[1] - cx))
    cells.append({"value": col[0], "box": [x0 - 3, y0 - 3, x1 + 4, y1 + 4], "kind": "word"})
# the digit codes 85/86/89 are two blobs each: merge same-word blobs
merged = {}
for c in cells:
    k = (c["kind"], c["value"]) if c["kind"] == "word" else id(c)
    if k in merged:
        b = merged[k]["box"]; c2 = c["box"]
        merged[k]["box"] = [min(b[0], c2[0]), min(b[1], c2[1]), max(b[2], c2[2]), max(b[3], c2[3])]
    else:
        merged[k] = c
cells = list(merged.values())
rng = random.Random(1572); ids = rng.sample(range(10, 99), len(cells))
for c, i in zip(cells, ids):
    c["id"] = f"T{i}"
cells.sort(key=lambda c: c["id"])
CW, CH, NC = 110, 110, 9
rows = (len(cells) + NC - 1) // NC
sheet = Image.new("RGB", (NC * CW, rows * CH), "white"); d = ImageDraw.Draw(sheet)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
except OSError:
    font = ImageFont.load_default()
for n, c in enumerate(cells):
    gx, gy = (n % NC) * CW, (n // NC) * CH
    d.rectangle([gx, gy, gx + CW - 1, gy + CH - 1], outline="grey")
    d.text((gx + 4, gy + 2), c["id"], fill="blue", font=font)
    crop = im.crop(tuple(c["box"])); s = min(2.5, (CW - 12) / crop.width, (CH - 32) / crop.height)
    crop = crop.resize((max(1, int(crop.width * s)), max(1, int(crop.height * s))), Image.LANCZOS)
    sheet.paste(crop.convert("RGB"), (gx + (CW - crop.width) // 2, gy + 26 + (CH - 26 - crop.height) // 2))
sheet.save(HERE / "sign_sheet_blind_1572.png")
json.dump(cells, open(HERE / "sign_id_map_1572.json", "w"), indent=0)
from collections import Counter
print(len(cells), "cells;", dict(Counter(c["value"] for c in cells)))
