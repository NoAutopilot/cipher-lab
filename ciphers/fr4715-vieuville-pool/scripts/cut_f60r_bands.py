#!/usr/bin/env python3
"""Cut f.60r (no.37, Gallica canvas 135) into per-line bands that keep the interlinear gloss with its line.

tools/iiif_lines.py found the 32 line centres (pitch 47 px) but cuts bands at the midpoints between centres, which
splits the period gloss written in the interline above a word-code between two crops. This script (GAPS-fr4715-
vieuville-pool-2, 2 Oct 2026) reuses those centres and cuts each band from (midpoint above - EXTRA) to (midpoint
below + 2), so the gloss above line N stays in band N; 3 segments of SEG px with OVERLAP, upscaled 2x LANCZOS,
a corner tick at each segment boundary (iiif_lines.py step 4), and an overlay with line numbers. Same shape as
fr4715-montholon-1589/images/regen_f81r_crops.sh (private cut precedent in this pool, documented there).

    python3 ciphers/fr4715-vieuville-pool/scripts/cut_f60r_bands.py [--lines 1,2,3] [--overlay]
"""
import argparse, json, os, sys
from PIL import Image, ImageDraw

SRC = 'ciphers/fr4715-vieuville-pool/images/src_ark_12148_btv1b52509819x_f135_560_1600_3250_1850.jpg'
OUT = 'ciphers/fr4715-vieuville-pool/images/f60r_bands'
CENTRES = [201,265,310,353,396,446,485,529,570,613,660,705,752,801,843,889,937,982,1033,1087,1139,1189,1247,
           1311,1369,1429,1475,1521,1593,1647,1705]   # iiif_lines.py --dry-run, 2 Oct 2026 14:24 UTC, region y px; its first centre (146) is the
           # gloss row above line 1 (five interlinear words), not a text line -- dropped, and line 1's band starts 75 px above its centre
EXTRA = 16
SEG, OVERLAP, SCALE = 1150, 60, 2   # first cut (f60r_bands/, 2 Oct 2026 14:28 UTC): a Sonnet pass declined it as unreadable;
# --seg 600 --scale 3 --out .../f60r_bands3 is the re-cut (the f.81r lesson: narrow segments, 3x), 1800 px wide crops

def bands():
    out = []
    for i, c in enumerate(CENTRES):
        top = (CENTRES[i-1] + c) // 2 - EXTRA if i else max(0, c - 75)
        bot = (c + CENTRES[i+1]) // 2 + 2 if i + 1 < len(CENTRES) else min(1850, c + 40)
        out.append((top, bot))
    return out

def main():
    global OUT, SEG, SCALE
    ap = argparse.ArgumentParser()
    ap.add_argument('--lines', default='')
    ap.add_argument('--overlay', action='store_true')
    ap.add_argument('--seg', type=int, default=SEG)
    ap.add_argument('--scale', type=int, default=SCALE)
    ap.add_argument('--out', default=OUT)
    ap.add_argument('--key', default='f60r_bands')
    a = ap.parse_args()
    OUT, SEG, SCALE = a.out, a.seg, a.scale
    im = Image.open(SRC); W, H = im.size
    want = set(int(x) for x in a.lines.split(',') if x) or set(range(1, len(CENTRES) + 1))
    os.makedirs(OUT, exist_ok=True)
    entries = {}
    for n, (top, bot) in enumerate(bands(), 1):
        if n not in want: continue
        x0, s = 0, 1
        while x0 < W:
            x1 = min(W, x0 + SEG)
            crop = im.crop((x0, top, x1, bot)).resize(((x1 - x0) * SCALE, (bot - top) * SCALE), Image.LANCZOS)
            d = ImageDraw.Draw(crop)
            if x0 > 0: d.line([(0, 0), (0, 14)], fill=(255, 0, 0), width=3)
            if x1 < W: d.line([(crop.width - 1, 0), (crop.width - 1, 14)], fill=(255, 0, 0), width=3)
            name = f'f60r_L{n:02d}_s{s}.jpg'
            crop.save(os.path.join(OUT, name), quality=90)
            entries[name] = {'box_region': [x0, top, x1 - x0, bot - top], 'box_native': [560 + x0, 1600 + top, x1 - x0, bot - top],
                             'scale': SCALE, 'line': f'L{n:02d}', 'segment': f's{s}'}
            if x1 >= W: break
            x0 = x1 - OVERLAP; s += 1
    if a.overlay:
        ov = im.copy(); d = ImageDraw.Draw(ov)
        for n, (top, bot) in enumerate(bands(), 1):
            d.line([(0, top), (W, top)], fill=(0, 0, 255), width=2)
            d.text((5, CENTRES[n-1] - 8), f'L{n:02d}', fill=(255, 0, 0))
        ov.resize((1625, 925)).save(os.path.join(OUT, 'f60r_bands_overlay.jpg'), quality=85)
    mp = 'ciphers/fr4715-vieuville-pool/images/manifest.json'
    m = json.load(open(mp))
    m.setdefault(a.key, {'source': SRC, 'canvas': 135, 'date': '2 Oct 2026', 'script': 'scripts/cut_f60r_bands.py',
                                 'note': 'per-line bands keeping the interlinear gloss above each line; 2x LANCZOS; regenerable, crops not committed'})
    m[a.key].update({'seg': SEG, 'scale': SCALE, 'out': OUT})
    m[a.key]['crops'] = entries
    json.dump(m, open(mp, 'w'), indent=1, ensure_ascii=False)
    print(f'{len(entries)} crops -> {OUT}')

if __name__ == '__main__':
    main()
