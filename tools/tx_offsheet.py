#!/usr/bin/env python3
"""Sheet inventory as the instrument (PREREG benchmark-tx/PREREG-txeng2-2.md X1; TXE2-SHEET, 9 Oct 2026).

Read-free: no model call, no truth file opened by `detect` or `grow`.

  detect  per reference position of an item, an off-sheet score from the line crops alone:
          1. each line crop is binarised (Otsu), the cipher band found by the row-ink profile, connected
             components merged by x-overlap into blobs (s1/s2 segment pairs are stitched at the offset that
             best matches their column-ink profiles over the overlap);
          2. the blobs are aligned to a skeleton read (a reader pass WITH its CLEAR rows, so clear words absorb
             their blobs) by a monotone DP over blob spans (cost: log width ratio to the label's expected
             width, re-estimated twice; internal gaps; skipped blobs/tokens), then the skeleton is mapped to
             the item's reference positions with tx_bench.align (sign labels only);
          3. each tile is normalised to a 32x32 ink-bbox bitmap (aspect kept) + coarse orientation histogram;
             the sheet's cells are the labels of the reader vocabulary, each represented by its CONSENSUS tiles
             (both readers give that label at that position, the glyph_atlas-style "secure" tiles); off-sheet
             score = min over cells of the mean distance to the cell's k nearest consensus tiles (self excluded);
          4. flagged = any reader NEW:/X_/? label at the position, then the top-scoring rest, q% of tiled
             positions in all (q caps the union, so the gate's <= 15% holds by construction).
          Writes a TSV: line, pos, ref_sign, tile box, score, rank_share, reader_flag, flagged.
  grow    the flagged tiles clustered by shape (agglomerative, average linkage, distance threshold), each
          cluster with >= min_size tiles -> a new cell NEW_k, exemplar = the medoid tile; writes the grown
          sheet PNG (base cells: label + 3 consensus exemplars; grown cells: NEW_k + medoid + 2 nearest
          members, never a value) and a cells TSV.
  recall  (scoring step, run only after detect's output is committed) recall of the baseline's errors
          (tx_bench.position_errors) among flagged positions; share of all tiled and of scored positions.

Config JSON per item (see benchmark-tx/txeng2/txe2-sheet/items/*.json):
  {"item": id, "truth_for_ref": path (only ref_sign/pos/line are read by detect), "lines": {line: [crop, ...]},
   "skeleton": {line: [label|"CLEAR", ...]} or "skeleton_pass": path, "passes": [pathA, pathB],
   "line_prefix": "f89" or null, "label_map": path or null, "band": [lo, hi] fraction of crop height or null}

Must catch: an off-vocabulary sign (one the sheet has no cell for) whose tile matches no cell's consensus tiles.
Must NOT block / known blind spot: a consensus misread (both readers give the same wrong on-sheet label) -- its tile
becomes a consensus tile of the wrong cell and scores on-sheet; an on-sheet look-alike confusion likewise.
Offline test: tools/tests/test_tx_offsheet.py (synthetic glyph lines with a planted off-sheet shape).
"""
import argparse
import csv
import json
import math
import os
import sys
from collections import defaultdict

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench as tb  # noqa: E402

FLAG_PREFIXES = ('NEW', 'X_', '?')


# ---------------------------------------------------------------- image helpers
def otsu(g):
    hist = np.bincount(g.ravel(), minlength=256).astype(float)
    tot = g.size
    sum_all = np.dot(np.arange(256), hist)
    wb = sb = 0.0
    best, thr = -1, 128
    for t in range(256):
        wb += hist[t]
        if wb == 0:
            continue
        wf = tot - wb
        if wf == 0:
            break
        sb += t * hist[t]
        mb, mf = sb / wb, (sum_all - sb) / wf
        v = wb * wf * (mb - mf) ** 2
        if v > best:
            best, thr = v, t
    return thr


def load_ink(path):
    g = np.asarray(Image.open(path).convert('L'), dtype=np.uint8)
    return g < otsu(g)


