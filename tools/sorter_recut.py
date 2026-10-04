#!/usr/bin/env python3
"""Re-cut a sign-sorter page so that ONE TILE = ONE SIGN, on straight (deskewed) line strips (shared, 4 Oct 2026).

Generalised from ciphers/fr16045-pisany-rome-1585/sorter/recut.py (PIS-RECUT) for LL-RECUT (Longlee f.101v): the method
is the same, the target supplies its region image, line traces, reader columns and old tile centres. Library, not CLI:

    import sorter_recut as sr
    cfg = sr.Cfg(pitch=140, half=120, xmin=15, xmax=2870)
    sr.run(grey, traces, pages, cols, centres, out_dir, pages_dir, cfg, debug=None)

  grey     uint8 array of the region (the same image the traces were measured on)
  traces   list of per-line centre y(x) arrays (len = region width)
  pages    page names, one per line (written as pages_dir/<page>.jpg; tile ids <page>_<kk>)
  cols     per line, the reader columns in x order as (pile, family) pairs ([] when no reader row belongs to the line)
  centres  per line, a position estimate x for each column (the earlier cut's tile centres), same length as cols
  fallback per line, the pile an unaligned tile falls back to when its shape cluster holds no aligned tile

1. Deskew: each column x of the region is shifted so that y(x) lands on the strip's middle row (a shear; at ~3 degrees a
   shear is indistinguishable from a rotation). recentre() first corrects the trace per 300 px window on the strip's own
   row-ink peak. Every strip is the full region width and HALF px either side of the centre.
2. Segment by the sign's own ink: background-normalised binarisation (pixel < REL x grey closing), 8-connected components;
   a component belongs to the line if its median row is within OWN x pitch of the centre and it has ink within CORE x pitch.
   Components overlapping in x by more than MERGE of the narrower are one sign (pairwise union, never a grown span). A group
   wider than SPLIT x the line's median sign width is cut into round(width / median) pieces at the column-ink minima nearest
   the equal-width cut points. Over-splits a little on purpose (the owner merges fast).
3. Starting piles, value-blind: tiles and columns aligned in x order by monotone DP (cost |dx|, skip SKIP px); a tile within
   CLEAR px takes that column's pile. Every other tile goes to the pile its shape cluster (k-means on 32x32 bitmaps + aspect
   and height, NCLU clusters) mostly holds among the clear tiles, and is a focus candidate. Focus (<= NFOCUS): those, ranked
   by cluster size (frequent shapes first), at most PER_CLU per cluster.
Writes out_dir/signs.tsv, labels.tsv, clusters.tsv, focus.tsv, fit_recut.tsv, and region.json (SORTER-PAGEVIEW, 4 Oct
2026: each line's trace, so tools/sign_sorter.py --region can show a tile on the original page region; write_region()). Offline test: tools/tests/test_sorter_recut.py.
"""
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi


@dataclass
class Cfg:
    pitch: int
    half: int = 120
    xmin: int = 15          # ink left of this column is ignored (margin)
    xmax: int = 10 ** 9     # ink right of this column is ignored (scan edge)
    rel: float = 0.72
    own: float = 0.50
    core: float = 0.30
    dot: float = 0.14
    split: float = 1.45
    skip: float = 45
    clear: float = 30
    merge: float = 0.6
    nclu: int = 60
    per_clu: int = 2
    recentre: int = 60
    nfocus: int = 40
    minpix: int = 25
    jpeg: int = 82
    generic: tuple = ()     # catch-all piles (split-rare, one-reader): an unaligned tile goes to its cluster's most common
                            # OTHER pile when that holds >= GEN_MIN tiles and >= GEN_SHARE of the cluster's aligned tiles
    gen_min: int = 3
    gen_share: float = 0.25


def smooth(v, k):
    return np.convolve(v.astype(float), np.ones(k) / k, 'same')


def deskew(grey, tr, cfg):
    """Column-wise shear: out[r, x] = grey[round(tr[x]) - pitch + r, x] (one pitch either side, the labelling margin)."""
    H, W = grey.shape; h2 = cfg.pitch; out = np.full((2 * h2 + 1, W), 255, np.uint8)
    for x in range(W):
        c = int(round(tr[x])); lo, hi = c - h2, c + h2 + 1
        a, b = max(0, lo), min(H, hi)
        out[a - lo:b - lo, x] = grey[a:b, x]
    return out


