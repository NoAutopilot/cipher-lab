#!/usr/bin/env python3
"""Segment the cipher signs of Raince to Madame (Dupuy 452 ff.28r-29v) from the line crops.

Rebuilds each page column at native resolution from images/crops/ (boxes in
images/crops/manifest.json) plus the two gutter strips in images/gutter/ (f28v and f29v run past
the crop columns' inner edge; fetched 23 Sept 2026, registered to the crops at offset 0,0), then:
binarise (fixed threshold), connected components, one text line per component by the column's
row-ink peaks, merge components into signs (x-overlap within a line: dots, flags and stems above
or below a body), and keep only the cipher block (CIPHER_SPAN below, set by eye on the
reconstructed columns).

Writes glyphs/signs.tsv (one row per segmented sign: sid, page, line, x-order, bbox in page
coordinates, component count) and glyphs/signs_bitmaps.npz (normalised 48x48 bitmaps) that
cluster.py reads. Deterministic; run from anywhere.
"""
import json
import os

import cv2
import numpy as np
from PIL import Image
from scipy.ndimage import uniform_filter1d
from scipy.signal import find_peaks

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
IMG = os.path.join(TARGET, "images")

THRESH = 150          # ink = darker than this (Otsu gives 138-155 on these columns)
BG_K = 41             # closing size: wider than any stroke, narrower than the shadow
REL_THRESH = 0.62     # ink = darker than 62% of the local paper (THRESH 150 of ~242 paper)
RULE_H = 121          # a vertical ink run this tall is a page edge, not a stroke
MIN_AREA = 25         # components smaller than this are specks
LINE_DIST = 80        # min px between line centres (true pitch ~105-115 in the cipher blocks)
NORM = 48
LINE_FIT_ITERS = 3
SPLIT_W = 72          # boxes at least this wide are tested for touching signs
SPLIT_MARGIN = 18
SPLIT_MAX_INK = 4

# Page column: (origin x, origin y, x-limits of the writing, gutter strips (file, x, y)).
PAGES = {
    "f28r": dict(xlim=(4600, 7800), gutter=[]),
    "f28v": dict(xlim=(600, 4395), gutter=[("f35_x4200_y400_w300_h4900.jpg", 4200, 400)]),
    "f29r": dict(xlim=(4700, 8000), gutter=[]),
    "f29v": dict(xlim=(600, 4262), gutter=[("f36_x4050_y500_w350_h1200.jpg", 4050, 500)]),
}

# Cipher block, per page: (first line index, x of first cipher sign on that line or None,
# last line index, x after the last cipher sign on that line or None). Line indices are the
# 0-based detected lines of this script (see lines.tsv). Set by eye on 23 Sept 2026.
CIPHER_SPAN_FILE = os.path.join(HERE, "cipher_span.json")


def build_column(page):
    man = json.load(open(os.path.join(IMG, "crops", "manifest.json")))["crops"]
    cs = [c for c in man if c["crop"].startswith(page)]
    x0 = min(c["box"][0] for c in cs)
    y0 = min(c["box"][1] for c in cs)
    x1 = max(c["box"][2] for c in cs)
    y1 = max(c["box"][3] for c in cs)
    for g, gx, gy in PAGES[page]["gutter"]:
        a = Image.open(os.path.join(IMG, "gutter", g))
        x1 = max(x1, gx + a.size[0])
    can = np.full((y1 - y0, x1 - x0), 255, np.uint8)
    for c in sorted(cs, key=lambda c: c["crop"]):
        a = np.array(Image.open(os.path.join(IMG, "crops", c["crop"])).convert("L"))
        b = c["box"]
        h, w = min(a.shape[0], b[3] - b[1]), min(a.shape[1], b[2] - b[0])
        can[b[1] - y0:b[1] - y0 + h, b[0] - x0:b[0] - x0 + w] = a[:h, :w]
    for g, gx, gy in PAGES[page]["gutter"]:
        a = np.array(Image.open(os.path.join(IMG, "gutter", g)).convert("L"))
        ys, xs = gy - y0, gx - x0
        ya, xa = max(0, -ys), 0
        h = min(a.shape[0] - ya, can.shape[0] - (ys + ya))
        # only fill what the crops did not cover (x beyond the crops' right edge)
        xc = max(c["box"][2] for c in cs) - gx
        can[ys + ya:ys + ya + h, xs + xc:xs + a.shape[1]] = a[ya:ya + h, xc:]
    return can, x0, y0


def detect_lines(ink):
    prof = uniform_filter1d(ink.sum(axis=1).astype(float), 25)
    peaks, _ = find_peaks(prof, distance=LINE_DIST, prominence=prof.max() * 0.08)
    return peaks


