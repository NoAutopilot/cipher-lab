"""AVS-175: cut single-sign crops for the 124 f.134 K look (PREREG-AVS-175.md).
Usage: python3 cut_k124.py SCRATCH_DIR  (expects p124-000.jpg = 00124.pdf page 6, p126-000.jpg = 00126.pdf page 4,
extracted with pdfimages -j; writes SCRATCH_DIR/signs/<id>.png, neutral-id copies and a contact sheet; nothing goes into git)."""
import json, random, sys, os
from PIL import Image, ImageDraw
S = sys.argv[1]; here = os.path.dirname(os.path.abspath(__file__))
img = {'124': Image.open(os.path.join(S, 'p124-000.jpg')).convert('L'),
       '126': Image.open(os.path.join(S, 'p126-000.jpg')).convert('L')}
boxes = json.load(open(os.path.join(here, 'boxes_k124.json')))
os.makedirs(os.path.join(S, 'signs'), exist_ok=True)
ids = list(boxes); rng = random.Random(175); neutral = rng.sample(range(10, 10 + len(ids)), len(ids))
key = {}
sheet = Image.new('L', (len(ids) * 140, 170), 255); d = ImageDraw.Draw(sheet)
for i, k in enumerate(ids):
    src, x0, y0, x1, y1 = boxes[k]
    c = img[src].crop((x0, y0, x1, y1))
    c.save(os.path.join(S, 'signs', k + '.png'))
    n = 'S%d' % neutral[i]; key[n] = k
    c.resize((c.width * 2, c.height * 2)).save(os.path.join(S, 'signs', n + '.png'))
    sheet.paste(c, (i * 140, 30)); d.text((i * 140, 5), k[:3], fill=0)
sheet.save(os.path.join(S, 'contact_k124.png'))
json.dump(key, open(os.path.join(here, 'key_k124.json'), 'w'), indent=1, sort_keys=True)
print(json.dumps(key, sort_keys=True))
