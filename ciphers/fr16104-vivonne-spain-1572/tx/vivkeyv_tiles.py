#!/usr/bin/env python3
"""VIV-KEYV (14 Oct 2026): rebuild the 12-tile blind montage for the label-e shape check from tx/vivkeyv_tiles.tsv.

Needs the line crops (untracked): images/p67 from the manifest "viv67" regenerate commands (1 openapi request + the
--image re-cut), images/p63 c199_f193v / c198_f192v from
  tools/iiif_lines.py --ark btv1b9009663p --canvas 199 --iiif-host openapi --region 1300,600,2980,4560 --out <folder>/images/p63 --prefix c199_f193v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
  tools/iiif_lines.py --ark btv1b9009663p --canvas 198 --iiif-host openapi --region 1200,700,2900,4250 --out <folder>/images/p63 --prefix c198_f192v --follow-slope 400 --distance 70 --max-width 1600 --overlap 150 --debug
Usage: python3 tx/vivkeyv_tiles.py OUT.jpg   (run from the target folder). No image goes into git.
"""
import csv, sys
from PIL import Image, ImageDraw
rows = list(csv.DictReader(open('tx/vivkeyv_tiles.tsv'), delimiter='\t'))
tiles = []
for r in rows:
    x = int(r['x_centre']); im = Image.open('images/' + r['crop']).convert('RGB')
    a = max(0, x - 55); t = im.crop((a, 0, min(im.width, x + 55), im.height)).resize((330, 3 * im.height))
    cx = (x - a) * 3; ImageDraw.Draw(t).polygon([(cx - 10, 0), (cx + 10, 0), (cx, 18)], fill=(220, 0, 0))
    tiles.append((r['tile'], t))
H = max(t.height for _, t in tiles)
c = Image.new('RGB', (4 * 345, 3 * (H + 30)), 'white'); d = ImageDraw.Draw(c)
for i, (n, t) in enumerate(tiles):
    X = (i % 4) * 345; Y = (i // 4) * (H + 30); c.paste(t, (X, Y + 25)); d.text((X + 5, Y + 5), n, fill='black')
c.save(sys.argv[1] if len(sys.argv) > 1 else 'vivkeyv_blind.jpg')
