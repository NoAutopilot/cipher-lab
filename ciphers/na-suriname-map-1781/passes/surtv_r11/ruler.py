"""R11-SURTV: draw an x ruler (every 50 px, labelled every 100) on a crop for locating sign centres by eye."""
import sys
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]; x0 = int(sys.argv[3]) if len(sys.argv) > 3 else 0; x1 = int(sys.argv[4]) if len(sys.argv) > 4 else None
im = Image.open(src).convert('RGB'); w, h = im.size; x1 = x1 or w
im = im.crop((x0, 0, x1, h)); d = ImageDraw.Draw(im)
for x in range((x0 // 50) * 50, x1, 50):
    if x < x0: continue
    d.line([(x - x0, 0), (x - x0, 12 if x % 100 else 24)], fill=(255, 0, 0), width=2)
    if x % 100 == 0: d.text((x - x0 + 3, 12), str(x), fill=(255, 0, 0))
im.save(out)
