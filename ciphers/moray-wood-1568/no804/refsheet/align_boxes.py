"""RUN1-MOR (account 1, 4 Oct 2026): map the 134 glyph positions of ciphertext.tsv onto the GAPS5 column segments
(images/pairs_glyph_boxes_2026-10-02.json) with no vision call, so the no.804 labelling reference sheet can be cut by
script. Dynamic programming per line over the segments: one glyph = one segment, one glyph = two adjacent segments
(over-split), two glyphs = one segment cut at its midpoint (merged); a '|' row consumes no segment and is rewarded when
it sits on a wide inter-segment gap. Costs are in units of the line's median segment width (scale-free).
Validated against the 32 position->segment pairs GAPS5 fixed by eye against its numbered overlay
(images/pairs_sheets_2026-10-02.py, which numbers glyphs per line without the '|' rows); the agreement count is printed and written to the output header.
The anchors are hard constraints by default (penalty 5.0 per miss); --free runs without them and is the validation
figure (26/32 on 4 Oct 2026: the free DP drifts by one or two segments late in L1 and L3, where GAPS5 found merged cuts).
--eye (RUN4-MOR, 4 Oct 2026) adds the eye anchors read on the full-size P4 (sha1 a4e84895...) at the line ends and at the
boxes RUN3-MOR flagged (no804/refsheet/eyecheck.tsv); they override GAPS5's where both exist (two cases, both boxes RUN3-MOR
flagged wrong/clipped: GAPS5 'L1.14' 14 -- seg 13 is o+x merged, seg 14 the loop of M; GAPS5 'L1.38' (40,'L') -- seg 38 is r+A
merged, seg 39 the slashed z (Z5), seg 40 the whole M), and two eye-set boxes replace the DP box
where the GAPS5 segmentation cut a glyph in two (L2.21 P / L2.22 N). L3 segments 39-44 are fold shadow and stay unmatched.
--m-left PX (default 0) widens every M box leftward by PX, for the loop of M when it sits in the preceding segment.
usage: python3 align_boxes.py [--free] [--eye] [--m-left PX] > boxes.tsv"""
import json, statistics, os
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
G = json.load(open(f'{D}/images/pairs_glyph_boxes_2026-10-02.json'))
rows = [l.rstrip('\n').split('\t') for l in open(f'{D}/ciphertext.tsv') if not l.startswith('#')][1:]
# GAPS5 eye-fixed anchors (position -> 1-based segment, or (segment, half) for a merged segment)
ANCH = {'L1.5': 5, 'L1.8': 8, 'L1.10': 10, 'L1.11': 11, 'L1.14': 14, 'L1.17': 17, 'L1.18': 18, 'L1.20': 20, 'L1.23': 23,
        'L1.25': 25, 'L1.27': 27, 'L1.30': 32, 'L1.31': 33, 'L1.34': 36, 'L1.38': (40, 'L'), 'L1.40': 41, 'L1.41': 42,
        'L1.44': 45, 'L2.30': 29, 'L3.3': 3, 'L3.4': 4, 'L3.7': 7, 'L3.14': 15, 'L3.25': 26, 'L3.27': 28, 'L3.28': 29,
        'L3.30': 31, 'L3.31': 32, 'L3.33': 34, 'L3.35': 36, 'L4.1': 1, 'L4.4': 4}
# RUN4-MOR eye anchors (glyph numbering as ANCH), read on the full-size P4 image 4 Oct 2026
EYE = {'L1.13': (13, 'L'), 'L1.14': (13, 'R'), 'L1.15': 14, 'L1.36': (38, 'L'), 'L1.37': (38, 'R'), 'L1.38': 39, 'L1.39': 40,
       'L2.38': 37, 'L2.39': 38, 'L2.40': (39, 'L'), 'L2.41': (39, 'R'), 'L2.42': 40, 'L2.43': 41,
       'L3.36': (37, 'L'), 'L3.37': (37, 'R'), 'L3.38': 38}
