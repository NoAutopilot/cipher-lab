# GAPS55-na-suriname-map-1781 (account-4), 3 Oct 2026: build the 8 shuffled tiles for the blind M/N row-mark call.
# Same queries and no-mark controls as GAPS49; the dots control is replaced by two of 2077's own [u-dots] tokens
# (L15:0, L08:3; dots 17/17 in GAPS45) cut as single-sign tiles; the left-page M/N tiles and the two 2077 tiles are
# upscaled 2x (Lanczos). Run from the target folder.
import json, random
from PIL import Image
D = 'passes/signcmp_gaps55/'
SRC = [('a', 'images/crops_gaps49/g49_a_L01.jpg', 'left M first sign', 'query', 2),
       ('b', 'images/crops_gaps49/g49_b_L01.jpg', 'left N first sign', 'query', 2),
       ('c', 'images/crops_gaps49/g49_c_L01.jpg', 'right M sign', 'query', 1),
       ('d', 'images/crops_gaps49/g49_d_L01.jpg', 'right N middle sign', 'query', 1),
       ('f', 'images/crops_gaps49/g49_f_L01.jpg', 'left K b', 'control-none', 1),
       ('g', 'images/crops_gaps49/g49_g_L01.jpg', 'right O k', 'control-none', 1),
       ('u1', 'images/crops_gaps55/g55_u1_L01.jpg', '2077 L15:0 [u-dots]', 'control-dots', 2),
       ('u2', 'images/crops_gaps55/g55_u2_L01.jpg', '2077 L08:3 [u-dots]', 'control-dots', 2)]
order = list(range(len(SRC)))
random.Random(20261058).shuffle(order)
key = {}
for t, i in enumerate(order, 1):
    k, path, what, cls, sc = SRC[i]
    im = Image.open(path)
    if sc != 1: im = im.resize((im.width * sc, im.height * sc), Image.LANCZOS)
    im.save(f'{D}tiles/T{t}.jpg', quality=95)
    key[f'T{t}'] = {'crop': path, 'id': k, 'what': what, 'class': cls, 'scale': sc}
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
print({t: v['id'] for t, v in key.items()})
