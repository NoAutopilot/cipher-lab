"""Build 3x3 contact sheets: 6 scans + 3 disk controls per sheet, seeded shuffle, tile letters only.
usage: sheets.py IMGDIR WIDTH OUTDIR KEYJSON SEED CTRL_CIPHER CTRL_PLAIN CTRL_PS ORDERS..."""
import sys, json, random, os
from PIL import Image, ImageDraw
imgdir, width, out, keyf, seed = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], int(sys.argv[5])
ctrls = {"CTRL-CIPHER": sys.argv[6], "CTRL-PLAIN": sys.argv[7], "CTRL-PS": sys.argv[8]}
orders = sys.argv[9:]
rng = random.Random(seed); os.makedirs(out, exist_ok=True)
TW, TH = 700, 520
key = {}
for si in range(0, len(orders), 6):
    items = orders[si:si+6] + list(ctrls)
    rng.shuffle(items)
    n = si // 6 + 1; key[n] = {}
    sheet = Image.new("RGB", (3*TW, 3*TH), "white"); d = ImageDraw.Draw(sheet)
    for i, it in enumerate(items):
        L = "ABCDEFGHI"[i]; key[n][L] = it
        f = ctrls[it] if it in ctrls else os.path.join(imgdir, f"s{int(it):04d}_{width}.jpg")
        im = Image.open(f).convert("RGB"); im.thumbnail((TW-10, TH-30))
        x, y = (i % 3)*TW, (i // 3)*TH
        sheet.paste(im, (x+5, y+28)); d.rectangle([x, y, x+40, y+26], fill="black"); d.text((x+14, y+7), L, fill="white")
    sheet.save(os.path.join(out, f"sheet{n:02d}.png"))
json.dump(key, open(keyf, "w"), indent=0)
print(len(key), "sheets")
