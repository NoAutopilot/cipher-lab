#!/usr/bin/env python3
"""C1161-275 (15 Oct 2026): place every S token by counting signs on the line strip against the line's own ciphertext.tsv sequence.
Ink connected components on a tracked writing band are grouped into blobs; the blobs are aligned to the sign sequence by dynamic programming
(1:1, two signs in one blob, one sign over two blobs, skipped blob, missed sign), with expected widths per label re-estimated from the
alignments. Labels are used to count and for widths only. The line's own strip and the previous line's strip are both tried (c185R_L23
sits on c185R_L22's strip); the lower mean cost wins.
python3 s275/count_locate.py            -> s275/positions.tsv (all S tokens) and s275/L1_check.txt (hand-counted recut/positions.tsv)"""
import collections, csv, math, os, statistics, sys
import numpy as np
from scipy import ndimage
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools')); import lookalike_pass as LP
build = LP._line_strips(os.path.join(T, 'la', 'crops', 'manifest.json'), '', '{line}_s*')
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
seq = collections.defaultdict(list)
for r in rows:
    seq[r['line']].append(r['sign'])
lines = list(seq)
_cache = {}


def strip(ln):
    if ln not in _cache:
        try:
            _cache[ln] = np.array(build(ln))
        except SystemExit:
            _cache[ln] = None
    return _cache[ln]


def comps(A, ink=110):
    dead = (A < 40).mean(0) > 0.6
    I = (A < ink) & ~dead[None, :]
    lab, n = ndimage.label(I, structure=np.ones((3, 3)))
    out = []
    for k, sl in enumerate(ndimage.find_objects(lab), 1):
        ys, xs = sl
        area = int((lab[sl] == k).sum())
        if area < 25:
            continue
        out.append((xs.start, xs.stop, ys.start, ys.stop, area))
    return I, out


def band_candidates(I, k=3):
    prof = np.convolve(I.sum(1).astype(float), np.ones(41) / 41, 'same')
    cs = []
    for y in np.argsort(-prof):
        if y < 25 or y > len(prof) - 25:
            continue
        if all(abs(y - c) > 70 for c in cs):
            cs.append(int(y))
        if len(cs) >= k:
            break
    return cs


def track(C, c, half=38):
    """components whose box meets the band around a running centre, left to right; returns blobs (x0, x1, yc)."""
    acc, base = [], float(c)
    for x0, x1, y0, y1, a in sorted(C):
        if y1 < base - half or y0 > base + half or (y1 - y0) > 220:
            continue
        acc.append([x0, x1, (y0 + y1) / 2])
        base = 0.85 * base + 0.15 * min(max((y0 + y1) / 2, base - 20), base + 20)
    blobs = []
    for x0, x1, yc in acc:
        if blobs and x0 <= blobs[-1][1] + 3:
            b = blobs[-1]; b[1] = max(b[1], x1); b[2] = (b[2] + yc) / 2
        else:
            blobs.append([x0, x1, yc])
    return [b for b in blobs if b[1] - b[0] >= 5]


def align(signs, blobs, ew):
    n, m = len(signs), len(blobs)
    INF = 1e18
    w = lambda s: ew.get(s, ew['_'])
    def wc(i0, i1, j0, j1):  # signs i0..i1-1 on blobs j0..j1-1
        width = blobs[j1 - 1][1] - blobs[j0][0]
        exp = sum(w(s) for s in signs[i0:i1])
        return math.log(max(width, 3) / exp) ** 2
    D = np.full((n + 1, m + 1), INF); B = {}
    D[0, :] = [1.5 * j for j in range(m + 1)]  # leading noise blobs
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i, j] >= INF:
                continue
            d = D[i, j]
            moves = []
            if i < n and j < m: moves.append((1, 1, wc(i, i + 1, j, j + 1)))
            if i + 1 < n and j < m: moves.append((2, 1, 1.2 + wc(i, i + 2, j, j + 1)))
            if i < n and j + 1 < m: moves.append((1, 2, 1.0 + wc(i, i + 1, j, j + 2)))
            if j < m: moves.append((0, 1, 1.5))
            if i < n: moves.append((1, 0, 3.0))
            for di, dj, cst in moves:
                if d + cst < D[i + di, j + dj]:
                    D[i + di, j + dj] = d + cst; B[(i + di, j + dj)] = (i, j)
    # trailing blobs free-ish
    jend = min(range(m + 1), key=lambda j: D[n, j] + 1.5 * (m - j))
    cost = D[n, jend] + 1.5 * (m - jend)
    path, cur = [], (n, jend)
    while cur != (0, 0) and cur in B:
        prv = B[cur]; path.append((prv, cur)); cur = prv
    path.reverse()
    place = {}
    for (i0, j0), (i1, j1) in path:
        for i in range(i0, i1):
            if j1 > j0:
                x0, x1 = blobs[j0][0], blobs[j1 - 1][1]
                if i1 - i0 == 2:  # two signs in one blob: split by expected width
                    a, b = w(signs[i0]), w(signs[i0 + 1]); cut = x0 + (x1 - x0) * a / (a + b)
                    x0, x1 = (x0, cut) if i == i0 else (cut, x1)
                place[i] = (x0, x1, blobs[j0][2], (i1 - i0, j1 - j0))
            else:
                place[i] = None
    return cost / max(1, n), place


import json as _json
_Y0 = {}
for _e in _json.load(open(os.path.join(T, 'la', 'crops', 'manifest.json')))['iiif_lines']:
    _ln = _e['crop'][:9]
    if _e.get('box'):
        _Y0[_ln] = min(_Y0.get(_ln, 10 ** 9), _e['box'][1])
