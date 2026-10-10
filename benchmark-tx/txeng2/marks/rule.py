#!/usr/bin/env python3
"""MARKS-DEV2 (PREREG-txeng2-21 section MARKS-DEV2, push c29543f04; TXE2-MARKS, 10 Oct 2026): the ':' mark-class shape rule,
read-free, on the 37 f.102r line crops of BnF fr.16105 (vivonne1573-f102r-dev2).

READ-FREE: no reader, no truth, no key, no pass output, no label. Inputs: the 74 crops c105_f102r_L01..L37_s{1,2}.jpg, the
folder's images/manifest.json (crop geometry) and one `tools/glyph_atlas.py segment` run (default mode, the OL1-BOXES recipe)
over the 74 crops. Committed BEFORE any run against the truth.

Step 1 (components, the OL1-BOXES recipe, benchmark-tx/txeng2/oracle1/build_ol1_boxes.py, unchanged): segment signs + marks
kept as boxes; centre in line coordinates; a box kept from s_i when its centre lies in [m_(i-1), m_i) (overlap midpoints);
crop-relative ghost rule unchanged (drop when darkest-10% grey / crop median grey > max(0.45, 1.25 x the crop's median ratio
over its segment sign boxes)); reading order = ascending line-coordinate centre x (tie: y). The functions are imported from
build_ol1_boxes.py where they exist (crop_geometry, GHOST); the per-line loop is copied without the overlay/sorter output.

Step 2 (the ':' candidate, PREREG wording; the interpretations below are fixed here, before scoring):
  m = the line's median sign height = median box height over the line's kept boxes of kind 'sign' (line coordinates).
  small: a component whose larger bbox side, max(w, h), is under 0.35 x m.
  a pair (a above b): both small; x-overlap = overlap of their x-intervals / the narrower width >= 0.50; vertical gap =
    top of b - bottom of a, with 0 <= gap < 1.0 x min(h_a, h_b) (a negative gap = not stacked).
  no third component overlapping either: no other kept box in the line whose x-interval overlaps a's or b's x-interval by
    >= 0.50 of the narrower width (the same overlap measure; a stroke in the column voids the pair).
  pairing: candidate pairs taken greedily by smallest vertical gap; each component in at most one pair.
Mapping to reading positions (PREREG: by x-order as OL1-BOXES orders boxes): the pair is collapsed to one unit at the mean of
its two centres, the line's units are re-sorted by centre x, and the candidate's position index = its 0-based rank among the
units. The line's unit count (n_units) is written beside each candidate so the scorer can set it beside the position count.

  python3 benchmark-tx/txeng2/marks/rule.py SEGDIR      (SEGDIR = the segment output; see run.sh)
Writes benchmark-tx/txeng2/marks/{boxes.tsv,candidates.tsv,doubt.tsv}. Prints counts only."""
import csv, json, os, sys
import numpy as np
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, os.path.join(ROOT, 'benchmark-tx/txeng2/oracle1'))
from build_ol1_boxes import crop_geometry, GHOST  # noqa: E402

M = os.path.join(ROOT, 'benchmark-tx/txeng2/marks')
IMG = 'ciphers/fr16104-vivonne-spain-1572/images'
LINES = ['f102r_L%02d' % i for i in range(1, 38)]
SMALL, XOV, VGAP = 0.35, 0.50, 1.0


def line_boxes(seg, line):
    """OL1-BOXES recipe for one two-crop line: kept boxes as dicts with line-coordinate geometry, in reading order."""
    crops = ['%s/c105_%s_s%d.jpg' % (IMG, line, k) for k in (1, 2)]
    names = [os.path.basename(c)[:-4] for c in crops]
    geo = {n: crop_geometry(c) for n, c in zip(names, crops)}
    grey = {n: np.asarray(Image.open(os.path.join(ROOT, c)).convert('L'), dtype=float) for n, c in zip(names, crops)}
    mids = [(geo[names[i + 1]][0] + geo[names[i]][1]) / 2.0 for i in range(len(names) - 1)]
    lo = {n: (mids[i - 1] if i > 0 else -1e9) for i, n in enumerate(names)}
    hi = {n: (mids[i] if i < len(mids) else 1e9) for i, n in enumerate(names)}
    cand = [(s, 'sign') for s in csv.DictReader(open(os.path.join(seg, 'signs.tsv')), delimiter='\t')]
    cand += [(m, 'mark') for m in csv.DictReader(open(os.path.join(seg, 'marks.tsv')), delimiter='\t')]
    ratio = {}
    for s, kind in cand:
        n = s['page']
        if n in geo:
            x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h')); patch = grey[n][y:y + h, x:x + w]
            ratio[id(s)] = np.quantile(patch, 0.1) / np.median(grey[n]) if patch.size else 9.0
    floor = {n: max(GHOST, 1.25 * float(np.median([ratio[id(s)] for s, kd in cand if s['page'] == n and kd == 'sign'] or [GHOST])))
             for n in names}
    kept, ghosts = [], 0
    for s, kind in cand:
        n = s['page']
        if n not in geo:
            continue
        x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
        patch = grey[n][y:y + h, x:x + w]
        gx = geo[n][0] + (x + w / 2.0) * geo[n][2]
        if not (lo[n] <= gx < hi[n]):
            continue
        if patch.size == 0 or ratio[id(s)] > floor[n]:
            ghosts += 1; continue
        sc = geo[n][2]
        # line coordinates: x from the crop's page x0; y from the crop's page y0 (manifest box) so s1/s2 share one frame
        y0 = _crop_y0(crops[names.index(n)])
        kept.append({'gx': gx, 'kind': kind, 'crop': n, 'x': x, 'y': y, 'w': w, 'h': h,
                     'lx0': geo[n][0] + x * sc, 'lx1': geo[n][0] + (x + w) * sc,
                     'ly0': y0 + y * sc, 'ly1': y0 + (y + h) * sc})
    kept.sort(key=lambda t: (t['gx'], t['y']))
    for k, b in enumerate(kept):
        b['order'] = k
    return kept, ghosts


