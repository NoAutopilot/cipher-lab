"""Build the sign-sorter data file: one small grayscale PNG crop per box from the PUBLIC page images
(glyphs/crops/<page>.png, coordinates glyphs/signs.tsv), grouped into piles by the pass-A label in
glyphs/box_labels.tsv. Output: sorter/data.json (embedded into the page by build_page.py).
No museum material is used (RESTRICTED.md)."""
import base64, csv, io, json, os
from collections import defaultdict
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(HERE, '..', 'glyphs')
signs = {r['sid']: r for r in csv.DictReader(open(os.path.join(G, 'signs.tsv')), delimiter='\t')}
labels = list(csv.DictReader(open(os.path.join(G, 'box_labels.tsv')), delimiter='\t'))
pages = {}
piles = defaultdict(list)
fam = {}
skipped = 0
for r in labels:
    s = signs[r['sid']]
    p = s['page']
    path = os.path.join(G, 'crops', p + '.png')
    if not os.path.exists(path):
        skipped += 1
        continue
    if p not in pages:
        pages[p] = ImageOps.autocontrast(Image.open(path).convert('L'), cutoff=1)
    x, y, w, h = (int(s[k]) for k in ('x', 'y', 'w', 'h'))
    pad = 3
    c = pages[p].crop((max(0, x - pad), max(0, y - pad), x + w + pad, y + h + pad))
    c.thumbnail((72, 72), Image.LANCZOS)
    buf = io.BytesIO()
    c.save(buf, 'PNG', optimize=True)
    piles[r['sign']].append({'sid': r['sid'], 'img': base64.b64encode(buf.getvalue()).decode()})
    fam[r['sign']] = r['family']
out = {'piles': [{'id': k, 'family': fam[k], 'items': v} for k, v in piles.items()], 'skipped': skipped}
json.dump(out, open(os.path.join(HERE, 'data.json'), 'w'))
print(len(out['piles']), 'piles', sum(len(p['items']) for p in out['piles']), 'crops; skipped', skipped,
      os.path.getsize(os.path.join(HERE, 'data.json')) // 1024, 'KB')
