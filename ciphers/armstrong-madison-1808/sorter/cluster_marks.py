#!/usr/bin/env python3
"""ARM-SORTER (4 Oct 2026): value-blind initial piles and the "Check these first" list for the mark sorter.

  python3 ciphers/armstrong-madison-1808/sorter/cluster_marks.py [--k 28] [--sheet OUT.png]

Reads signs.tsv (segment_marks.py) and passages.tsv; writes clusters.tsv (sid, cluster), labels.tsv (sid, sign, family:
the initial pile is the cluster name M01, M02, ... numbered by size, arbitrary, no shorthand value anywhere) and
focus.tsv (sid TAB question, no header, as tools/sign_sorter.py --focus reads it; at most 30). Features as tools/glyph_atlas.py cluster: each tile binarised (ink < 0.62 x a
41 px grey closing), cropped to its box, padded square and resized to 48x48 (aspect kept), HOG (9 orientations, 8x8
cells, 2x2 blocks) plus log height and log width, standardised, PCA(30), k-means with a deliberate over-split (fixed
seed 20261004). Focus, in this order: (1) named spots the two transcriptions or the image leave open (flourish, tick,
gutter-merged boxes, the 'numeral 3' and '31?' spots, a mark ms does not count); (2) in every passage where
ciphertext_ms.txt and codex glyphs.tsv disagree on the mark count, largest disagreement first, its widest tile (two
marks merged?) where glyphs.tsv counts more, its smallest (a fragment or a dot?) where it counts fewer, and both where
the counts differ by 8 or more; (3) the tiles nearest the boundary between two clusters (second-nearest centre
distance / nearest closest to 1), until 30.
"""
import argparse, csv, math
from pathlib import Path
import numpy as np, cv2
from skimage.feature import hog
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
HERE = Path(__file__).resolve().parent; T = HERE.parent

NAMED = [
    ('p1-L07a_01', 'Flourish before 200 (p.1), cut with the 2; neither source counts it; a mark?'),
    ('p1-L07b_01', 'Tick after 38 (p.1): glyphs counts a mark, ms a tick on 38; a mark?'),
    ('p1-L09a_22', "End of p.1 line 9, ms reads '31?'; mark or digits?"),
    ('p3-L04a_02', "p.3 line 4, ms reads a numeral 3 here; a 3 or a mark?"),
    ('p3-L02a_02', 'Before 58 (p.3): glyphs counts a mark, ms none; a mark?'),
    ('p2-L02a_02', 'At the binding edge, gutter line in the box; which part is a mark?'),
    ('p2-L03a_20', 'At the binding edge; one mark or two?'),
    ('p2-L04b_08', 'At the binding edge, gutter line in the box; any mark?'),
    ('p2-L11b_07', 'At the binding edge; mark or gutter?'),
    ('p2-L14a_08', 'At the binding edge; mark or gutter?'),
    ('p3-L13a_01', 'Against the gutter line; which part is a mark?'),
]

