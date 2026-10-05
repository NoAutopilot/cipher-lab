#!/usr/bin/env python3
"""N9-GRAZ: cut the key-table z-like cells (Tomokiyo a row 3, Tomokiyo r row 1, Lasry R row 5, Lasry Unknown 2nd) at 3x as
unlabelled strips #75-#78 (order shuffled), appended to z_occ.tsv's answer sheet as table_cells.tsv; sheet_tables.jpg. Disk only."""
import sys, random
from pathlib import Path
from PIL import Image, ImageDraw
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; S = H.parents[2] / "sources/cryptiana/web"
cells = [("Tomokiyo a row 3 (key A)", "francisGramont.png", (0, 82, 40, 118)), ("Tomokiyo r row 1 (key R)", "francisGramont.png", (390, 28, 428, 64)),
         ("Lasry R row 5 (key R)", "GL/BnF_fr3071_f17.png", (628, 220, 668, 260)), ("Lasry Unknown 2nd", "GL/BnF_fr3071_f17.png", (52, 412, 98, 454))]
ids = [75, 76, 77, 78]; random.Random(5).shuffle(ids); rows = ["id\tcell\tfile\tbox"]; ims = []
for (nm, f, b), i in zip(cells, ids):
    im = Image.open(S / f).convert("RGB").crop(b); im = im.resize((im.width * 4, im.height * 4))
    lab = Image.new("RGB", (im.width + 70, im.height), "white"); lab.paste(im, (70, 0)); ImageDraw.Draw(lab).text((4, 4), f"#{i}", fill=(0, 0, 0))
    lab.save(H / "strips" / f"{i:03d}.jpg", quality=90); ims.append((i, lab)); rows.append(f"{i}\t{nm}\t{f}\t{b}")
(H / "table_cells.tsv").write_text("\n".join(rows) + "\n")
ims.sort(); W = sum(l.width + 10 for _, l in ims); sh = Image.new("RGB", (W, max(l.height for _, l in ims)), (150, 150, 150)); x = 0
for _, l in ims: sh.paste(l, (x, 0)); x += l.width + 10
sh.save(H / "sheet_tables.jpg", quality=90)
