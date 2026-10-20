"""Taller crops of the two doubted S lines (SHERWOOD-CELLS, 20 Oct 2026), the mrows/crop_slips.py way: box from
images/crops/manifest.json (tools/iiif_lines.py, 18 Oct 2026), widened 45 px up and down, split in two halves, x1.5."""
import json, os
from PIL import Image
H = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
man = {e['crop']: e for e in json.load(open(os.path.join(H, 'images/crops/manifest.json')))['iiif_lines']}
for c in ['p346_L09.jpg', 'p345_L10.jpg']:
    e = man[c]; x0, y0, x1, y1 = e['box']
    im = Image.open(os.path.join(H, 'images', e['source_file']))
    for k, (a, b) in enumerate([(x0, (x0 + x1) // 2 + 100), ((x0 + x1) // 2 - 100, x1)]):
        cr = im.crop((a, y0 - 45, b, y1 + 45))
        cr = cr.resize((int(cr.width * 1.5), int(cr.height * 1.5)))
        cr.save(os.path.join(H, 'cells/cipher', c.replace('.jpg', '_h%d.jpg' % (k + 1))), quality=88)