def recentre(grey, tr, cfg):
    """Per 300 px window (step 150) the smoothed row-ink peak within +-cfg.recentre px of the middle row gives a
    correction; median over five windows, interpolated in x."""
    st = deskew(grey, tr, cfg); c = cfg.pitch; W = st.shape[1]; R = cfg.recentre
    bg = ndi.grey_closing(st, size=(31, 31)).astype(float) + 1; ink = st < cfg.rel * bg
    xs = list(range(0, W - 150, 150)); d = []
    for x in xs:
        pr = smooth(ink[:, x:x + 300].sum(1), 31)[c - R:c + R + 1]
        d.append(int(np.argmax(pr)) - R if pr.max() > 0 else 0)
    d = np.array(d, float); d = np.array([np.median(d[max(0, i - 2):i + 3]) for i in range(len(d))])
    return tr + np.interp(np.arange(W), [x + 150 for x in xs], d)


def segment(strip, cfg):
    """Sign boxes (x0, y0, x1, y1) in strip coords (centre row = pitch), and the line's median sign width."""
    p = cfg.pitch; c = p
    bg = ndi.grey_closing(strip, size=(31, 31)).astype(float) + 1
    ink = strip < cfg.rel * bg
    ink[:, :cfg.xmin] = False; ink[:, cfg.xmax:] = False
    lab, n = ndi.label(ink, structure=np.ones((3, 3)))
    comps = []
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        ys, xs = np.nonzero(lab[sl] == i); ys = ys + sl[0].start; xs = xs + sl[1].start
        if len(ys) < cfg.minpix: continue
        if abs(np.median(ys) - c) > cfg.own * p: continue
        if np.abs(ys - c).min() > cfg.core * p: continue
        comps.append([xs.min(), ys.min(), xs.max(), ys.max(), len(ys)])
    comps.sort()
    par = list(range(len(comps)))

    def root(i):
        while par[i] != i: i = par[i]
        return i
    for i, b in enumerate(comps):
        for j in range(i):
            g = comps[j]; ov = min(g[2], b[2]) - max(g[0], b[0])
            if ov > cfg.merge * min(g[2] - g[0] + 1, b[2] - b[0] + 1): par[root(i)] = root(j)
    gs = defaultdict(list)
    for i, b in enumerate(comps): gs[root(i)].append(b)
    groups = sorted([min(b[0] for b in v), min(b[1] for b in v), max(b[2] for b in v), max(b[3] for b in v), sum(b[4] for b in v)]
                    for v in gs.values())
    big = [g for g in groups if max(g[2] - g[0], g[3] - g[1]) >= cfg.dot * p]
    wmed = float(np.median([g[2] - g[0] + 1 for g in big])) if big else 40.0
    prof = ndi.uniform_filter1d((ink & (np.abs(np.arange(ink.shape[0])[:, None] - c) < cfg.core * p)).sum(0).astype(float), 5)
    out = []
    for g in groups:
        w = g[2] - g[0] + 1
        if w <= cfg.split * wmed:
            out.append(g[:4]); continue
        k = max(2, int(round(w / wmed))); cuts = [g[0]]
        for j in range(1, k):
            t = g[0] + j * w / k; lo, hi = int(t - .35 * w / k), int(t + .35 * w / k)
            cuts.append(lo + int(np.argmin(prof[lo:hi + 1])))
        cuts.append(g[2] + 1)
        for a, b in zip(cuts, cuts[1:]):
            sub = ink[:, a:b] & (lab[:, a:b] > 0)
            rows = np.nonzero(sub[max(0, g[1]):g[3] + 1].any(1))[0]
            y0, y1 = (g[1] + rows.min(), g[1] + rows.max()) if len(rows) else (g[1], g[3])
            out.append([a, y0, b - 1, y1])
    return out, wmed


def align(tx, cx, skip):
    """Monotone DP: tiles at tx, columns at cx (both sorted). Returns {tile index: column index}."""
    n, m = len(tx), len(cx); D = np.full((n + 1, m + 1), 1e18); B = np.zeros((n + 1, m + 1), int)
    D[0, :] = np.arange(m + 1) * skip; D[:, 0] = np.arange(n + 1) * skip
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            opts = (D[i - 1, j - 1] + abs(tx[i - 1] - cx[j - 1]), D[i - 1, j] + skip, D[i, j - 1] + skip)
            k = int(np.argmin(opts)); D[i, j] = opts[k]; B[i, j] = k
    i, j, res = n, m, {}
    while i > 0 and j > 0:
        k = B[i, j]
        if k == 0: res[i - 1] = j - 1; i -= 1; j -= 1
        elif k == 1: i -= 1
        else: j -= 1
    return res


