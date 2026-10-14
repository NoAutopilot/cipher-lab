#!/usr/bin/env python3
"""BAL169-F22B: re-fetch the exemplar canvases (Baluze 169, 2400 px) and cut the line bands this job read, into OUT (not committed).
Bands are (x0, y0, x1, y1) on the 2400-px image. f.22r marks: images/b169sweep/src_c048_f22r_*.jpg (already on disk), L03 x 880-1600.
Usage: python3 regen_crops.py OUT_DIR   (openapi.bnf.fr, 5 requests, >= 3.2 s apart; take/release the host in ROOM.md first)
"""
import os, sys, time, urllib.request
from PIL import Image
ARK = 'btv1b9001488b'
BANDS = {79: [(850, 1960, 2300, 2160), (850, 2080, 2300, 2280), (850, 2230, 2300, 2420), (850, 2400, 2300, 2590),
              (850, 2520, 2300, 2720), (850, 2650, 2300, 2830)],
         165: [(300, 640, 2300, 840), (300, 1850, 2300, 2030), (300, 2160, 2300, 2340), (300, 2260, 2300, 2440)],
         177: [(770, 750, 2180, 920), (770, 860, 2180, 1030), (770, 1060, 2180, 1230), (770, 1160, 2180, 1330),
               (770, 2540, 2180, 2720), (770, 2640, 2180, 2820), (770, 2740, 2180, 2920), (770, 2840, 2180, 3020)]}
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for c, bands in BANDS.items():
    p = os.path.join(out, f'c{c}.jpg')
    if not os.path.exists(p):
        req = urllib.request.Request(f'https://openapi.bnf.fr/iiif/image/v3/ark:/12148/{ARK}/f{c}/full/2400,/0/default.jpg',
                                     headers={'User-Agent': 'cipher-lab research script (contact via repository)'})
        open(p, 'wb').write(urllib.request.urlopen(req).read()); time.sleep(3.3)
    im = Image.open(p)
    for i, b in enumerate(bands):
        im.crop(b).save(os.path.join(out, f'c{c}_band{i+1}.jpg'))
