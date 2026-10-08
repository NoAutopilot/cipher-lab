"""FAM-WVOH: reference strip + blind panels of 33 targets and 10 fresh decoys (PREREG-FAM-WVOH.md). Run from the target folder.
Crop step: tile boxes from sorter/signs.tsv + sorter/bands.tsv cut from images/01109_p3_400full.jpg (same as d2wvo/build_montage.py)."""
import csv, random
from PIL import Image, ImageDraw, ImageFont
rows = list(csv.DictReader(open('realign/tile_letters.tsv'), delimiter='\t'))
tg = [r for r in rows if r['grade_after'] == 'C' and r['gloss_letter_realign'] != r['value_after']]
ag = [r for r in rows if r['grade_after'] == 'C' and r['gloss_letter_realign'] == r['value_after']]
assert len(tg) == 33 and len(ag) == 159
REF = [('d', 'f23_C10_01_005'), ('d', 'f23_C07_01_012'), ('g', 'f23_C07_01_006'), ('g', 'f23_C05_01_006'),
       ('h', 'f23_C03_01_003'), ('h', 'f23_C07_01_003'), ('i', 'f23_C06_01_006'), ('s', 'f23_C04_01_016')]
d2 = {l.split('\t')[2] for l in open('d2wvo/panel_key.tsv') if l.split('\t')[1] == 'D'}
excl = d2 | {s for _, s in REF}
pool = [r for r in ag if r['sid'] not in excl]
rng = random.Random(1613)
dpool = [r for r in pool if r['settled_sign'] == 'k22' and r['value_after'] == 'd']
dd = rng.sample(dpool, 2)
rest = [r for r in pool if r not in dd]
dec = dd + rng.sample(rest, 8)
panels = [('T', r) for r in tg] + [('D', r) for r in dec]
rng.shuffle(panels)
bands = {r['page']: r for r in csv.DictReader(open('sorter/bands.tsv'), delimiter='\t')}
signs = {r['sid']: r for r in csv.DictReader(open('sorter/signs.tsv'), delimiter='\t')}
img = Image.open('images/01109_p3_400full.jpg').convert('RGB')
W = 520
font = ImageFont.load_default(20)
def panel(sid, label):
    s = signs[sid]; b = bands[s['page']]
    x = 550 + int(s['x']); y = int(b['strip_y0']) + int(s['y']); w = int(s['w']); h = int(s['h'])
    cx = x + w // 2; x0, x1 = cx - 200, cx + 200
    y0, y1 = min(int(b['band_y0']), y) - 150, max(int(b['band_y1']), y + h) + 20
    c = img.crop((x0, y0, x1, y1)).copy()
    ImageDraw.Draw(c).rectangle((x - x0, y - y0, x - x0 + w, y - y0 + h), outline=(255, 0, 0), width=3)
    c = c.resize((W, int(c.height * W / c.width)))
    p = Image.new('RGB', (W, 30 + c.height), 'white'); ImageDraw.Draw(p).text((5, 5), label, fill='black', font=font)
    p.paste(c, (0, 30)); return p, (x, y, w, h)
def sheet(ps, out, cols=3):
    ph = max(p.height for p in ps); n = (len(ps) + cols - 1) // cols
    sh = Image.new('RGB', (cols * (W + 10), n * (ph + 10)), 'white')
    for j, p in enumerate(ps): sh.paste(p, ((j % cols) * (W + 10), (j // cols) * (ph + 10)))
    sh.save(out, quality=88)
refp = [panel(s, 'REFERENCE: letter above box = %s' % v)[0] for v, s in REF]
sheet(refp, 'famwvoh/reference_strip.jpg', cols=4)
key = open('famwvoh/panel_key.tsv', 'w')
key.write('panel\tkind\tsid\trow\tidx\tsign\tvalue_after\tgloss_r10\tgloss_realign\tpage_box\n')
ps = []
for i, (kind, r) in enumerate(panels, 1):
    p, (x, y, w, h) = panel(r['sid'], 'Q%02d' % i); ps.append(p); p.save('famwvoh/panels/Q%02d.jpg' % i, quality=88)
    key.write('Q%02d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%d,%d,%d,%d\n' % (i, kind, r['sid'], r['row'], r['idx'], r['settled_sign'],
              r['value_after'], r['gloss_letter_r10'], r['gloss_letter_realign'], x, y, w, h))
for k in range(0, len(ps), 12):
    sheet(ps[k:k + 12], 'famwvoh/montage_%d.jpg' % (k // 12 + 1))
