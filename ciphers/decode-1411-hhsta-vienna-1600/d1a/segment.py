#!/usr/bin/env python3
"""D1A-D1411: split a line crop into ink groups by vertical-projection gaps (placement aid only).
  python3 d1a/segment.py CROP [mingap] -> prints x-ranges of groups"""
import sys
from PIL import Image
import numpy as np
def groups(path, mingap=14, thr=None):
    g = np.asarray(Image.open(path).convert("L"), dtype=float)
    h = g.shape[0]; band = g[int(h*.2):int(h*.8)]
    t = thr or (np.median(band) - 60)
    col = (band < t).sum(0) > 1
    out = []; x = 0; n = len(col)
    while x < n:
        if col[x]:
            s = x
            while x < n and (col[x:x+mingap].any()):
                x += 1
            out.append((s, x))
        x += 1
    return [o for o in out if o[1]-o[0] > 6]
if __name__ == "__main__":
    print(groups(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 14))
