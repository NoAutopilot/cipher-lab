#!/usr/bin/env python3
"""R14-LVNEYE (6 Oct 2026): 2x context crops of the 10 4610 p3 control rows that both round-d readers (A7, B7) read the same
against the H control sign, for an eye check of the control itself. Usage: eyecrops.py PAGE300.png OUTDIR
PAGE300.png is `pdftoppm -png -r 300 -f 3 -l 3 04610.pdf` (sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591). Blob boxes are the
round-d blobs_d.tsv rows (label, x0, x1, yc) matched to the aligned_d.tsv rows by token context; crop = box +-260 px, yc -70..+60,
upscaled 2x, JPEG q70. Offline."""
import sys, os
from PIL import Image
R = [('01_L12-12_120v126', 1406, 1488, 1176), ('02_L15-2_85v35', 319, 437, 1400), ('03_L16-10_150v250', 1137, 1377, 1506),
     ('04_L16-13_112v12', 1424, 1467, 1510), ('05_L17-6_61v31', 674, 797, 1573), ('06_L18-8_81v87', 1057, 1175, 1676),
     ('07_L22-3_32v82', 879, 1037, 2012), ('08_L23-3_51v61', 523, 568, 2161), ('09_L24-15_130v136', 1752, 1836, 2315),
     ('10_L31-4_12v2', 587, 626, 2932)]
im = Image.open(sys.argv[1]).convert('L'); os.makedirs(sys.argv[2], exist_ok=True)
for n, x0, x1, y in R:
    c = im.crop((x0 - 260, y - 70, x1 + 260, y + 60)); c.resize((c.width * 2, c.height * 2)).save(os.path.join(sys.argv[2], 'eye_%s.jpg' % n), quality=70)
