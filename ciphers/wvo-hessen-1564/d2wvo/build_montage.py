"""D2-WVO: build the blind montage of 33 target + 10 decoy f.23 tiles (PREREG-D2-WVO.md). Run from the target folder."""
import csv, random
from PIL import Image, ImageDraw, ImageFont
rows = list(csv.DictReader(open('realign/tile_letters.tsv'), delimiter='\t'))
tg = [r for r in rows if r['grade_after'] == 'C' and r['gloss_letter_realign'] != r['value_after']]
ag = [r for r in rows if r['grade_after'] == 'C' and r['gloss_letter_realign'] == r['value_after']]
assert len(tg) == 33 and len(ag) == 159
dec = random.Random(1564).sample(ag, 10)
panels = [('T', r) for r in tg] + [('D', r) for r in dec]
random.Random(1564).shuffle(panels)
bands = {r['page']: r for r in csv.DictReader(open('sorter/bands.tsv'), delimiter='\t')}
signs = {r['sid']: r for r in csv.DictReader(open('sorter/signs.tsv'), delimiter='\t')}
img = Image.open('images/01109_p3_400full.jpg').convert('RGB')
W, H = 520, 300
crops = []
key = open('d2wvo/panel_key.tsv', 'w')
key.write('panel\tkind\tsid\trow\tidx\tsign\tvalue_after\tgloss_r10\tgloss_realign\tpage_box\n')
for i, (kind, r) in enumerate(panels, 1):
    s = signs[r['sid']]; b = bands[s['page']]
    x = 550 + int(s['x']); y = int(b['strip_y0']) + int(s['y']); w = int(s['w']); h = int(s['h'])
    cx = x + w // 2
    x0, x1 = cx - 200, cx + 200
    y0, y1 = min(int(b['band_y0']), y) - 150, max(int(b['band_y1']), y + h) + 20
    c = img.crop((x0, y0, x1, y1)).copy()
    d = ImageDraw.Draw(c)
    d.rectangle((x - x0, y - y0, x - x0 + w, y - y0 + h), outline=(255, 0, 0), width=3)
    c = c.resize((W, int(c.height * W / c.width)))
    lab = Image.new('RGB', (W, 30), 'white'); ImageDraw.Draw(lab).text((5, 5), 'P%02d' % i, fill='black', font=ImageFont.load_default(20))
    p = Image.new('RGB', (W, 30 + c.height), 'white'); p.paste(lab, (0, 0)); p.paste(c, (0, 30))
    crops.append(p)
    key.write('P%02d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%d,%d,%d,%d\n' % (i, kind, r['sid'], r['row'], r['idx'], r['settled_sign'],
              r['value_after'], r['gloss_letter_r10'], r['gloss_letter_realign'], x, y, w, h))
    p.save('d2wvo/panels/P%02d.jpg' % i, quality=88)
# montage sheets of 12 panels (3 x 4), so each vision look stays a strip-sized image
for k in range(0, len(crops), 12):
    grp = crops[k:k + 12]; ph = max(p.height for p in grp)
    sheet = Image.new('RGB', (3 * W + 20, 4 * ph + 30), 'white')
    for j, p in enumerate(grp):
        sheet.paste(p, ((j % 3) * (W + 10), (j // 3) * (ph + 10)))
    sheet.save('d2wvo/montage_%d.jpg' % (k // 12 + 1), quality=88)
