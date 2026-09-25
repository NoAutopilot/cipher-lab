import csv, sys, json, cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

boxes = {r['box']: r for r in csv.DictReader(open('f57v_boxes.tsv'), delimiter='\t')}
types = json.load(open('atlas_review/f57v_types.json'))
img = cv2.imread('glyphs/crops/f57v.png', cv2.IMREAD_GRAYSCALE)
SCALE = 8
MARGIN = 6
CELL_W, CELL_H = 130, 170
FONT = ImageFont.load_default()

def crop_sid(sid):
    r = boxes[sid]
    x, y, w, h = int(r['x']), int(r['y']), int(r['w']), int(r['h'])
    y0, y1 = max(0, y - MARGIN), min(img.shape[0], y + h + MARGIN)
    x0, x1 = max(0, x - MARGIN), min(img.shape[1], x + w + MARGIN)
    sub = img[y0:y1, x0:x1]
    sub = cv2.resize(sub, None, fx=SCALE, fy=SCALE, interpolation=cv2.INTER_CUBIC)
    return Image.fromarray(sub)

def montage(group, out, max_per_type=6, cols=6):
    cells = []  # (label, img)
    for t in group:
        sids = types.get(t, [])
        if not sids:
            print('MISSING TYPE', t); continue
        for sid in sids[:max_per_type]:
            cells.append((f"{t} {sid.split('_',1)[1]}", crop_sid(sid)))
        # spacer marker
    rows = (len(cells) + cols - 1) // cols
    canvas = Image.new('L', (cols * CELL_W, rows * CELL_H), 255)
    draw = ImageDraw.Draw(canvas)
    for i, (label, im) in enumerate(cells):
        r, c = divmod(i, cols)
        # fit image into cell
        iw, ih = im.size
        maxw, maxh = CELL_W - 8, CELL_H - 30
        sc = min(maxw / iw, maxh / ih, 1.0)
        im2 = im.resize((max(1,int(iw*sc)), max(1,int(ih*sc))))
        x0 = c * CELL_W + (CELL_W - im2.width) // 2
        y0 = r * CELL_H + 4
        canvas.paste(im2, (x0, y0))
        draw.text((c * CELL_W + 4, r * CELL_H + CELL_H - 24), label, fill=0, font=FONT)
        draw.rectangle([c*CELL_W, r*CELL_H, c*CELL_W+CELL_W-1, r*CELL_H+CELL_H-1], outline=180)
    canvas.save(out)
    print('wrote', out, canvas.size, len(cells), 'cells')

if __name__ == '__main__':
    name = sys.argv[1]
    group = sys.argv[2:]
    montage(group, f'atlas_review/{name}.png')
