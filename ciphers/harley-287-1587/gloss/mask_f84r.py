"""RUN1-HAR (4 Oct 2026): blank the gloss out of the f.84r cipher-line crops cut by tools/iiif_lines.py (images/f84r_masked/).
For each crop: find the cipher line within +-WIN px of the given centre as the row band (25 px) with the most dark pixels (< DARK grey:
the cipher strokes are heavier than the gloss hand; the right-half crops slope off the left half's centre), keep rows
[peak-TOP, peak+BOT] and paint every other row white, so no gloss letter above or below survives as readable text.
    python3 gloss/mask_f84r.py [--top 78] [--bot 36]
Rewrites the crops in place and adds "masked_rows" to each manifest entry. Idempotent (masked rows stay white)."""
import argparse, json, os
import numpy as np
from PIL import Image
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images', 'f84r_masked')
ap = argparse.ArgumentParser(); ap.add_argument('--top', type=int, default=78); ap.add_argument('--bot', type=int, default=36)
ap.add_argument('--win', type=int, default=35); ap.add_argument('--dark', type=int, default=110)
a = ap.parse_args()
m = json.load(open(os.path.join(D, 'manifest.json')))
ents = [x for v in m.values() for x in (v if isinstance(v, list) else [v]) if isinstance(x, dict) and 'box' in x]
BLANK = {'f84rM_L10_s2.jpg'}
REGION_Y, CENTRES = 500, [369, 647, 921, 1218, 1460, 1775, 1994, 2290, 2570, 2887, 3202, 3490, 3936, 4164, 4410]
for e in ents:
    p = os.path.join(D, e['crop']); im = np.array(Image.open(p).convert('L')).astype(float)
    c = REGION_Y + CENTRES[e['band'] - 1] - e['box'][1]
    if 'slope_fit' in e:  # --follow-slope sheared strip: the fitted line runs along the strip's centre row
        c = im.shape[0] // 2
    ink = (im < a.dark).sum(1); lo, hi = max(0, c - a.win), min(len(ink), c + a.win + 1)
    peak = lo + int(np.argmax(np.convolve(ink[lo:hi], np.ones(25) / 25, 'same')))
    keep = (max(0, peak - a.top), min(im.shape[0], peak + a.bot))
    im[:keep[0]] = 255; im[keep[1]:] = 255
    if e['crop'] in BLANK:  # no cipher in the crop, only the next line's gloss (blanked after the passes, see NOTES.md)
        im[:] = 255
    Image.fromarray(im.astype('uint8')).save(p, quality=92)
    e['masked_rows'] = {'keep': list(keep), 'peak': peak, 'rule': f'peak-{a.top}..peak+{a.bot}, rest white (gloss/mask_f84r.py)'}
json.dump(m, open(os.path.join(D, 'manifest.json'), 'w'), indent=1)
print(len(ents), 'crops masked')
