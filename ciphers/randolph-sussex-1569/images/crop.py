#!/usr/bin/env python3
"""Cut native-resolution line segments of the cipher passages on BL Cotton Caligula C II f.277r-v.

Reads images/img/f277r_s1.jpg and f277v_s1.jpg (full-resolution IIIF stitches, see manifest.json) and writes
images/crops/native/<id>_s<k>.jpg plus images/crops/native/manifest.json with each crop's source file and
pixel box (left, top, right, bottom). Nothing is rescaled: every crop is at the page image's own resolution,
each at most MAX_W px wide so the image reader does not downscale it. Consecutive segments of a line overlap
by about 10 percent of the segment width. Written 23 Sept 2026.

Line ids: f277r_L1..L8 is the main cipher block; L1 begins in plaintext and L8 ends in plaintext, and those
stretches are the opening and resuming context (separate crops of the whole plaintext lines above and below
were cut in a first run and dropped to keep the folder under 30 MB). f277r_B1..B3 and f277r_C1..C2
are two shorter passages further down the recto, located on 23 Sept 2026 from the page image and not in the
21 Sept transcription. f277v_L1 is the one cipher line on the verso. Only the part of a line that holds
cipher (plus some context) is cut where the rest is plain.

Run from anywhere: python3 ciphers/randolph-sussex-1569/images/crop.py
"""
import json
import os
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "crops", "native")
MAX_W = 2400
QUALITY = 75  # 85 asked for; lowered to keep the folder under 30 MB (see NOTES.md)
GRAY = True  # brown ink on buff paper: greyscale keeps the strokes and halves the file size
# Levels stretch on the greyscale: paper (grey ~205-225) goes to white, ink (grey ~60-180) is darkened
# linearly. Resolution is untouched; this only whitens the paper texture, which is most of the JPEG size,
# so the folder stays under the 30 MB cap. The unmodified page images stay in img/.
LEVELS = (70, 200)

# id, source image, top, bottom, left, right, number of segments
LINES = [
    ("f277r_L1", "img/f277r_s1.jpg", 1050, 1330, 1250, 6450, 4),
    ("f277r_L2", "img/f277r_s1.jpg", 1260, 1530, 1250, 6450, 4),
    ("f277r_L3", "img/f277r_s1.jpg", 1470, 1740, 1250, 6450, 4),
    ("f277r_L4", "img/f277r_s1.jpg", 1680, 1960, 1250, 6450, 4),
    ("f277r_L5", "img/f277r_s1.jpg", 1880, 2190, 1250, 6450, 4),
    ("f277r_L6", "img/f277r_s1.jpg", 2070, 2380, 1250, 6450, 4),
    ("f277r_L7", "img/f277r_s1.jpg", 2370, 2660, 1250, 6450, 4),
    ("f277r_L8", "img/f277r_s1.jpg", 2620, 2920, 1250, 6450, 4),
    ("f277r_B1", "img/f277r_s1.jpg", 3780, 4060, 3650, 6600, 2),
    ("f277r_B2", "img/f277r_s1.jpg", 4020, 4300, 1150, 6600, 4),
    ("f277r_B3", "img/f277r_s1.jpg", 4270, 4550, 1150, 4200, 2),
    ("f277r_C1", "img/f277r_s1.jpg", 7180, 7480, 1150, 4200, 2),
    ("f277r_C2", "img/f277r_s1.jpg", 7660, 7940, 1150, 6600, 4),
    ("f277v_L1", "img/f277v_s1.jpg", 4150, 4430, 1500, 5300, 3),
]


def segments(left, right, n):
    """n boxes spanning [left, right] with ~10% overlap between neighbours."""
    width = (right - left) / (n - 0.1 * (n - 1))
    step = width * 0.9
    return [(round(left + i * step), round(min(right, left + i * step + width))) for i in range(n)]


def main():
    os.makedirs(OUT, exist_ok=True)
    cache, manifest = {}, {"written": "2026-09-23", "quality": QUALITY, "grayscale": GRAY,
                        "levels": LEVELS, "crops": []}
    for lid, src, top, bottom, left, right, n in LINES:
        if src not in cache:
            cache[src] = Image.open(os.path.join(HERE, src))
        im = cache[src]
        for k, (x0, x1) in enumerate(segments(left, right, n), 1):
            assert x1 - x0 <= MAX_W, (lid, k, x1 - x0)
            c = im.crop((x0, top, x1, bottom))
            if GRAY:
                c = c.convert("L")
                if LEVELS:
                    lo, hi = LEVELS
                    c = c.point([max(0, min(255, round((v - lo) * 255 / (hi - lo)))) for v in range(256)])
            name = f"{lid}_s{k}.jpg"
            c.save(os.path.join(OUT, name), quality=QUALITY, optimize=True)
            manifest["crops"].append({"file": name, "source": "images/" + src, "line": lid, "segment": k,
                                      "box": [x0, top, x1, bottom], "size": [x1 - x0, bottom - top]})
    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=1)
    print(len(manifest["crops"]), "crops written to", OUT)


if __name__ == "__main__":
    main()