_Y0 = {}


def _crop_y0(path):
    d, f = os.path.split(path)
    if not _Y0:
        for c in json.load(open(os.path.join(ROOT, d, 'manifest.json'))).get('iiif_lines', []):
            _Y0[c['crop']] = c['box'][1]
    return _Y0.get(f, 0)


def xov(a, b):
    o = min(a['lx1'], b['lx1']) - max(a['lx0'], b['lx0'])
    return o / max(1e-9, min(a['lx1'] - a['lx0'], b['lx1'] - b['lx0']))


def candidates(boxes):
    """The PREREG ':' rule on one line's kept boxes; returns (pairs, m)."""
    sh = [b['ly1'] - b['ly0'] for b in boxes if b['kind'] == 'sign']
    if not sh:
        return [], 0.0
    m = float(np.median(sh))
    small = [b for b in boxes if max(b['lx1'] - b['lx0'], b['ly1'] - b['ly0']) < SMALL * m]
    pairs = []
    for i, a in enumerate(small):
        for b in small[i + 1:]:
            top, bot = (a, b) if a['ly0'] <= b['ly0'] else (b, a)
            if xov(top, bot) < XOV:
                continue
            gap = bot['ly0'] - top['ly1']
            hmin = min(top['ly1'] - top['ly0'], bot['ly1'] - bot['ly0'])
            if not (0 <= gap < VGAP * hmin):
                continue
            if any(c is not top and c is not bot and (xov(c, top) >= XOV or xov(c, bot) >= XOV) for c in boxes):
                continue
            pairs.append((gap, top, bot))
    pairs.sort(key=lambda t: (t[0], t[1]['gx']))
    used, out = set(), []
    for gap, top, bot in pairs:
        if id(top) in used or id(bot) in used:
            continue
        used.add(id(top)); used.add(id(bot)); out.append((top, bot))
    return out, m


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    seg = sys.argv[1]
    brow, crow, drow, tot = [], [], [], 0
    for line in LINES:
        boxes, ghosts = line_boxes(seg, line)
        pairs, m = candidates(boxes)
        members = {id(b) for p in pairs for b in p}
        units = [(b['gx'], None) for b in boxes if id(b) not in members]
        units += [((t['gx'] + u['gx']) / 2.0, k) for k, (t, u) in enumerate(pairs)]
        units.sort(key=lambda t: t[0])
        rank = {k: i for i, (_, k) in enumerate(units) if k is not None}
        for b in boxes:
            brow.append((line, b['order'], b['kind'], b['crop'], b['x'], b['y'], b['w'], b['h']))
        for k, (t, u) in enumerate(pairs):
            crow.append((line, rank[k], len(units), len(boxes), '%.1f' % m, t['order'], u['order'],
                         '%.1f' % ((t['gx'] + u['gx']) / 2.0)))
            drow.append((line, rank[k], "':' shape candidate (two small stacked components, no stroke in the column); "
                                       "box order %d+%d of %d; check the sign here, no value proposed" % (t['order'], u['order'], len(boxes))))
        tot += len(boxes)
    with open(os.path.join(M, 'boxes.tsv'), 'w') as f:
        f.write('line\torder\tkind\tcrop\tx\ty\tw\th\n'); f.writelines('\t'.join(map(str, r)) + '\n' for r in brow)
    with open(os.path.join(M, 'candidates.tsv'), 'w') as f:
        f.write('line\tposition\tn_units\tn_boxes\tmedian_sign_h\tbox_top\tbox_bottom\tline_x\n')
        f.writelines('\t'.join(map(str, r)) + '\n' for r in crow)
    with open(os.path.join(M, 'doubt.tsv'), 'w') as f:
        f.write('line\tposition\treason\n'); f.writelines('\t'.join(map(str, r)) + '\n' for r in drow)
    print('lines', len(LINES), 'boxes', tot, 'candidates', len(crow), 'lines with a candidate', len({r[0] for r in crow}))


if __name__ == '__main__':
    main()
