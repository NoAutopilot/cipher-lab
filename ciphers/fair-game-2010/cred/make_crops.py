"""FAIR-CRED (14 Oct 2026): cut one strip per marked credit line (the marked row and up to two rows below it) from
Rossignol's screenshots (regen_screens.sh) and stack them into labelled contact sheets. Images stay untracked."""
import csv
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps
HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "images" / "scratch"
OUT = SRC / "cred"; OUT.mkdir(parents=True, exist_ok=True)
rows = [r for r in csv.DictReader(open(HERE.parent / "reconcile_2026-10-03.tsv"), delimiter="\t") if r["y"]]
seen, strips = set(), []
for r in rows:
    key = (r["image"], r["y"])
    if key in seen:  # two marks on one row (SHOPMAN, FRANCO): one strip
        continue
    seen.add(key)
    im = Image.open(SRC / r["image"]).convert("RGB")
    y = int(r["y"]); x0, x1 = (150, 1110)
    c = im.crop((x0, max(0, y - 14), x1, min(im.height, y + 64))).resize(((x1 - x0) * 2, 156), Image.LANCZOS)
    c = ImageOps.autocontrast(c)
    c.save(OUT / f"strip_{int(r['idx']):02d}.png")
    strips.append((r["idx"], c))
PER = 11
for s in range(0, len(strips), PER):
    grp = strips[s:s + PER]
    sheet = Image.new("RGB", (grp[0][1].width + 80, 164 * len(grp)), "black")
    d = ImageDraw.Draw(sheet)
    for i, (idx, c) in enumerate(grp):
        sheet.paste(c, (80, i * 164 + 4)); d.text((6, i * 164 + 40), f"#{idx}", fill="white")
        d.line((0, i * 164 + 162, sheet.width, i * 164 + 162), fill=(90, 90, 90))
    sheet.save(OUT / f"sheet_{s // PER + 1}.png")
print(len(strips), "strips,", (len(strips) + PER - 1) // PER, "sheets ->", OUT)
