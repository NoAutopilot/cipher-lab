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

def track_lines(im, lines, shift, strip=270, win=14, gap=30):
    import numpy as np
    g = np.array(im.convert('L')).astype(float)
    ink = (g < 110).astype(float)
    W = ink.shape[1]
    xs = list(range(0, W, strip))
    k = np.ones(15) / 15
    profs = [np.convolve(ink[:, x:x + strip].sum(1), k, 'same') for x in xs]
    out = {}
    for n in sorted(lines, reverse=True):          # bottom line first, so each line can be held above the next
        c, pts = CENTRES[n - 1] + shift, []
        below = out.get(n + 1)
        for j, x in enumerate(xs):
            lo, hi = c - win, c + win
            if below is not None:
                hi = min(hi, int(below[min(W - 1, x + strip // 2)]) - gap)
            y = lo + int(np.argmax(profs[j][lo:hi])) if hi > lo else hi
            pts.append(y); c = y
        mids = [x + strip // 2 for x in xs]
        out[n] = [int(round(v)) for v in np.interp(range(W), mids, pts)]
    return out


def straight(im, track, x0, x1, ab):
    above, below = ab
    out = Image.new('RGB', (x1 - x0, above + below), 'white')
    for x in range(x0, x1):
        c = track[x]
        out.paste(im.crop((x, c - above, x + 1, c + below)), (x - x0, 0))
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
    ap.add_argument('--centred', type=int, nargs=2, metavar=('ABOVE', 'BELOW'), default=None,
                    help='GAPS-4 (2 Oct 2026): cut each segment centred on the line itself (centre-ABOVE .. centre+BELOW) '
                         'instead of the gloss-keeping midpoint band, for the dense digit blocks')
    ap.add_argument('--slope', type=float, default=0.0,
                    help='px the line centre moves per full region width, left to right (dense blocks: about -20)')
    ap.add_argument('--shift', type=int, default=0, help='px added to every centre (dense blocks: about +6)')
    ap.add_argument('--track', action='store_true',
                    help='GAPS-4 (2 Oct 2026): follow each line by its ink row profile in 270 px strips (the lines curve up '
                         'to 60 px at the right edge) and cut a straightened band, centred-ABOVE..centre+BELOW per column; '
                         'a line is kept at least 30 px above the next line\'s track (L13 otherwise jumps onto L14)')
    ap.add_argument('--segments', default='', help='only these segment numbers, e.g. 4,5,6')
    a = ap.parse_args()
    OUT, SEG, SCALE = a.out, a.seg, a.scale
    im = Image.open(SRC); W, H = im.size
    want = set(int(x) for x in a.lines.split(',') if x) or set(range(1, len(CENTRES) + 1))
    segs_wanted = set(int(x) for x in a.segments.split(',') if x)
    tracks = track_lines(im, sorted(want), a.shift) if a.track else {}
    os.makedirs(OUT, exist_ok=True)
    entries = {}
    for n, (top, bot) in enumerate(bands(), 1):
        if n not in want: continue
        x0, s = 0, 1
        while x0 < W:
            x1 = min(W, x0 + SEG)
            if a.track:
                if not segs_wanted or s in segs_wanted:
                    crop = straight(im, tracks[n], x0, x1, a.centred or (30, 28)).resize(((x1 - x0) * SCALE, sum(a.centred or (30, 28)) * SCALE), Image.LANCZOS)
                    name = f'f60r_L{n:02d}_s{s}.jpg'
                    crop.save(os.path.join(OUT, name), quality=90)
                    entries[name] = {'box_region': [x0, 'tracked', x1 - x0, sum(a.centred or (30, 28))], 'track_px': tracks[n][x0:x1:100],
                                     'scale': SCALE, 'line': f'L{n:02d}', 'segment': f's{s}'}
                if x1 >= W: break
                x0 = x1 - OVERLAP; s += 1
                continue
            if a.centred:
                c = CENTRES[n-1] + a.shift + int(a.slope * ((x0 + x1) / 2) / W)
                top, bot = max(0, c - a.centred[0]), min(H, c + a.centred[1])
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
