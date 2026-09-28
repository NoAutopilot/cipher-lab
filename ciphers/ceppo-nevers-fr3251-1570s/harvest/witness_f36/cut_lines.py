#!/usr/bin/env python3
"""Re-cut the fr.3252 f.36-37 witness line crops (HARVEST-D, 28 Sept 2026) from the committed native regions.

  python3 cut_lines.py            # writes lines/ (1x, 1700 px segments) and lines2x/ (850 px segments, upscaled 2x)
Each crop is one cipher line with the interlinear gloss above it (autocontrast, band = centre-120..centre+65 native px
for 2x; centre-85..centre+80 for 1x). Line centres were set by eye on the regions' own 250 px grids. Only the five
2x crops cited in alignment_pairs.tsv are committed (as JPEG, cited/); the rest regenerate from this script.
"""
import json
from pathlib import Path
from PIL import Image, ImageOps

HERE = Path(__file__).resolve().parent
BLOCKS = [
    ('c38_f36v_top.jpg', 'v36top', [(c + 15, 1000) for c in [200, 305, 410, 510, 612, 712]], 1000, 3900),
    ('c38_f36v_mid.jpg', 'v36mid', [(c + 15, x) for c, x in [(150, 2950), (245, 1000), (345, 1000), (432, 1000), (552, 2680), (645, 1000)]], 1000, 3900),
    ('c37_f36r_cipher.jpg', 'r36', [(c + 15, x) for c, x in [(150, 1920), (240, 40), (340, 40), (430, 40), (780, 2130), (855, 40), (940, 40), (1030, 40), (1130, 40), (1228, 40), (1322, 40), (1420, 40), (1518, 40), (1615, 40), (1705, 40)]], 40, 3080),
    ('c38_f37r_cipher.jpg', 'r37', [(255, 280), (345, 280)], 280, 3179),
]


def cut(outdir, seg, ov, up, dn, scale):
    out = []
    (HERE / outdir).mkdir(exist_ok=True)
    for src, pref, lines, x0, x1 in BLOCKS:
        im = Image.open(HERE / src).convert('L'); W, H = im.size
        for i, (c, xs) in enumerate(lines, 1):
            xs = max(xs, x0); y0 = max(0, c - up); y1 = min(H, c + dn)
            band = ImageOps.autocontrast(im.crop((xs, y0, min(W, x1), y1)), cutoff=1)
            w = band.size[0]; k = 1; a = 0
            while a < w:
                b = min(w, a + seg); name = f'{outdir}/{pref}_L{i:02d}_s{k}.png'
                p = band.crop((a, 0, b, band.size[1]))
                if scale != 1:
                    p = p.resize((p.size[0] * scale, p.size[1] * scale), Image.LANCZOS)
                p.save(HERE / name)
                out.append({'crop': name, 'src': src, 'box': [xs + a, y0, xs + b, y1], 'scale': scale})
                if b == w:
                    break
                a = b - ov; k += 1
    json.dump(out, open(HERE / outdir / 'crops_manifest.json', 'w'), indent=0)
    return len(out)


if __name__ == '__main__':
    print(cut('lines', 1700, 150, 85, 80, 1), cut('lines2x', 850, 120, 120, 65, 2))
