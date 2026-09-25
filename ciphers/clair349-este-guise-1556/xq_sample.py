#!/usr/bin/env python3
"""ZX-349B step 1: sample X? and S-coded tokens from passC/passD, crop estimated positions, build contact sheets.

No per-token pixel bounding boxes exist in passC.tsv/passD.tsv (line, position, token only) -- unlike
dupuy452-carpi-1520/glyphs/classified.tsv, which has real x,y,w,h. Position is estimated proportionally: for a
token at position P of T total tokens counted by that pass on that line, x_center = (P-0.5)/T * line_width, then
a generous window (>= 260px, or 2.5x the average per-token pitch on that line, whichever is larger) is cut around
it. This is an approximation for eyeballing shape clusters, not a claimed exact crop -- each thumbnail is labelled
with the pass's own note text so a mis-centred crop can still be judged from the description plus whatever ink is
visible in the window.

Usage: python3 xq_sample.py {xq|sign} --seed 42 --n 40 --out images/atlas/xq_crops
"""
import argparse, csv, os, random, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PASSES = ['passC.tsv', 'passD.tsv']


def load_pass(name):
    path = os.path.join(HERE, name)
    with open(path) as f:
        return list(csv.DictReader(f, delimiter='\t'))


def line_token_count(rows, line):
    return sum(1 for r in rows if r['line'] == line)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('kind', choices=['xq', 'sign'])
    ap.add_argument('--seed', type=int, default=42)
    ap.add_argument('--n', type=int, default=40)
    ap.add_argument('--out', default=None)
    ap.add_argument('--cols', type=int, default=5)
    args = ap.parse_args()

    out_dir = args.out or os.path.join(HERE, 'images', 'atlas', f'{args.kind}_crops')
    os.makedirs(out_dir, exist_ok=True)

    all_rows = []
    pass_rows = {}
    for p in PASSES:
        rows = load_pass(p)
        pass_rows[p] = rows
        for r in rows:
            all_rows.append((p, r))

    if args.kind == 'xq':
        pool = [(p, r) for p, r in all_rows if r['token'] == 'X?']
    else:
        pool = [(p, r) for p, r in all_rows if r['token'].startswith('S') and r['token'][1:].isdigit()]

    random.seed(args.seed)
    sample = random.sample(pool, min(args.n, len(pool)))

    index_rows = []
    thumbs = []
    for idx, (pname, row) in enumerate(sample, start=1):
        line = row['line']
        pos = int(row['position'])
        rows = pass_rows[pname]
        total = line_token_count(rows, line)
        img_path = os.path.join(HERE, 'images', 'lines', f'line{line}.jpg')
        im = Image.open(img_path)
        w, h = im.size
        pitch = w / max(total, 1)
        x_center = (pos - 0.5) / max(total, 1) * w
        win = max(260, pitch * 2.5)
        x0 = max(0, int(x_center - win / 2))
        x1 = min(w, int(x_center + win / 2))
        crop = im.crop((x0, 0, x1, h))
        # cap thumbnail height for the montage
        max_h = 160
        if crop.height > max_h:
            ratio = max_h / crop.height
            crop = crop.resize((max(1, int(crop.width * ratio)), max_h))
        label = f'{idx:02d}'
        crop_name = f'{args.kind}{idx:02d}_{pname}_L{line}_P{pos}.jpg'
        crop.save(os.path.join(out_dir, crop_name), quality=85)
        thumbs.append((label, crop, row['token'], row['note']))
        index_rows.append({
            'idx': idx, 'pass': pname, 'line': line, 'position': pos,
            'token': row['token'], 'kind': row['kind'], 'grade': row['grade'],
            'note': row['note'], 'crop': os.path.relpath(os.path.join(out_dir, crop_name), HERE),
            'est_window_px': f'{x0}-{x1}',
        })

    idx_path = os.path.join(HERE, f'{args.kind}_index.tsv')
    with open(idx_path, 'w', newline='') as f:
        wtr = csv.DictWriter(f, fieldnames=['idx', 'pass', 'line', 'position', 'token', 'kind', 'grade', 'note', 'crop', 'est_window_px'], delimiter='\t')
        wtr.writeheader()
        wtr.writerows(index_rows)

    # contact sheet
    cols = args.cols
    rows_n = (len(thumbs) + cols - 1) // cols
    cell_w = max(t[1].width for t in thumbs) + 20
    cell_h = 160 + 40
    sheet = Image.new('RGB', (cell_w * cols, cell_h * rows_n), 'white')
    draw = ImageDraw.Draw(sheet)
    for i, (label, crop, token, note) in enumerate(thumbs):
        r, c = divmod(i, cols)
        x = c * cell_w + 10
        y = r * cell_h + 10
        sheet.paste(crop, (x, y))
        draw.text((x, y + 165), f'{label} ({token})', fill='black')
    sheet_path = os.path.join(HERE, 'images', 'atlas', f'{args.kind}_sheet.jpg')
    sheet.save(sheet_path, quality=80)

    print(f'wrote {idx_path}')
    print(f'wrote {sheet_path} ({sheet.width}x{sheet.height})')
    print(f'{len(sample)} sampled from pool of {len(pool)} (seed {args.seed})')


if __name__ == '__main__':
    main()