for _ln in lines:  # c188L crops carry no box: line index x 150 px as the page-y proxy
    _Y0.setdefault(_ln, 150 * int(_ln.split('_L')[1]))


def cands(ln, ew):
    """every (page y, cost, strip, band c, placement, blobs) for LN on its own, previous and next strip."""
    k = lines.index(ln); out = []
    for sl in [lines[j] for j in (k - 1, k, k + 1) if 0 <= j < len(lines) and lines[j][:5] == ln[:5]]:
        A = strip(sl)
        if A is None:
            continue
        I, C = comps(A)
        for c in band_candidates(I, 4):
            bl = track(C, c)
            if len(bl) < 0.4 * len(seq[ln]):
                continue
            cost, place = align(seq[ln], bl, ew)
            out.append((_Y0[sl] + c, cost, sl, c, place, bl))
    return out


def fit_block(blk, ew):
    """one band per line, page y strictly increasing by >= 60 px down the block (no two lines on one written line): DP over lines."""
    L = [ln for ln in lines if ln[:5] == blk]
    C = [cands(ln, ew) for ln in L]
    INF = 1e18; best = [dict() for _ in L]
    for i, cs in enumerate(C):
        for a, ca in enumerate(cs):
            if i == 0 or not best[i - 1]:
                best[i][a] = (ca[1], None); continue
            opts = [(bv[0] + ca[1], b) for b, bv in best[i - 1].items() if ca[0] - C[i - 1][b][0] >= 60]
            if opts:
                best[i][a] = min(opts)
            else:
                best[i][a] = (min(bv[0] for bv in best[i - 1].values()) + ca[1] + 5.0, min(best[i - 1], key=lambda b: best[i - 1][b][0]))
    res = {}
    a = min(best[-1], key=lambda a: best[-1][a][0]) if best[-1] else None
    for i in range(len(L) - 1, -1, -1):
        if a is None:
            res[L[i]] = None; continue
        y, cost, sl, c, place, bl = C[i][a]
        res[L[i]] = (cost, sl, c, place, bl)
        a = best[i][a][1]
    return res


def estimate(fits):
    obs = collections.defaultdict(list)
    for ln, f in fits.items():
        if f is None:
            continue
        for i, p in f[3].items():
            if p and p[3] == (1, 1):
                obs[seq[ln][i]].append(p[1] - p[0])
    allw = [v for vs in obs.values() for v in vs]
    ew = {'_': statistics.median(allw)}
    for s, vs in obs.items():
        if len(vs) >= 3:
            ew[s] = statistics.median(vs)
    return ew


def run():
    Sl = [ln for ln in lines if 'S' in seq[ln]]
    ew = {'_': 60.0}
    for s in seq:
        pass
    for s in {x for l in seq.values() for x in l if x.startswith('[PLAIN')}:
        ew[s] = 240.0
    fits = {}
    for it in range(3):
        fits = {}
        for blk in sorted({ln[:5] for ln in lines}):
            fits.update(fit_block(blk, ew))
        ew2 = estimate(fits)
        for s in ew:
            if s.startswith('[PLAIN') and s not in ew2:
                ew2[s] = 240.0
        ew = ew2
        print('iter', it, 'mean cost', round(statistics.mean(f[0] for f in fits.values() if f), 3), file=sys.stderr)
    with open(os.path.join(H, 'positions.tsv'), 'w') as f:
        f.write('line\tpos\tstrip\tx\tc\tpitch\tline_cost\tmove\tflag\n')
        for ln in Sl:
            fb = fits[ln]
            if fb is None:
                print('no fit', ln, file=sys.stderr); continue
            cost, sl, c, place, bl = fb
            span = [p for p in place.values() if p]
            pitch = (max(p[1] for p in span) - min(p[0] for p in span)) / len(seq[ln])
            for i, s in enumerate(seq[ln]):
                if s != 'S':
                    continue
                p = place.get(i)
                if p is None:  # missed sign: interpolate between neighbours
                    L = [place[k] for k in range(i - 1, -1, -1) if place.get(k)][:1]
                    R = [place[k] for k in range(i + 1, len(seq[ln])) if place.get(k)][:1]
                    x = int(((L[0][1] if L else R[0][0] - pitch) + (R[0][0] if R else L[0][1] + pitch)) / 2); yc = c; mv = 'miss'
                else:
                    x = int((p[0] + p[1]) / 2); yc = p[2]; mv = f'{p[3][0]}:{p[3][1]}'
                flag = 'poor' if cost > 0.6 or mv != '1:1' else ''
                f.write(f'{ln}\t{i + 1}\t{sl}\t{x}\t{int(yc)}\t{pitch:.1f}\t{cost:.3f}\t{mv}\t{flag}\n')
    return fits


if __name__ == '__main__':
    run()
    P = {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(H, 'positions.tsv')), delimiter='\t')}
    out, ok = [], 0
    for r in csv.DictReader(open(os.path.join(T, 'recut', 'positions.tsv')), delimiter='\t'):
        q = P[(r['line'], r['pos'])]
        good = q['strip'] == r['strip'] and abs(int(q['x']) - int(r['x'])) <= 0.5 * float(q['pitch'])
        ok += good
        out.append(f"{r['line']}/{r['pos']} hand {r['strip']} x{r['x']}  count {q['strip']} x{q['x']} pitch {q['pitch']} -> {'ok' if good else 'MISS'}")
    out.append(f'L1: {ok}/6 within 0.5 pitch -> {"PASS" if ok >= 5 else "FAIL"}')
    open(os.path.join(H, 'L1_check.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
