#!/usr/bin/env python3
"""PIS-RECUT (4 Oct 2026): re-cut the f.75r sorter so that ONE TILE = ONE SIGN, on straight (deskewed) line strips.

Owner, on the v2 page: many tiles straddled two signs or cut one in half (f75_L08_02 = looped l + the b beside it), because
build_inputs.py fitted ink-profile blobs to the readers' column COUNT; and the lines slope ~160 px across the region, so the
context strip showed the line above. tighten_tiles.py trimmed only vertically. This script replaces both for the page.

  python3 ciphers/fr16045-pisany-rome-1585/sorter/recut.py [--debug DIR]
  writes sorter/pages/f75_L<nn>.jpg (deskewed), signs.tsv, labels.tsv, focus.tsv, fit_recut.tsv, clusters.tsv
  (the v2 cut is kept for the record as signs_v2.tsv / signs_tight_v2.tsv / labels_v2.tsv / focus_v2.tsv)

1. Deskew. Per line, build_inputs.traces() gives the line centre y(x) on the Gallica region already on disk. Each column x
   of the region is shifted so that y(x) lands on the strip's middle row (a shear; the slope is ~3 degrees, so a shear is
   indistinguishable from a rotation at this size). Every strip is the full region width and HALF px either side of the
   centre, so the sorter's context view (lines above and below at the same x window) shows straight, neighbouring lines.
2. Segment by the sign's own ink: background-normalised binarisation (pixel < REL x grey closing), 8-connected components
   on the strip +- one pitch. A component belongs to this line if its median row is within OWN x pitch of the centre and it
   has ink within CORE x pitch of it (crosses and descenders of the lines above/below fail one test or the other).
   Components whose x-ranges overlap by more than half of the narrower are one sign (two strokes, dots above). Small
   marks (longer side < DOT x pitch) with no overlap stay their own tile (the owner merges fast; a dot sign is possible).
   A group wider than SPLIT x the line's median sign width is cut into round(width / median) pieces at the column-ink
   minima nearest the equal-width cut points (touching signs: q q, b e x).
3. Starting piles, value-blind. Columns of tx/ciphertext_draft.tsv (pass A vs pass B) carry the v2 tile's x centre as a
   position estimate; tiles and columns are aligned in x order by dynamic programming (cost |dx|, skip cost SKIP px).
   A tile matched within CLEAR px takes that column's pile (same naming as build_inputs.py: S15, S10/S41, S21+1r,
   split-rare, one-reader, NOCELL). Every other tile goes to the pile its shape cluster (k-means on 32x32 bitmaps + aspect,
   NCLU clusters over the page) mostly holds among the clear tiles, and is a focus candidate. Focus (<= 40): unclear
   tiles ranked by their cluster's size (frequent shapes first), at most PER_CLU per cluster.
"""
import argparse, csv, shutil, sys
from collections import Counter, defaultdict
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage as ndi
from sklearn.cluster import KMeans

S = Path(__file__).resolve().parent; T = S.parent; P = S / 'pages'
sys.path.insert(0, str(S))
import build_inputs as bi  # noqa: E402  (traces(), norm(), PITCH, the region image)

HALF = 120; REL = 0.72; OWN = 0.50; CORE = 0.30; DOT = 0.14; SPLIT = 1.45; SKIP = 45; CLEAR = 30; MERGE = 0.6; NCLU = 60
PER_CLU = 2; RECENTRE = 60; NFOCUS = 40; MINPAIR = 4


def deskew(grey, tr):
    """Column-wise shear: out[r, x] = grey[round(tr[x]) - HALF2 + r, x], HALF2 = one pitch (labelling margin)."""
    H, W = grey.shape; h2 = bi.PITCH; out = np.full((2 * h2 + 1, W), 255, np.uint8)
    for x in range(W):
        c = int(round(tr[x])); lo, hi = c - h2, c + h2 + 1
        a, b = max(0, lo), min(H, hi)
        out[a - lo:b - lo, x] = grey[a:b, x]
    return out


def recentre(grey, tr):
    """The v2 traces sit up to ~50 px off the line on some strips (L08). On the deskewed strip, per 300 px window (step 150)
    the smoothed row-ink peak within +-RECENTRE px of the middle row gives a correction; median over five windows."""
    st = deskew(grey, tr); c = bi.PITCH; W = st.shape[1]
    bg = ndi.grey_closing(st, size=(31, 31)).astype(float) + 1; ink = st < REL * bg
    xs = list(range(0, W - 150, 150)); d = []
    for x in xs:
        pr = bi.smooth(ink[:, x:x + 300].sum(1), 31)[c - RECENTRE:c + RECENTRE + 1]
        d.append(int(np.argmax(pr)) - RECENTRE if pr.max() > 0 else 0)
    d = np.array(d, float); d = np.array([np.median(d[max(0, i - 2):i + 3]) for i in range(len(d))])
    return tr + np.interp(np.arange(W), [x + 150 for x in xs], d)


