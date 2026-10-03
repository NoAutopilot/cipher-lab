"""GF4d (3 Oct 2026): find the ruled cell grid of the SHD 1812 deciphering-table photographs (jfbouch.fr) so
tools/iiif_lines.py can cut one crop per cell column-band. Prints, per image, the vertical rule x positions and,
per column strip, the horizontal rule y positions. Reads the local JPEGs only."""
import json, sys
import numpy as np
from PIL import Image

def groups(idx, gap):
    out = []
    for i in idx:
        if not out or i - out[-1][-1] > gap: out.append([i])
        else: out[-1].append(i)
    return [int(np.mean(g)) for g in out]

def vlines(a):
    d = a < 80
    h = a.shape[0]
    col = d[int(h*.1):int(h*.9)].sum(0)
    return groups(np.where(col > 0.25 * (h*.8))[0], 60)

def hlines(a, x0, x1):
    d = a[:, x0:x1] < 80
    row = d.sum(1)
    return groups(np.where(row > 0.45 * (x1 - x0))[0], 60)

res = {}
for f in sys.argv[1:]:
    a = np.asarray(Image.open(f).convert("L"))
    v = vlines(a)
    strips = []
    for x0, x1 in zip(v, v[1:]):
        w = x1 - x0
        strips.append({"x0": x0, "x1": x1, "h": hlines(a, x0 + w // 10, x1 - w // 10)})
    res[f] = {"v": v, "strips": strips}
    print(f, v)
    for s in strips: print("  ", s["x0"], s["x1"], s["h"])
json.dump(res, open("grid.json", "w"), indent=1)
