#!/usr/bin/env python3
"""Cut native-resolution line-pair crops of BnF Dupuy 452, folio 28 (Raince to Madame) and
folio 24 (Raince to Robertet), from the full-resolution Gallica IIIF fetches in images/img/.

Source canvases (ark:/12148/btv1b10036146c), all fetched at IIIF /full/full/0/native.jpg,
8299-8315 x 6214 px:
  f29 -> folio 24 recto   (Raince to Robertet: ~7 plain lines, then cipher)
  f30 -> folio 24 verso   (left page of the opening; cipher tail, then plain close+signature;
                            the right page of this canvas, folio 25 recto, is blank -- not cropped)
  f31 -> folio 25 verso + facing blank (address wrapper only, no text -- not cropped; full-res
                            kept only as a reduced reference image, see manifest note)
  f34 -> folio 28 recto   (Raince to Madame: plain intro, then cipher tail)
  f35 -> folio 28 verso (left column, entirely cipher) + folio 29 recto (right column, entirely
                            cipher), one photographed opening
  f36 -> folio 29 verso (left column: ~6 cipher lines then plain close+signature) + folio 30
                            recto (right column, plain only -- not cropped)

Method: for each page-column, take a per-column ink density row profile (pixels darker than
INK_THRESH, summed across the column's x-range) and find line centres as local maxima at least
MIN_LINE_GAP px apart with prominence PEAK_PROMINENCE (checked by eye against the source images
on 23 Sept 2026: this rejects paper-texture/watermark noise while keeping genuine lines, and a
gap well above the page's own median pitch is a real paragraph break, not a missed line -- left
as a wider band rather than papered over with an interpolated centre). Band boundaries are the
midpoints between consecutive centres (i.e. the low-ink whitespace between lines), so a crop's
edge falls in whitespace, not through ink. Every detected line is cropped, not only the ones
read as cipher on this pass -- this worker does not transcribe or judge plain vs cipher (per its
brief), and the surrounding plain text gives a transcriber the sentence context anyway.

Two adjacent lines are grouped into one crop ("one or two lines of writing" per the brief) to
roughly halve the file count. Each page-column is far wider than the 2400 px cap, so every band
is still cut into two overlapping horizontal segments (_s1 = left/first, _s2 = right/second),
exactly as ciphers/dupuy468-anhalt/images/crop.py does for the same reason.

Tone: crops are saved as plain crops of the (already JPEG-compressed) source -- no separate
contrast stretch is applied here, unlike the Anhalt gloss crop.py, since this pass is not
targeting a faint interlinear gloss.

Run from anywhere: python3 ciphers/dupuy452-carpi-1520/images/crop.py
"""
import json
import os

import numpy as np
from PIL import Image
from scipy.signal import find_peaks

Image.MAX_IMAGE_PIXELS = None

HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(HERE, "img")
OUT = os.path.join(HERE, "crops")
QUALITY = 60
INK_THRESH = 170
MIN_LINE_GAP = 85
PEAK_PROMINENCE = 40
SEG_WIDTH = 2200

# (output prefix, source file, column x-range) -- one entry per page-side actually carrying text.
PAGES = [
    ("f24r", "btv1b10036146c_f29_folio24r_full.jpg", (4550, 8250)),
    ("f24v", "btv1b10036146c_f30_folio24v25r_full.jpg", (150, 4150)),
    ("f28r", "btv1b10036146c_f34_folio28r_full.jpg", (4550, 8250)),
    ("f28v", "btv1b10036146c_f35_folio28v29r_full.jpg", (150, 4300)),
    ("f29r", "btv1b10036146c_f35_folio28v29r_full.jpg", (4500, 8280)),
    ("f29v", "btv1b10036146c_f36_folio29v30r_full.jpg", (150, 4150)),
]


def find_line_centres(ink, min_gap=MIN_LINE_GAP, prominence=PEAK_PROMINENCE):
    """Line centres = local maxima of the row ink-density profile, at least min_gap px
    apart. Parameters calibrated by hand on this volume's hand/pitch (23 Sept 2026, corrected
    after a first pass at distance=110 silently merged adjacent lines in the tightest-spaced
    cipher passages -- verified against the pixel ink profile itself, not by eye): distance 85
    (just under the tightest real inter-line pitch measured, ~95-100 px, in the dense cipher
    blocks), prominence 40 (rejects paper-texture/watermark noise while keeping genuine,
    lighter-ink lines; valleys between real lines reach near-zero ink count, so 85 does not
    split a single line into two)."""
    peaks, _ = find_peaks(ink, distance=min_gap, prominence=prominence)
    return [int(p) for p in peaks]


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = []
    per_page_counts = {}
    for prefix, fname, (x0, x1) in PAGES:
        path = os.path.join(IMG, fname)
        im = Image.open(path).convert("RGB")
        gray = np.array(im.convert("L"))
        col = gray[:, x0:x1]
        ink = (col < INK_THRESH).sum(axis=1)
        peaks = find_line_centres(ink)
        # Gaps well above the page's own median pitch are real paragraph breaks (blank space,
        # nothing to crop), not missed lines -- checked by eye against the source images on
        # 23 Sept 2026, so no interpolation is applied; a band spanning such a gap is simply
        # wider (its two lines have visible white space between them in the crop).
        if not peaks:
            print(f"{prefix}: no lines detected, skipping")
            continue
        # band boundaries: midpoints between consecutive centres; pad first/last by half the
        # median pitch so the first and last lines get a symmetric margin too.
        diffs = np.diff(peaks)
        pitch = int(np.median(diffs)) if len(diffs) else 150
        bounds = [peaks[0] - pitch // 2]
        for a, b in zip(peaks, peaks[1:]):
            bounds.append((a + b) // 2)
        bounds.append(peaks[-1] + pitch // 2)
        bounds = [max(0, b) for b in bounds]
        bounds = [min(im.height, b) for b in bounds]

        n_lines = len(peaks)
        n_bands = 0
        li = 0
        band_idx = 0
        while li < n_lines:
            top = bounds[li]
            two = li + 1 < n_lines
            bottom = bounds[li + 2] if two else bounds[li + 1]
            band_idx += 1
            n_bands += 1
            seg_ranges = [
                (x0, min(x1, x0 + SEG_WIDTH)),
                (max(x0, x1 - SEG_WIDTH), x1),
            ]
            for si, (sx0, sx1) in enumerate(seg_ranges, 1):
                box = (sx0, top, sx1, bottom)
                name = f"{prefix}_L{band_idx:02d}_s{si}.jpg"
                im.crop(box).save(os.path.join(OUT, name), quality=QUALITY)
                manifest.append({
                    "crop": name,
                    "source": f"img/{fname}",
                    "box": [int(v) for v in box],
                    "lines_in_band": 2 if two else 1,
                })
            li += 2 if two else 1
        per_page_counts[prefix] = {"lines_detected": n_lines, "bands": n_bands}
        print(prefix, "lines:", n_lines, "bands:", n_bands)

    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump({
            "written_by": "images/crop.py",
            "date": "23 September 2026",
            "method": "row ink-density profile, local-maxima line centres, midpoint band "
                       "boundaries, 2 lines per band, 2 overlapping x-segments per band "
                       "(page columns exceed the 2400px cap)",
            "quality": QUALITY,
            "per_page": per_page_counts,
            "crops": manifest,
        }, f, indent=1)
    print(len(manifest), "crops total")


if __name__ == "__main__":
    main()
