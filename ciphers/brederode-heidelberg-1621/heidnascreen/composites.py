"""HEID-NA-SCREEN (16 Oct 2026): 700 px composites, 4 tiles per image (2x2) (each tile the scan at its fetched 700 px width, not shrunk),
with planted controls shuffled in by a seed; the key (tile -> scan or control) is written to KEYJSON and not read until the calls are made.
usage: composites.py IMGDIR OUTDIR KEYJSON SEED CTRL_NAME=FILE[,FILE...] ... -- ORDERS...
A control name may be given more than once (planted twice)."""
import sys, json, random, os
from PIL import Image, ImageDraw
imgdir, out, keyf, seed = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
i = sys.argv.index("--"); ctrl_args, orders = sys.argv[5:i], sys.argv[i + 1:]
items = [("scan", o, os.path.join(imgdir, f"s{int(o):04d}_700.jpg")) for o in orders]
for c in ctrl_args:
    name, f = c.split("=", 1); items.append(("ctrl", name, f))
rng = random.Random(seed); rng.shuffle(items); os.makedirs(out, exist_ok=True)
key = {}
PER = 4
for n in range(0, len(items), PER):
    grp = items[n:n + PER]; ims = [Image.open(f).convert("RGB") for _, _, f in grp]
    ims = [im if im.width <= 700 else im.resize((700, round(im.height * 700 / im.width))) for im in ims]
    RH = max(im.height for im in ims) + 30; comp = Image.new("RGB", (1410, RH * 2), "white"); d = ImageDraw.Draw(comp)
    for j, (im, it) in enumerate(zip(ims, grp)):
        lab = f"{n // PER + 1:02d}{'ABCD'[j]}"; key[lab] = [it[0], it[1]]; x, y = (j % 2) * 710, (j // 2) * RH
        comp.paste(im, (x, y + 30)); d.rectangle([x, y, x + 60, y + 26], fill="black"); d.text((x + 8, y + 7), lab, fill="white")
    comp.save(os.path.join(out, f"comp{n // PER + 1:02d}.jpg"), quality=90)
json.dump(key, open(keyf, "w"), indent=0); print(len(key), "tiles", (len(items) + PER - 1) // PER, "composites")
