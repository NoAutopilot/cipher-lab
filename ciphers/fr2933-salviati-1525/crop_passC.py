#!/usr/bin/env python3
"""Pass-C crops: for each (line,pos) in recon_box_f55v/disagreements.tsv, crop the box (keyed off the
integer position in f55v_boxes.tsv -- a split position like 8.5 shares its parent box, e.g. pos 8) at 5x
zoom from glyphs/crops/f55v.png, padded to include the immediate left/right neighbour boxes on the same
line for context. Writes passC_crops/L<line>_P<pos>.png. Blind script: reads only line/pos, never the
passA/passB code columns, so it carries no information about either pass's call into the crop images.
"""
import csv, os, math
from PIL import Image

ZOOM = 5
PAD_PX = 12  # native-resolution padding around the box before zoom, to show a little neighbour ink

boxes = {}  # line -> list of (pos_float, x, y, w, h)
with open('f55v_boxes.tsv') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        boxes.setdefault(int(r['line']), []).append(
            (float(r['pos']), int(r['x']), int(r['y']), int(r['w']), int(r['h']))
        )
for line in boxes:
    boxes[line].sort(key=lambda t: t[0])

im = Image.open('glyphs/crops/f55v.png')
W, H = im.size

os.makedirs('passC_crops', exist_ok=True)

rows = list(csv.DictReader(open('recon_box_f55v/disagreements.tsv'), delimiter='\t'))
manifest = []
for r in rows:
    line = int(r['line'])
    pos = float(r['pos'])
    parent_pos = math.floor(pos)
    line_boxes = boxes.get(line, [])
    # exact match first (integer position), else the box whose integer pos equals parent_pos
    match = None
    for bp, x, y, w, h in line_boxes:
        if bp == pos or int(bp) == parent_pos:
            match = (bp, x, y, w, h)
            break
    if match is None:
        manifest.append((line, r['pos'], 'NO_BOX_FOUND', ''))
        continue
    bp, x, y, w, h = match
    idx = line_boxes.index(match)
    prev_b = line_boxes[idx - 1] if idx > 0 else None
    next_b = line_boxes[idx + 1] if idx + 1 < len(line_boxes) else None
    x0 = x - PAD_PX
    y0 = y - PAD_PX
    x1 = x + w + PAD_PX
    y1 = y + h + PAD_PX
    if prev_b:
        x0 = min(x0, prev_b[1] + prev_b[3] - 4)
    if next_b:
        x1 = max(x1, next_b[1] + 4)
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(W, x1), min(H, y1)
    crop = im.crop((x0, y0, x1, y1))
    crop = crop.resize((crop.width * ZOOM, crop.height * ZOOM), Image.LANCZOS)
    fname = f'passC_crops/L{line}_P{r["pos"]}.png'
    crop.save(fname)
    manifest.append((line, r['pos'], fname, f'box x{x},y{y},w{w},h{h} parent_pos={bp}'))

with open('passC_crops/manifest.tsv', 'w') as f:
    f.write('line\tpos\tfile\tnote\n')
    for row in manifest:
        f.write('\t'.join(str(c) for c in row) + '\n')

print(f'{len(rows)} disagreement rows -> passC_crops/, manifest passC_crops/manifest.tsv')
missing = [m for m in manifest if m[2] == 'NO_BOX_FOUND']
if missing:
    print(f'{len(missing)} rows had no matching box: {missing}')
