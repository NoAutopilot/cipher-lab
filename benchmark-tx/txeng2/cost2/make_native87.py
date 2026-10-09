#!/usr/bin/env python3
"""TXE2-COST2 (X8b): arm b crops for ceppo-f87-S -- the same tracked, per-segment-sheared line bands as
harvest/cut_folio_lines.py's lines2x, at NATIVE scale (no 2x upscale), TWO segments per line cut at the column-ink
minimum nearest the line's midpoint (no overlap). The functions are taken from cut_folio_lines.py unchanged (its source
is executed up to its module-level loop, so the tracking is the same code). Crops are not committed (regenerable).
    python3 benchmark-tx/txeng2/cost2/make_native87.py OUTDIR"""
import json, sys
from pathlib import Path
from PIL import Image, ImageOps
H87 = Path('ciphers/ceppo-nevers-fr3251-1570s/harvest')
src = (H87 / 'cut_folio_lines.py').read_text()
ns = {'__file__': str(H87 / 'cut_folio_lines.py')}
exec(src.split('\nfor folio, (src, centres, follow)')[0], ns)
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
f, centres, _ = ns['FOLIOS']['f87']; HALF = ns['HALF']
im = Image.open(H87 / 'f87' / f).convert('L'); W, H = im.size
tracks = ns['track_lines'](im, centres); at = ns['at']; man = []
for i, c in enumerate(centres, 1):
    tr = tracks[i - 1]
    band = ImageOps.autocontrast(ns['sheared_band'](im, (at(tr, W) - at(tr, 0)) / W, at(tr, 0), HALF), cutoff=1)
    cuts = [0, ns['gap_cut'](band, W // 2), W]
    for k in range(2):
        a, b = cuts[k], cuts[k + 1]; ya, yb = at(tr, a), at(tr, b); m = (yb - ya) / (b - a)
        seg = im.transform((b - a, 2 * HALF), Image.AFFINE, (1, 0, a, m, 1, ya - HALF), resample=Image.BICUBIC)
        seg = ImageOps.autocontrast(seg, cutoff=1); name = f'f87_L{i:02d}_s{k + 1}.png'; seg.save(out / name)
        man.append({'crop': name, 'src': f, 'box': [a, round(ya), b, round(yb)], 'scale': 1})
json.dump(man, open(out / 'crops_manifest.json', 'w'), indent=0)
print(len(man), 'crops ->', out)
