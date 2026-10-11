#!/usr/bin/env python3
"""TXE3-5 BOXES (11 Oct 2026): build the Birago arms (machine, owner, owner-trash-only, owner-recut-only, 20 size-matched random
controls) from the owner's L74 page boxes, classify them all in ONE glyph_atlas classify --boxes call against the Birago 1572 family
atlas, write one tx_bench output per arm (kind=sign boxes in reading order, sign = k1) and score each with tx_bench on
birago1572-no87 (--coverage-diagnostic: 12 of 27 lines). Reads the oracle answers; never writes them. PREREG-txeng3-5.md."""
import csv, os, subprocess, sys, json, random, collections, re
from PIL import Image
R = 'benchmark-tx/txeng3/5'; O = 'benchmark-tx/txeng2/oracle1'; A = 'ciphers/nevers-birago-fr3251-1572/atlas'
HAND = 'birago1572-no87'; MH = '68'; NSEED = 20
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
boxes = [r for r in rd(f'{O}/boxes/boxes_recut_all.tsv') if r['hand'] == HAND]
for b in boxes:
    for k in 'xywh': b[k] = int(b[k])
    b['order'] = int(re.search(r'_b(\d+)', b['box_id']).group(1))
settled = {r['sid']: r['status'] for r in rd(f'{O}/answers/birago/settled.tsv')}
recuts = rd(f'{O}/answers/birago/recuts.tsv')
trash = [s for s, st in settled.items() if st in ('not-letter', 'aside')]
assert all(any(b['box_id'] == s for b in boxes) for s in trash) and all(any(b['box_id'] == r['tile'] for b in boxes) for r in recuts)
sizes = {}
for b in boxes:
    if b['crop'] not in sizes: sizes[b['crop']] = Image.open(b['crop']).size

def apply(bs, drop, rc):
    """drop: set of box_ids to delete; rc: {box_id: (x,y,w,h)} new geometry (clipped to the crop)."""
    out = []
    for b in bs:
        if b['box_id'] in drop: continue
        c = dict(b)
        if b['box_id'] in rc:
            x, y, w, h = rc[b['box_id']]; W, H = sizes[b['crop']]
            x = max(0, min(x, W - 1)); y = max(0, min(y, H - 1)); w = max(1, min(w, W - x)); h = max(1, min(h, H - y))
            c.update(x=x, y=y, w=w, h=h)
        out.append(c)
    return out

owner_rc = {r['tile']: tuple(int(r[f'new_{k}']) for k in 'xywh') for r in recuts}
deltas = [(r['tile'], tuple(int(r[f'new_{k}']) - int(r[f'old_{k}']) for k in 'xywh')) for r in recuts]
arms = {'machine': apply(boxes, set(), {}), 'owner': apply(boxes, set(trash), owner_rc),
        'owner_trash_only': apply(boxes, set(trash), {}), 'owner_recut_only': apply(boxes, set(), owner_rc)}
bybid = {b['box_id']: b for b in boxes}
area = lambda b: b['w'] * b['h']
touched = set(trash) | set(owner_rc)
for seed in range(NSEED):
    rnd = random.Random(1000 + seed); used = set(); drop = set(); rc = {}
    for s in trash:                      # a random untouched box among the 10 nearest in area
        pool = sorted((b for b in boxes if b['box_id'] not in touched | used), key=lambda b: abs(area(b) - area(bybid[s])))[:10]
        pick = rnd.choice(pool); used.add(pick['box_id']); drop.add(pick['box_id'])
    for s, (dx, dy, dw, dh) in deltas:   # the same geometric change on a random size-matched untouched box
        pool = sorted((b for b in boxes if b['box_id'] not in touched | used), key=lambda b: abs(area(b) - area(bybid[s])))[:10]
        p = rnd.choice(pool); used.add(p['box_id']); rc[p['box_id']] = (p['x'] + dx, p['y'] + dy, p['w'] + dw, p['h'] + dh)
    arms[f'control_s{seed:02d}'] = apply(boxes, drop, rc)
os.makedirs(f'{R}/arms', exist_ok=True)
allp = f'{R}/arms/all_boxes.tsv'
with open(allp, 'w') as f:
    f.write('box_id\tcrop\tx\ty\tw\th\tline\torder\tkind\n')
    for arm, bs in arms.items():
        for b in bs:
            f.write(f"{arm}|{b['box_id']}\t{b['crop']}\t{b['x']}\t{b['y']}\t{b['w']}\t{b['h']}\t{b['line']}\t{b['order']}\t{b['kind']}\n")
print({k: len(v) for k, v in list(arms.items())[:5]}, 'arms', len(arms))
kp = f'{R}/arms/all_boxes.k.tsv'
if not os.path.exists(kp) or '--reclassify' in sys.argv:
    print(subprocess.run([sys.executable, 'tools/glyph_atlas.py', 'classify', '--out', A, '--labels', f'{A}/labels.json', '--boxes', allp,
                          '--tsv', kp, '--topk', '3', '--boxes-median-h', MH], check=True, capture_output=True, text=True).stdout)
K = rd(kp)
per = collections.defaultdict(list)
for r in K:
    arm, bid = r['box'].split('|', 1); per[arm].append(r)
os.makedirs(f'{R}/outputs', exist_ok=True)
for arm, rows in per.items():
    for marks in ('signs', 'withmarks'):
        rows2 = sorted((r for r in rows if marks == 'withmarks' or r['kind'] == 'sign'), key=lambda r: (r['line'], int(r['pos'])))
        with open(f'{R}/outputs/{arm}.{marks}.tsv', 'w') as f:
            f.write('line\tpos\tsign\n'); n = collections.Counter()
            for r in rows2:
                n[r['line']] += 1; f.write(f"{r['line']}\t{n[r['line']]}\t{r['code']}\n")
print('outputs written:', len(per) * 2)
