#!/usr/bin/env python3
"""Cut 1x line crops (native resolution, <=1700 px segments, 150 px overlap) of the cipher lines of fr.3251 ff.21v,
35, 87 from the committed native regions (HARVEST-D, 28 Sept 2026). Line centres set by eye on each region's grid.
  python3 cut_folio_lines.py      # writes <folio>/lines/<folio>_Lnn_sk.png and <folio>/lines/crops_manifest.json
Lines on f.21v mix prose and cipher: a reader transcribes only the cipher signs.
"""
import json
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
FOLIOS = {
    'f21v': ('c23_cipher_w.jpg', [120, 200, 280, 376, 456, 536, 610, 690, 760, 836, 910]),
    'f35': ('c36_cipher_w.jpg', [206, 300]),
    'f87': ('c88_cipher_w.jpg', [185, 290, 395, 500, 600, 700]),
}

for folio, (src, centres) in FOLIOS.items():
    im = Image.open(HERE / folio / src).convert('L'); W, H = im.size
    (HERE / folio / 'lines').mkdir(exist_ok=True); out = []
    for i, c in enumerate(centres, 1):
        y0, y1 = max(0, c - 60), min(H, c + 60)
        band = ImageOps.autocontrast(im.crop((0, y0, W, y1)), cutoff=1); a = 0; k = 1
        while a < W:
            b = min(W, a + 1700); name = f'lines/{folio}_L{i:02d}_s{k}.png'
            band.crop((a, 0, b, y1 - y0)).save(HERE / folio / name)
            out.append({'crop': name, 'src': src, 'box': [a, y0, b, y1]})
            if b == W:
                break
            a = b - 150; k += 1
    json.dump(out, open(HERE / folio / 'lines' / 'crops_manifest.json', 'w'), indent=0)
    print(folio, len(out))