def stitch(inks, min_ov=60, max_ov=700):
    """Join left-to-right segments at the overlap that best matches column ink profiles."""
    out = inks[0]
    offsets = [0]
    for nxt in inks[1:]:
        h = min(out.shape[0], nxt.shape[0])
        a, b = out[:h].sum(0).astype(float), nxt[:h].sum(0).astype(float)
        best, bo = -2, min_ov
        for ov in range(min_ov, min(max_ov, len(a), len(b))):
            x, y = a[-ov:], b[:ov]
            if x.std() == 0 or y.std() == 0:
                continue
            c = np.corrcoef(x, y)[0, 1]
            if c > best:
                best, bo = c, ov
        offsets.append(out.shape[1] - bo)
        out = np.concatenate([out[:h], nxt[:h, bo:]], axis=1)
    return out, offsets


def band_rows(ink, band=None):
    h = ink.shape[0]
    if band:
        return int(band[0] * h), int(band[1] * h)
    prof = ink.sum(1).astype(float)
    k = max(3, h // 25)
    prof = np.convolve(prof, np.ones(k) / k, mode='same')
    lo, hi = int(0.25 * h), int(0.8 * h)
    pk = lo + int(np.argmax(prof[lo:hi]))
    thr = 0.3 * prof[pk]
    a = pk
    while a > 0 and prof[a] > thr:
        a -= 1
    b = pk
    while b < h - 1 and prof[b] > thr:
        b += 1
    pad = max(2, (b - a) // 6)
    return max(0, a - pad), min(h, b + pad)


def blobs(ink, rows):
    from scipy import ndimage
    a, b = rows
    sub = ink[a:b]
    lab, n = ndimage.label(sub, structure=np.ones((3, 3)))
    objs = ndimage.find_objects(lab)
    bx = []
    for i, sl in enumerate(objs):
        if sl is None:
            continue
        ys, xs = sl
        area = int((lab[sl] == i + 1).sum())
        if area < 12:
            continue
        bx.append([xs.start, xs.stop, ys.start + a, ys.stop + a])
    bx.sort()
    merged = []
    for x0, x1, y0, y1 in bx:
        if merged:
            m = merged[-1]
            ov = min(m[1], x1) - max(m[0], x0)
            if ov > 0.4 * min(x1 - x0, m[1] - m[0]):
                m[0], m[1], m[2], m[3] = min(m[0], x0), max(m[1], x1), min(m[2], y0), max(m[3], y1)
                continue
        merged.append([x0, x1, y0, y1])
    return merged


# ---------------------------------------------------------------- alignment of blobs to a skeleton read
def dp_align(bl, skel, exp_w, med):
    """bl: blobs [x0,x1,..]; skel: labels; returns per skeleton index a (i0,i1) blob span or None."""
    n, m = len(bl), len(skel)
    INF = 1e18
    D = np.full((n + 1, m + 1), INF)
    P = {}
    D[0, 0] = 0
    SKIPB, SKIPT = 1.2, 1.5
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i, j]
            if d >= INF:
                continue
            if i < n:  # skip a blob (noise, a stroke of a neighbour line)
                w = bl[i][1] - bl[i][0]
                c = d + SKIPB * min(1.0, w / med + 0.3)
                if c < D[i + 1, j]:
                    D[i + 1, j] = c; P[(i + 1, j)] = (i, j, None)
            if j < m:
                c = d + SKIPT
                if c < D[i, j + 1]:
                    D[i, j + 1] = c; P[(i, j + 1)] = (i, j, None)
                kmax = 25 if skel[j] == 'CLEAR' else 4
                for k in range(1, kmax + 1):
                    if i + k > n:
                        break
                    x0, x1 = bl[i][0], bl[i + k - 1][1]
                    w = x1 - x0
                    gaps = sum(max(0, bl[t + 1][0] - bl[t][1]) for t in range(i, i + k - 1))
                    e = exp_w.get(skel[j], med)
                    c = d + abs(math.log(max(w, 2) / e)) + (0 if skel[j] == 'CLEAR' else 1.5 * gaps / med) \
                        + 0.25 * (k - 1) * (0 if skel[j] == 'CLEAR' else 1)
                    if c < D[i + k, j + 1]:
                        D[i + k, j + 1] = c; P[(i + k, j + 1)] = (i, j, (i, i + k))
    out = [None] * m
    i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, span = P[(i, j)]
        if span is not None and pj == j - 1:
            out[j - 1] = span
        i, j = pi, pj
    return out


def align_line(bl, skel, iters=2):
    ws = [b[1] - b[0] for b in bl]
    med = float(np.median(ws)) if ws else 20.0
    exp_w = {'CLEAR': med * 4}
    spans = None
    for _ in range(iters + 1):
        spans = dp_align(bl, skel, exp_w, med)
        acc = defaultdict(list)
        for lab, sp in zip(skel, spans):
            if sp:
                acc[lab].append(bl[sp[1] - 1][1] - bl[sp[0]][0])
        exp_w = {k: float(np.median(v)) for k, v in acc.items()}
        exp_w.setdefault('CLEAR', med * 4)
    return spans


# ---------------------------------------------------------------- features
def tile_feature(ink, box, size=32):
    x0, x1, y0, y1 = box
    t = ink[y0:y1, x0:x1]
    if t.sum() == 0:
        return np.zeros(size * size + 8)
    ys, xs = np.nonzero(t)
    t = t[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    h, w = t.shape
    s = max(h, w)
    canvas = np.zeros((s, s), dtype=np.uint8)
    canvas[(s - h) // 2:(s - h) // 2 + h, (s - w) // 2:(s - w) // 2 + w] = t * 255
    im = Image.fromarray(canvas).resize((size, size), Image.BILINEAR)
    v = np.asarray(im, dtype=float).ravel() / 255.0
    from scipy import ndimage
    g = ndimage.gaussian_filter(v.reshape(size, size), 1.0)
    gy, gx = np.gradient(g)
    ang = (np.arctan2(gy, gx) % np.pi)
    mag = np.hypot(gx, gy)
    hist = np.histogram(ang, bins=8, range=(0, np.pi), weights=mag)[0]
    hist = hist / (hist.sum() + 1e-9)
    gv = g.ravel()
    gv = (gv - gv.mean()) / (gv.std() + 1e-9) / math.sqrt(len(gv))
    return np.concatenate([gv, hist * 2.0])


def dist(a, b):
    n = len(a) - 8
    corr = float(np.dot(a[:n], b[:n]))
    return (1 - corr) + float(np.abs(a[n:] - b[n:]).sum())


# ---------------------------------------------------------------- item loading
def norm_label(s, lm):
    s = (s or '').strip()
    return lm.get(s, s) if lm else s


def load_item(cfg):
    lm = tb.load_label_map(cfg['label_map']) if cfg.get('label_map') else None
    truth = tb.read_tsv(cfg['truth_for_ref'])
    ref = defaultdict(list)
    for r in truth:
        ref[r['line']].append((float(r['pos']), r['pos'], norm_label(r['ref_sign'], lm)))
    for k in ref:
        ref[k].sort()
    passes = [tb.load_output([p], prefix=cfg.get('line_prefix')) for p in cfg['passes']]
    passes = [{k: [norm_label(s, lm) for s in v] for k, v in p.items()} for p in passes]
    skel = cfg.get('skeleton')
    if not skel:
        sp = tb.load_output([cfg['skeleton_pass']], prefix=cfg.get('line_prefix'))
        skel = {k: ['CLEAR' if s.startswith('CLEAR') else norm_label(s, lm) for s in v] for k, v in sp.items()}
    return lm, ref, passes, skel


def map_to_ref(ref_labels, seq):
    """{seq index: ref index} via tx_bench.align (labels only)."""
    sub = [(i, s) for i, s in enumerate(seq) if s != 'CLEAR']
    path = tb.align(ref_labels, [set() for _ in ref_labels], [s for _, s in sub])
    out, k = {}, 0
    for ri, s in path:
        if s is not None:
            if ri is not None:
                out[sub[k][0]] = ri
            k += 1
    return out


def detect(cfg, q=0.15, knn=3, debug_dir=None):
    lm, ref, passes, skel = load_item(cfg)
    rows, feats = [], []
    for ln, crops in cfg['lines'].items():
        inks = [load_ink(c) for c in crops]
        ink, _ = stitch(inks) if len(inks) > 1 else (inks[0], [0])
        rr = band_rows(ink, cfg.get('band'))
        bl = blobs(ink, rr)
        sk = skel.get(ln, [])
        spans = align_line(bl, sk)
        rl = [lab for _, _, lab in ref.get(ln, [])]
        m = map_to_ref(rl, sk)
        flags_at = defaultdict(list)
        for p in passes:
            if ln not in p:
                continue
            for ri, s in tb.align(rl, [set() for _ in rl], p[ln]):
                if ri is not None and s:
                    flags_at[ri].append(s)
        for si, ri in m.items():
            sp = spans[si]
            if sp is None:
                continue
            box = [bl[sp[0]][0], bl[sp[1] - 1][1], min(b[2] for b in bl[sp[0]:sp[1]]),
                   max(b[3] for b in bl[sp[0]:sp[1]])]
            _, pos, lab = ref[ln][ri]
            reads = flags_at.get(ri, [])
            rows.append(dict(line=ln, pos=pos, ref_sign=lab, x0=box[0], x1=box[1], y0=box[2], y1=box[3],
                             reads='|'.join(reads),
                             reader_flag=int(any(s.startswith(FLAG_PREFIXES) for s in reads)),
                             consensus=(reads[0] if len(reads) >= 2 and len(set(reads)) == 1
                                        and not reads[0].startswith(FLAG_PREFIXES) else '')))
            feats.append(tile_feature(ink, box))
        if debug_dir:
            os.makedirs(debug_dir, exist_ok=True)
            im = Image.fromarray(((~ink) * 255).astype(np.uint8)).convert('RGB')
            from PIL import ImageDraw
            d = ImageDraw.Draw(im)
            d.line([(0, rr[0]), (im.width, rr[0])], fill=(0, 114, 178))  # BGR colour: blue band edges
            d.line([(0, rr[1]), (im.width, rr[1])], fill=(0, 114, 178))  # BGR colour
            for r in rows:
                if r['line'] == ln:
                    d.rectangle([r['x0'], r['y0'], r['x1'] - 1, r['y1'] - 1], outline=(230, 159, 0))  # BGR colour
                    d.text((r['x0'], max(0, r['y0'] - 11)), str(r['pos']), fill=(0, 0, 0))
            im.save(os.path.join(debug_dir, '%s_tiles.png' % ln))
    F = np.array(feats)
    cells = defaultdict(list)
    for i, r in enumerate(rows):
        if r['consensus']:
            cells[r['consensus']].append(i)
    cells = {k: v for k, v in cells.items() if len(v) >= 2}
    for i, r in enumerate(rows):
        best = 9e9
        for lab, idx in cells.items():
            ds = sorted(dist(F[i], F[j]) for j in idx if j != i)
            if not ds:
                continue
            best = min(best, float(np.mean(ds[:knn])))
        r['score'] = round(best, 4)
    order = sorted(range(len(rows)), key=lambda i: -rows[i]['score'])
    # q caps the WHOLE flagged share (score flags + reader flags together): reader-flagged positions are taken
    # first, then the top-scoring rest until floor(q * N) positions are flagged.
    cap = int(math.floor(q * len(rows)))
    nreader = sum(r['reader_flag'] for r in rows)
    left = max(0, cap - nreader)
    for rank, i in enumerate(order):
        rows[i]['rank_share'] = round((rank + 1) / len(rows), 4)
        rows[i]['flagged'] = int(rows[i]['reader_flag'] == 1)
        if not rows[i]['flagged'] and left > 0:
            rows[i]['flagged'] = 1
            left -= 1
    return rows, F, sorted(cells)


COLS = ['line', 'pos', 'ref_sign', 'x0', 'x1', 'y0', 'y1', 'reads', 'consensus', 'reader_flag', 'score',
        'rank_share', 'flagged']


def write_tsv(path, rows, cols, header=None):
    with open(path, 'w', newline='') as f:
        if header:
            f.write('# %s\n' % header)
        w = csv.DictWriter(f, fieldnames=cols, delimiter='\t', extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)


# ---------------------------------------------------------------- grow
def tile_image(cfg, r, h=48):
    crops = cfg['lines'][r['line']]
    if len(crops) == 1:
        g = Image.open(crops[0]).convert('L')
    else:
        inks = [load_ink(c) for c in crops]
        _, offs = stitch(inks)
        ims = [np.asarray(Image.open(c).convert('L')) for c in crops]
        hh = min(i.shape[0] for i in ims)
        full = ims[0][:hh]
        for o, im in zip(offs[1:], ims[1:]):
            ov = full.shape[1] - o
            full = np.concatenate([full, im[:hh, ov:]], axis=1)
        g = Image.fromarray(full)
    t = g.crop((int(r['x0']) - 2, int(r['y0']) - 2, int(r['x1']) + 2, int(r['y1']) + 2))
    s = h / max(1, t.height)
    return t.resize((max(8, int(t.width * s)), h))


def grow(cfg, rows, F, base_cells, thr=0.9, min_size=3, out_png=None, out_tsv=None):
    from sklearn.cluster import AgglomerativeClustering
    idx = [i for i, r in enumerate(rows) if r['flagged']]
    cells = []
    if len(idx) >= 2:
        M = np.array([[dist(F[i], F[j]) for j in idx] for i in idx])
        cl = AgglomerativeClustering(n_clusters=None, metric='precomputed', linkage='average',
                                     distance_threshold=thr).fit(M)
        groups = defaultdict(list)
        for k, lab in enumerate(cl.labels_):
            groups[lab].append(k)
        n = 0
        for lab, mem in sorted(groups.items(), key=lambda t: -len(t[1])):
            if len(mem) < min_size:
                continue
            n += 1
            sub = M[np.ix_(mem, mem)]
            med = mem[int(np.argmin(sub.sum(1)))]
            near = sorted(mem, key=lambda k: M[med, k])
            cells.append(dict(cell='NEW_%d' % n, size=len(mem), medoid='%s:%s' % (rows[idx[med]]['line'],
                              rows[idx[med]]['pos']), members=','.join('%s:%s' % (rows[idx[k]]['line'],
                              rows[idx[k]]['pos']) for k in mem), _show=[idx[k] for k in near[:3]]))
    if out_tsv:
        write_tsv(out_tsv, cells, ['cell', 'size', 'medoid', 'members'],
                  'grown cells (value-blind): exemplar = medoid tile; members = line:pos of flagged tiles')
    if out_png:
        from PIL import ImageDraw
        entries = []
        for lab in base_cells:
            ex = [i for i, r in enumerate(rows) if r['consensus'] == lab][:3]
            entries.append((lab, ex))
        for c in cells:
            entries.append((c['cell'], c['_show']))
        cw, ch, cols = 260, 70, 5
        nrow = (len(entries) + cols - 1) // cols
        sheet = Image.new('RGB', (cw * cols, ch * nrow + 30), 'white')
        d = ImageDraw.Draw(sheet)
        d.text((8, 8), 'Sign sheet (base labels + grown NEW_k cells; NEW_k = a recurring sign with no label: write NEW_k)',
               fill=(0, 0, 0))
        for k, (lab, ex) in enumerate(entries):
            x, y = (k % cols) * cw, 30 + (k // cols) * ch
            d.rectangle([x + 2, y + 2, x + cw - 3, y + ch - 3], outline=(80, 80, 80))
            d.text((x + 6, y + 6), lab, fill=(0, 0, 0))
            xx = x + 70
            for i in ex:
                t = tile_image(cfg, rows[i])
                if xx + t.width > x + cw - 4:
                    break
                sheet.paste(t, (xx, y + 10))
                xx += t.width + 6
        sheet.save(out_png)
    for c in cells:
        c.pop('_show', None)
    return cells


# ---------------------------------------------------------------- recall (scoring)
def recall(cfg, det_rows, base, exclude_flagged=False):
    lm = tb.load_label_map(cfg['label_map']) if cfg.get('label_map') else None
    T = tb.read_tsv(cfg['truth_for_ref'])
    if exclude_flagged:  # verifier-flagged truth rows counted as excluded (tx_bench --exclude-flagged convention)
        T = tb.drop_flagged(T)
    if lm:
        T = tb.map_truth(T, lm)
    o = tb.load_output([base], prefix=cfg.get('line_prefix'))
    if lm:
        o = {k: [lm.get(s, s) for s in v] for k, v in o.items()}
    eb = tb.position_errors(T, o)
    fl = {(r['line'], str(r['pos'])) for r in det_rows if int(r['flagged'])}
    tiled = {(r['line'], str(r['pos'])) for r in det_rows}
    errs = [k for k, v in eb.items() if v]
    rfl = {(r['line'], str(r['pos'])) for r in det_rows if int(r['flagged']) and int(r.get('reader_flag') or 0)}
    return dict(item=cfg['item'], exclude_flagged=bool(exclude_flagged), errors=len(errs),
                caught=sum(1 for k in errs if k in fl),
                caught_reader_flag=sum(1 for k in errs if k in rfl),
                caught_score_only=sum(1 for k in errs if k in fl and k not in rfl),
                errors_untiled=sum(1 for k in errs if k not in tiled), tiled=len(tiled), flagged=len(fl),
                share_tiled=round(len(fl) / max(1, len(tiled)), 3), scored=len(eb),
                flagged_scored=sum(1 for k in eb if k in fl),
                share_scored=round(sum(1 for k in eb if k in fl) / max(1, len(eb)), 3))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    a = sub.add_parser('detect'); a.add_argument('config'); a.add_argument('--out', required=True)
    a.add_argument('--q', type=float, default=0.15); a.add_argument('--knn', type=int, default=3)
    a.add_argument('--debug-dir')
    g = sub.add_parser('grow'); g.add_argument('configs', nargs='+'); g.add_argument('--det', nargs='+', required=True)
    g.add_argument('--thr', type=float, default=0.9); g.add_argument('--min-size', type=int, default=3)
    g.add_argument('--png', required=True); g.add_argument('--tsv', required=True)
    r = sub.add_parser('recall'); r.add_argument('config'); r.add_argument('--det', required=True)
    r.add_argument('--base', required=True)
    r.add_argument('--exclude-flagged', action='store_true',
                   help='drop verifier-flagged truth rows (tx_bench convention); report beside the as-measured run')
    args = ap.parse_args(argv)
    if args.cmd == 'detect':
        cfg = json.load(open(args.config))
        rows, F, cells = detect(cfg, args.q, args.knn, args.debug_dir)
        write_tsv(args.out, rows, COLS, 'tx_offsheet detect %s q=%s knn=%s cells=%s (read-free)' %
                  (cfg['item'], args.q, args.knn, ' '.join(cells)))
        print('%s: %d tiled positions, %d flagged, %d consensus cells' %
              (cfg['item'], len(rows), sum(r['flagged'] for r in rows), len(cells)))
    elif args.cmd == 'grow':
        cfg = json.load(open(args.configs[0]))
        rows, F, cells = detect(cfg)
        det = {(d['line'], d['pos']): d for d in tb.read_tsv(args.det[0])}
        for rr in rows:
            rr['flagged'] = int(det[(rr['line'], rr['pos'])]['flagged'])
        out = grow(cfg, rows, F, cells, args.thr, args.min_size, args.png, args.tsv)
        print('grown cells: %d (%s)' % (len(out), ', '.join('%s n=%d' % (c['cell'], c['size']) for c in out)))
    else:
        cfg = json.load(open(args.config))
        print(json.dumps(recall(cfg, tb.read_tsv(args.det), args.base, args.exclude_flagged)))


if __name__ == '__main__':
    main()
