#!/usr/bin/env python3
"""F36-GLOSS (3 Oct 2026): cut the clerk's interlinear gloss band of fr.3252 f.36-37 into crops for an eye read.

Centres are the row-ink-profile centres of tools/iiif_lines.py (run on the committed native regions in
../../../ceppo-nevers-fr3251-1570s/harvest/witness_f36/, command in NOTES.md), not HARVEST-D's eye grid, whose f.36r
centres drift between rows from about L08. Band = centre-105 .. centre+20 native px (gloss letters plus the tops of the
cipher signs as anchors), segments of 700 native px with 60 px overlap, upscaled 3x. Crops are regenerated, not committed.
  python3 cut_gloss.py   -> crops/<line>_s<k>.png and crops/crops_manifest.json
"""
import json
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
SRC = HERE / '../../../ceppo-nevers-fr3251-1570s/harvest/witness_f36'
# (source, prefix, [(centre, x_start)], x0, x1) -- f.36r renumbered r36n (14 lines; HARVEST-D's grid had 15)
BLOCKS = [
    ('c37_f36r_cipher.jpg', 'r36n', [(158, 1920), (252, 40), (353, 40), (438, 40), (780, 2130), (861, 40), (966, 40),
                                     (1068, 40), (1164, 40), (1271, 40), (1390, 40), (1490, 40), (1571, 40), (1682, 40)], 40, 3080),
    ('c38_f36v_top.jpg', 'v36top', [(c, 1000) for c in (227, 342, 447, 559, 675, 773)], 1000, 3900),
    ('c38_f36v_mid.jpg', 'v36mid', [(151, 2950), (244, 1000), (359, 1000), (481, 1000), (558, 2680), (671, 1000)], 1000, 3900),
    ('c38_f37r_cipher.jpg', 'r37', [(197, 280), (300, 280)], 280, 3179),
]


def main(seg=700, ov=60, up=105, dn=20, scale=3):
    out = []
    (HERE / 'crops').mkdir(exist_ok=True)
    for src, pref, lines, x0, x1 in BLOCKS:
        im = Image.open(SRC / src).convert('L'); W, H = im.size
        for i, (c, xs) in enumerate(lines, 1):
            xs = max(xs, x0); y0 = max(0, c - up); y1 = min(H, c + dn)
            band = ImageOps.autocontrast(im.crop((xs, y0, min(W, x1), y1)), cutoff=1)
            w = band.size[0]; a = 0; k = 1
            while a < w:
                b = min(w, a + seg)
                p = band.crop((a, 0, b, band.size[1])).resize(((b - a) * scale, band.size[1] * scale), Image.LANCZOS)
                name = f'crops/{pref}_L{i:02d}_s{k}.png'; p.save(HERE / name)
                out.append({'crop': name, 'src': src, 'box': [xs + a, y0, xs + b, y1], 'scale': scale})
                if b == w:
                    break
                a = b - ov; k += 1
    json.dump(out, open(HERE / 'crops/crops_manifest.json', 'w'), indent=0)
    print(len(out), 'crops')


if __name__ == '__main__':
    main()
