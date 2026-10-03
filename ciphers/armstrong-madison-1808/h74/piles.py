#!/usr/bin/env python3
"""H74b (3 Oct 2026): provisional shape piles for the H74 sorter tiles -- starting labels for a person to correct, not readings.

Rule (deterministic, no model):
- Each tile of h74/signs.tsv is re-cut from its line crop with cut_tiles.py's ink rule (grey < 150, 3x3 closing) and only
  the tile's own 8-connected component kept (the largest one inside the box), made a 48x48 aspect-kept bitmap
  (tools/glyph_atlas.py bitmap()).
- Features as tools/glyph_atlas.py feats(): HOG (9 orientations, 8x8 cells, 2x2 blocks), StandardScaler + PCA(40) +
  unit scaling, plus log height and width relative to the median tile height, weight 3. k-means, K = --k (36),
  n_init 10, random_state 20260924 (glyph_atlas SEED).
- Pile name: the pile's medoid (member nearest the centroid) against every exemplar on Tomokiyo's 38-type sheet
  (h59/person_pack/tomokiyo_38_types.png; rows at a 29.9 px pitch, ink = grey < 110 and unsaturated; the thin grey "Total: N"
  caption breaks into specks under that threshold and a component area >= 5 px drops it), projected through the SAME scaler and PCA, size relative to the sheet's
  own median glyph height. If the nearest exemplar lies within the pile's own 75th-percentile member-to-centroid
  distance, the pile is named "T<type>" (a, b ... when two piles take one type); otherwise a neutral "s<NN>".
- Family = stroke class of the pile's median box: "dot" (longer side < 12 px), "flat" (w >= 2h), "upright" (h >= 1.5w),
  else "compact".
Writes h74/labels.tsv (sid, sign, family) and h74/piles.tsv (pile, family, n, medoid, nearest type, distance, gate).
"""
import argparse, csv, os, sys
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); REPO = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import glyph_atlas as ga  # noqa: E402
import cv2  # noqa: E402
from skimage.feature import hog  # noqa: E402
from sklearn.cluster import KMeans  # noqa: E402
from sklearn.decomposition import PCA  # noqa: E402
from sklearn.preprocessing import StandardScaler  # noqa: E402

LEFT = ['00', '02', '10', '12', '14', '16', '18', '20', '22', '23', '24', '26', '28', '29', '32', '33', '34', '35', '36', '38']
RIGHT = ['40', '42', '44', '46', '47', '48', '60', '62', '64', '65', '66', '68', '70', '72', '73', '74', '76', '78']


def own_component(ink):
    n, lab, st, _ = cv2.connectedComponentsWithStats(ink, 8)
    if n < 2:
        return ink
    i = 1 + int(np.argmax(st[1:, cv2.CC_STAT_AREA]))
    m = (lab == i).astype(np.uint8)
    ys, xs = np.nonzero(m)
    return m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]


def tiles():
    pages = {}
    rows = list(csv.DictReader(open(os.path.join(H, 'signs.tsv')), delimiter='\t'))
    lines = {r['line']: r['crop'] for r in csv.DictReader(open(os.path.join(H, 'lines.tsv')), delimiter='\t')}
    bms, dims = [], []
    for r in rows:
        if r['page'] not in pages:
            img = cv2.imread(os.path.join(T, lines[r['page']]), 0)
            ink = cv2.morphologyEx((img < 150).astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
            pages[r['page']] = ink
        x, y, w, h = (int(r[k]) for k in 'xywh')
        m = own_component(pages[r['page']][y:y + h, x:x + w])
        bms.append(ga.bitmap(m)); dims.append((m.shape[0], m.shape[1]))
    return rows, np.array(bms), np.array(dims, float)


def sheet_exemplars():
    im = cv2.imread(os.path.join(T, 'h59/person_pack/tomokiyo_38_types.png'), cv2.IMREAD_UNCHANGED)[:, :, :3]
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY); s = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)[:, :, 1]
    ink = ((g < 110) & (s < 60)).astype(np.uint8)
    out = []
    for names, x0, x1, y0 in ((LEFT, 58, 664, 16), (RIGHT, 718, 1150, 19)):
        for i, t in enumerate(names):
            yc = int(round(y0 + 29.9 * i)); band = ink[yc - 14:yc + 15, x0:x1]
            n, lab, st, _ = cv2.connectedComponentsWithStats(band, 8)
            comps = [(st[j, 0], j) for j in range(1, n) if st[j, cv2.CC_STAT_AREA] >= 5]
            for cx, j in sorted(comps):
                m = (lab == j).astype(np.uint8); ys, xs = np.nonzero(m)
                m = m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
                out.append((t, ga.bitmap(m), m.shape))
    return out


