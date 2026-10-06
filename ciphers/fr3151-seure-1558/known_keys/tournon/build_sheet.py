"""R12A-SEUT (6 Oct 2026): image-exemplar reference sheet for the Tournon 1556 cipher block (BnF fr. 3138 fo. 22r).
Tiles cut from the leaf's own line crops (../images/tv/, rebuilt by ../regen_images.sh) at the boxes in exemplars.tsv."""
from PIL import Image, ImageDraw, ImageOps
import csv, os
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, 'exemplars.tsv')), delimiter='\t'))
T = []
for r in rows:
    im = Image.open(os.path.join(here, '../images/tv/tv_%s.jpg' % r['crop'])).convert('L')
    t = ImageOps.autocontrast(im.crop((int(r['x0']), 62, int(r['x1']), 198)), cutoff=1)
    T.append((r['label'], t))
cols, cw, ch = 8, 170, 190
sheet = Image.new('L', (cols * cw, ((len(T) + cols - 1) // cols) * ch), 255)
d = ImageDraw.Draw(sheet)
for i, (l, t) in enumerate(T):
    x, y = (i % cols) * cw, (i // cols) * ch
    t.thumbnail((cw - 10, ch - 30)); sheet.paste(t, (x + 5, y + 25))
    d.text((x + 5, y + 5), l, fill=0); d.rectangle([x, y, x + cw - 1, y + ch - 1], outline=150)
sheet.save(os.path.join(here, 'exemplar_sheet.png')); print(sheet.size, len(T), 'tiles')
