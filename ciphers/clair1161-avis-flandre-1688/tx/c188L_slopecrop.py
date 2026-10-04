"""NEAR3-C1TX-c188L (4 Oct 2026): slope-following line crops of f189 left (c188L), used for the reconciliation.
The leaf's lines rise about 0.05-0.08 px per px to the right, so a level band (tools/iiif_lines.py, one centre per line)
holds the target line on the left and the next line on the right. Here each line is tracked strip by strip (250 px
strips, ink-profile peak within 45 px of the previous one) from its left-hand centre, and cut in three segments
(x 450-1500, 1350-2400, 2250-3150 of the region), each band spanning the line's own track there (-85/+75 px).
Usage: python3 tx/c188L_slopecrop.py NATIVE_REGION.jpg OUTDIR [--quality 25]
NATIVE_REGION = https://gallica.bnf.fr/iiif/ark:/12148/btv1b90010063/f189/100,50,3150,4600/full/0/native.jpg
(sha1 dd16bb37cd08eaf2c35b4d955dcc62de31fa9a80 on 4 Oct 2026). Writes OUTDIR/c188L_Lnn_s1..s3.jpg + boxes.json."""
import json, sys
import numpy as np
from PIL import Image
from scipy.signal import find_peaks
from scipy.ndimage import gaussian_filter1d
src, out = sys.argv[1], sys.argv[2]
q = int(sys.argv[sys.argv.index('--quality') + 1]) if '--quality' in sys.argv else 95
img = Image.open(src).convert('L'); im = np.asarray(img).astype(float)
L1 = [280, 420, 600, 720, 850, 990, 1140, 1260, 1390, 1530, 1660, 1800, 1920, 2050, 2190, 2330, 2460, 2580, 2710, 2850,
      2980, 3130, 3270, 3400, 3540, 3670, 3800]  # left-hand centres read by eye from the overlay
segs = [(450, 1500), (1350, 2400), (2250, 3150)]
xs = list(range(500, 3150, 250)); prof = {}
for x in xs:
    p = gaussian_filter1d((im[:, x - 125:x + 125] < 110).sum(1).astype(float), 10)
    prof[x] = find_peaks(p, distance=70, prominence=5)[0]
man = []
for i, c in enumerate(L1, 1):
    y = c; row = {}
    for x in xs:
        cand = prof[x][np.abs(prof[x] - y) < 45]
        if len(cand): y = int(cand[np.argmin(np.abs(cand - y))])
        row[x] = y
    for j, (a, b) in enumerate(segs, 1):
        ys = [row[x] for x in xs if a <= x <= b]
        box = (a, max(0, min(ys) - 85), b, min(img.height, max(ys) + 75))
        f = 'c188L_L%02d_s%d.jpg' % (i, j); img.crop(box).save('%s/%s' % (out, f), quality=q, optimize=True)
        man.append({'crop': f, 'box_region_xyxy': list(box), 'line': i, 'segment': j})
json.dump(man, open('%s/boxes.json' % out, 'w'), indent=1)
print(len(man), 'crops')
