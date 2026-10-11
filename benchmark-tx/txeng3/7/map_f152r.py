#!/usr/bin/env python3
"""TXE3-7 step 2: label-blind box -> token map for birago1572-f152r (PREREG-txeng3-7.md, target P).
Atlas page f152r lines 2-5 = letter lines L01-L04 (line 1 is the prose line above the run). Prose boxes outside the cipher run
are removed by an x bound read from the line image before any alignment (L01: cipher right of x=2520 src px, after
"...et che bisogna"; L04: cipher left of x=2460, before ", con uolermi"); then the width-only DP of atlas/no87_map.py
(1:1, 2:1, 1:2, skip a box, skip a token; no label on either side steers it) aligns boxes in x order to the tokens of the
line read of record (benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv). Writes benchmark-tx/txeng3/7/f152r_box_token.tsv
(sid, line, pos, op). Run from the repo root."""
import csv, sys, os, importlib.util, collections
A = 'ciphers/nevers-birago-fr3251-1572/atlas'; W = 'benchmark-tx/txeng3/7'
spec = importlib.util.spec_from_file_location('no87_map', f'{A}/no87_map.py'); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
S = [r for r in csv.DictReader(open(f'{A}/signs.tsv'), delimiter='\t') if r['page'] == 'f152r']
toks = collections.defaultdict(list)
for r in csv.DictReader(open('benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv'), delimiter='\t'):
    toks[r['line']].append(r)
XB = {'f152r_L01': lambda cx: cx > 2520, 'f152r_L04': lambda cx: cx < 2460}
out = []; stats = {}
for li, L in ((2, 'f152r_L01'), (3, 'f152r_L02'), (4, 'f152r_L03'), (5, 'f152r_L04')):
    bx = sorted((r for r in S if int(r['line']) == li), key=lambda r: int(r['x']))
    n0 = len(bx)
    bx = [r for r in bx if XB.get(L, lambda cx: True)(int(r['x']) + int(r['w']) / 2)]
    bw = [int(r['w']) for r in bx]; n = len(toks[L])
    Wmed = sorted(bw)[len(bw) // 2]
    path = M.dp(bw, n, Wmed)
    ops = collections.Counter(op for _, _, op in path)
    for (i, j, op) in path:
        if op == '1:1':
            out.append((bx[i]['sid'], L, toks[L][j]['pos'], op))
    stats[L] = dict(boxes_line=n0, boxes_in_run=len(bx), tokens=n, ops=dict(ops),
                    x_range=(int(bx[0]['x']), int(bx[-1]['x']) + int(bx[-1]['w'])))
with open(f'{W}/f152r_box_token.tsv', 'w') as f:
    f.write('sid\tline\tpos\top\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in out))
print(stats); print('1:1 tokens', len(out), 'of', sum(len(v) for v in toks.values()))
