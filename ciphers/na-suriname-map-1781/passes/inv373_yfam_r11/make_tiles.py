"""R11-SURY: cut one tile per [y-fam] token (tokens.tsv), shuffle (seed 1781), write anon_key.tsv and contact sheets."""
import csv, random, sys
from PIL import Image, ImageDraw
out = sys.argv[1] if len(sys.argv) > 1 else '.'
rows = [r for r in csv.DictReader((l for l in open('tokens.tsv') if not l.startswith('#')), delimiter='\t')]
random.seed(1781); order = list(range(len(rows))); random.shuffle(order)
tiles, key = [], []
for k, i in enumerate(order):
    r = rows[i]
    f = ('../inv373_0693_r10/crops/' if r['src'] == '0692' else 'c93n/') + r['crop'] + '.jpg'
    im = Image.open(f).convert('L'); w, h = im.size; x = int(r['x'])
    x0 = max(0, x - 70)
    if r['src'] == '0692': t = im.crop((x0, int(h * 0.38), min(w, x + 70), h))
    else: y = int(r['y']); t = im.crop((x0, y - 95, min(w, x + 70), y + 75))
    t = t.resize((t.size[0] * 3, t.size[1] * 3), Image.LANCZOS).convert('RGB')
    d = ImageDraw.Draw(t); cx = (x - x0) * 3; H = t.size[1]
    d.polygon([(cx - 8, H), (cx + 8, H), (cx, H - 14)], fill=(255, 0, 0))
    tiles.append(t); key.append((f'A{k+1:02d}', r['tok']))
open('anon_key.tsv', 'w').write('# anonymised tile id -> token (seed 1781)\nanon\ttok\n' + ''.join(f'{a}\t{b}\n' for a, b in key))
H = max(t.size[1] for t in tiles)
for s in range(0, len(tiles), 9):
    part = tiles[s:s + 9]; sheet = Image.new('RGB', (3 * 430, ((len(part) + 2) // 3) * (H + 24)), 'white'); d = ImageDraw.Draw(sheet)
    for j, t in enumerate(part):
        X = (j % 3) * 430; Y = (j // 3) * (H + 24); d.text((X + 4, Y + 4), f'A{s+j+1:02d}', fill=(0, 0, 255)); sheet.paste(t, (X, Y + 20))
    sheet.save(f'{out}/sheet{s//9}.png')