def segment(strip):
    """Sign boxes (x0, y0, x1, y1) in strip coords, centre row = PITCH."""
    p = bi.PITCH; c = p
    bg = ndi.grey_closing(strip, size=(31, 31)).astype(float) + 1
    ink = strip < REL * bg
    ink[:, :15] = False; ink[:, 2870:] = False       # the scan's dark right edge starts at x ~2880 (build_inputs.blobs)
    lab, n = ndi.label(ink, structure=np.ones((3, 3)))
    comps = []
    for i, sl in enumerate(ndi.find_objects(lab), 1):
        ys, xs = np.nonzero(lab[sl] == i); ys = ys + sl[0].start; xs = xs + sl[1].start
        if len(ys) < 25: continue
        if abs(np.median(ys) - c) > OWN * p: continue
        if np.abs(ys - c).min() > CORE * p: continue
        comps.append([xs.min(), ys.min(), xs.max(), ys.max(), len(ys)])
    comps.sort()
    # merge x-overlapping components (a sign in two strokes, a dot above a sign)
    groups = []                                      # union-find on component pairs, never on a grown group's span
    par = list(range(len(comps)))
    def root(i):
        while par[i] != i: i = par[i]
        return i
    for i, b in enumerate(comps):
        for j in range(i):
            g = comps[j]; ov = min(g[2], b[2]) - max(g[0], b[0])
            if ov > MERGE * min(g[2] - g[0] + 1, b[2] - b[0] + 1): par[root(i)] = root(j)
    gs = defaultdict(list)
    for i, b in enumerate(comps): gs[root(i)].append(b)
    for v in gs.values():
        groups.append([min(b[0] for b in v), min(b[1] for b in v), max(b[2] for b in v), max(b[3] for b in v), sum(b[4] for b in v)])
    groups.sort()
    big = [g for g in groups if max(g[2] - g[0], g[3] - g[1]) >= DOT * p]
    wmed = float(np.median([g[2] - g[0] + 1 for g in big])) if big else 40.0
    prof = ndi.uniform_filter1d((ink & (np.abs(np.arange(ink.shape[0])[:, None] - c) < CORE * p)).sum(0).astype(float), 5)
    out = []
    for g in groups:
        w = g[2] - g[0] + 1
        if w <= SPLIT * wmed:
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


