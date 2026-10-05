#!/usr/bin/env python3
"""List flat pure-white patches (white-out candidates) in images/Rayburn-Cryptogram.jpg.

D2B-RAY, 5 Oct 2026. Paper background median is 247; a patch is a connected region of pixels >= 253
after a 2-iteration binary opening, area >= 300 px. The bottom-edge and fold-crease components are
listed too and are classified by eye in copy_condition.tsv (see NOTES.md). --contrast OUT writes a
(a-215)*6 contrast stretch that shows the sharp-edged patches. Needs pillow, numpy, scipy.
"""
import argparse, os
import numpy as np
from PIL import Image
from scipy import ndimage as nd

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument("--image", default=os.path.join(HERE, "images", "Rayburn-Cryptogram.jpg"))
ap.add_argument("--thr", type=int, default=253)
ap.add_argument("--contrast")
args = ap.parse_args()
a = np.asarray(Image.open(args.image).convert("L")).astype(int)
m = nd.binary_opening(a >= args.thr, iterations=2)
lab, n = nd.label(m)
print("x0\tx1\ty0\ty1\tarea")
for i, o in enumerate(nd.find_objects(lab)):
    s = int((lab[o] == i + 1).sum())
    if s >= 300:
        print(f"{o[1].start}\t{o[1].stop}\t{o[0].start}\t{o[0].stop}\t{s}")
if args.contrast:
    Image.fromarray(np.clip((a - 215) * 6, 0, 255).astype("uint8")).save(args.contrast)
