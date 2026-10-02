"""Build pair-comparison sheets for GAPS5-moray-wood-1568 from glyphs2.json segments (verified by eye against the
numbered overlay, vision call 1). Segment numbers are 1-based per line. Blind sheets: shuffled, lettered, for the one
strong-model call. Labelled sheets: 1x, for the committed evidence."""
import json, random, sys, csv
from PIL import Image, ImageDraw, ImageFont
S = sys.argv[1]; SRC = sys.argv[2]
im = Image.open(SRC).convert('L')
G = json.load(open(f'{S}/seg/glyphs2.json'))
def seg(line, a, b=None):
    """native box spanning segments a..b (1-based) of a line, full band height"""
    gs = G[line]['glyphs']; b = b or a
    x0 = gs[a-1][0]; x1 = gs[b-1][2]; y0 = gs[a-1][1]; y1 = gs[a-1][3]
    return [x0, y0, x1, y1]
def split(line, a, half):
    """left or right half of a merged segment"""
    x0, y0, x1, y1 = seg(line, a); m = (x0 + x1) // 2
    return [x0, y0, m, y1] if half == 'L' else [m, y0, x1, y1]
# (position label, his label, box)
XD = [('L1.8','xd',seg('L1',8)),('L1.17','xd',seg('L1',17)),('L1.20','xd',seg('L1',20)),('L1.31','xd',seg('L1',33)),
      ('L1.34','xd',seg('L1',36)),('L3.7','xd',seg('L3',7)),('L3.35','xd',seg('L3',36))]
X  = [('L1.5','x',seg('L1',5)),('L1.14','x VOID: M bowl',seg('L1',14)),('L1.18','x',seg('L1',18)),('L1.30','x',seg('L1',32)),
      ('L3.25','x',seg('L3',26)),('L3.30','x',seg('L3',31)),('L3.33','x',seg('L3',34))]
EC = [('L1.41','e?',seg('L1',42)),('L1.11','e',seg('L1',11)),('L3.31','e',seg('L3',32)),('L1.23','c',seg('L1',23)),('L1.27','c',seg('L1',27))]
XS = [('L3.28','X?',seg('L3',29)),('L4.4','Xs',seg('L4',4)),('L2.30','X',seg('L2',29)),('L3.30','x',seg('L3',31)),('L1.5','x',seg('L1',5))]
ZZ = [('L3.3','Zz?',seg('L3',3)),('L3.4','Zz?',seg('L3',4)),('L4.1','Zz',seg('L4',1)),('L1.10','Z3',seg('L1',10)),('L1.44','Z3',seg('L1',45)),
      ('L3.27','Z3',seg('L3',28)),('L1.40','Z2',seg('L1',41)),('L3.14','Z2',seg('L3',15)),('L1.25','Z5',seg('L1',25)),('L1.38','Z5 VOID: M bowl',split('L1',40,'L'))]
SHEETS = {'q1_xd_vs_x': XD + X, 'q2_e_vs_c': EC, 'q3_X_vs_Xs': XS, 'q4_Zz_vs_Z3': ZZ}
random.seed(20261002)
font = ImageFont.load_default(size=22)
fontb = ImageFont.load_default(size=30)
PAD = 10
keyrows = []
for name, cells in SHEETS.items():
    for mode in ('blind', 'labelled'):
        scale = 2 if mode == 'blind' else 1
        order = list(range(len(cells)))
        if mode == 'blind': random.shuffle(order)
        crops = []
        for i in order:
            pos, lab, (x0, y0, x1, y1) = cells[i]
            c = im.crop((x0-PAD, y0, x1+PAD, y1))
            if scale != 1: c = c.resize((c.width*scale, c.height*scale), Image.LANCZOS)
            crops.append((pos, lab, c))
        ncol = 7 if len(crops) > 7 else len(crops)
        cw = max(c.width for _,_,c in crops) + 16; ch = max(c.height for _,_,c in crops) + 50
        nrow = (len(crops) + ncol - 1) // ncol
        sheet = Image.new('L', (ncol*cw, nrow*ch), 255); d = ImageDraw.Draw(sheet)
        for k, (pos, lab, c) in enumerate(crops):
            r, col = divmod(k, ncol); X0 = col*cw + (cw - c.width)//2; Y0 = r*ch + 40
            sheet.paste(c, (X0, Y0)); d.rectangle([col*cw+2, r*ch+2, (col+1)*cw-3, (r+1)*ch-3], outline=120)
            if mode == 'blind':
                letter = chr(65 + k); d.text((col*cw+8, r*ch+6), letter, fill=0, font=fontb)
                keyrows.append((name, letter, pos, lab))
            else:
                d.text((col*cw+8, r*ch+6), f'{pos} ({lab})', fill=0, font=font)
        out = f'{S}/sheets/{name}_{mode}.png'; sheet.save(out, optimize=True)
        print(out, sheet.size, round(__import__('os').path.getsize(out)/1024), 'KB')
with open(f'{S}/sheets/blind_key.tsv', 'w') as f:
    f.write('sheet\tletter\tposition\this_label\n')
    for r in keyrows: f.write('\t'.join(r) + '\n')
