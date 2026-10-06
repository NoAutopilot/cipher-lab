"""R11-SURTV: cut one tile per token (tokens.tsv + R11-SURY's LETY tokens), scale to a common height, and write either a
labelled location-check sheet (--check) or anonymised shuffled contact sheets (seed 1781) + anon_key.tsv."""
import csv, random, sys
from PIL import Image, ImageDraw
R = '../../images/'; L = '../inv373_0693_r10/crops/'; S = '../inv373_yfam_r11/'
SRC = {'2039': R + '2039_legend_native.jpg', '2061': R + '2061_battery_legend_native.jpg', 's0693': S + 'c93n/s0693_native.jpg'}
def rows(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith('#')), delimiter='\t')]
toks = rows('tokens.tsv')
for r in rows(S + 'tokens.tsv'):
    toks.append({'tok': 'l' + r['tok'][1:], 'cls': 'LETY', 'ref': f"letter {r['line']} {r['word']} ({r['gloss']})",
                 'src': r['crop'] if r['src'] == '0692' else 's0693', 'x': r['x'], 'y': r['y'], 'hw': '70', 'up': '95', 'down': '75'})
TH = 240
def tile(r):
    s = r['src']; im = Image.open(SRC.get(s, L + s + '.jpg')).convert('L'); w, h = im.size; x, hw = int(r['x']), int(r['hw'])
    if r['y']: y = int(r['y']); box = (max(0, x - hw), max(0, y - int(r['up'])), min(w, x + hw), min(h, y + int(r['down'])))
    else: box = (max(0, x - hw), int(h * 0.38), min(w, x + hw), h)
    t = im.crop(box); k = TH / t.size[1]; t = t.resize((max(1, int(t.size[0] * k)), TH), Image.LANCZOS).convert('RGB')
    d = ImageDraw.Draw(t); cx = int((x - box[0]) * k); d.polygon([(cx - 7, TH), (cx + 7, TH), (cx, TH - 12)], fill=(255, 0, 0))
    return t
check = '--check' in sys.argv
order = list(range(len(toks)))
if not check: random.seed(1781); random.shuffle(order)
tiles, key = [], []
for k, i in enumerate(order):
    tiles.append(tile(toks[i])); key.append((f'B{k+1:02d}', toks[i]['tok'], toks[i]['cls']))
if not check:
    open('anon_key.tsv', 'w').write('# anonymised tile id -> token, class (seed 1781)\nanon\ttok\tcls\n' + ''.join(f'{a}\t{b}\t{c}\n' for a, b, c in key))
W = 330
for s in range(0, len(tiles), 12):
    part = tiles[s:s + 12]; sheet = Image.new('RGB', (4 * W, ((len(part) + 3) // 4) * (TH + 24)), 'white'); d = ImageDraw.Draw(sheet)
    for j, t in enumerate(part):
        X = (j % 4) * W; Y = (j // 4) * (TH + 24); lab = key[s + j][0] + ((' ' + key[s + j][1]) if check else '')
        d.text((X + 4, Y + 4), lab, fill=(0, 0, 255)); sheet.paste(t.crop((0, 0, min(t.size[0], W - 6), TH)), (X, Y + 20))
    sheet.save(f"{'check' if check else 'sheet'}{s // 12}.png")
print(len(tiles), 'tiles')