def tile(g, x, y, w, h):
    t = g[y:y+h, x:x+w]
    bg = cv2.morphologyEx(g[max(0,y-30):y+h+30, max(0,x-30):x+w+30], cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (41, 41)))
    bg = bg[y-max(0,y-30):y-max(0,y-30)+h, x-max(0,x-30):x-max(0,x-30)+w]
    ink = (t.astype(float) / np.maximum(bg.astype(float), 1) < 0.62).astype(np.uint8) * 255
    s = max(w, h); pad = np.zeros((s, s), np.uint8); pad[(s-h)//2:(s-h)//2+h, (s-w)//2:(s-w)//2+w] = ink
    return cv2.resize(pad, (48, 48), interpolation=cv2.INTER_AREA)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--k', type=int, default=28); ap.add_argument('--sheet')
    a = ap.parse_args()
    S = list(csv.DictReader(open(HERE/'signs.tsv'), delimiter='\t')); imgs = {}
    bms, feats = [], []
    for s in S:
        if s['page'] not in imgs: imgs[s['page']] = cv2.imread(str(T/'images'/(s['page']+'.jpg')), cv2.IMREAD_GRAYSCALE)
        x, y, w, h = (int(s[k]) for k in 'xywh'); b = tile(imgs[s['page']], x, y, w, h); bms.append(b)
        f = hog(b, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2))
        feats.append(np.concatenate([f, [math.log(h) * 3, math.log(w) * 3]]))
    X = np.array(feats); X = (X - X.mean(0)) / (X.std(0) + 1e-6)
    Z = PCA(30, random_state=20261004).fit_transform(X)
    km = KMeans(a.k, n_init=20, random_state=20261004).fit(Z)
    D = km.transform(Z); lab = km.labels_
    order = [c for c, _ in sorted(((c, -(lab == c).sum()) for c in range(a.k)), key=lambda t: (t[1], t[0]))]
    name = {c: f'M{i+1:02d}' for i, c in enumerate(order)}
    with open(HERE/'clusters.tsv', 'w') as f:
        f.write('sid\tcluster\n'); [f.write(f"{s['sid']}\t{name[l]}\n") for s, l in zip(S, lab)]
    with open(HERE/'labels.tsv', 'w') as f:
        f.write('sid\tsign\tfamily\n'); [f.write(f"{s['sid']}\t{name[l]}\tmarks\n") for s, l in zip(S, lab)]
    sids = {s['sid'] for s in S}; focus = [(sid, q) for sid, q in NAMED if sid in sids]; seen = {sid for sid, _ in focus}
    P = list(csv.DictReader(open(HERE/'passages.tsv'), delimiter='\t'))
    P = sorted((p for p in P if p['ms_marks'] != p['glyph_tokens']), key=lambda p: -abs(int(p['ms_marks']) - int(p['glyph_tokens'])))
    for p in P:
        runs = p['runs'].split(','); ts = [s for s in S if s['run'] in runs and s['sid'] not in seen]
        if not ts: continue
        n = len([s for s in S if s['run'] in runs]); diff = int(p['glyph_tokens']) - int(p['ms_marks'])
        msg = f"{p['where'].split(' (')[0]}: ms {p['ms_marks']}, glyphs {p['glyph_tokens']}, cut {n}"
        wide = max(ts, key=lambda s: int(s['w'])); sm = min(ts, key=lambda s: max(int(s['w']), int(s['h'])))
        picks = [(wide, '; widest: one mark or two?'), (sm, '; smallest tile: mark or speck?')]
        if diff < 0: picks.reverse()
        for t, q in picks[:2 if abs(diff) >= 8 else 1]:
            if t['sid'] not in seen: focus.append((t['sid'], msg + q)); seen.add(t['sid'])
    Ds = np.sort(D, 1); ratio = Ds[:, 1] / np.maximum(Ds[:, 0], 1e-6)
    second = np.argsort(D, 1)[:, 1]
    for i in np.argsort(ratio):
        if len(focus) >= 30: break
        sid = S[i]['sid']
        if sid in seen: continue
        focus.append((sid, f'Shape between piles {name[lab[i]]} and {name[second[i]]}; which pile?')); seen.add(sid)
    with open(HERE/'focus.tsv', 'w') as f:
        [f.write(f'{s}\t{q}\n') for s, q in focus[:30]]
    sizes = sorted(((lab == c).sum() for c in range(a.k)), reverse=True)
    print(len(S), 'tiles,', a.k, 'piles, sizes', sizes, '; focus', min(30, len(focus)))
    if a.sheet:
        rows = []
        for c in order:
            idx = [i for i in range(len(S)) if lab[i] == c][:24]
            row = np.full((50, 50 * 25), 255, np.uint8); cv2.putText(row, name[c], (2, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
            for j, i in enumerate(idx): row[1:49, 50*(j+1)+1:50*(j+1)+49] = 255 - bms[i]
            rows.append(row)
        cv2.imwrite(a.sheet, np.vstack(rows))

if __name__ == '__main__': main()