def segment(page):
    can, x0, y0 = build_column(page)
    xa, xb = (v - x0 for v in PAGES[page]["xlim"])
    # divide out the paper background (grey closing = the page with the writing removed), so the
    # gutter shadow does not fuse with the signs beside it
    bg = cv2.morphologyEx(can, cv2.MORPH_CLOSE, np.ones((BG_K, BG_K), np.uint8))
    bg = cv2.GaussianBlur(bg, (0, 0), BG_K / 3)
    norm = can.astype(float) / np.maximum(bg.astype(float), 1)
    ink = (norm < REL_THRESH).astype(np.uint8)
    ink[:, :max(0, xa)] = 0
    ink[:, xb:] = 0
    ink = cv2.morphologyEx(ink, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    # remove the page edge / gutter rule (a vertical run taller than any stroke) so a sign that
    # touches it is not discarded with it
    rule = cv2.morphologyEx(ink, cv2.MORPH_OPEN, np.ones((RULE_H, 1), np.uint8))
    rule = cv2.dilate(rule, np.ones((1, 3), np.uint8))
    ink[rule > 0] = 0
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink, connectivity=8)
    # drop specks, page edges, the gutter shadow and long thin rules (no cipher sign is taller
    # than ~130 px or wider than ~150 px here; a lone "I" is ~50 px tall)
    keep = [i for i in range(1, n) if st[i, 4] >= MIN_AREA and st[i, 3] <= 160 and st[i, 2] <= 200
            and not (st[i, 3] > 100 and st[i, 3] > 4 * st[i, 2])
            and not (st[i, 2] <= 10 and st[i, 3] > 2.5 * st[i, 2])]   # sliver left of a removed rule
    lines = detect_lines(ink)
    # assign each component to a line by its ink centroid. The lines slope across the column
    # (up to ~40 px over 3700 px), so a flat page-wide centre puts tall or low signs on the
    # neighbouring line; fit y = a + b*x per line on the components assigned to it and
    # re-assign to the nearest fitted line, LINE_FIT_ITERS times.
    cx_all = np.array([cen[i][0] for i in keep])
    cy_all = np.array([cen[i][1] for i in keep])
    big = np.array([st[i, 4] >= 150 for i in keep])
    fits = [(float(l), 0.0) for l in lines]
    for _ in range(LINE_FIT_ITERS):
        pred = np.stack([a + b * cx_all for a, b in fits], axis=1)
        li_all = np.argmin(np.abs(pred - cy_all[:, None]), axis=1)
        new = []
        for li, (a, b) in enumerate(fits):
            sel = (li_all == li) & big
            if sel.sum() < 8:
                new.append((a, b))
                continue
            bb, aa = np.polyfit(cx_all[sel], cy_all[sel], 1)
            res = np.abs(cy_all[sel] - (aa + bb * cx_all[sel]))
            ok = res < max(12.0, 2.5 * np.median(res))
            if ok.sum() >= 8:
                bb, aa = np.polyfit(cx_all[sel][ok], cy_all[sel][ok], 1)
            new.append((float(aa), float(bb)))
        fits = new
    comps = []
    for k, i in enumerate(keep):
        x, y, w, h, area = st[i]
        cy = cy_all[k]
        ly = np.array([a + b * cx_all[k] for a, b in fits])
        li = int(np.argmin(np.abs(ly - cy)))
        if abs(ly[li] - cy) > 90:         # margin marks, page edge below the last line
            continue
        if h <= 22 and w >= 1.5 * h and cy > ly[li] + 12:
            continue                      # a detached rho tail ("~" under the previous sign)
        comps.append(dict(id=i, x=x, y=y, w=w, h=h, area=area, line=li))
    signs = []
    for li in range(len(lines)):
        cl = sorted([c for c in comps if c["line"] == li], key=lambda c: c["x"])
        groups = []
        for c in cl:
            if groups:
                g = groups[-1]
                gx0, gx1 = g["x"], g["x"] + g["w"]
                ov = min(gx1, c["x"] + c["w"]) - max(gx0, c["x"])
                small = min(g["w"], c["w"])
                vgap = max(g["y"], c["y"]) - min(g["y"] + g["h"], c["y"] + c["h"])
                vov = -vgap                      # vertical overlap in px when positive
                a_s, a_l = sorted((g["area"], c["area"]))
                attach = a_s < 0.35 * a_l or vov < 0.3 * min(g["h"], c["h"])
                if ov > 0.5 * small and vgap < 25 and attach:
                    nx0 = min(gx0, c["x"]); nx1 = max(gx1, c["x"] + c["w"])
                    ny0 = min(g["y"], c["y"]); ny1 = max(g["y"] + g["h"], c["y"] + c["h"])
                    g.update(x=nx0, y=ny0, w=nx1 - nx0, h=ny1 - ny0, area=g["area"] + c["area"])
                    g["ids"].append(c["id"])
                    continue
            groups.append(dict(x=c["x"], y=c["y"], w=c["w"], h=c["h"], area=c["area"], ids=[c["id"]]))
        for g in groups:
            sub = lab[g["y"]:g["y"] + g["h"], g["x"]:g["x"] + g["w"]]
            g["mask"] = np.isin(sub, g["ids"])
            for piece in split_wide(g):
                piece["line"] = li
                signs.append(piece)
    return can, lab, lines, signs, x0, y0


