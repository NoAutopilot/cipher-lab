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
    # The signs.tsv boxes are tight around the base stroke and leave out marks above it (the dot of X-DOT,
    # the bar over 6 or X), so pad generously above and a little below (owner caught the clipping, 1 Oct 2026).
    top, bot, side = max(10, int(.9 * h)), max(6, int(.35 * h)), 5
    c = pages[p].crop((max(0, x - side), max(0, y - top), x + w + side, y + h + bot))
    c.thumbnail((96, 96), Image.LANCZOS)
    buf = io.BytesIO()
    c.save(buf, 'PNG', optimize=True)
    piles[r['sign']].append({'sid': r['sid'], 'img': base64.b64encode(buf.getvalue()).decode(), 'p': p, 'b': [x, y, w, h]})
    fam[r['sign']] = r['family']
# whole page images (public crops) for the context view, as grayscale JPEG
page_img = {}
for p, im in pages.items():
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=82, optimize=True)
    page_img[p] = base64.b64encode(buf.getvalue()).decode()
out = {'piles': [{'id': k, 'family': fam[k], 'items': v} for k, v in piles.items()], 'skipped': skipped, 'pages': page_img}
json.dump(out, open(os.path.join(HERE, 'data.json'), 'w'))
print(len(out['piles']), 'piles', sum(len(p['items']) for p in out['piles']), 'crops; skipped', skipped,
      os.path.getsize(os.path.join(HERE, 'data.json')) // 1024, 'KB')
