# SUR-POS6B (account 2, LANE DEFAULT-A2-2013, 13 Oct 2026): same-hand look at 4.VEL 2039 legend k pos 6 (7 vs r). Panel of 4 settled
# r and 4 settled 7 tiles (all conf H in ciphertext_2039_legend.tsv) from the same legend, unlabelled and shuffled; queries = the target
# plus two known-answer H controls (p pos 30 = r, r pos 9 = 7) not in the panel. Boxes located by eye on 4x zooms of the on-disk native
# images (no fetch). Seed 20261013. Usage (from the target folder): python3 passes/signcmp_surpos6b/build_call.py
import json, random
from PIL import Image, ImageDraw
D = 'passes/signcmp_surpos6b/'
L = 'images/2039_legend_native.jpg'; R = 'images/2039_legend_right_native.jpg'
PANEL = {'r_l3': (L, (1132, 752, 1156, 785), 'r'), 'r_n2': (L, (1884, 750, 1902, 782), 'r'),
         'r_f16': (L, (1650, 650, 1676, 688), 'r'), 'r_p25': (L, (256, 852, 278, 892), 'r'),
         '7_m11': (L, (1696, 752, 1713, 782), '7'), '7_n6': (L, (1959, 750, 1976, 782), '7'),
         '7_e6': (L, (270, 655, 288, 688), '7'), '7_o2': (R, (148, 745, 166, 780), '7')}
QS = {'T_k6': (L, (850, 752, 876, 785), 'target'), 'C_p30_r': (L, (386, 852, 404, 892), 'r'),
      'C_r9_7': (L, (1626, 848, 1644, 882), '7')}
rng = random.Random(20261013)
pk = sorted(PANEL); rng.shuffle(pk); qk = sorted(QS); rng.shuffle(qk)
key = {'panel': {lab: [k, PANEL[k][0], list(PANEL[k][1]), PANEL[k][2]] for lab, k in zip('ABCDEFGH', pk)},
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
sheet([(lab, (v[1], v[2])) for lab, v in key['panel'].items()], 'panel.jpg')
sheet([(lab, (v[1], v[2])) for lab, v in key['queries'].items()], 'queries.jpg')
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
print({k: v[0] for k, v in key['panel'].items()}, {k: v[0] for k, v in key['queries'].items()})
