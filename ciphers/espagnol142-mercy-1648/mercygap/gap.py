"""MERCY-GAP (17 Oct 2026): pixel gap between adjacent digits on f22r r16-r24, aligned to ciphertext.tsv.

Ink runs (seg.py) are aligned to the row's digit string by DP: one run = 1-3 digits (touching digits), two runs = one digit
(a broken stroke), or a run under 10 px skipped (a dot). Gap between consecutive digits: white columns between their runs,
0 if they share a run. Normalized by the row's median single-digit run width (digits other than 1). Writes mercygap/gaps.tsv.
"""
import sys, numpy as np
from PIL import Image
sys.path.insert(0, __file__.rsplit('/', 1)[0]); import seg

def wexp(d): return 20.0 if d == '1' else 45.0

def align(runs, ds):
    R, N = len(runs), len(ds); INF = 1e18
    C = np.full((R + 1, N + 1), INF); B = {}; C[0, 0] = 0
    for i in range(R + 1):
        for j in range(N + 1):
            c = C[i, j]
            if c >= INF: continue
            if i < R and runs[i][1] - runs[i][0] < 10:              # skip a dot
                if c + 0.5 < C[i + 1, j]: C[i + 1, j] = c + 0.5; B[(i + 1, j)] = (i, j, 'skip')
            for k in (1, 2, 3):                                       # one run, k digits
                if i < R and j + k <= N:
                    w = runs[i][1] - runs[i][0]; e = sum(wexp(d) for d in ds[j:j + k])
                    cc = c + ((w - e) / e) ** 2 * 4 + (k - 1) * 0.3
                    if cc < C[i + 1, j + k]: C[i + 1, j + k] = cc; B[(i + 1, j + k)] = (i, j, 'k%d' % k)
            if i + 1 < R and j < N:                                   # two runs, one digit
                w = runs[i + 1][1] - runs[i][0]; e = wexp(ds[j])
                gap = runs[i + 1][0] - runs[i][1]
                cc = c + ((w - e) / e) ** 2 * 4 + 1.0 + (gap / 10.0) ** 2
                if cc < C[i + 2, j + 1]: C[i + 2, j + 1] = cc; B[(i + 2, j + 1)] = (i, j, 'split')
    # path
    i, j = R, N; path = []
    if C[R, N] >= INF: return None, INF
    while (i, j) != (0, 0):
        pi, pj, op = B[(i, j)]; path.append((pi, i, pj, j, op)); i, j = pi, pj
    return path[::-1], C[R, N]

def row_gaps(page, row, box):
    runs = seg.runs(page, box); toks = seg.digits(row)
    ds = ''.join(s for _, s in toks)
    owner = []                                   # digit index -> (token pos, digit idx in token)
    for pos, s in toks:
        for k in range(len(s)): owner.append((pos, k))
    path, cost = align(runs, ds)
    span = [None] * len(ds); runid = [None] * len(ds)
    for ri, ri2, dj, dj2, op in path:
        if op == 'skip': continue
        for d in range(dj, dj2): span[d] = (runs[ri][0], runs[ri2 - 1][1]); runid[d] = ri
    single = [span[d][1] - span[d][0] for ri, ri2, dj, dj2, op in path if op == 'k1' for d in [dj] if ds[d] != '1']
    med = float(np.median(single))
    out = []
    for d in range(len(ds) - 1):
        g = 0 if runid[d] == runid[d + 1] else span[d + 1][0] - span[d][1]
        (p1, k1), (p2, k2) = owner[d], owner[d + 1]
        kind = 'intra' if p1 == p2 else 'between'
        out.append((row, p1, p2, ds[d], ds[d + 1], kind, g, round(g / med, 3), round(med, 1)))
    return out, cost, len(runs), len(ds)

if __name__ == '__main__':
    page = np.asarray(Image.open(seg.D + 'images/f22r_canvas58.jpg').convert('L'))
    allg = []
    for row, box in zip(seg.ROWS, seg.bands()):
        g, cost, nr, nd = row_gaps(page, row, box); allg += g
        print(row, 'runs', nr, 'digits', nd, 'align cost %.2f' % cost, file=sys.stderr)
    with open(seg.D + 'mercygap/gaps.tsv', 'w') as f:
        f.write('row\tpos1\tpos2\td1\td2\tkind\tgap_px\tg_norm\tmed_w\n')
        for r in allg: f.write('\t'.join(map(str, r)) + '\n')
