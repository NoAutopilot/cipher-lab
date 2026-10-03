# A2-RAA9, 3 Oct 2026. Run: python3 ciphers/na-raad-azie-1800/scripts/leaf3_mirror_test.py
# Is leaf 3's left-page cipher a mirror-image bleed-through of leaf 2's right page?
# Compare downsampled ink maps: leaf2 right page flipped L-R vs leaf3 left page, best integer shift;
# controls: unflipped, and flipped leaf2 LEFT page (plain Dutch, different text).
import os, numpy as np
IMG = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'images') + '/'
from PIL import Image
def ink(f, box, flip, scale=8):
    im = Image.open(IMG + f).convert('L').crop(box)
    if flip: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im = im.resize((im.width//scale, im.height//scale))
    a = 255 - np.asarray(im, float)
    a = a - np.median(a); a[a < 0] = 0
    return a
def best(a, b, r=40):
    h = min(a.shape[0], b.shape[0]) - 2*r; w = min(a.shape[1], b.shape[1]) - 2*r
    A = a[r:r+h, r:r+w]; A = (A - A.mean())/A.std()
    out = (-1, 0, 0)
    for dy in range(-r, r+1):
        for dx in range(-r, r+1, 2):
            B = b[r+dy:r+dy+h, r+dx:r+dx+w]; B = (B - B.mean())/B.std()
            c = float((A*B).mean())
            if c > out[0]: out = (c, dy, dx)
    return out
l3L = ink('209_leaf3.jpg', (0, 0, 2287, 2790), False)
for name, box, flip in [('leaf2 right, flipped', (2287,0,4574,2790), True),
                        ('leaf2 right, unflipped', (2287,0,4574,2790), False),
                        ('leaf2 left, flipped', (0,0,2287,2790), True),
                        ('leaf4 right, flipped', (2287,0,4574,2790), True)]:
    f = '209_leaf4.jpg' if 'leaf4' in name else '209_leaf2.jpg'
    print(name, 'r=%.3f dy=%d dx=%d' % best(l3L, ink(f, box, flip)))
print('--- leaf3 right page')
l3R = ink('209_leaf3.jpg', (2287, 0, 4574, 2790), False)
for name, f, box, flip in [('leaf2 left, flipped','209_leaf2.jpg',(0,0,2287,2790),True),
                           ('leaf2 left, unflipped','209_leaf2.jpg',(0,0,2287,2790),False),
                           ('leaf4 left, flipped','209_leaf4.jpg',(0,0,2287,2790),True),
                           ('leaf2 right, flipped','209_leaf2.jpg',(2287,0,4574,2790),True)]:
    print(name, 'r=%.3f dy=%d dx=%d' % best(l3R, ink(f, box, flip)))