def bitmap(a):
    h, w = a.shape; s = max(h, w); pad = np.zeros((s, s), bool)
    pad[(s - h) // 2:(s - h) // 2 + h, (s - w) // 2:(s - w) // 2 + w] = a
    return np.array(Image.fromarray((pad * 255).astype(np.uint8)).resize((32, 32), Image.BILINEAR), float) / 255


REGION_STEP = 8   # region.json samples each line's centre trace every REGION_STEP px of x


def write_region(out_dir, grey, cfg, used, region_image=None):
    """SORTER-PAGEVIEW (4 Oct 2026): region.json, so the sorter can show a tile on the ORIGINAL page region (continuous, no
    trimmed strips) with its box drawn there. A strip-page pixel (x, y) of line <page> is region pixel
    (x, round(trace(x)) - half + y): the shear moves columns vertically only, so a tile box [x, y, w, h] is a parallelogram
    on the region whose left and right edges stay vertical. trace is sampled every `step` px (last sample at x = W - 1);
    the page interpolates linearly, which is within 1 px of the deskew's own rounding at 8 px steps."""
    import json
    H, W = grey.shape; xs = list(range(0, W, REGION_STEP)) + ([W - 1] if (W - 1) % REGION_STEP else [])
    doc = {'W': W, 'H': H, 'half': cfg.half, 'pitch': cfg.pitch, 'step': REGION_STEP, 'image': region_image,
           'lines': {p: [int(round(tr[x])) for x in xs] for p, tr in used}}
    with open(Path(out_dir) / 'region.json', 'w') as o: json.dump(doc, o, separators=(',', ':'))
    return doc


def region_y(doc, page, x, y):
    """Region row of strip-page pixel (x, y) of line `page` (the inverse of the shear; region.json's own interpolation)."""
    t = doc['lines'][page]; st = doc['step']; i = min(int(x // st), len(t) - 2); x0 = i * st
    x1 = doc['W'] - 1 if i + 1 == len(t) - 1 else (i + 1) * st
    f = (x - x0) / max(1, x1 - x0)
    return t[i] + f * (t[i + 1] - t[i]) - doc['half'] + y


def run(grey, traces, pages, cols, centres, out_dir, pages_dir, cfg, fallback=None, debug=None, focus_word='shape',
        region_image=None):
    from sklearn.cluster import KMeans
    out_dir, pages_dir = Path(out_dir), Path(pages_dir); pages_dir.mkdir(parents=True, exist_ok=True)
    fallback = fallback or ['one-reader'] * len(pages)
    tiles, stats, bms, used = [], [], [], []
    for page, tr, cl, cx, fb in zip(pages, traces, cols, centres, fallback):
        tr = recentre(grey, tr, cfg); strip = deskew(grey, tr, cfg); boxes, wmed = segment(strip, cfg); used.append((page, tr))
        off = cfg.pitch - cfg.half
        Image.fromarray(strip[off:off + 2 * cfg.half + 1]).save(pages_dir / f'{page}.jpg', quality=cfg.jpeg)
        cx = list(cx)[:len(cl)]
        txs = [(b[0] + b[2]) / 2 for b in boxes]; m = align(txs, cx, cfg.skip) if cx else {}
        stats.append((page, len(boxes), len(cl) if cl else '', sum(1 for i in m if abs(txs[i] - cx[m[i]]) <= cfg.clear)))
        for k, (x0, y0, x1, y1) in enumerate(boxes, 1):
            y0p, y1p = max(0, y0 - off), min(2 * cfg.half, y1 - off)
            sid = f'{page}_{k:02d}'; j = m.get(k - 1); clear = j is not None and abs(txs[k - 1] - cx[j]) <= cfg.clear
            lab, fam = cl[j] if clear else (None, None)
            tiles.append(dict(sid=sid, page=page, x=int(x0), y=int(y0p), w=int(x1 - x0 + 1), h=int(y1p - y0p + 1),
                              sign=lab, family=fam, col=(j + 1 if j is not None else ''),
                              dx=(round(abs(txs[k - 1] - cx[j])) if j is not None else ''),
                              colpile=(cl[j][0] if j is not None else fb)))
            bg = ndi.grey_closing(strip[y0:y1 + 1, x0:x1 + 1], size=(15, 15)).astype(float) + 1
            g = strip[y0:y1 + 1, x0:x1 + 1]; aspect = (x1 - x0 + 1) / (y1 - y0 + 1)
            bms.append(np.r_[bitmap(g < cfg.rel * np.maximum(bg, g.max() * .9)).ravel(),
                             [np.log(aspect) * 2, np.log((y1 - y0 + 1) / cfg.pitch)]])
        if debug:
            im = Image.fromarray(strip[off:off + 2 * cfg.half + 1]).convert('RGB'); d = ImageDraw.Draw(im)
            for k, (x0, y0, x1, y1) in enumerate(boxes, 1):
                d.rectangle((x0, y0 - off, x1, y1 - off), outline=(255, 0, 0) if k % 2 else (0, 0, 255), width=2)
                d.text((x0, 2 * cfg.half - 14), str(k), fill=(200, 0, 0))
            Path(debug).mkdir(parents=True, exist_ok=True); im.save(Path(debug) / f'debug_{page}.jpg', quality=80)
    X = np.array(bms); km = KMeans(cfg.nclu, n_init=4, random_state=0).fit(X); cl = km.labels_
    dist = np.linalg.norm(X - km.cluster_centers_[cl], axis=1)
    major = {}
    for c in range(cfg.nclu):
        cnt = Counter(t['sign'] for t, k in zip(tiles, cl) if k == c and t['sign'])
        major[c] = cnt.most_common(1)[0][0] if cnt else None
        spec = [(v, n) for v, n in cnt.most_common() if v not in cfg.generic]
        if cfg.generic and spec and spec[0][1] >= cfg.gen_min and spec[0][1] >= cfg.gen_share * sum(cnt.values()):
            major[c] = spec[0][0]
    fam_of = {t['sign']: t['family'] for t in tiles if t['sign']}
    size = Counter(cl); cand = []
    for t, c, dd in zip(tiles, cl, dist):
        t['cluster'] = int(c)
        if t['sign']: continue
        guess = major[c] or t['colpile'] or 'one-reader'
        t['sign'] = guess; t['family'] = fam_of.get(guess, guess.split('/')[0].split('+')[0])
        cand.append((-size[c], dd, t, c))
    cand.sort(key=lambda q: (q[0], q[1])); per = Counter(); focus = []
    for _, _, t, c in cand:
        if per[c] >= cfg.per_clu: continue
        per[c] += 1
        near = f"nearest reader column {t['col']} ({t['colpile']}, {t['dx']} px off)" if t['col'] else 'no reader column near it'
        focus.append((t['sid'], f"{t['sid'].split('_', 1)[1]}: cut from the ink, {near}; started in {t['sign']} by {focus_word} "
                                f"(a shape seen {size[c]} times on the page). Right pile, another sign, or a bad cut?"))
        if len(focus) >= cfg.nfocus: break

    def w(name, rows, keys):
        with open(out_dir / name, 'w') as o:
            o.write('\t'.join(keys) + '\n'); o.writelines('\t'.join(str(r[k]) for k in keys) + '\n' for r in rows)
    w('signs.tsv', tiles, ['sid', 'page', 'x', 'y', 'w', 'h'])
    write_region(out_dir, grey, cfg, used, region_image)
    w('labels.tsv', tiles, ['sid', 'sign', 'family'])
    w('clusters.tsv', tiles, ['sid', 'cluster', 'col', 'dx'])
    with open(out_dir / 'focus.tsv', 'w') as o: o.writelines(f'{s}\t{q}\n' for s, q in focus)
    with open(out_dir / 'fit_recut.tsv', 'w') as o:
        o.write('page\ttiles\tcolumns\tclear\n'); o.writelines(f'{p}\t{b}\t{c}\t{k}\n' for p, b, c, k in stats)
    nclear = sum(s[3] for s in stats)
    print(len(tiles), 'tiles;', nclear, 'aligned to a reader column within', cfg.clear, 'px;',
          len(set(t['sign'] for t in tiles)), 'piles;', len(focus), 'focus')
    return tiles, stats


def small_pile(sorter_dir, labels_in='labels.tsv', labels_out='labels_small.tsv', min_h=18, min_ink=60, focus=None):
    """Put tiny tiles (under min_h px tall or under min_ink ink pixels; ink = darker than the strip's 8th percentile + 20)
    in one pile, SMALL; every other tile keeps its label. With focus='focus.tsv', SMALL tiles are dropped from that focus
    file (rewritten in place): the owner settles SMALL in one go, not one by one. Returns the number of small tiles."""
    H = Path(sorter_dir)
    rows = list(csv.DictReader(open(H / 'signs.tsv'), delimiter='\t')); pg = {}; small = set()
    for r in rows:
        p = pg.setdefault(r['page'], np.array(Image.open(H / 'pages' / f"{r['page']}.jpg").convert('L')))
        x, y, w, h = (int(r[k]) for k in ('x', 'y', 'w', 'h')); thr = np.percentile(p, 8) + 20
        if h < min_h or int((p[y:y + h, x:x + w] < thr).sum()) < min_ink: small.add(r['sid'])
    lab = list(csv.DictReader(open(H / labels_in), delimiter='\t'))
    for r in lab:
        if r['sid'] in small: r['sign'], r['family'] = 'SMALL', 'SMALL'
    with open(H / labels_out, 'w', newline='') as f:
        wr = csv.DictWriter(f, fieldnames=list(lab[0].keys()), delimiter='\t', lineterminator='\n'); wr.writeheader(); wr.writerows(lab)
    if focus:
        fl = [l for l in open(H / focus) if l.strip() and l.split('\t', 1)[0] not in small]
        with open(H / focus, 'w') as o: o.writelines(fl)
    print('small tiles', len(small), 'of', len(rows))
    return len(small)
