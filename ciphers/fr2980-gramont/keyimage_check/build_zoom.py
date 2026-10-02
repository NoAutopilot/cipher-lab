"""Zoom sheet for the key-image check (A2-GRA, 2 Oct 2026): f.30 eh windows vs the D and T shapes, Tomokiyo row 5 crosses."""
from PIL import Image, ImageDraw
import os
R = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(R, '..'); S = os.path.join(T, '../../sources/cryptiana/web')
tom = Image.open(f'{S}/francisGramont.png').convert('L'); leg = Image.open(f'{T}/legend_sheet.png').convert('L')
c = lambda n: Image.open(f'{T}/images/crops_f30/{n}.jpg').convert('L')
P = [('Tomokiyo row 5, x225-320 (under l m n)', tom.crop((225, 132, 320, 168)), 5),
     ('Tomokiyo d col + t col (x78-105 | x440-470)', None, 0),
     ('Legend k19 (Lasry D) | k45 (Lasry T)', None, 0),
     ('f30r L04a x470-680 (pos 5-8: z3 eh dl Rt)', c('f30r_L04a').crop((470, 0, 680, 147)), 2),
     ('f30r L04a x1150-1348 (pos ~15-17: A2 n6 eh)', c('f30r_L04a').crop((1150, 0, 1348, 147)), 2),
     ('f30r L04b x1290-1500 (pos ~35-37: n6 eh B8)', c('f30r_L04b').crop((1290, 0, 1500, 147)), 2),
     ('f30r L08a x760-1060 (pos ~14-16: 5 eh sl)', c('f30r_L08a').crop((760, 0, 1060, 147)), 2)]
a = tom.crop((78, 30, 105, 125)); b = tom.crop((440, 30, 470, 125)); im = Image.new('L', (a.width + b.width + 10, 95), 255); im.paste(a, (0, 0)); im.paste(b, (a.width + 10, 0)); P[1] = (P[1][0], im, 4)
k19 = leg.crop((222, 222, 330, 300)); k45 = leg.crop((662, 552, 770, 630)); im = Image.new('L', (226, 78), 255); im.paste(k19, (0, 0)); im.paste(k45, (118, 0)); P[2] = (P[2][0], im, 2)
out = [(l, i.resize((i.width * s, i.height * s))) for l, i, s in P]
W = max(i.width for _, i in out); H = sum(i.height + 22 for _, i in out)
sh = Image.new('L', (W, H), 255); d = ImageDraw.Draw(sh); y = 0
for l, i in out:
    d.text((4, y + 4), l, fill=0); sh.paste(i, (0, y + 20)); y += i.height + 22
sh.save(f'{R}/zoom.png'); print(sh.size)
