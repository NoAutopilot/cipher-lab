# R7-SUR2 (account 2), 6 Oct 2026: 2-3-sign context tiles for the second blind same-hand call (changed instrument after
# R7-SUR's single-sign gate FAIL). Same 14 boxes as passes/signcmp_r7sur/cut_tiles.py, widened by PAD native px each side
# so one neighbour sign shows on each side; 3x Lanczos; a white header strip with a red triangle marks the centred sign.
# Shuffled to Q1-Q6 / R1-R8 with a fresh seed. Run from the target folder.
import json, os, random, sys
from PIL import Image, ImageDraw
sys.path.insert(0, 'passes/signcmp_r7sur')
from cut_tiles import SIGNS
D = 'passes/signcmp_r7sur2/'
OUT = 'images/crops_r7sur2'
PAD, S, HDR, SEED = 45, 3, 30, 20261007
os.makedirs(OUT, exist_ok=True); os.makedirs(D + 'tiles', exist_ok=True)
im = Image.open('images/2077_legend_native.jpg')
tiles = {}
for sid, lp, code, val, role, (x0, y0, x1, y1) in SIGNS:
    box = (max(0, x0 - PAD), y0, min(im.width, x1 + PAD), y1)
    t = im.crop(box).convert('RGB'); t = t.resize((t.width * S, t.height * S), Image.LANCZOS)
    c = Image.new('RGB', (t.width, t.height + HDR), 'white'); c.paste(t, (0, HDR))
    cx = ((x0 + x1) / 2 - box[0]) * S
    ImageDraw.Draw(c).polygon([(cx - 10, 4), (cx + 10, 4), (cx, HDR - 4)], fill=(220, 0, 0))
    c.save(f'{OUT}/{sid}.jpg', quality=95); tiles[sid] = (lp, code, val, role, box)
qs = [s for s in SIGNS if s[4] in ('query', 'control-query')]
rs = [s for s in SIGNS if s[4].startswith('ref')]
rng = random.Random(SEED); rng.shuffle(qs); rng.shuffle(rs)
key = {}
for pre, group in (('Q', qs), ('R', rs)):
    for i, s in enumerate(group, 1):
        Image.open(f'{OUT}/{s[0]}.jpg').save(f'{D}tiles/{pre}{i}.jpg', quality=95)
        key[f'{pre}{i}'] = {'id': s[0], 'linepos': s[1], 'code': s[2], 'current': s[3], 'role': s[4], 'ctx_box': tiles[s[0]][4]}
json.dump(key, open(D + 'blind_key.json', 'w'), indent=1)
print({k: v['id'] for k, v in key.items()})
