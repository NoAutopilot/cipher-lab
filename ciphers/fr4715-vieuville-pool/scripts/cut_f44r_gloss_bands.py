#!/usr/bin/env python3
"""GAPS-fr4715-vieuville-pool-10 (2 Oct 2026): overlapping two-line gloss bands of no.21 f.44r L01-L20 from the native region
images/src_ark_12148_btv1b52509819x_f103_450_1300_3250_2700.jpg. Centres are tools/iiif_lines.py's row-profile
centres for --region 0,0,3250,1060 (pasted in NOTES.md); a midpoint band would split each interlinear gloss from
the code it glosses, so each crop runs from 70 pct of the gap above the centre to 35 pct of the gap below (the
gloss stays with the line under it), 3 overlapping segments, 1.5x. Crops are regenerable, not committed.
usage: cut_f44r_gloss_bands.py OUTDIR"""
import sys, os
from PIL import Image
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = [111, 163, 205, 251, 307, 354, 409, 457, 527, 589, 652, 693, 739, 783, 831, 886, 921, 963, 1014, 1051, 1103]
SEG = [(0, 1200), (1025, 2225), (2050, 3250)]
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
im = Image.open(os.path.join(HERE, 'images/src_ark_12148_btv1b52509819x_f103_450_1300_3250_2700.jpg'))
# the centres do not follow the leaf's slant (a gloss fell out of the crop of its own line in a first cut), so the
# crops are overlapping two-line bands: 160 px tall every 100 px from y 40 to 1100, each gloss whole in at least one
for i, up in enumerate(range(40, 1000, 100)):
    dn = up + 160
    for s, (x0, x1) in enumerate(SEG, 1):
        c = im.crop((x0, int(up), x1, int(dn)))
        c = c.resize((int(c.width * 1.5), int(c.height * 1.5)), Image.LANCZOS)
        c.save(os.path.join(out, f'f44r_g{i+1:02d}_s{s}.jpg'), quality=88)
print('wrote', 30, 'crops to', out)
