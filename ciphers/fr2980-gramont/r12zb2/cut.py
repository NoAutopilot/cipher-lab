#!/usr/bin/env python3
"""R12D-GRAZB2: cut one tight sign box per r12zb/occ.tsv token (PREREG-R12D-GRAZB2.md). Applies r12zb2/fixes.tsv
(id, run offset such as -1, or an x0:x1 pixel range, reason). Writes r12zb2/tiles/<id>.png (sorter tiles, unlabelled, shuffled ids),
r12zb2/check/<id>.jpg (worker's eye-check overlay: box on +-3 signs, code shown) and r12zb2/boxes.tsv.
python3 r12zb2/cut.py"""
import sys
from pathlib import Path
from PIL import Image, ImageDraw
if "--help" in sys.argv: print(__doc__); sys.exit()
H = Path(__file__).resolve().parent; T = H.parent
sys.path.insert(0, str(H)); from seg import align
halves = {l.split("\t")[0]: l.split("\t")[2].split() for l in (H / "halves.tsv").read_text().splitlines()[1:]}
fixes = {}
fp = H / "fixes.tsv"
if fp.exists():
    for l in fp.read_text().splitlines()[1:]:
        if l.strip(): r = l.split("\t"); fixes[r[0]] = r[1]
cache = {}
(H / "tiles").mkdir(exist_ok=True); (H / "check").mkdir(exist_ok=True)
rows = ["id\tset\tsrc\tline_pos\timage\tj\tn\tcode_here\tx0\tx1\tfix"]
for l in (T / "r12zb/occ.tsv").read_text().splitlines()[1:]:
    sid, st, src, lp, img, xf = l.split("\t")
    toks = halves[img]; n = len(toks); pos = int(lp.split()[1])
    second = img.endswith(("b.jpg", "_s2.jpg"))
    first = img[:-5] + "a.jpg" if img.endswith("b.jpg") else img.replace("_s2.jpg", "_s1.jpg")
    j = pos - len(halves[first]) if second else pos  # token index in this half, from the line position
    if img not in cache: cache[img] = align(T / img, n)[0]
    bx = cache[img]; fx = fixes.get(sid, "")
    if fx and ":" in fx: x0, x1 = map(int, fx.split(":"))
    else:
        jj = j + (int(fx) if fx else 0); x0, x1 = bx[jj]
    im = Image.open(T / img).convert("L"); w, h = im.size
    a, b = max(0, x0 - 3), min(w, x1 + 3)
    tile = im.crop((a, 0, b, h)); tile = tile.resize((max(1, int(tile.width * 200 / h)), 200))
    tile.save(H / "tiles" / f"{int(sid):03d}.png")
    # eye-check overlay
    cx0 = max(0, bx[max(0, j - 3)][0] - 10); cx1 = min(w, bx[min(n - 1, j + 3)][1] + 10)
    cx0 = min(cx0, a); cx1 = max(cx1, b)
    ov = im.crop((cx0, 0, cx1, h)).convert("RGB"); d = ImageDraw.Draw(ov)
    d.rectangle([a - cx0, 1, b - cx0, h - 2], outline=(255, 0, 0), width=2)
    for X in range((cx0 // 25 + 1) * 25, cx1, 25):  # ruler in line-image pixels: long tick every 100, label every 100
        d.line([(X - cx0, h - (14 if X % 100 == 0 else 6)), (X - cx0, h)], fill=(0, 0, 255), width=1)
        if X % 100 == 0: d.text((X - cx0 + 2, h - 14), str(X), fill=(0, 0, 255))
    lab = Image.new("RGB", (ov.width, h + 22), "white"); lab.paste(ov, (0, 22))
    ctx = " ".join(("[" + t + "]") if k == j else t for k, t in enumerate(toks) if abs(k - j) <= 3)
    ImageDraw.Draw(lab).text((3, 3), f"#{sid} {st} {lp} : {ctx} {('fix ' + fx) if fx else ''}", fill=(0, 0, 0))
    lab.save(H / "check" / f"{int(sid):03d}.jpg", quality=88)
    rows.append(f"{sid}\t{st}\t{src}\t{lp}\t{img}\t{j}\t{n}\t{toks[j]}\t{x0}\t{x1}\t{fx}")
(H / "boxes.tsv").write_text("\n".join(rows) + "\n")
# contact sheets of the check overlays for the worker, 8 per sheet
ids = sorted(int(r.split("\t")[0]) for r in rows[1:])
for k in range(0, len(ids), 8):
    ims = [Image.open(H / "check" / f"{i:03d}.jpg") for i in ids[k:k + 8]]
    W = max(i.width for i in ims); S = Image.new("RGB", (W, sum(i.height + 6 for i in ims)), (120, 120, 120)); y = 0
    for i in ims: S.paste(i, (0, y)); y += i.height + 6
    S.save(H / "check" / f"sheet_{k // 8 + 1:02d}.jpg", quality=80)
print(len(rows) - 1, "tiles")
