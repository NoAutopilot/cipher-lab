#!/usr/bin/env python3
"""R12D-GRAZB2: segment a line half-crop into sign boxes by column ink profile. Library + --stats over r12zb/occ.tsv lines.
python3 r12zb2/seg.py --stats"""
import sys
from pathlib import Path
import numpy as np
from PIL import Image
H = Path(__file__).resolve().parent; T = H.parent

def ink(img):
    a = np.asarray(Image.open(img).convert("L"), dtype=float)
    thr = min(a.mean() - 1.2 * a.std(), 150)  # dark ink on paper
    return a < thr

def segments(img, gap=2, minw=None):
    b = ink(img); h, w = b.shape
    prof = b.sum(0)
    on = prof > max(1, 0.02 * h)
    segs = []; i = 0
    while i < w:
        if on[i]:
            j = i
            while j < w and on[j]: j += 1
            segs.append([i, j]); i = j
        else: i += 1
    # merge segments separated by gaps < gap px
    m = []
    for s in segs:
        if m and s[0] - m[-1][1] < gap: m[-1][1] = s[1]
        else: m.append(s)
    minw = minw or max(3, h * 0.06)
    m = [s for s in m if s[1] - s[0] >= minw or b[:, s[0]:s[1]].sum() > h * 2]
    return m, b

if __name__ == "__main__" and "--stats" in sys.argv:
    import collections
    rows = [l.split("\t") for l in (T / "r12zb/occ.tsv").read_text().splitlines()[1:]]
    import re
    seen = {}
    for r in rows:
        img = T / r[4]
        if img in seen: continue
        segs, b = segments(img)
        # token count n: recompute from x_frac? approximate by r12zb occ (not stored); print seg count
        seen[img] = len(segs)
    for k, v in seen.items(): print(k.name, v)

def align(img, n):
    """Assign n tokens to sign boxes: split over-wide ink runs, then DP-group runs (1-3 per token, small runs skippable)
    minimising squared deviation from the line's mean sign width. Returns list of (x0, x1) per token and the ink mask."""
    segs, b = segments(img)
    if not segs: return None, b
    span = segs[-1][1] - segs[0][0]; w = span / n
    sp = []
    for s in segs:
        k = max(1, round((s[1] - s[0]) / w)) if (s[1] - s[0]) > 1.6 * w else 1
        step = (s[1] - s[0]) / k
        sp += [[int(s[0] + i * step), int(s[0] + (i + 1) * step)] for i in range(k)]
    m = len(sp); INF = 1e18
    D = [[INF] * (n + 1) for _ in range(m + 1)]; P = [[None] * (n + 1) for _ in range(m + 1)]; D[0][0] = 0
    for i in range(m + 1):
        for t in range(n + 1):
            if D[i][t] == INF: continue
            if i < m:  # skip a small run as noise
                wd = sp[i][1] - sp[i][0]
                c = D[i][t] + (0.6 if wd < 0.45 * w else 3.0)
                if c < D[i + 1][t]: D[i + 1][t] = c; P[i + 1][t] = (i, t, None)
            if t < n:
                for g in (1, 2, 3):
                    if i + g > m: break
                    gw = sp[i + g - 1][1] - sp[i][0]
                    c = D[i][t] + ((gw - w) / w) ** 2 + 0.15 * (g - 1)
                    if c < D[i + g][t + 1]: D[i + g][t + 1] = c; P[i + g][t + 1] = (i, t, (sp[i][0], sp[i + g - 1][1]))
            if t + 2 <= n and i < m:  # one run holding two touching signs
                x0, x1 = sp[i]; hw = (x1 - x0) / 2
                c = D[i][t] + 2 * ((hw - w) / w) ** 2 + 0.8
                if c < D[i + 1][t + 2]: D[i + 1][t + 2] = c; P[i + 1][t + 2] = (i, t, "two", (x0, int(x0 + hw), x1))
    if D[m][n] == INF: return None, b
    out = []; i, t = m, n
    while (i, t) != (0, 0):
        pr = P[i][t]; pi, pt, box = pr[0], pr[1], pr[2]
        if box == "two": x0, xm, x1 = pr[3]; out += [(xm, x1), (x0, xm)]
        elif box: out.append(box)
        i, t = pi, pt
    return out[::-1], b
