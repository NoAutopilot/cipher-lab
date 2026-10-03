#!/usr/bin/env python3
"""F36R-REREAD (3 Oct 2026): cut sign-row crops of fr.3252 f.36r cipher rows r36n_L09-L14 for two blind sign passes.

Row bands are the row-ink-profile bands of tools/iiif_lines.py, run on the committed native region:
  python3 tools/iiif_lines.py --image ciphers/ceppo-nevers-fr3251-1570s/harvest/witness_f36/c37_f36r_cipher.jpg \
      --out <scratch> --prefix r36 --debug
  -> centres 44 158 252 353 438 558 678 780 861 966 1068 1164 1271 1390 1490 1571 1682 (bands 12-17 = r36n_L09-L14;
     44, 558, 678 are prose rows, so profile band k >= 9 is r36n_L(k-3)).
Each crop: band +-12 px, x 40..3080 in four non-overlapping 760 px segments, autocontrast, upscaled 2x. Crops are
regenerated, not committed (.gitignore).   python3 cut_f36r.py -> crops/r36n_L??_s?.png, crops/crops_manifest.json
"""
import json
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
SRC = HERE / '../../../ceppo-nevers-fr3251-1570s/harvest/witness_f36/c37_f36r_cipher.jpg'
BANDS = {9: (1116, 1217), 10: (1217, 1330), 11: (1330, 1440), 12: (1440, 1530), 13: (1530, 1626), 14: (1626, 1733)}
X0, X1, SEG, PAD, SCALE = 40, 3080, 760, 12, 2


def main():
    im = Image.open(SRC).convert('L'); W, H = im.size
    (HERE / 'crops').mkdir(exist_ok=True); out = []
    for ln, (y0, y1) in BANDS.items():
        y0, y1 = max(0, y0 - PAD), min(H, y1 + PAD)
        for k, a in enumerate(range(X0, X1, SEG), 1):
            b = min(X1, a + SEG)
            p = ImageOps.autocontrast(im.crop((a, y0, b, y1)), cutoff=1)
            p = p.resize((p.size[0] * SCALE, p.size[1] * SCALE), Image.LANCZOS)
            name = f'crops/r36n_L{ln:02d}_s{k}.png'; p.save(HERE / name)
            out.append({'crop': name, 'src': SRC.name, 'box': [a, y0, b, y1], 'scale': SCALE})
    json.dump(out, open(HERE / 'crops/crops_manifest.json', 'w'), indent=0)
    print(len(out), 'crops')


if __name__ == '__main__':
    main()
