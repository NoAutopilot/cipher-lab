#!/usr/bin/env python3
"""GLY-11106 (8 Oct 2026): map glyph_atlas boxes (atlas/signs.tsv) to transcription positions (ciphertext.tsv) for WVO
11106 p.2, so the sorter can pile tiles by the reconciled label and the focus questions point at tiles.

No reader x-positions exist. Per line, the kept boxes (x order) are aligned to the transcription positions by a
monotone DP on widths and positions: a box takes one position (cost |w - W(label)| / Wmed), or two neighbouring positions when two
signs are joined into one box (cost |w - W(a) - W(b)| / Wmed + MERGE), or is skipped (SKIPB; fragments, under FRAG x
the median sign height both ways, are dropped before the DP); a position may go unmatched (SKIPT). W(label) starts at
the median box width and is re-estimated from the 1:1 matches for ITER rounds (labels with < 3 matches keep the
median). Each match also pays LAM x |box centre - predicted centre| / Wmed, the predicted centre being the
position's share of the line's ink span by cumulative estimated widths (this anchors the DP against drift). A 1:1 match is 'firm' when its width cost is under FIRM. Writes atlas/boxmap.tsv (sid, line, pos, label,
kind, agree, cost, firm, joined): joined=1 marks a box carrying two positions (pos 'a+b', label 'x+y').
Approximate by construction; the purity check scores the atlas only on firm, 2-reader-agreed 1:1 matches.
"""
import csv, statistics as st
from collections import defaultdict
from pathlib import Path

FRAG, MERGE, SKIPB, SKIPT, FIRM, MH, ITER, LAM = 0.6, 0.35, 0.9, 0.9, 0.45, 22, 3, 1.5
here = Path(__file__).resolve().parent
B = list(csv.DictReader(open(here / 'signs.tsv'), delimiter='\t'))
T = list(csv.DictReader(open(here.parent / 'ciphertext.tsv'), delimiter='\t'))
lines = sorted({t['line'] for t in T})
kept = {L: sorted([b for b in B if b['page'] == L and not (int(b['h']) < FRAG * MH and int(b['w']) < FRAG * MH * 1.5)],
                  key=lambda b: int(b['x'])) for L in lines}
wmed = st.median(int(b['w']) for L in lines for b in kept[L])


def dp(bx, tx, W):
    n, m = len(bx), len(tx); INF = 1e18
    D = [[INF] * (m + 1) for _ in range(n + 1)]; P = [[None] * (m + 1) for _ in range(n + 1)]; D[0][0] = 0
    w = [int(b['w']) for b in bx]; tw = [W(t['sign']) for t in tx]
    cx = [int(b['x']) + int(b['w']) / 2 for b in bx]; x0, x1 = int(bx[0]['x']), int(bx[-1]['x']) + int(bx[-1]['w'])
    tot = sum(tw); cum = [sum(tw[:k]) for k in range(m + 1)]; sc = (x1 - x0) / tot
    est = lambda a, b: x0 + sc * (cum[a] + cum[b + 1]) / 2          # predicted centre of positions a..b
    pos = lambda i, a, b: LAM * abs(cx[i] - est(a, b)) / (sc * wmed)
    for i in range(n + 1):
        for j in range(m + 1):
            d = D[i][j]
            if d >= INF: continue
            def go(a, b, c, op):
                if c < D[a][b]: D[a][b] = c; P[a][b] = (i, j, op)
            if i < n and j < m: go(i + 1, j + 1, d + abs(w[i] - tw[j]) / wmed + pos(i, j, j), 1)
            if i < n and j + 1 < m: go(i + 1, j + 2, d + abs(w[i] - tw[j] - tw[j + 1]) / wmed + MERGE + pos(i, j, j + 1), 2)
            if i < n: go(i + 1, j, d + SKIPB, 0)
            if j < m: go(i, j + 1, d + SKIPT, -1)
    out, i, j = {}, n, m
    while (i, j) != (0, 0):
        pi, pj, op = P[i][j]
        if op == 1: out[pi] = ([pj], abs(w[pi] - tw[pj]) / wmed)
        elif op == 2: out[pi] = ([pj, pj + 1], abs(w[pi] - tw[pj] - tw[pj + 1]) / wmed)
        i, j = pi, pj
    return out


widths = {}
for it in range(ITER + 1):
    W = lambda s: widths.get(s, wmed)
    maps = {L: dp(kept[L], [t for t in T if t['line'] == L], W) for L in lines}
    acc = defaultdict(list)
    for L in lines:
        tx = [t for t in T if t['line'] == L]
        for bi, (js, c) in maps[L].items():
            if len(js) == 1 and c < FIRM: acc[tx[js[0]]['sign']].append(int(kept[L][bi]['w']))
    widths = {s: st.median(v) for s, v in acc.items() if len(v) >= 3}
rows, seen = [], set()
for L in lines:
    tx = [t for t in T if t['line'] == L]
    for bi, b in enumerate(kept[L]):
        seen.add(b['sid'])
        if bi in maps[L]:
            js, c = maps[L][bi]; ts = [tx[j] for j in js]
            rows.append([b['sid'], L, '+'.join(t['pos'] for t in ts), '+'.join(t['sign'] for t in ts), ts[0]['kind'],
                         int(all(t['note'] == '2-reader agree' for t in ts)), f'{c:.2f}', int(len(js) == 1 and c < FIRM), int(len(js) == 2)])
        else: rows.append([b['sid'], L, '', '', 'unmatched', '', '', 0, 0])
for b in B:
    if b['sid'] not in seen: rows.append([b['sid'], b['page'], '', '', 'fragment', '', '', 0, 0])
with open(here / 'boxmap.tsv', 'w') as o:
    o.write('sid\tline\tpos\tlabel\tkind\tagree\tcost\tfirm\tjoined\n')
    for r in rows: o.write('\t'.join(map(str, r)) + '\n')
cov = sum(len(r[2].split('+')) for r in rows if r[2])
print(f'{len(B)} boxes ({sum(1 for r in rows if r[4] == "fragment")} fragments), {sum(1 for r in rows if r[2])} matched '
      f'({sum(r[8] for r in rows)} joined), covering {cov}/{len(T)} positions; {sum(r[7] for r in rows)} firm 1:1, '
      f'{sum(1 for r in rows if r[7] and r[5] == 1)} firm+agreed')
