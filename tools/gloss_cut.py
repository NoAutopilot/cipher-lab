#!/usr/bin/env python3
"""gloss_cut.py -- stroke-level (below the component) removal of interlinear gloss from line crops.

`tools/iiif_lines.py --mask-neighbours` whitens whole ink components whose share inside the band is low. A gloss letter
whose pen stroke touches a cipher sign is one component with that sign and survives (TXE2-RECUT, fr.3623 f.23r:
"q", "a", "fr", "i", "up" kept, benchmark-tx/txeng2/recut/RESULTS.md). This tool cuts below the component: it fits the
cipher row's core band per column window from the crop's own ink profile, draws an envelope (core top - UP, core
bottom + DOWN, median-smoothed across x), and replaces every ink pixel outside the envelope (with a HALO px rim) by the
local paper shade (iiif_lines.local_paper), i.e. a row-wise cut through a joined component plus inpainting of the
cut rows from the band's own background. Ink inside the envelope is never touched.

Scope (CLAUDE.md 8a): meant for crops of one cipher row with gloss rows above/below at a known offset (interlinear
decipherments). It must NOT be used on a crop whose cipher signs have ascenders/descenders reaching past UP/DOWN --
those tips are cut too; the --debug overlay draws the envelope so the cut is judged by eye before any read. It does
not read, score or label anything.

Usage:
  python3 tools/gloss_cut.py CROP.jpg [CROP2.jpg ...] --out DIR [--up 10 --down 10 --ink 150 --frac 0.3
      --win 160 --step 40 --halo 2 --stem-width 0] [--debug]
Writes DIR/<name> (same size as the input), DIR/<stem>_cut_debug.jpg with --debug (red-free: blue envelope lines,
removed ink tinted orange), and DIR/gloss_cut.tsv (crop, core_top_med, core_bot_med, removed_px, kept_px).
"""
import argparse, os, sys
import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from iiif_lines import local_paper, _dilate, label_components  # noqa: E402


def core_band(prof, frac):
    """Contiguous run of rows around the profile's maximum whose ink count is >= frac * max. (top, bottom) inclusive."""
    if prof.max() <= 0:
        return None
    k = np.ones(5) / 5
    p = np.convolve(prof, k, mode='same')
    c = int(np.argmax(p)); thr = frac * p[c]
    t = c
    while t > 0 and p[t - 1] >= thr:
        t -= 1
    b = c
    while b < len(p) - 1 and p[b + 1] >= thr:
        b += 1
    return t, b


def envelope(ink, frac=0.3, win=160, step=40, up=10, down=10):
    """Per-column (top, bottom) rows of the kept envelope, from windowed core bands, median-smoothed and interpolated."""
    h, w = ink.shape
    xs, ts, bs = [], [], []
    for x0 in range(0, max(1, w - win + 1), step):
        cb = core_band(ink[:, x0:x0 + win].sum(1).astype(float), frac)
        if cb:
            xs.append(x0 + win / 2); ts.append(cb[0]); bs.append(cb[1])
    if not xs:
        return np.zeros(w, int), np.full(w, h - 1), (0, h - 1)

    def med(a, r=2):
        a = np.array(a, float)
        return np.array([np.median(a[max(0, i - r):i + r + 1]) for i in range(len(a))])
    ts, bs = med(ts), med(bs)
    cols = np.arange(w)
    top = np.interp(cols, xs, ts) - up
    bot = np.interp(cols, xs, bs) + down
    return np.clip(np.round(top), 0, h - 1).astype(int), np.clip(np.round(bot), 0, h - 1).astype(int), \
        (float(np.median(ts)), float(np.median(bs)))


def cut(img, ink_thr=150, frac=0.3, win=160, step=40, up=10, down=10, halo=2, stem_width=0):
    rgb = img.convert('RGB')
    arr = np.asarray(rgb).copy()
    gray = np.asarray(rgb.convert('L'))
    ink = gray < ink_thr
    top, bot, med = envelope(ink, frac, win, step, up, down)
    rows = np.arange(ink.shape[0])[:, None]
    outside = (rows < top[None, :]) | (rows > bot[None, :])
    gone = ink & outside
    if stem_width:      # --stem-width: keep an outside piece that touches the envelope and is a thin stroke (an
        lab, n = label_components(gone)          # ascender/descender of a sign); remove wide pieces (letters) and
        for i in range(1, n + 1):                # pieces wholly outside, whatever their width
            ys, xs = np.nonzero(lab == i)
            touches = ((ys == top[xs] - 1) | (ys == bot[xs] + 1)).any()
            if touches and xs.max() - xs.min() + 1 <= stem_width:
                gone[lab == i] = False
        outside = outside & ~(ink & ~gone & outside)
    if halo:
        gone = _dilate(gone, halo) & outside
    paper = local_paper(arr.astype(float), _dilate(ink, halo) if halo else ink)
    arr[gone] = np.clip(paper[gone], 0, 255).astype(np.uint8)
    rem = ink & gone
    return Image.fromarray(arr), top, bot, med, int(rem.sum()), int((ink & ~rem).sum()), rem


def debug_image(img, top, bot, removed):
    a = np.asarray(img.convert('RGB')).copy()
    a[removed] = (230, 159, 0)          # Okabe-Ito orange: removed ink (# BGR colour not used; RGB here)
    im = Image.fromarray(a); d = ImageDraw.Draw(im)
    d.line(list(zip(range(len(top)), top.tolist())), fill=(0, 114, 178), width=1)   # Okabe-Ito blue envelope
    d.line(list(zip(range(len(bot)), bot.tolist())), fill=(0, 114, 178), width=1)
    return im


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('crops', nargs='+'); ap.add_argument('--out', required=True)
    ap.add_argument('--ink', type=int, default=150); ap.add_argument('--frac', type=float, default=0.3)
    ap.add_argument('--win', type=int, default=160); ap.add_argument('--step', type=int, default=40)
    ap.add_argument('--up', type=int, default=10); ap.add_argument('--down', type=int, default=10)
    ap.add_argument('--halo', type=int, default=2); ap.add_argument('--stem-width', type=int, default=0); ap.add_argument('--debug', action='store_true')
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    rows = ['crop\tcore_top_med\tcore_bot_med\tup\tdown\tremoved_px\tkept_px']
    for p in a.crops:
        im = Image.open(p)
        res, top, bot, med, rem, kept, removed = cut(im, a.ink, a.frac, a.win, a.step, a.up, a.down, a.halo, a.stem_width)
        name = os.path.basename(p)
        res.save(os.path.join(a.out, name), quality=90)
        if a.debug:
            debug_image(im, top, bot, removed).save(os.path.join(a.out, os.path.splitext(name)[0] + '_cut_debug.jpg'),
                                                     quality=85)
        rows.append(f'{name}\t{med[0]:.0f}\t{med[1]:.0f}\t{a.up}\t{a.down}\t{rem}\t{kept}')
    with open(os.path.join(a.out, 'gloss_cut.tsv'), 'w') as f:
        f.write('\n'.join(rows) + '\n')
    print('\n'.join(rows))


if __name__ == '__main__':
    main()
