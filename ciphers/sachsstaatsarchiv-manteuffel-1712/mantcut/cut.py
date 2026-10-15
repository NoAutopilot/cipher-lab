#!/usr/bin/env python3
"""MANT-CUT (15 Oct 2026) step 1, outcome-blind: cut the 4|9 digit of every y49/known.tsv slot out of its committed strip
with tools/glyph_atlas.py's cut_digits (the `digits` option added by this job), from the strip's settled tokens (non-digit
marks such as '?' and '~' dropped). Writes mantcut/located.tsv (box per slot, blank if the token was not placed) and,
with --sheet, mantcut/sheet_known.png: the clean known-4/known-9 slots, each box drawn on its strip context, for the one
location check by eye. No 4/9 score here. --check: exit 1 if located.tsv is stale."""
import os, re, sys
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'y49')); sys.path.insert(0, os.path.join(ROOT, 'yshape'))
sys.path.insert(0, os.path.join(ROOT, '..', '..', 'tools'))
import census49 as C
import glyph_atlas as G
from locate import crop_path
H = ['leaf', 'tokid', 'crop', 'settled', 'known', 'kind', 'digit_index', 'status', 'x', 'y', 'w', 'h', 'xh']
def cut_all():
    toks = {lf: t for lf, _, _, t in C.LEAVES}
    cache, rows = {}, []
    for k in C.rows('y49/known.tsv'):
        lf, tid, crop = k['leaf'], k['tokid'], k['crop']
        seq = [t for t in toks[lf] if t['crop'] == crop]
        clean = [re.sub(r'\D', '', t['settled']) for t in seq]
        idx = next(i for i, t in enumerate(seq) if t['tokid'] == tid)
        tok = clean[idx]
        kept = [c for c in clean if c]
        ki = sum(1 for c in clean[:idx] if c)
        di = sum(len(c) for c in kept[:ki]) + next(i for i, c in enumerate(tok) if c in '49')
        p = crop_path(lf, crop)
        if p not in cache:
            cache[p] = G.cut_digits(np.array(Image.open(p).convert('L')), kept)
        bx, xh = cache[p]
        b = bx[di]
        kind = 'conflict' if (k['known'] == '9' and '4' in tok) else ('clean' if k['known'] in tok else 'other')
        rows.append([lf, tid, crop, tok, k['known'], kind, di, 'located' if b else 'unlocated', *(b or ('',) * 4), xh])
    return rows
def main():
    rows = cut_all()
    txt = '\t'.join(H) + '\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    p = os.path.join(HERE, 'located.tsv')
    if '--check' in sys.argv:
        stale = not os.path.exists(p) or open(p).read() != txt
        print('STALE located.tsv' if stale else 'up to date'); sys.exit(1 if stale else 0)
    open(p, 'w').write(txt)
    from collections import Counter
    print(Counter((r[5], r[7]) for r in rows))
    if '--sheet' in sys.argv:
        import cv2
        cells = []
        for r in rows:
            if r[5] != 'clean' or r[7] != 'located':
                continue
            g = np.array(Image.open(crop_path(r[0], r[2])).convert('L'))
            x, y, w, h = r[8:12]
            x0, x1 = max(0, x - 60), min(g.shape[1], x + w + 60)
            c = cv2.cvtColor(g[:, x0:x1], cv2.COLOR_GRAY2BGR)
            cv2.rectangle(c, (x - x0, y), (x - x0 + w, y + h), (178, 114, 0), 2)  # BGR colour
            c = cv2.resize(c, (int(c.shape[1] * 90 / c.shape[0]), 90))
            c = cv2.copyMakeBorder(c, 22, 2, 2, 2, cv2.BORDER_CONSTANT, value=(255, 255, 255))
            cv2.putText(c, '%d %s %s' % (len(cells), r[0], r[3]), (2, 16), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
            cells.append(c)
        W = 300
        cells = [cv2.resize(c, (W, int(c.shape[0] * W / c.shape[1]))) if c.shape[1] > W else
                 cv2.copyMakeBorder(c, 0, 0, 0, W - c.shape[1], cv2.BORDER_CONSTANT, value=(255, 255, 255)) for c in cells]
        hh = max(c.shape[0] for c in cells)
        cells = [cv2.copyMakeBorder(c, 0, hh - c.shape[0], 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255)) for c in cells]
        per = 6
        rws = [np.hstack(cells[i:i + per] + [np.full_like(cells[0], 255)] * (per - len(cells[i:i + per])))
               for i in range(0, len(cells), per)]
        cv2.imwrite(os.path.join(HERE, 'sheet_known.png'), np.vstack(rws))
if __name__ == '__main__':
    main()