def tighten(mask, x, y, ncomp):
    ys, xs = np.nonzero(mask)
    if len(xs) == 0:
        return None
    m = mask[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    return dict(x=x + xs.min(), y=y + ys.min(), w=m.shape[1], h=m.shape[0], area=int(m.sum()),
                mask=m, ncomp=ncomp)


def split_wide(g):
    """Split a sign box that holds two or more touching signs: cut at the thinnest ink column
    (at most SPLIT_MAX_INK px of ink) at least SPLIT_MARGIN px from either edge, recursively.
    Median sign width is ~42 px; nothing narrower than SPLIT_W is touched."""
    mask = g["mask"]
    out = [tighten(mask, g["x"], g["y"], len(g["ids"]))]
    if g["w"] < SPLIT_W:
        return out
    col = mask.sum(axis=0)
    lo, hi = SPLIT_MARGIN, g["w"] - SPLIT_MARGIN
    if hi <= lo:
        return out
    c = lo + int(np.argmin(col[lo:hi]))
    if col[c] > SPLIT_MAX_INK:
        return out
    pieces = []
    for part, dx in ((mask[:, :c], 0), (mask[:, c + 1:], c + 1)):
        t = tighten(part, g["x"] + dx, g["y"], 1)
        if t is None or t["area"] < MIN_AREA:
            continue
        t["ids"] = [0]
        pieces.extend(split_wide(dict(t, mask=t["mask"])))
    return pieces or out


def bitmap(g):
    m = g["mask"].astype(np.uint8) * 255
    s = max(g["w"], g["h"])
    sq = np.zeros((s, s), np.uint8)
    oy, ox = (s - g["h"]) // 2, (s - g["w"]) // 2
    sq[oy:oy + g["h"], ox:ox + g["w"]] = m
    return cv2.resize(sq, (NORM, NORM), interpolation=cv2.INTER_AREA)


def all_signs():
    """Every segmented sign of the cipher block, in reading order, with its mask and line centre."""
    span = json.load(open(CIPHER_SPAN_FILE)) if os.path.exists(CIPHER_SPAN_FILE) else {}
    out, linerows = [], []
    for page in PAGES:
        can, lab, lines, signs, x0, y0 = segment(page)
        for li, ly in enumerate(lines):
            n = sum(1 for g in signs if g["line"] == li)
            linerows.append(f"{page}\t{li}\t{ly + y0}\t{n}")
        sp = span.get(page)
        for g in signs:
            li, gx = g["line"], g["x"] + x0
            if sp is None:
                continue
            (l0, xs0), (l1, xs1) = sp
            if li < l0 or li > l1:
                continue
            if li == l0 and xs0 is not None and gx + g["w"] / 2 < xs0:
                continue
            if li == l1 and xs1 is not None and gx + g["w"] / 2 > xs1:
                continue
            if g["area"] < 60 and g["h"] < 18:   # a lone dot or tick that merged into no sign
                continue
            out.append(dict(page=page, line=li, x=int(gx), y=int(g["y"] + y0), w=int(g["w"]), h=int(g["h"]),
                            area=int(g["area"]), ncomp=g["ncomp"], mask=g["mask"], line_y=float(lines[li] + y0)))
    out.sort(key=lambda g: (list(PAGES).index(g["page"]), g["line"], g["x"]))
    # local line centre: the page-wide peak drifts off the writing on sloping lines, so use the
    # median vertical centre of the 4 signs either side on the same line
    for i, g in enumerate(out):
        nb = [o["y"] + o["h"] / 2 for o in out[max(0, i - 4):i + 5]
              if o is not g and o["page"] == g["page"] and o["line"] == g["line"]]
        if nb:
            g["line_y"] = float(np.median(nb))
    return out, linerows


def main():
    signs, linerows = all_signs()
    with open(os.path.join(HERE, "lines.tsv"), "w") as f:
        f.write("page\tline\ty_centre\tsigns_on_line\n" + "\n".join(linerows) + "\n")
    with open(os.path.join(HERE, "signs.tsv"), "w") as f:
        f.write("sid\tpage\tline\tx\ty\tw\th\tarea\tncomp\n")
        for k, g in enumerate(signs):
            f.write(f"{k}\t{g['page']}\t{g['line']}\t{g['x']}\t{g['y']}\t{g['w']}\t{g['h']}\t{g['area']}\t{g['ncomp']}\n")
    np.savez_compressed(os.path.join(HERE, "signs_bitmaps.npz"), bm=np.array([bitmap(g) for g in signs]))
    print(f"{len(signs)} signs")


if __name__ == "__main__":
    main()
