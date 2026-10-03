# GAPS25-na-suriname-map-1781 (account-4), 3 Oct 2026: place every 2077 legend token on a sign-level ink box.
# Input: the line strips cut by tools/iiif_lines.py --image (passes/signcmp_gaps25/strips/s77_Lnn.jpg, box in strips/manifest.json)
# and ciphertext_2077_legend.tsv. Ink pieces = connected components (scipy) merged when they overlap in x; tokens are laid on
# the pieces by a width DP (cipher sign 1 unit, [dot] 0.25, plain word 0.75 per letter). Output boxes.tsv (line, pos, sign,
# piece box in native 2077_legend_native.jpg pixels) and an overlay per line for the worker's own location check.
# No values, no decode: only reader codes and positions. Usage: python3 passes/signcmp_gaps25/locate.py
import csv, json, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
D = 'passes/signcmp_gaps25/'
man = {e['crop']: e for e in json.load(open(D + 'strips/manifest.json'))['iiif_lines']}
toks = {}
for r in csv.reader((l for l in open('ciphertext_2077_legend.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] == 'line': continue
    toks.setdefault(r[0], []).append((int(r[1]), r[2]))
def exp(s):
    if s.startswith('w:'): return 0.75 * len(s[2:])
    if s == '[dot]': return 0.25
    return 1.0
def pieces(im):
    # column-profile pieces: a column is ink when more than MINK core-row pixels are dark, so a thin ruled diagonal
    # (2-4 px per column) does not join its neighbours; runs of ink columns are pieces, y extent from the dark mask.
    g = np.asarray(im.convert('L')).astype(float)
    h = g.shape[0]
    thr = min(np.percentile(g, 50) - 45, g.mean() - 2.0 * g.std())
    m = g < thr
    core = m[int(h * 0.22):int(h * 0.82)]
    col = core.sum(0)
    ink = col > 5
    out = []; x = 0; W = len(ink)
    while x < W:
        if ink[x]:
            x0 = x
            while x < W and ink[x]: x += 1
            if x - x0 >= 3:
                ys = np.where(m[:, x0:x].any(1))[0]
                out.append([x0, int(ys.min()), x, int(ys.max()) + 1])
        else: x += 1
    return out
def align(T, P):
    e = [exp(s) for _, s in T]; w = [p[2] - p[0] for p in P]
    u = sum(w) / max(sum(e), 1e-6)
    n, m = len(T), len(P); INF = 1e18
    C = np.full((n + 1, m + 1), INF); B = {}
    C[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c0 = C[i][j]
            if c0 >= INF: continue
            if j < m and C[i][j + 1] > c0 + 0.8:  # skip a piece (noise)
                C[i][j + 1] = c0 + 0.8; B[(i, j + 1)] = (i, j, 'skip')
            if i < n and C[i + 1][j] > c0 + 1.5:  # token with no piece
                C[i + 1][j] = c0 + 1.5; B[(i + 1, j)] = (i, j, 'none')
            for k in (1, 2, 3):
                if i < n and j + k <= m:
                    ww = P[j + k - 1][2] - P[j][0]
                    cost = c0 + abs(ww - e[i] * u) / u + 0.3 * (k - 1)
                    if cost < C[i + 1][j + k]: C[i + 1][j + k] = cost; B[(i + 1, j + k)] = (i, j, 'k')
            if i + 1 < n and j < m:  # two touching tokens in one piece
                cost = c0 + abs(w[j] - (e[i] + e[i + 1]) * u) / u + 0.6
                if cost < C[i + 2][j + 1]: C[i + 2][j + 1] = cost; B[(i + 2, j + 1)] = (i, j, 'pair')
    res = {}; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, t = B[(i, j)]
        if t == 'k':
            res[pi] = ('one' if j - pj == 1 else 'split%d' % (j - pj), [P[pj][0], min(p[1] for p in P[pj:j]), P[j - 1][2], max(p[3] for p in P[pj:j])])
        elif t == 'pair':
            for q, half in ((pi, 0), (pi + 1, 1)):
                x0, y0, x1, y1 = P[pj]; mid = (x0 + x1) // 2
                res[q] = ('pair', [x0, y0, mid, y1] if half == 0 else [mid, y0, x1, y1])
        elif t == 'none': res[pi] = ('none', None)
        i, j = pi, pj
    return res, C[n][m] / max(n, 1)
if __name__ == '__main__':
    out = open(D + 'boxes.tsv', 'w'); out.write('line\tpos\tsign\tfit\tx0\ty0\tx1\ty1\n')
    for L in sorted(toks):
        crop = 's77_%s.jpg' % L.split('_')[1]
        e = man[crop]; bx = e['box']; im = Image.open(D + 'strips/' + crop)
        P = pieces(im); T = toks[L]
        res, q = align(T, P)
        ov = im.convert('RGB'); d = ImageDraw.Draw(ov)
        for idx, (pos, s) in enumerate(T):
            f, b = res.get(idx, ('none', None))
            if b is None: out.write(f'{L}\t{pos}\t{s}\t{f}\t\t\t\t\n'); continue
            out.write(f'{L}\t{pos}\t{s}\t{f}\t{b[0]+bx[0]}\t{b[1]+bx[1]}\t{b[2]+bx[0]}\t{b[3]+bx[1]}\n')
            d.rectangle(b, outline=(255, 0, 0)); d.text((b[0], 2), str(pos), fill=(0, 0, 255))
        ov.save(D + 'overlay/%s.jpg' % L, quality=80)
        print(L, 'tokens', len(T), 'pieces', len(P), 'cost/token %.2f' % q, file=sys.stderr)
