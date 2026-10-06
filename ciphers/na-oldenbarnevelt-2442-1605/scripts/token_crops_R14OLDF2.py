#!/usr/bin/env python3
"""R14-OLDF2 (6 Oct 2026): tight re-cut of the C1 tokens whose R14-OLDF crops (scripts/token_crops_R14OLDF.py) straddled a
neighbouring word or line (C1_29, C1_31, C1_36, C1_44), plus C1_05 (flagged b8s424 / b8ss424). Boxes are in native pixels of
scan 006 on disk, eye-checked against a 1250x400 view of lines 4-6 (native 700,500 origin) before the blind call. Output:
images/crops_R14OLDF2/<label>.png (3x Lanczos) and <label>_1x.png; labels are neutral (T1-T5) so the reader sees no row id.
Map label -> token: transcription/R14OLDF2_labels.tsv. Re-run: python3 scripts/token_crops_R14OLDF2.py"""
import os
from PIL import Image
LEAF = "images/006_d027ee45-9cd0-44db-82cd-45ed3575eecb.jpg"
BOX = {  # label: (token, (x0, y0, x1, y1) native)
 "T1": ("C1_31", (1598, 508, 1930, 636)),
 "T2": ("C1_44", (735, 785, 985, 892)),
 "T3": ("C1_05", (1375, 158, 1694, 272)),
 "T4": ("C1_29", (1140, 518, 1365, 650)),
 "T5": ("C1_36", (755, 645, 958, 792)),
}
os.makedirs("images/crops_R14OLDF2", exist_ok=True)
im = Image.open(LEAF)
with open("transcription/R14OLDF2_labels.tsv", "w") as f:
    f.write("label\ttoken\tbox_native\n")
    for lab, (tok, b) in BOX.items():
        c = im.crop(b)
        c.save(f"images/crops_R14OLDF2/{lab}_1x.png")
        c.resize((c.width * 3, c.height * 3), Image.LANCZOS).save(f"images/crops_R14OLDF2/{lab}.png")
        f.write(f"{lab}\t{tok}\t{','.join(map(str, b))}\n")
        print(lab, tok, c.size)
