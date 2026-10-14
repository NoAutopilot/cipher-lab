# BAL22-SHAPE helper: preview tile placement for the 7 letter-sign tokens of 169 f.22r (location only, by eye on the debug overlay).
import sys; sys.path.insert(0, 'b167228')
from PIL import Image, ImageDraw
from sig_tiles import W, H
SRC = 'images/b169sweep/src_c048_f22r_1285,1140,2950,810.jpg'
def tile(x, y):
    return Image.open(SRC).convert('L').crop((x - W // 2, y - 90, x + W // 2, y + 120))
F22 = [('L01', 8, 'f', 2719, 96), ('L03', 4, 'r', 1217, 502), ('L03', 7, 'm', 1700, 502), ('L03', 9, 'n', 2019, 502),
       ('L03', 12, 'a', 2568, 502), ('L04', 1, 'n', 345, 690), ('L04', 3, 'u', 680, 690)]
if __name__ == '__main__':
    out = Image.new('L', (len(F22) * (W + 10), H + 30), 255); d = ImageDraw.Draw(out)
    for k, (l, p, v, x, y) in enumerate(F22):
        out.paste(tile(x, y), (k * (W + 10), 30)); d.text((k * (W + 10) + 5, 5), f'{l}/{p}', fill=0)
    out.save(sys.argv[1] if len(sys.argv) > 1 else 'balshape/f22/preview.png')