def align(tx, cx):
    """Monotone DP: tiles at tx, columns at cx (both sorted). Returns {tile index: column index}."""
    n, m = len(tx), len(cx); D = np.full((n + 1, m + 1), 1e18); B = np.zeros((n + 1, m + 1), int)
    D[0, :] = np.arange(m + 1) * SKIP; D[:, 0] = np.arange(n + 1) * SKIP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            opts = (D[i - 1, j - 1] + abs(tx[i - 1] - cx[j - 1]), D[i - 1, j] + SKIP, D[i, j - 1] + SKIP)
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


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    for f in ('signs', 'signs_tight', 'labels', 'focus'):          # the v2 cut, kept for the record (once)
        src, dst = S / f'{f}.tsv', S / f'{f}_v2.tsv'
        if src.exists() and not dst.exists(): shutil.copy(src, dst)
    v2 = defaultdict(list)
    for r in csv.DictReader(open(S / 'signs_v2.tsv'), delimiter='\t'):
        v2[r['page']].append(int(r['x']) + int(r['w']) / 2)
    draft = defaultdict(list)
    for r in csv.DictReader(open(T / 'tx' / 'ciphertext_draft.tsv'), delimiter='\t'):
        A = bi.norm(r['sign']) or 'UNREAD'
        if r['why'] == 'agree': draft[r['line']].append(('agree', A, A)); continue
        who, other = r['alt'].split(':', 1); other = bi.norm(other) or 'UNREAD'
        x, y = (A, other) if who == 'B' else (other, A)
        draft[r['line']].append(('gap' if r['why'] == 'gap' else 'differ', x, y))
    pairs = Counter((A, B) for v in draft.values() for k, A, B in v if k == 'differ')
    ones = Counter((A if A != '-' else B) for v in draft.values() for k, A, B in v if k == 'gap')

    def pile(kind, A, B):
        if kind == 'agree': return A, A
        if kind == 'differ': return (f'{A}/{B}' if pairs[(A, B)] >= MINPAIR else 'split-rare'), A
        one = A if A != '-' else B
        return (f'{one}+1r' if ones[one] >= MINPAIR else 'one-reader'), one

    grey = np.array(bi.src); tiles, stats, bms = [], [], []
    for n, tr in enumerate(bi.traces(), 1):
        page, line = f'f75_L{n:02d}', f'L{n:02d}'
        tr = recentre(grey, tr); strip = deskew(grey, tr); boxes, wmed = segment(strip)
        off = bi.PITCH - HALF                                        # strip row -> page row
        Image.fromarray(strip[off:off + 2 * HALF + 1]).save(P / f'{page}.jpg', quality=82)
        cols = draft[line]; cx = v2[page][:len(cols)]
        txs = [(b[0] + b[2]) / 2 for b in boxes]; m = align(txs, cx)
        stats.append((page, len(boxes), len(cols), sum(1 for i in m if abs(txs[i] - cx[m[i]]) <= CLEAR)))
        for k, (x0, y0, x1, y1) in enumerate(boxes, 1):
            y0p, y1p = max(0, y0 - off), min(2 * HALF, y1 - off)
            sid = f'{page}_{k:02d}'; j = m.get(k - 1); clear = j is not None and abs(txs[k - 1] - cx[j]) <= CLEAR
            lab, fam = pile(*cols[j]) if clear else (None, None)
            tiles.append(dict(sid=sid, page=page, x=int(x0), y=int(y0p), w=int(x1 - x0 + 1), h=int(y1p - y0p + 1),
                              sign=lab, family=fam, col=(j + 1 if j is not None else ''), dx=(round(abs(txs[k - 1] - cx[j])) if j is not None else ''),
                              colpile=(pile(*cols[j])[0] if j is not None else '')))
            bg = ndi.grey_closing(strip[y0:y1 + 1, x0:x1 + 1], size=(15, 15)).astype(float) + 1
            g = strip[y0:y1 + 1, x0:x1 + 1]; aspect = (x1 - x0 + 1) / (y1 - y0 + 1)
            bms.append(np.r_[bitmap(g < REL * np.maximum(bg, g.max() * .9)).ravel(), [np.log(aspect) * 2, np.log((y1 - y0 + 1) / bi.PITCH)]])
        if a.debug:
            im = Image.fromarray(strip[off:off + 2 * HALF + 1]).convert('RGB'); d = ImageDraw.Draw(im)
            for k, (x0, y0, x1, y1) in enumerate(boxes, 1):
                d.rectangle((x0, y0 - off, x1, y1 - off), outline=(255, 0, 0) if k % 2 else (0, 0, 255), width=2)
                d.text((x0, 2 * HALF - 14), str(k), fill=(200, 0, 0))
            Path(a.debug).mkdir(parents=True, exist_ok=True); im.save(Path(a.debug) / f'debug_{page}.jpg', quality=80)
    X = np.array(bms); km = KMeans(NCLU, n_init=4, random_state=0).fit(X); cl = km.labels_
    dist = np.linalg.norm(X - km.cluster_centers_[cl], axis=1)
    major = {}
    for c in range(NCLU):
        cnt = Counter(t['sign'] for t, k in zip(tiles, cl) if k == c and t['sign'])
        major[c] = cnt.most_common(1)[0][0] if cnt else None
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
        if per[c] >= PER_CLU: continue
        per[c] += 1
        near = f"nearest reader column {t['col']} ({t['colpile']}, {t['dx']} px off)" if t['col'] else 'no reader column near it'
        focus.append((t['sid'], f"{t['sid'].split('_', 1)[1]}: cut from the ink, {near}; started in {t['sign']} by shape "
                                f"(a shape seen {size[c]} times on the page). Right pile, another sign, or a bad cut?"))
        if len(focus) >= NFOCUS: break
    w = lambda name, rows, keys: (lambda o: (o.write('\t'.join(keys) + '\n'), o.writelines('\t'.join(str(r[k]) for k in keys) + '\n' for r in rows)))(open(S / name, 'w'))
    w('signs.tsv', tiles, ['sid', 'page', 'x', 'y', 'w', 'h'])
    w('labels.tsv', tiles, ['sid', 'sign', 'family'])
    w('clusters.tsv', tiles, ['sid', 'cluster', 'col', 'dx'])
    with open(S / 'focus.tsv', 'w') as o: o.writelines(f'{s}\t{q}\n' for s, q in focus)
    with open(S / 'fit_recut.tsv', 'w') as o:
        o.write('page\ttiles\tcolumns\tclear\n'); o.writelines(f'{p}\t{b}\t{c}\t{k}\n' for p, b, c, k in stats)
    nclear = sum(s[3] for s in stats)
    print(len(tiles), 'tiles;', nclear, 'aligned to a reader column within', CLEAR, 'px;', len(set(t['sign'] for t in tiles)), 'piles;', len(focus), 'focus')


if __name__ == '__main__':
    main()
