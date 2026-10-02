#!/usr/bin/env python3
"""Cut the no.37 f.60r lower cipher block (L25-L30 plus the unlisted row 'L28b', y about 1563) as straightened,
ink-tracked bands (GAPS-fr4715-vieuville-pool-5, 2 Oct 2026). Same tracking and straightening as
cut_f60r_bands.py --track (GAPS-4), with the missing centre inserted under its own label so the existing L29-L31
labels used by the other decode jobs are not renumbered. 600 px segments, 60 px overlap, 3x LANCZOS, (30, 28) band.

    python3 ciphers/fr4715-vieuville-pool/scripts/cut_f60r_lower.py [--overlay]
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from PIL import Image, ImageDraw
import cut_f60r_bands as cb

ROWS = [('L25', 1369), ('L26', 1429), ('L27', 1475), ('L28', 1521), ('L28b', 1563), ('L29', 1593), ('L30', 1647)]
OUT = 'ciphers/fr4715-vieuville-pool/images/f60r_lower3t'
SEG, OVERLAP, SCALE, AB = 600, 60, 3, (30, 28)


def tracks(im, strip=270, win=14, gap=30):
    g = np.array(im.convert('L')).astype(float); ink = (g < 110).astype(float); W = ink.shape[1]
    xs = list(range(0, W, strip)); k = np.ones(15) / 15
    profs = [np.convolve(ink[:, x:x + strip].sum(1), k, 'same') for x in xs]
    out, below = {}, None
    for lab, c0 in reversed(ROWS):
        c, pts = c0, []
        for j, x in enumerate(xs):
            lo, hi = c - win, c + win
            if below is not None:
                hi = min(hi, int(below[min(W - 1, x + strip // 2)]) - gap)
            y = lo + int(np.argmax(profs[j][lo:hi])) if hi > lo else hi
            pts.append(y); c = y
        out[lab] = [int(round(v)) for v in np.interp(range(W), [x + strip // 2 for x in xs], pts)]
        below = out[lab]
    return out


def main():
    im = Image.open(cb.SRC); W = im.size[0]
    tr = tracks(im); os.makedirs(OUT, exist_ok=True); entries = {}
    for lab, _ in ROWS:
        x0, s = 0, 1
        while x0 < W:
            x1 = min(W, x0 + SEG)
            crop = cb.straight(im, tr[lab], x0, x1, AB).resize(((x1 - x0) * SCALE, sum(AB) * SCALE), Image.LANCZOS)
            name = f'f60r_{lab}_s{s}.jpg'; crop.save(os.path.join(OUT, name), quality=90)
            entries[name] = {'x0': x0, 'x1': x1, 'track_px': tr[lab][x0:x1:100], 'scale': SCALE, 'line': lab, 'segment': f's{s}'}
            if x1 >= W: break
            x0 = x1 - OVERLAP; s += 1
    if '--overlay' in sys.argv:
        ov = im.crop((0, 1300, W, 1700)).convert('RGB'); d = ImageDraw.Draw(ov)
        for lab, _ in ROWS:
            d.line([(x, tr[lab][x] - 1300) for x in range(0, W, 10)], fill=(255, 0, 0), width=2)
            d.text((5, tr[lab][0] - 1310), lab, fill=(0, 0, 255))
        ov.resize((W // 2, 200)).save(os.path.join(OUT, 'overlay.jpg'), quality=85)
    mp = 'ciphers/fr4715-vieuville-pool/images/manifest.json'; m = json.load(open(mp))
    m['f60r_lower3t'] = {'source': cb.SRC, 'canvas': 135, 'date': '2 Oct 2026', 'script': 'scripts/cut_f60r_lower.py',
                         'note': 'lower block L25-L30 + unlisted row L28b (y~1563), ink-tracked straightened bands, 3x; regenerable, crops not committed',
                         'seg': SEG, 'scale': SCALE, 'out': OUT, 'crops': entries}
    json.dump(m, open(mp, 'w'), indent=1, ensure_ascii=False)
    print(f'{len(entries)} crops -> {OUT}')


if __name__ == '__main__':
    main()
