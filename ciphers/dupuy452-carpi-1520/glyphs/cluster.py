#!/usr/bin/env python3
"""Cluster the segmented signs (signs.tsv + signs_bitmaps.npz from segment.py) by shape.

Features per sign: HOG (9 orientations, 8x8 cells, 2x2 blocks) of the 48x48 aspect-preserving
bitmap, plus three scale/placement features (log height and log width relative to the page's
median sign, and the sign's vertical centre relative to its line centre, in median heights),
weighted so that size separates S/s, A/a and Delta/del-type pairs only when HOG cannot.
Distance: Euclidean on standardised PCA(40) components, i.e. a Mahalanobis-like distance on the
main shape variations. k-means with a deliberate over-split (K clusters, fixed seed); the
over-split clusters are merged by eye into sign types in labels.json (cluster -> code), since
two k-means clusters of one sign are harmless and one cluster of two signs is not.

Writes glyphs/clusters.tsv (sid -> cluster; the committed clusters_run1.tsv is the run the labels refer to) and, with --montage, one contact sheet per 20
clusters in the scratch directory given, for inspection.
"""
import csv
import os
import sys

import cv2
import numpy as np
from skimage.feature import hog
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

HERE = os.path.dirname(os.path.abspath(__file__))
K = 72
SEED = 20260923
SIZE_WEIGHT = 3.0


def load():
    rows = list(csv.DictReader(open(os.path.join(HERE, "signs.tsv")), delimiter="\t"))
    bm = np.load(os.path.join(HERE, "signs_bitmaps.npz"))["bm"]
    lines = {}
    for r in csv.DictReader(open(os.path.join(HERE, "lines.tsv")), delimiter="\t"):
        lines[(r["page"], r["line"])] = float(r["y_centre"])
    return rows, bm, lines


def features(rows, bm, lines):
    H = np.array([hog(b.astype(float) / 255, orientations=9, pixels_per_cell=(8, 8),
                      cells_per_block=(2, 2)) for b in bm])
    h = np.array([float(r["h"]) for r in rows])
    w = np.array([float(r["w"]) for r in rows])
    yc = np.array([float(r["y"]) + float(r["h"]) / 2 for r in rows])
    ly = np.array([lines[(r["page"], r["line"])] for r in rows])
    mh = np.median(h)
    extra = np.stack([np.log(h / mh), np.log(w / np.median(w)), (yc - ly) / mh], axis=1)
    Z = PCA(n_components=40, random_state=SEED).fit_transform(StandardScaler().fit_transform(H))
    Z = StandardScaler().fit_transform(Z)
    E = StandardScaler().fit_transform(extra) * SIZE_WEIGHT
    return np.hstack([Z, E])


def cluster(X):
    return KMeans(n_clusters=K, n_init=10, random_state=SEED).fit(X)


def montage(rows, bm, lab, dist, outdir, per=24, cell=56):
    os.makedirs(outdir, exist_ok=True)
    ks = sorted(set(lab))
    for start in range(0, len(ks), 18):
        chunk = ks[start:start + 18]
        sheet = np.full((len(chunk) * cell, (per + 2) * cell), 255, np.uint8)
        for ri, k in enumerate(chunk):
            idx = np.where(lab == k)[0]
            # nearest to the centre first, then a spread out to the farthest members
            idx = idx[np.argsort(dist[idx])]
            pick = list(idx[:per // 2]) + list(idx[len(idx) // 2:][:: max(1, len(idx) // 2 // (per // 2))][:per // 2])
            cv2.putText(sheet, f"{k}:{len(idx)}", (2, ri * cell + 32), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
            for ci, i in enumerate(pick[:per]):
                b = 255 - bm[i]
                r = rows[i]
                s = max(int(r["h"]), int(r["w"]))
                sc = min(1.0, (cell - 4) / 110) * s / 48   # keep true relative size, 110px -> full cell
                t = min(cell - 4, max(8, int(48 * sc)))
                b = cv2.resize(b, (t, t), interpolation=cv2.INTER_AREA)
                y0 = ri * cell + (cell - t) // 2
                x0 = (ci + 2) * cell + (cell - t) // 2
                sheet[y0:y0 + t, x0:x0 + t] = b
            cv2.line(sheet, (0, (ri + 1) * cell - 1), (sheet.shape[1], (ri + 1) * cell - 1), 200, 1)
        cv2.imwrite(os.path.join(outdir, f"sheet_{start:02d}.png"), sheet)


def main():
    rows, bm, lines = load()
    X = features(rows, bm, lines)
    km = cluster(X)
    lab = km.labels_
    dist = np.linalg.norm(X - km.cluster_centers_[lab], axis=1)
    with open(os.path.join(HERE, "clusters.tsv"), "w") as f:
        f.write("sid\tcluster\tdist\n")
        for r, k, d in zip(rows, lab, dist):
            f.write(f"{r['sid']}\t{k}\t{d:.3f}\n")
    if "--montage" in sys.argv:
        montage(rows, bm, lab, dist, sys.argv[sys.argv.index("--montage") + 1])
    print(f"{len(rows)} signs, {K} clusters")


if __name__ == "__main__":
    main()
