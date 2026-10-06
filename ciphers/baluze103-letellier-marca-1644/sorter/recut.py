#!/usr/bin/env python3
"""R9-BAL103 (6 Oct 2026): inputs for the f.50 owner sign sorter, one tile per sign, via tools/sorter_recut.py.

The two Gallica native pages already on disk (images/src_..._f111 = f.50r, _f112 = f.50v) are stacked into one grey array,
everything outside each side's cipher box (r8b/manifest_f50.json line boxes) blanked, one constant trace per line at its box
centre (recentre() then follows the ink). Reader columns = ciphertext.tsv's signs per line (the current settled draft,
pre-R8), positioned evenly across the line's own ink extent. Focus = r8b/focus.tsv's 28 questions mapped to the tile aligned
with that (line, position); a question whose column took no tile is reported and dropped.
  python3 ciphers/baluze103-letellier-marca-1644/sorter/recut.py [--debug DIR]
"""
import argparse, csv, json, sys
from collections import defaultdict
from pathlib import Path
import numpy as np
from PIL import Image
S = Path(__file__).resolve().parent; T = S.parent; R = S.parents[2]
sys.path.insert(0, str(R / 'tools'))
import sorter_recut as sr  # noqa: E402
Image.MAX_IMAGE_PIXELS = None
CFG = sr.Cfg(pitch=230, half=118, xmin=1200, xmax=4260, nclu=60)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--debug'); a = ap.parse_args()
    man = json.load(open(T / 'r8b' / 'manifest_f50.json'))['iiif_lines']
    srcs = {'f50r': 'src_ark_12148_btv1b9001389d_f111_0_0_4864_6996.jpg', 'f50v': 'src_ark_12148_btv1b9001389d_f112_0_0_4864_6996.jpg'}
    pg = {k: np.array(Image.open(T / 'images' / v).convert('L')) for k, v in srcs.items()}
    H = pg['f50r'].shape[0]; grey = np.full((2 * H, pg['f50r'].shape[1]), 255, np.uint8)
    lines = defaultdict(list)                     # line id -> boxes (f50v has two half crops per line)
    for e in man:
        side = 'f50r' if e['source_file'].endswith('f111_0_0_4864_6996.jpg') else 'f50v'
        stem = Path(e['crop']).stem; ln = stem if side == 'f50r' else stem.rsplit('_', 1)[0]
        lines[ln].append((side, e['box']))
    for ln, bx in lines.items():
        side = bx[0][0]; x0 = min(b[0] for _, b in bx); x1 = max(b[2] for _, b in bx)
        y0 = min(b[1] for _, b in bx); y1 = max(b[3] for _, b in bx); oy = 0 if side == 'f50r' else H
        grey[oy + y0:oy + y1, x0:x1] = pg[side][y0:y1, x0:x1]
    tx = defaultdict(list)
    for r in csv.DictReader(open(T / 'ciphertext.tsv'), delimiter='\t'): tx[r['line']].append(r['sign'])
    pages = sorted(lines); W = grey.shape[1]; traces, cols, centres = [], [], []
    for ln in pages:
        bx = lines[ln]; oy = 0 if bx[0][0] == 'f50r' else H
        y0 = min(b[1] for _, b in bx) + oy; y1 = max(b[3] for _, b in bx) + oy; yc = (y0 + y1) / 2
        traces.append(np.full(W, yc))
        band = grey[int(yc - 60):int(yc + 60)] < 120; ink = np.where(band.sum(0) > 3)[0]
        lo, hi = (ink.min(), ink.max()) if len(ink) else (1550, 4000)
        n = len(tx[ln]); cols.append([(s, s) for s in tx[ln]])
        centres.append([lo + (hi - lo) * (k + 0.5) / n for k in range(n)])
    sr.run(grey, traces, pages, cols, centres, S, S / 'pages', CFG, debug=a.debug)
    # preflight fix (R9-BAL103, the one allowed): a box cut tight on a thin stroke or a speck is solid or blank by
    # construction (preflight ink 3-60%: 121 of 1111 at page-scale 0.5); pad every box by PAD px, clamped to the strip
    PAD, SH = 6, 2 * CFG.half + 1
    rows = list(csv.DictReader(open(S / 'signs.tsv'), delimiter='\t'))
    with open(S / 'signs.tsv', 'w') as o:
        o.write('sid\tpage\tx\ty\tw\th\n')
        for r in rows:
            x, y, w, h = (int(r[k]) for k in ('x', 'y', 'w', 'h')); x0, y0 = max(0, x - PAD), max(0, y - PAD)
            x1, y1 = min(W - 1, x + w - 1 + PAD), min(SH - 1, y + h - 1 + PAD)
            o.write(f"{r['sid']}\t{r['page']}\t{x0}\t{y0}\t{x1 - x0 + 1}\t{y1 - y0 + 1}\n")
    # focus from r8b/focus.tsv: sid bal103b_<line>_<pos> -> the tile aligned with that column
    by = {}
    for r in csv.DictReader(open(S / 'clusters.tsv'), delimiter='\t'):
        if r['col']: by.setdefault((r['sid'].rsplit('_', 1)[0], int(r['col'])), []).append((int(r['dx']), r['sid']))
    out, miss = [], []
    for ln_ in open(T / 'r8b' / 'focus.tsv'):
        sid, q = ln_.rstrip('\n').split('\t', 1); _, side, l, pos = sid.split('_'); key = (f'{side}_{l}', int(pos))
        if key in by: out.append(f"{min(by[key])[1]}\t{q}\n")
        else: miss.append(sid)
    (S / 'focus_r8b.tsv').write_text(''.join(out))
    print(f'focus mapped {len(out)}/{len(out) + len(miss)}; unmapped: {" ".join(miss) or "none"}')


if __name__ == '__main__':
    main()
