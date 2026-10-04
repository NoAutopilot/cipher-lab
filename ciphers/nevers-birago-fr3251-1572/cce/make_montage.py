#!/usr/bin/env python3
"""BIR-CCE step 1 (4 Oct 2026): value-blind montage for the glyph-correspondence read.
Panel A: every non-blank cell of Tomokiyo's Ceppo-Nevers table image (nevers_add1.png) cut out WITHOUT its header,
labelled C01.. ; the id->(column letter,row) map goes to cce/ceppo_cells.tsv, which is never shown to the reader.
Panel B: 1572 query signs (owner-sort piles of off-sheet tiles + the T42/T50/T95 conflict signs), up to 4 tiles each
from sorter/pages strips, labelled by pile id only. No value, no plaintext anywhere on the montage.
  python3 cce/make_montage.py   -> cce/montage_ceppo.png, cce/montage_1572.png, cce/ceppo_cells.tsv, cce/query_tiles.tsv"""
import csv
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps
H = Path(__file__).resolve().parents[1]; O = Path(__file__).resolve().parent; R = H.parents[1]
img = Image.open(R / "sources/cryptiana/web/img/nevers_add1.png").convert("L")
cols = "abcdefghilmnopqrstuxyz"; x0, cw = 1, 33.95; rows = [(37, 73), (73, 109), (109, 145), (145, 181), (181, 217)]
cells = []
for ci, c in enumerate(cols):
    for ri, (y0, y1) in enumerate(rows):
        box = (int(x0 + ci * cw) + 2, y0 + 2, int(x0 + (ci + 1) * cw) - 2, y1 - 2)
        t = img.crop(box)
        if sum(1 for p in t.get_flattened_data() if p < 120) < 6:
            continue
        if ri == 4 and 6 <= ci <= 13:
            continue  # the table's own title text, not a cell
        cells.append((c, ri + 1, t))
extra = [("et", 1, (775, 38, 800, 66))] + [("null", i + 1, (774 + 23 * i, 148, 798 + 23 * i, 184)) for i in range(6)]
for v, r, b in extra:
    cells.append((v, r, img.crop(b)))
S = 72; W = 8
def montage(items, path, s=S):
    n = len(items); hgt = (n + W - 1) // W
    M = Image.new("L", (W * (s + 40), hgt * (s + 22)), 255); d = ImageDraw.Draw(M)
    for i, (lab, t) in enumerate(items):
        t = ImageOps.contain(t, (s, s)); x, y = (i % W) * (s + 40), (i // W) * (s + 22)
        M.paste(t, (x + (s - t.width) // 2, y)); d.text((x + 2, y + s + 4), lab, fill=0)
    M.save(path)
with open(O / "ceppo_cells.tsv", "w") as f:
    f.write("cell\tcolumn\trow\n")
    items = []
    for i, (c, r, t) in enumerate(cells):
        cid = f"C{i+1:02d}"; f.write(f"{cid}\t{c}\t{r}\n"); items.append((cid, t))
montage(items, O / "montage_ceppo.png")
lab = list(csv.DictReader(open(H / "sorter/signs.tsv"), delimiter="\t"))
geo = {r["sid"]: r for r in lab}
st = list(csv.DictReader(open(H / "sorter/owner-sort-2026-10-04/settled_labels.tsv"), delimiter="\t"))
pile = defaultdict(list)
for r in st:
    if r["sid"] in geo and (r["new_sign"].startswith("X_NEW") or r["new_sign"].split("-")[0] in ("T42", "T50", "T95")):
        pile[r["new_sign"]].append(r["sid"])
qi = []; qrows = []
for p in sorted(pile):
    for sid in pile[p][:4]:
        g = geo[sid]; pg = Image.open(H / "sorter/pages" / f"{g['page']}.jpg").convert("L")
        x, y, w, h = (int(g[k]) for k in "xywh")
        qi.append((f"Q{len(qi)+1:02d}", pg.crop((x - 4, max(0, y - 4), x + w + 4, y + h + 4))))
        qrows.append((f"Q{len(qi):02d}", p, sid))
montage(qi, O / "montage_1572.png")
with open(O / "query_tiles.tsv", "w") as f:
    f.write("qid\tpile\tsid\n"); [f.write(f"{q}\t{p}\t{s}\n") for q, p, s in qrows]
print(len(cells), "ceppo cells;", len(pile), "piles;", len(qi), "tiles")
