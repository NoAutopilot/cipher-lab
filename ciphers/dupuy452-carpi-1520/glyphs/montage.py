#!/usr/bin/env python3
"""Contact sheets from classified.tsv, cut from the page image (not the binarised mask).

  python3 montage.py sheet OUT.png          one row per sign type: count, then the 12 most typical
                                            members and the 8 least typical (highest d1), left to right
  python3 montage.py worst OUT.png TYPE N   the N least typical members of one type, with row numbers
  python3 montage.py rows OUT.png n n ...   given classified.tsv rows, with row numbers
"""
import csv
import os
import sys

import cv2
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import segment as sg  # noqa: E402

CELL = 60
_cols = {}


def col(page):
    if page not in _cols:
        _cols[page] = sg.build_column(page)
    return _cols[page]


def cut(r, pad=4):
    can, x0, y0 = col(r["page"])
    x, y, w, h = (int(r[k]) for k in "xywh")
    sub = can[max(0, y - y0 - pad):y - y0 + h + pad, max(0, x - x0 - pad):x - x0 + w + pad]
    s = max(sub.shape)
    t = max(10, min(CELL - 4, int(s * 0.45)))     # common scale: 0.45 px per page px
    f = t / s
    return cv2.resize(sub, (max(1, int(sub.shape[1] * f)), max(1, int(sub.shape[0] * f))), interpolation=cv2.INTER_AREA)


def paste(sheet, img, r, c, label=None):
    y0 = r * (CELL + (12 if label is not None else 0))
    x0 = c * CELL
    h, w = img.shape
    sheet[y0 + (CELL - h) // 2:y0 + (CELL - h) // 2 + h, x0 + (CELL - w) // 2:x0 + (CELL - w) // 2 + w] = img
    if label is not None:
        cv2.putText(sheet, str(label), (x0 + 2, y0 + CELL + 9), cv2.FONT_HERSHEY_SIMPLEX, 0.33, 0, 1)


def load():
    return list(csv.DictReader(open(os.path.join(HERE, "classified.tsv")), delimiter="\t"))


def sheet(out, typical=12, worst=8):
    rows = load()
    by = {}
    for r in rows:
        by.setdefault(r["type"], []).append(r)
    types = sorted(by, key=lambda t: -len(by[t]))
    sh = np.full((len(types) * CELL, (2 + typical + worst + 1) * CELL), 255, np.uint8)
    for i, t in enumerate(types):
        m = sorted(by[t], key=lambda r: float(r["d1"]))
        cv2.putText(sh, f"{t} {len(m)}", (3, i * CELL + 34), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
        for j, r in enumerate(m[:typical]):
            paste(sh, cut(r), i, 2 + j)
        tail = m[typical:][-worst:]
        for j, r in enumerate(tail):
            paste(sh, cut(r), i, 3 + typical + j)
        cv2.line(sh, ((2 + typical) * CELL + CELL // 2, i * CELL + 8), ((2 + typical) * CELL + CELL // 2, i * CELL + CELL - 8), 160, 1)
        cv2.line(sh, (0, (i + 1) * CELL - 1), (sh.shape[1], (i + 1) * CELL - 1), 225, 1)
    cv2.imwrite(out, sh)


def grid(out, rs, per=18):
    n = len(rs)
    sh = np.full((((n + per - 1) // per) * (CELL + 12)), 255, np.uint8)
    sh = np.full((((n + per - 1) // per) * (CELL + 12), per * CELL), 255, np.uint8)
    for k, r in enumerate(rs):
        paste(sh, cut(r), k // per, k % per, r["n"])
    cv2.imwrite(out, sh)


if __name__ == "__main__":
    mode, out = sys.argv[1], sys.argv[2]
    if mode == "sheet":
        sheet(out)
    elif mode == "worst":
        t, n = sys.argv[3], int(sys.argv[4])
        rs = sorted([r for r in load() if r["type"] == t], key=lambda r: -float(r["d1"]))[:n]
        grid(out, rs)
    elif mode == "rows":
        rows = load()
        grid(out, [rows[int(n)] for n in sys.argv[3:]])
