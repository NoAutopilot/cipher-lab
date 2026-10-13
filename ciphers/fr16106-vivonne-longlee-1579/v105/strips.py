#!/usr/bin/env python3
"""VIV-105: group tools/iiif_lines.py bands (images/v105/<page>/manifest.json) into strips of N bands, full text width,
scaled to <= 2400 px wide, for one-page-per-call blind reads. Readers number lines within each strip.
Regenerate: run v105/fetch.py, then the four iiif_lines.py commands in NOTES.md "## VIV-105", then
python3 v105/strips.py f105r f105v f106r f106v. Output images/v105/strips/<page>_S<k>.jpg (untracked) + v105/strips.tsv."""
import json, sys
from PIL import Image
N, MARGIN, MAXW = 4, 45, 2400
rows = []
for page in sys.argv[1:]:
    m = json.load(open(f"images/v105/{page}/manifest.json"))["iiif_lines"]
    src = "images/v105/" + {"f105r": "c110_f105r", "f105v": "c111_f105v", "f106r": "c111_f106r", "f106v": "c112_f106v"}[page] + ".jpg"
    im = Image.open(src)
    bands = {}
    for e in m:
        if not e["crop"].startswith(page):
            continue
        x0, y0, x1, y1 = e["box"]; b = bands.setdefault(e["band"], [x0, y0, x1, y1])
        b[0] = min(b[0], x0); b[1] = min(b[1], y0); b[2] = max(b[2], x1); b[3] = max(b[3], y1)
    keys = sorted(bands)
    for k in range(0, len(keys), N):
        grp = [bands[i] for i in keys[k:k + N]]
        x0 = min(g[0] for g in grp); x1 = max(g[2] for g in grp)
        y0 = max(0, min(g[1] for g in grp) - MARGIN); y1 = min(im.size[1], max(g[3] for g in grp) + MARGIN)
        c = im.crop((x0, y0, x1, y1))
        if c.size[0] > MAXW:
            c = c.resize((MAXW, round(c.size[1] * MAXW / c.size[0])), Image.LANCZOS)
        s = k // N + 1
        out = f"images/v105/strips/{page}_S{s:02d}.jpg"
        import os; os.makedirs("images/v105/strips", exist_ok=True)
        c.save(out, quality=90)
        rows.append(f"{page}\tS{s:02d}\tbands {keys[k]}-{keys[min(k+N, len(keys))-1]}\t{x0},{y0},{x1-x0},{y1-y0}\t{c.size[0]}x{c.size[1]}\t{out}")
open("v105/strips.tsv", "w").write("page\tstrip\tbands\tbox_in_page_image\tsize\tfile\n" + "\n".join(rows) + "\n")
print("\n".join(rows))
