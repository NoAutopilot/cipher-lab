# SUR-POS6 (account 1, LANE DEFAULT-A1-1840, 13 Oct 2026): one blind sign call on 4.VEL 2039 legend k pos 6 (7 vs r) against the
# Nieuw Secreet sheet's E-row 7 and T-row r tiles (boxes from passes/signcmp_sur2039r/blind_key.json: R_E7, R_Tr), with two
# known-answer H controls from the same legend line (l pos 3 = r, m pos 11 = 7). Reference and query labels shuffled (seed
# 20261013); no value, reading or code on the image. Usage (from the target folder): python3 passes/signcmp_surpos6/build_call.py
import json, random
from PIL import Image, ImageDraw
D = 'passes/signcmp_surpos6/'
SHEET = 'images/inv86_0003_left_native.jpg'; LEG = 'images/2039_legend_native.jpg'
REFS = {'R_E7': (SHEET, (248, 945, 292, 1012), '7'), 'R_Tr': (SHEET, (115, 2730, 185, 2795), 'r')}
QS = {'T_k6': (LEG, (850, 752, 876, 785), 'target'), 'C_l3_r': (LEG, (1132, 752, 1156, 785), 'r'),
      'C_m11_7': (LEG, (1696, 752, 1713, 782), '7')}
rng = random.Random(20261013)
rk = sorted(REFS); rng.shuffle(rk); qk = sorted(QS); rng.shuffle(qk)
key = {'refs': {lab: [k] + [REFS[k][0], list(REFS[k][1]), REFS[k][2]] for lab, k in zip('XY', rk)},
       'queries': {f'Q{i+1}': [k, QS[k][0], list(QS[k][1]), QS[k][2]] for i, k in enumerate(qk)}}
def tile(f, b, pad=6, H=160):
    im = Image.open(f).convert('L'); x0, y0, x1, y1 = b
    im = im.crop((max(0, x0 - pad), max(0, y0 - pad), x1 + pad, y1 + pad)); s = H / im.size[1]
    return im.resize((max(20, int(im.size[0] * s)), H))
def sheet(items, out):
    tiles = [(lab, tile(f, tuple(b))) for lab, (f, b) in items]
    W = sum(max(t.size[0], 80) + 40 for _, t in tiles) + 20; c = Image.new('L', (W, 220), 255); d = ImageDraw.Draw(c); x = 20
    for lab, t in tiles:
        c.paste(t, (x, 40)); d.rectangle([x - 1, 39, x + t.size[0], 40 + t.size[1]], outline=128); d.text((x + 2, 10), lab, fill=0)
        x += max(t.size[0], 80) + 40
    c.save(D + out, quality=92)
sheet([(lab, (v[1], v[2])) for lab, v in key['refs'].items()], 'refs.jpg')
sheet([(lab, (v[1], v[2])) for lab, v in key['queries'].items()], 'queries.jpg')
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
print({k: v[0] for k, v in key['refs'].items()}, {k: v[0] for k, v in key['queries'].items()})
