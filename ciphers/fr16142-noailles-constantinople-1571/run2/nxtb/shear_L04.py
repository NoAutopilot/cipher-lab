"""Re-cut c516b line 4 by hand: iiif_lines --follow-slope tracked the ink smear (line 5) twice.
Straight shear y = Y0 + B*x (region coords; region origin 1150,1330 on canvas 516 native), B = mean of neighbours L03/L06."""
import sys
from PIL import Image
import numpy as np
src, out = sys.argv[1], sys.argv[2]
X0, Y0R, Y0, B, HALF = 1150, 1330, 515.0, -0.0225, 85
a = np.asarray(Image.open(src).convert('L'))
for k, (x0, x1) in enumerate([(0, 1850), (1750, 3600)], 1):
    w = x1 - x0; strip = np.full((2 * HALF, w), 255, np.uint8)
    for x in range(w):
        yc = int(round(Y0 + B * (x0 + x))) + Y0R
        strip[:, x] = a[yc - HALF:yc + HALF, X0 + x0 + x]
    Image.fromarray(strip).save(f'{out}/c516b_L04_s{k}.jpg', quality=90)
