#!/usr/bin/env python3
"""Cut native-resolution line crops of BnF Dupuy 468 f.28r-v (Gallica btv1b10035959t canvases 63, 64).

Reads images/img/c63_full.jpg (f.28r) and c64_full.jpg (f.28v), 4039 x 5950 px each (IIIF full/full,
see manifest.json), and writes images/crops/<page>_L<nn>_s<k>.jpg plus images/crops/manifest.json with
each crop's source file and pixel box (left, top, right, bottom). Nothing is rescaled. Each line is cut in
two overlapping segments (each under 2400 px wide). The band runs ABOVE px above the line's centre (room
for the interlinear gloss, which sits above the word it glosses) and BELOW px below, so a crop also shows
the lower edge of the line above; the line being transcribed is the one in the lower part of the crop.

Tone: greyscale, levels stretch (LO, HI) and gamma GAMMA. The interlinear gloss is a faint grey
(ink ~140-200 on paper ~243); the stretch darkens it and whitens the paper. The unmodified page images
stay in img/. Line centres were measured on 23 Sept 2026 as dark-pixel row-profile peaks checked by eye.

Line ids: r = f.28r (canvas 63), v = f.28v (canvas 64). r00 is the address line, r01-r30 the body;
v01-v11 are the verso lines that carry cipher (v12-v17 are plain Latin, transcribed directly).
Run from anywhere: python3 ciphers/dupuy468-anhalt/images/crop.py
"""
import json
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "crops")
QUALITY = 80
ABOVE, BELOW = 175, 85
LO, HI, GAMMA = 90, 240, 1.4
SEGS = {"r": [(380, 2250), (1950, 3850)], "v": [(300, 2250), (1950, 3950)]}
SRC = {"r": "img/c63_full.jpg", "v": "img/c64_full.jpg"}
CENTRES = {
    "r": [840, 1105, 1252, 1425, 1560, 1700, 1830, 1996, 2120, 2250, 2378, 2515, 2650, 2767, 2918, 3050,
          3175, 3330, 3486, 3612, 3755, 3900, 4030, 4140, 4258, 4387, 4535, 4644, 4767, 4893, 5005],
    "v": [None, 775, 905, 1022, 1150, 1260, 1370, 1470, 1600, 1720, 1856, 1990],
}


def lut():
    t = []
    for v in range(256):
        x = min(1.0, max(0.0, (v - LO) / (HI - LO)))
        t.append(int(round(255 * x ** GAMMA)))
    return t


def main():
    os.makedirs(OUT, exist_ok=True)
    table = lut()
    man = []
    for page, cs in CENTRES.items():
        im = Image.open(os.path.join(HERE, SRC[page])).convert("L").point(table)
        for n, y in enumerate(cs):
            if y is None:
                continue
            for k, (x0, x1) in enumerate(SEGS[page], 1):
                box = (x0, max(0, y - ABOVE), x1, min(im.height, y + BELOW))
                name = f"{page}{n:02d}_s{k}.jpg"
                im.crop(box).save(os.path.join(OUT, name), quality=QUALITY)
                man.append({"crop": name, "source": SRC[page], "box": box})
    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump({"written_by": "images/crop.py", "date": "23 September 2026",
                   "tone": {"levels": [LO, HI], "gamma": GAMMA}, "crops": man}, f, indent=1)
    print(len(man), "crops")


if __name__ == "__main__":
    main()
