"""Re-cut f75 L08 s2 and L09 s1/s2 as sheared strips (PIS-T, 4 Oct 2026).

tools/iiif_lines.py --follow-slope tracked L08's right half and all of L09 onto the line above (the "Xp lambda q" line is
faint across the stain), so these three crops are cut here from the same cached source with a fixed slope b=0.05
(the mean of the tool's own fits on L01-L07) and the left-edge centres the row profile gives (1133, 1270).
"""
from PIL import Image
import numpy as np, os
D = os.path.dirname(os.path.abspath(__file__))
src = np.array(Image.open(os.path.join(D, "src_ark_12148_btv1b9060906j_f156_680_1830_3060_3520.jpg")).convert("L"))
B, H = 0.05, 140
def cut(y0, x0, x1, name):
    out = np.full((H, x1 - x0), 255, np.uint8)
    for x in range(x0, x1):
        c = int(round(y0 + B * x)); a = c - H // 2
        lo, hi = max(a, 0), min(a + H, src.shape[0])
        out[lo - a:hi - a, x - x0] = src[lo:hi, x]
    Image.fromarray(out).save(os.path.join(D, name), quality=90)
cut(1133, 1460, 3060, "f75_L08_s2.jpg")
cut(1270, 0, 1600, "f75_L09_s1.jpg")
cut(1270, 1460, 3060, "f75_L09_s2.jpg")
