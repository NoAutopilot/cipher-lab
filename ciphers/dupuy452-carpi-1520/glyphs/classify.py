#!/usr/bin/env python3
"""Classify every segmented sign against the labelled prototypes (prototypes.npz), and split
boxes that hold two touching signs.

Feature space: HOG of the 48x48 aspect-preserving bitmap (as cluster.py), standardised and
reduced to 40 PCA components fitted on the prototypes, plus log height, log width and the
vertical offset from the line centre, each scaled by the prototypes' medians and weighted
SIZE_WEIGHT. Classifier: k nearest prototypes (K_NN), distance-weighted vote. d1 = distance to
the nearest prototype, the confidence used everywhere below.

Split: a box at least SPLIT_MIN_W px wide is cut at every column (step 2) between SPLIT_EDGE px
from either edge; the cut is kept when both halves classify as real signs (not FRAG) with d1
below the whole box's d1 and below ACCEPT_D (the 97th percentile of the prototypes'
leave-one-out d1). Applied recursively (three touching signs). FRAG (specks, detached tails,
page artefacts) is dropped.

Writes glyphs/classified.tsv: one row per final sign, reading order, with type, d1, vote share,
whether it came from a split, and its bbox.
"""
import csv
import os
import sys

import cv2
import numpy as np
from skimage.feature import hog
from sklearn.neighbors import NearestNeighbors

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import segment as sg  # noqa: E402

K_NN = 5
SIZE_WEIGHT = 0.1
FRAG_MAX = 24
OV_TOL = 6
FRAG_FLAT = 16          # a flat stroke this low is a detached rho tail or a dash, whatever its width
SPLIT_MIN_W = 56
SPLIT_EDGE = 14
TAIL_BELOW = 20
SPLIT_GAIN = 0.75
HOLE_MIN = 6
WIDE_TYPES = {"cross4", "dbar", "U", "pi", "m", "L", "six", "yogh", "zslash", "x", "lamL", "box3", "Tbox", "heart"}
SEED = 20260923


def hogf(b):
    return hog(b.astype(float) / 255, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))


class Model:
    """k nearest prototypes on [HOG (L2-normalised) | blurred 24x24 bitmap (L2-normalised) |
    SIZE_WEIGHT * (log h, log w)]. No PCA whitening: it pulled z onto I and 7 onto T by
    amplifying low-variance directions (hard-case accuracy 4% whitened vs 51% plain, prototype
    4-fold CV 98% either way; tested 23 Sept 2026)."""

    def __init__(self):
        P = np.load(os.path.join(HERE, "prototypes.npz"))
        self.lab = P["label"]
        self.X = self.embed(P["bm"], P["h"], P["w"])
        self.nn = NearestNeighbors(n_neighbors=K_NN + 1).fit(self.X)
        d, i = self.nn.kneighbors(self.X)
        self.accept = float(np.percentile(d[:, 1], 97))     # leave-one-out nearest distance
        keep = self.lab != "FRAG"
        self.lab_nf = self.lab[keep]
        self.nn_nf = NearestNeighbors(n_neighbors=K_NN).fit(self.X[keep])

    @staticmethod
    def embed(bms, h, w):
        out = []
        for b in bms:
            v = hogf(b)
            p = cv2.GaussianBlur(cv2.resize(b, (24, 24), interpolation=cv2.INTER_AREA).astype(float), (5, 5), 1.2).ravel()
            out.append(np.concatenate([v / (np.linalg.norm(v) + 1e-9), p / (np.linalg.norm(p) + 1e-9)]))
        ex = np.stack([np.log(np.asarray(h, float) / 30), np.log(np.asarray(w, float) / 40)], axis=1) * SIZE_WEIGHT
        return np.hstack([np.array(out), ex])

    def classify(self, bms, h, w, dy):
        """FRAG (speck, detached tail, artefact) may win only for a mark under FRAG_MAX px in both
        directions or at most FRAG_FLAT px high: the bitmaps are size-normalised, so a speck can look like any stroke and a
        real sign like a speck; size decides that one question."""
        X = self.embed(bms, h, w)
        d, i = self.nn.kneighbors(X, n_neighbors=K_NN)
        d2, i2 = self.nn_nf.kneighbors(X, n_neighbors=K_NN)
        out = []
        for k, (dd, ii) in enumerate(zip(d, i)):
            lab = self.lab
            if max(h[k], w[k]) >= FRAG_MAX and h[k] > FRAG_FLAT:
                dd, ii, lab = d2[k], i2[k], self.lab_nf
            votes = {}
            for dist, j in zip(dd, ii):
                votes[lab[j]] = votes.get(lab[j], 0) + 1 / (dist + 1e-6)
            best = max(votes, key=votes.get)
            out.append((str(best), float(dd[0]), votes[best] / sum(votes.values())))
        return out


