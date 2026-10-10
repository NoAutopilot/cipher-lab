#!/usr/bin/env python3
"""MARKS-DEV2b candidate-pool report (read-free; box geometry only, no truth, no pass): imports rule.py's own functions and
reports, per run, boxes, boxes under 0.35 x the line's median sign height, small pairs that are stacked and x-overlapping
(before the stroke test), and the pairs surviving the stroke test (= rule candidates). Also the quantiles of max-side/median.
  python3 benchmark-tx/txeng2/marks2/pool.py SEGDIR > benchmark-tx/txeng2/marks2/pool.tsv"""
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rule  # noqa: E402

seg = sys.argv[1]
tb = ts = tst = tc = 0; ratios = []
print('line\tboxes\tsmall\tstacked_pairs\tcandidates\tmedian_sign_h')
for line in rule.LINES:
    boxes, _ = rule.line_boxes(seg, line)
    sh = [b['ly1'] - b['ly0'] for b in boxes if b['kind'] == 'sign']
    m = float(np.median(sh)) if sh else 0.0
    small = [b for b in boxes if m and max(b['lx1'] - b['lx0'], b['ly1'] - b['ly0']) < rule.SMALL * m]
    ratios += [max(b['lx1'] - b['lx0'], b['ly1'] - b['ly0']) / m for b in boxes if m]
    st = 0
    for i, a in enumerate(small):
        for b in small[i + 1:]:
            top, bot = (a, b) if a['ly0'] <= b['ly0'] else (b, a)
            gap = bot['ly0'] - top['ly1']; hmin = min(top['ly1'] - top['ly0'], bot['ly1'] - bot['ly0'])
            if rule.xov(top, bot) >= rule.XOV and 0 <= gap < rule.VGAP * hmin:
                st += 1
    c = len(rule.candidates(boxes)[0])
    print('%s\t%d\t%d\t%d\t%d\t%.1f' % (line, len(boxes), len(small), st, c, m))
    tb += len(boxes); ts += len(small); tst += st; tc += c
q = np.quantile(ratios, [0.01, 0.05, 0.10, 0.25])
print('TOTAL\t%d\t%d\t%d\t%d\tq01=%.2f q05=%.2f q10=%.2f q25=%.2f' % (tb, ts, tst, tc, *q))
