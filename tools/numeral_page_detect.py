#!/usr/bin/env python3
"""Score manuscript page images for numeral/symbol-run density (cipher-page triage), no model reading.

Built for RUN4-RAA (4 Oct 2026, na-raad-azie-1800): sweep 167 Nationaal Archief thumbnails for a cipher
leaf and hand only the top ~10 to an eye. Reusable for any thumbnail sweep of a digitised bundle.

Detector (stated, so a control can test it): each image is split into page units (a spread wider than
1.2 x its height is cut in two), each unit resampled to --width px wide (default 600), background-
normalised (divide by a 31 px box blur) and thresholded at 0.80. Text lines come from the row ink profile.
In each line the connected ink components are measured. Digit and symbol-cipher writing is many small,
separate, upright glyphs of near-equal height spaced along the line; Dutch/French cursive prose is joined
words -- fewer, wider components with tall ascender/descender loops. Per line:
  sep  = components per line-height of ink width (glyph separation),
  narrow = share of components with width/height in 0.25-1.1 and height 0.35-1.2 x the line's median
           height (digit-shaped),
  line score = sep * narrow.
The unit score is the mean of its top-5 line scores (so a cipher block inside a prose page still counts);
the image score is its best unit. Higher = more digit/symbol-like.

Meant to catch: a full or half page of digit groups or symbol rows (a Janssens-style digit grid, the
Smissaert 209 paired digit rows). Must NOT be relied on for: a single coded line or a code number quoted
in prose (one line cannot move a top-5 mean), and tables/accounts in figures, which it will rank high too
(that is why the top candidates go to an eye, never straight to a verdict).

Usage: numeral_page_detect.py IMG [IMG ...] [--width 600] [--tsv out.tsv]
Offline test: tools/tests/test_numeral_page_detect.py (synthetic digit page vs synthetic cursive page).
"""
import argparse
import sys

import numpy as np
from PIL import Image
from scipy import ndimage


def units(img):
    w, h = img.size
    if w > 1.2 * h:
        return [img.crop((0, 0, w // 2, h)), img.crop((w // 2, 0, w, h))]
    return [img]


def binarize(unit, width):
    g = unit.convert("L")
    g = g.resize((width, max(1, round(g.size[1] * width / g.size[0]))), Image.LANCZOS)
    a = np.asarray(g, dtype=float)
    bg = ndimage.uniform_filter(a, 31) + 1.0
    ink = (a / bg) < 0.80
    # trim 4% margins (page edges, binding shadow)
    h, w = ink.shape
    my, mx = int(0.04 * h), int(0.04 * w)
    ink[:my] = ink[h - my:] = False
    ink[:, :mx] = ink[:, w - mx:] = False
    return ink


def lines(ink):
    prof = ink.sum(1).astype(float)
    if prof.max() == 0:
        return []
    on = prof > max(2.0, 0.15 * np.percentile(prof[prof > 0], 90))
    out, start = [], None
    for y, v in enumerate(on):
        if v and start is None:
            start = y
        elif not v and start is not None:
            if y - start >= 4:
                out.append((start, y))
            start = None
    if start is not None and len(on) - start >= 4:
        out.append((start, len(on)))
    return out


def line_score(band):
    lab, n = ndimage.label(band)
    if n < 4:
        return None
    objs = ndimage.find_objects(lab)
    hs = np.array([s[0].stop - s[0].start for s in objs], float)
    ws = np.array([s[1].stop - s[1].start for s in objs], float)
    keep = (hs * ws) >= 6  # drop specks
    hs, ws = hs[keep], ws[keep]
    if len(hs) < 4:
        return None
    mh = np.median(hs)
    cols = np.where(band.any(0))[0]
    span = (cols[-1] - cols[0] + 1) if len(cols) else 1
    sep = len(hs) / (span / max(mh, 1.0))
    asp = ws / hs
    narrow = np.mean((asp >= 0.25) & (asp <= 1.1) & (hs >= 0.35 * mh) & (hs <= 1.2 * mh))
    return float(sep * narrow)


def score_image(path, width=600):
    img = Image.open(path)
    best = 0.0
    for u in units(img):
        ink = binarize(u, width)
        ls = [s for (a, b) in lines(ink) if (s := line_score(ink[a:b])) is not None]
        if ls:
            best = max(best, float(np.mean(sorted(ls)[-5:])))
    return best


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("images", nargs="+")
    p.add_argument("--width", type=int, default=600)
    p.add_argument("--tsv")
    a = p.parse_args(argv)
    rows = [(f, score_image(f, a.width)) for f in a.images]
    out = open(a.tsv, "w") if a.tsv else sys.stdout
    out.write("image\tscore\n")
    for f, s in rows:
        out.write(f"{f}\t{s:.4f}\n")


if __name__ == "__main__":
    main()
