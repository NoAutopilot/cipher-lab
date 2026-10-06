# R7-SUR (account 2), 6 Oct 2026: cut single-sign tiles from the native 2077 legend image for the blind same-hand call.
# Boxes are native pixels of images/2077_legend_native.jpg (2450x2050 region of 10711x5110), located by eye on 2x ruler views
# of the GAPS19 line bands (images/crops_2077_leg/manifest.json). Run from the target folder.
import os
from PIL import Image
OUT = 'images/crops_r7sur'
SIGNS = [  # id, line:pos, reader code, current value/grade, role, (x0,y0,x1,y1)
    ('q1', 'L08:51', 'g', 'l H', 'query', (1925, 825, 1958, 895)),
    ('q2', 'L10:30', 'g', 'l H', 'query', (912, 1030, 950, 1105)),
    ('q3', 'L11:17', '[sigma]', 'i M', 'query', (578, 1120, 602, 1190)),
    ('q4', 'L10:66', '[sigma]', 'e M', 'query', (2019, 1030, 2047, 1105)),
    ('c1', 'L08:37', 'g', 'l H (GAPS37 F2)', 'control-query', (1500, 828, 1532, 895)),
    ('c2', 'L08:5', 'g', 'g H (GAPS37 F1)', 'control-query', (556, 828, 580, 895)),
    ('rg1', 'L06:4', 'g', 'g C', 'ref F1 g', (225, 670, 260, 755)),
    ('rg2', 'L11:19', 'g', 'g H', 'ref F1 g', (625, 1120, 655, 1190)),
    ('rl1', 'L10:61', 'g', 'l C', 'ref F2 l', (1881, 1030, 1908, 1105)),
    ('rl2', 'L12:26', 'g', 'l C', 'ref F2 l', (1445, 1235, 1478, 1315)),
    ('re1', 'L11:7', 'a', 'e H', 'ref e-class', (256, 1120, 276, 1190)),
    ('re2', 'L11:15', 'a', 'e H', 'ref e-class', (530, 1120, 550, 1190)),
    ('ri1', 'L06:8', '[f-loop]', 'i M', 'ref i-class', (307, 670, 331, 755)),
    ('ri2', 'L10:60', 'm', 'i H', 'ref i-class', (1845, 1030, 1880, 1105)),
]
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    im = Image.open('images/2077_legend_native.jpg')
    for sid, lp, code, val, role, box in SIGNS:
        t = im.crop(box)
        t.resize((t.width * 3, t.height * 3), Image.LANCZOS).save(f'{OUT}/{sid}.jpg', quality=95)
    print(len(SIGNS), 'tiles ->', OUT)