EYEBOX = {'L2.21': (3212, 3278), 'L2.22': (3268, 3350)}  # x0, x1 on P4; y from the line band
INF = 1e9
import sys
HARD = '--free' not in sys.argv
GAPS5 = dict(ANCH)
if '--eye' in sys.argv: ANCH = {**ANCH, **EYE}
MLEFT = int(sys.argv[sys.argv.index('--m-left') + 1]) if '--m-left' in sys.argv else 0
def align(L, gidx):
    toks = [(r[1], r[2]) for r in rows if r[0] == L]
    segs = G[L]['glyphs']; n, m = len(toks), len(segs)
    med = statistics.median(s[2] - s[0] for s in segs)
    w = lambda a, b: (segs[b-1][2] - segs[a][0]) / med  # width of segs a..b-1
    gap = lambda j: (segs[j][0] - segs[j-1][2]) / med if 0 < j < m else 1.0
    def pen(i, want):  # 5.0 when token i carries a GAPS5 anchor and this move does not put it there
        a = ANCH.get(gidx.get(f'{L}.{toks[i][0]}')) if HARD else None
        return 0 if a is None or a == want else 5.0
    C = [[INF] * (m + 1) for _ in range(n + 1)]; B = {}
    C[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            c = C[i][j]
            if c >= INF: continue
            if i < n and toks[i][1] == '|':
                nc = c + (0 if gap(j) >= 0.4 else 0.8)
                if nc < C[i+1][j]: C[i+1][j] = nc; B[(i+1, j)] = (i, j, 'gap')
                continue
            if i < n and j < m:
                nc = c + abs(w(j, j+1) - 1) + pen(i, j + 1)
                if nc < C[i+1][j+1]: C[i+1][j+1] = nc; B[(i+1, j+1)] = (i, j, '1:1')
            if i < n and j + 1 < m:
                nc = c + abs(w(j, j+2) - 1) + 0.6 + pen(i, j + 1)
                if nc < C[i+1][j+2]: C[i+1][j+2] = nc; B[(i+1, j+2)] = (i, j, '1:2')
            if i + 1 < n and j < m and toks[i+1][1] != '|':
                nc = c + abs(w(j, j+1) - 2) + 0.6 + pen(i, (j + 1, 'L')) + pen(i + 1, (j + 1, 'R'))
                if nc < C[i+2][j+1]: C[i+2][j+1] = nc; B[(i+2, j+1)] = (i, j, '2:1')
            if j < m:  # unmatched segment (ink fragment, flourish)
                nc = c + 1.2
                if nc < C[i][j+1]: C[i][j+1] = nc; B[(i, j+1)] = (i, j, 'skip')
    out = []; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, k = B[(i, j)]
        if k == '1:1': out.append((toks[pi], [pj + 1], segs[pj][:2] + segs[pj][2:], k))
        elif k == '1:2': out.append((toks[pi], [pj + 1, pj + 2], [segs[pj][0], segs[pj][1], segs[pj+1][2], segs[pj][3]], k))
        elif k == '2:1':
            x0, y0, x1, y1 = segs[pj]; mid = (x0 + x1) // 2
            out.append((toks[pi+1], [(pj + 1, 'R')], [mid, y0, x1, y1], k)); out.append((toks[pi], [(pj + 1, 'L')], [x0, y0, mid, y1], k))
        i, j = pi, pj
    return [o for o in reversed(out)]
res = []; gidx = {}
for L in ['L1', 'L2', 'L3', 'L4']:
    g = 0
    for r in rows:  # GAPS5 numbers glyphs per line ignoring '|' rows; ciphertext.tsv's pos counts them
        if r[0] == L and r[2] != '|': g += 1; gidx[f'{L}.{r[1]}'] = f'{L}.{g}'
    for (pos, sign), sg, box, k in align(L, gidx):
        if '--eye' in sys.argv and gidx[f'{L}.{pos}'] in EYEBOX: box = [EYEBOX[gidx[f'{L}.{pos}']][0], box[1], EYEBOX[gidx[f'{L}.{pos}']][1], box[3]]; k = 'eye'
        if sign == 'M' and MLEFT: box = [box[0] - MLEFT] + list(box[1:])
        res.append((f'{L}.{pos}', sign, sg, box, k))
ok = tot = 0; bad = []
for p, s, sg, box, k in res:
    if gidx[p] in GAPS5:
        tot += 1; a = GAPS5[gidx[p]]; got = sg[0] if len(sg) == 1 else sg
        if got == a or (isinstance(a, int) and a in sg): ok += 1
        else: bad.append(f'{p}:{got}!={a}')
eok = sum(1 for p, s, sg, box, k in res if gidx[p] in EYE and (sg[0] if len(sg) == 1 else sg) in (EYE[gidx[p]], [EYE[gidx[p]]]) or (gidx[p] in EYE and isinstance(EYE[gidx[p]], int) and EYE[gidx[p]] in sg))
print(f'# align_boxes.py (RUN1-MOR 4 Oct 2026){" anchors as constraints" if HARD else " --free (anchors not used)"}: {len(res)} positions; GAPS5 eye anchors agree {ok}/{tot}' + (f'; disagree {bad}' if bad else '') + (f'; --eye (RUN4-MOR) anchors met {eok}/{len(EYE)}, eye boxes {len(EYEBOX)}' if '--eye' in sys.argv else '') + (f'; --m-left {MLEFT}' if MLEFT else ''))
print('position\tglyph_no\tsign\tsegments\tmode\tx0\ty0\tx1\ty1')
for p, s, sg, box, k in res:
    print(p, gidx[p], s, ','.join(str(x) if isinstance(x, int) else f'{x[0]}{x[1]}' for x in sg), k, *box, sep='\t')