def piece(mask, x, y, line_y):
    ys, xs = np.nonzero(mask)
    if len(xs) == 0:
        return None
    m = mask[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    g = dict(x=x + int(xs.min()), y=y + int(ys.min()), w=m.shape[1], h=m.shape[0], area=int(m.sum()),
             mask=m, line_y=line_y)
    return g


def feats(g):
    return sg.bitmap(g), g["h"], g["w"], g["y"] + g["h"] / 2 - g["line_y"]


def try_split(model, g, whole, depth=0):
    """Return a list of (sign, (label, d1, share)) pieces for g."""
    if g["w"] < SPLIT_MIN_W or depth > 2:
        return [(g, whole)]
    cands = []
    for c in range(SPLIT_EDGE, g["w"] - SPLIT_EDGE, 2):
        R = piece(g["mask"][:, c:], g["x"] + c, g["y"], g["line_y"])
        for strip in (False, True):
            lm = g["mask"][:, :c].copy()
            if strip:
                # the tail of a following rho runs left under this sign: drop the rows below
                # TAIL_BELOW px under the line centre from the left piece and give them to nobody
                cut_row = int(g["line_y"] + TAIL_BELOW - g["y"])
                if cut_row <= 0 or cut_row >= lm.shape[0]:
                    continue
                lm[cut_row:, :] = False
            L = piece(lm, g["x"], g["y"], g["line_y"])
            if L is None or R is None or L["area"] < 60 or R["area"] < 60:
                continue
            cands.append((c, L, R))
    if not cands:
        return [(g, whole)]
    fl = [feats(L) for _, L, _ in cands] + [feats(R) for _, _, R in cands]
    res = model.classify([f[0] for f in fl], [f[1] for f in fl], [f[2] for f in fl], [f[3] for f in fl])
    n = len(cands)
    best = None
    for k, (c, L, R) in enumerate(cands):
        rl, rr = res[k], res[n + k]
        if "FRAG" in (rl[0], rr[0]):
            continue
        worst = max(rl[1], rr[1])
        if (worst < SPLIT_GAIN * whole[1] and worst < model.accept and min(rl[2], rr[2]) >= 0.6
                and (best is None or worst < best[0])):
            best = (worst, L, R, rl, rr)
    if best is None:
        return [(g, whole)]
    _, L, R, rl, rr = best
    return try_split(model, L, rl, depth + 1) + try_split(model, R, rr, depth + 1)


def holes(mask, min_area=HOLE_MIN):
    """Number of enclosed white regions of at least min_area px (contour hierarchy)."""
    m = np.pad(mask.astype(np.uint8), 2)
    cs, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    if hier is None:
        return 0
    return sum(1 for c, h in zip(cs, hier[0]) if h[3] >= 0 and cv2.contourArea(c) >= min_area)


def shape_rules(mask, pr):
    """Settle the two pairs the kNN mixes, by topology rather than appearance:
    o / th by the number of enclosed holes (a bar across the ring makes two); lam / Del by
    whether the outline encloses a hole at all (a closed triangle does, a caret does not)."""
    t = pr[0]
    if t in ("o", "th"):
        k = holes(mask)
        if k == 0:
            return pr, ""
        nt = "th" if k >= 2 else "o"
        return (nt, pr[1], pr[2]), ("o/th" if nt != t else "")
    if t in ("lam", "Del"):
        nt = "Del" if holes(mask) >= 1 else "lam"
        return (nt, pr[1], pr[2]), ("lam/Del" if nt != t else "")
    return pr, ""


def split_rho(model, g, r):
    """A rho whose tail touches the sign before it: above the tail line, find the rho head at
    the right (ink columns up to the first empty column going left); ink further left above the
    tail line is the previous sign. Keep the split when that sign classifies (not FRAG, d1 below
    ACCEPT)."""
    top = int(g["line_y"] + TAIL_BELOW - g["y"])
    if top <= 5:
        return [(g, r)]
    b0 = max(0, int(g["line_y"] - 12 - g["y"]))
    b1 = max(b0 + 1, int(g["line_y"] + 6 - g["y"]))
    colink = g["mask"][b0:b1, :].sum(axis=0)       # mid-line band: the tail never passes here
    c = g["w"] - 1
    while c >= 0 and colink[c] == 0:
        c -= 1
    while c >= 0 and colink[c] > 0:
        c -= 1
    if c < 12 or g["mask"][:top, :c].sum() < 60:
        return [(g, r)]
    lm = np.zeros_like(g["mask"])
    lm[:top, :c] = g["mask"][:top, :c]
    rm = g["mask"].copy()
    rm[:top, :c] = False
    L = piece(lm, g["x"], g["y"], g["line_y"])
    R = piece(rm, g["x"], g["y"], g["line_y"])
    if L is None or R is None:
        return [(g, r)]
    fl = [feats(L), feats(R)]
    rl, rr = model.classify([f[0] for f in fl], [f[1] for f in fl], [f[2] for f in fl], [f[3] for f in fl])
    if rl[0] == "FRAG" or rl[1] > model.accept:
        return [(g, r)]
    return [(L, rl), (R, rr if rr[0] != "FRAG" else r)]


def run():
    model = Model()
    signs, _ = sg.all_signs()
    fl = [feats(g) for g in signs]
    res = model.classify([f[0] for f in fl], [f[1] for f in fl], [f[2] for f in fl], [f[3] for f in fl])
    final = []
    for sid, (g, r) in enumerate(zip(signs, res)):
        if r[0] == "rho" and g["w"] >= 60:
            pieces = split_rho(model, g, r)
        elif g["w"] >= SPLIT_MIN_W and r[0] not in WIDE_TYPES:
            pieces = try_split(model, g, r)
        else:
            pieces = [(g, r)]
        for p, pr in pieces:
            if pr[0] == "FRAG":
                continue
            pr, rule = shape_rules(p["mask"], pr)
            final.append(dict(src=sid, page=g["page"], line=g["line"], x=p["x"], y=p["y"], w=p["w"], h=p["h"],
                              type=pr[0], d1=pr[1], share=pr[2], split=len(pieces) > 1, rule=rule))
    return final, model


def load_overrides():
    fn = os.path.join(HERE, "overrides.tsv")
    return {(o["page"], int(o["line"]), int(o["x"])): o for o in
            csv.DictReader((l for l in open(fn) if not l.startswith("#")), delimiter="\t")}


def apply_overrides(final):
    """By-eye settlements (overrides.tsv). Matched to the nearest sign on the same page, same or
    adjacent line, left edge within OV_TOL px (a segmentation tweak moves boxes by a few px).
    A two-sign box 'a,b' becomes two rows sharing the box; DROP removes the sign."""
    ov = load_overrides()
    idx = {}
    for j, s in enumerate(final):
        idx.setdefault(s["page"], []).append(j)
    target = {}
    missing = []
    for k, o in ov.items():
        page, line, x = k
        best = None
        for j in idx.get(page, []):
            s = final[j]
            dl, dx = abs(int(s["line"]) - line), abs(int(s["x"]) - x)
            if dl <= 1 and dx <= OV_TOL and (best is None or (dl, dx) < best[0]):
                best = ((dl, dx), j)
        if best is None or best[1] in target:
            missing.append(k)
        else:
            target[best[1]] = o
    out = []
    for j, s in enumerate(final):
        o = target.get(j)
        if o is None:
            out.append(s)
            continue
        if o["type"] == "DROP":
            continue
        parts = o["type"].split(",")
        for i, t in enumerate(parts):
            w = s["w"] // len(parts)
            out.append(dict(s, x=s["x"] + i * w, w=w if len(parts) > 1 else s["w"], type=t,
                            rule="override" + ("-split" if len(parts) > 1 else "")))
    return out, missing


def main():
    final, model = run()
    final, missing = apply_overrides(final)
    if missing:
        print("overrides not matched (segmentation changed?):", missing)
    with open(os.path.join(HERE, "classified.tsv"), "w") as f:
        f.write("n\tsrc_sid\tpage\tline\tx\ty\tw\th\ttype\td1\tvote_share\tfrom_split\trule\n")
        for n, s in enumerate(final):
            f.write(f"{n}\t{s['src']}\t{s['page']}\t{s['line']}\t{s['x']}\t{s['y']}\t{s['w']}\t{s['h']}\t"
                    f"{s['type']}\t{s['d1']:.3f}\t{s['share']:.2f}\t{int(s['split'])}\t{s['rule']}\n")
    from collections import Counter
    c = Counter(s["type"] for s in final)
    print(len(final), "signs;", len(c), "types; accept d1 <", round(model.accept, 2),
          "; from splits:", sum(s["split"] for s in final))
    print(sorted(c.items(), key=lambda x: -x[1]))


if __name__ == "__main__":
    main()
