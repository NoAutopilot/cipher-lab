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

# id, source image, left, right, number of segments, body centre (y) of the writing in each segment.
# The lines drift up or down by as much as 110 px across the page, so each segment gets its own band:
# ABOVE px above the centre (room for ascenders and the marks written over some symbols) and BELOW px below.
# Centres were measured on 23 Sept 2026 as the peak of the dark-pixel row profile within each segment and
# checked by eye; f277v_L1 s1 was set by eye (the profile locked onto the line above).
ABOVE, BELOW = 170, 130
LINES = [
    ("f277r_L1", "img/f277r_s1.jpg", 1250, 6450, 4, [1178, 1112, 1087, 1117]),
    ("f277r_L2", "img/f277r_s1.jpg", 1250, 6450, 4, [1396, 1343, 1331, 1337]),
    ("f277r_L3", "img/f277r_s1.jpg", 1250, 6450, 4, [1571, 1559, 1571, 1549]),
    ("f277r_L4", "img/f277r_s1.jpg", 1250, 6450, 4, [1823, 1783, 1761, 1782]),
    ("f277r_L5", "img/f277r_s1.jpg", 1250, 6450, 4, [2043, 2047, 2038, 2086]),
    ("f277r_L6", "img/f277r_s1.jpg", 1250, 6450, 4, [2269, 2259, 2254, 2297]),
    ("f277r_L7", "img/f277r_s1.jpg", 1250, 6450, 4, [2532, 2525, 2499, 2502]),
    ("f277r_L8", "img/f277r_s1.jpg", 1250, 6450, 4, [2779, 2778, 2745, 2737]),
    ("f277r_B1", "img/f277r_s1.jpg", 3650, 6600, 2, [3875, 3877]),
    ("f277r_B2", "img/f277r_s1.jpg", 1150, 6600, 4, [4179, 4175, 4134, 4117]),
    ("f277r_B3", "img/f277r_s1.jpg", 1150, 4200, 2, [4414, 4371]),
    ("f277r_C1", "img/f277r_s1.jpg", 1150, 4200, 2, [7372, 7314]),
    ("f277r_C2", "img/f277r_s1.jpg", 1150, 6600, 4, [7877, 7851, 7795, 7749]),
    ("f277v_L1", "img/f277v_s1.jpg", 1500, 5300, 3, [4300, 4241, 4185]),
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
    for lid, src, left, right, n, centres in LINES:
        if src not in cache:
            cache[src] = Image.open(os.path.join(HERE, src))
        im = cache[src]
        for k, ((x0, x1), cy) in enumerate(zip(segments(left, right, n), centres), 1):
            top, bottom = cy - ABOVE, cy + BELOW
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
