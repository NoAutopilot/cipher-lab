"""Cut one strip per f.30 'eh' and CROSS occurrence from the committed line-half crops (images/crops_f30),
for the shape split (A2-GRA3, 3 Oct 2026). Position in the half is estimated proportionally from passR_f30.tsv's
half lengths; the strip spans +-3.5 sign widths, the target column is marked by two ticks, and the line's
neighbouring codes are printed above. Writes crops/f30_split/<line>_<pos>_<sign>.jpg and sheet_<n>.jpg.
  python3 split_shapes_crops.py"""
import os, sys
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__))
if '--help' in sys.argv: print(__doc__); sys.exit()
rows = {}
for l in open(os.path.join(H, 'passR_f30.tsv')):
    r, c = l.rstrip('\n').split('\t')
    if r != 'row': rows[r] = c.split()
ct = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'ciphertext_f30.tsv'))][1:]
byline = {}
for line, pos, s, cf in ct: byline.setdefault(line, []).append(s)
out = os.path.join(H, 'crops', 'f30_split'); os.makedirs(out, exist_ok=True)
strips = []
for line, pos, s, cf in ct:
    if s not in ('eh', 'CROSS'): continue
    pos = int(pos); na = len(rows[line + 'a']); nb = len(rows[line + 'b'])
    half, i, n = ('a', pos, na) if pos < na else ('b', pos - na, nb)
    im = Image.open(os.path.join(H, 'images', 'crops_f30', f'{line}{half}.jpg')).convert('L')
    w, h = im.size; sw = w / n; x = (i + 0.5) * sw
    x0, x1 = max(0, int(x - 3.5 * sw)), min(w, int(x + 3.5 * sw))
    st = im.crop((x0, 0, x1, h)).convert('RGB')
    d = ImageDraw.Draw(st); tx = x - x0
    d.line([(tx, 0), (tx, 12)], fill=(255, 0, 0), width=3); d.line([(tx, h - 12), (tx, h)], fill=(255, 0, 0), width=3)
    seq = byline[line]; ctx = ' '.join(seq[max(0, pos - 3):pos]) + ' [' + s + '] ' + ' '.join(seq[pos + 1:pos + 4])
    lab = Image.new('RGB', (max(st.width, 700), st.height + 24), 'white'); lab.paste(st, (0, 24))
    ImageDraw.Draw(lab).text((4, 4), f'{line} pos{pos} {cf}: {ctx}', fill=(0, 0, 0))
    lab.save(os.path.join(out, f'{line}_{pos}_{s}.jpg'), quality=88); strips.append(lab)
for k in range(0, len(strips), 8):
    grp = strips[k:k + 8]; W = max(g.width for g in grp); Ht = sum(g.height + 6 for g in grp)
    sh = Image.new('RGB', (W, Ht), 'gray'); y = 0
    for g in grp: sh.paste(g, (0, y)); y += g.height + 6
    sh.save(os.path.join(out, f'sheet_{k // 8 + 1}.jpg'), quality=85)
print(len(strips), 'strips')