def hogs(bms):
    return np.array([hog(b.astype(float) / 255, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2)) for b in bms])


def family(h, w):
    if max(h, w) < 12:
        return 'dot'
    if w >= 2 * h:
        return 'flat'
    if h >= 1.5 * w:
        return 'upright'
    return 'compact'


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--k', type=int, default=36)
    a = ap.parse_args()
    rows, bm, dims = tiles()
    ex = sheet_exemplars()
    medh = np.median(dims[:, 0])
    sc1 = StandardScaler().fit(hogs(bm)); pca = PCA(n_components=40, random_state=ga.SEED).fit(sc1.transform(hogs(bm)))
    Z0 = pca.transform(sc1.transform(hogs(bm))); sc2 = StandardScaler().fit(Z0)
    E0 = np.log(np.maximum(dims, 1) / medh); sc3 = StandardScaler().fit(E0)
    X = np.hstack([sc2.transform(Z0), sc3.transform(E0) * 3.0])
    edims = np.array([e[2] for e in ex], float); emedh = np.median(edims[:, 0])
    XE = np.hstack([sc2.transform(pca.transform(sc1.transform(hogs([e[1] for e in ex])))),
                    sc3.transform(np.log(np.maximum(edims, 1) / emedh)) * 3.0])
    km = KMeans(n_clusters=a.k, n_init=10, random_state=ga.SEED).fit(X)
    lab = km.labels_; dist = np.linalg.norm(X - km.cluster_centers_[lab], axis=1)
    order = sorted(range(a.k), key=lambda c: -int((lab == c).sum()))
    names, fams, prow, used = {}, {}, [], {}
    for idx, c in enumerate(order):
        mem = np.where(lab == c)[0]; med = mem[np.argmin(dist[mem])]
        de = np.linalg.norm(XE - X[med], axis=1); j = int(np.argmin(de)); gate = float(np.percentile(dist[mem], 75))
        t = ex[j][0]
        if de[j] <= gate:
            used[t] = used.get(t, 0) + 1; nm = f'T{t}'
        else:
            nm = f's{idx + 1:02d}'
        names[c] = nm
        mh, mw = np.median(dims[mem], axis=0); fams[c] = family(mh, mw)
        prow.append([nm, fams[c], len(mem), rows[med]['sid'], t, f'{de[j]:.2f}', f'{gate:.2f}'])
    # suffix types taken by more than one pile
    seen = {}
    for c in order:
        nm = names[c]
        if nm.startswith('T') and used[nm[1:]] > 1:
            seen[nm] = seen.get(nm, 0) + 1; names[c] = nm + 'abcdefghij'[seen[nm] - 1]
    for r, c in zip(prow, order):
        r[0] = names[c]
    with open(os.path.join(H, 'labels.tsv'), 'w') as f:
        f.write('sid\tsign\tfamily\n' + ''.join(f"{r['sid']}\t{names[l]}\t{fams[l]}\n" for r, l in zip(rows, lab)))
    with open(os.path.join(H, 'piles.tsv'), 'w') as f:
        f.write('pile\tfamily\tn\tmedoid\tnearest_type\tdist\tgate_p75\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in prow))
    print(f'tiles {len(rows)}, sheet exemplars {len(ex)} of {len(set(e[0] for e in ex))} types, K {a.k}, seed {ga.SEED}')
    print(f"named after a type: {sum(n.startswith('T') for n in names.values())}, neutral: {sum(n.startswith('s') for n in names.values())}")
    for r in prow:
        print('\t'.join(map(str, r)))


if __name__ == '__main__':
    main()
