#!/usr/bin/env python3
"""THUR-MEAD (10 Oct 2026): fixed-box crops of the Meadowe key sheet (BL Add MS 4166 f.102v-103r, DECODE R4890 P2/P3, and the
second copy R4891 P2/P3). tools/iiif_lines.py --image was run first and clipped table rows (its row ink profile reads the
sheet's ruled lines as text lines), so the table regions are cut by explicit boxes here instead.
python3 make_crops.py   (writes crops/*.jpg at native resolution, JPEG q70)
"""
import os
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
H = os.path.dirname(os.path.abspath(__file__))
BOXES = {
 'IMG_R4890_I28428_P2.jpg': {
  'r4890p2_head_a': (500, 750, 2900, 1750), 'r4890p2_head_b': (2700, 750, 5100, 1750), 'r4890p2_head_c': (4900, 750, 7246, 1750)},
 'IMG_R4890_I28428_P3.jpg': {
  'r4890p3_head_a': (0, 600, 1600, 1700), 'r4890p3_head_b': (1400, 600, 3000, 1700),
  'r4890p3_unc_a': (4600, 1400, 6250, 3950), 'r4890p3_unc_b': (4600, 3850, 6250, 6350), 'r4890p3_unc_c': (4600, 6250, 6250, 8750),
  'r4890p3_names_1a': (2550, 1450, 3650, 5050), 'r4890p3_names_1b': (2550, 4950, 3650, 8550),
  'r4890p3_names_2a': (3600, 1450, 4700, 5050), 'r4890p3_names_2b': (3600, 4950, 4700, 8550)},
}
def main():
    os.makedirs(os.path.join(H, 'crops'), exist_ok=True)
    for img, boxes in BOXES.items():
        im = Image.open(os.path.join(H, 'images', img))
        for name, box in boxes.items():
            im.crop(box).convert('RGB').save(os.path.join(H, 'crops', name + '.jpg'), quality=70)
            print(name, img, box)
if __name__ == '__main__':
    main()
