#!/usr/bin/env python3
"""Third look at the positions where two blind reads of two crop sets disagree (TXE-N, M20; 9 Oct 2026).

  python3 tools/tx_shift_look.py build --s0 PASS0.tsv --s1 PASS1.tsv --crops0 DIR0 --crops1 DIR1 --signs SIGNS.tsv
          --page f178v --out DIR [--seed 1] [--rows 16] [--max-rows 48] [--scale 4]
  python3 tools/tx_shift_look.py resolve --s0 PASS0.tsv --s1 PASS1.tsv --out DIR --answers ANS.tsv [ANS2.tsv ...]
          --write OUT.tsv

Lesson answered (research/TX-IDEAS-2026-10-09.md M20; TXE-B 9 Oct 2026): a sign cut at a band edge or a segment edge
is misread in one rendering and read in another. Two crop sets whose band and segment boundaries are shifted by half
(tools/iiif_lines.py --shift-bands 0.5 --shift-segments 0.5) give every sign one central and one edge rendering;
where the two blind reads disagree, the position is doubtful by construction (not by a model's say-so), and only
those positions get a third look. A whole third re-pass repeats the first passes' errors (TX-VIEWS, phi 0.71-0.76).

build: per line, the S1 read is aligned to the S0 read with tools/reconcile_passes.py's Needleman-Wunsch (the same
disagreement set as its disagreements.tsv). Every column where they differ (substitution or indel) becomes one row:
the sign's x is estimated from its read position scaled onto the page's atlas boxes of that line (geometry only, the
box file's x/y/w/h -- no label, no truth), and a window of +-WIN px around it is cut from the S0 crop and from the S1
crop (the segment where the window sits most central; S1 crops carry iiif_lines.py's 40 px marker margin), upscaled
SCALE x, stacked as view a / view b with a red caret at the estimate. The two readings are numbered 1/2 in a seeded
random order (key.tsv, never given to the reader); a gap is offered as "no sign here". The reader sheet (sheet_NN.md)
names the row images, the left and right agreed neighbour cells, and the options; answers: 1, 2, a cell T##, or ?.
Rows beyond --max-rows keep the S0 reading (listed in key.tsv with sheet 0).
resolve: agreed columns keep the agreed sign; a disagreement takes the pick (1/2 -> that reading, possibly no sign;
a cell -> that cell; ? or unanswered -> the S0 reading). Writes line, pos, sign (tx_bench format) and picks.tsv.
Test: python3 tools/tests/test_tx_shift_look.py (offline, synthetic)."""
import argparse, csv, json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reconcile_passes import nw
from PIL import Image, ImageDraw


def load(path):
    out = {}
    with open(path, newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            out.setdefault(r['line'], []).append((int(r['pos']), r['sign']))
    return {k: [s for _, s in sorted(v)] for k, v in out.items()}


def columns(x, y):
    """[(i, j, sx, sy, agree)] for one line; i/j None on a gap."""
    return [(i, j, x[i] if i is not None else None, y[j] if j is not None else None,
             i is not None and j is not None and x[i] == y[j]) for i, j in nw(x, y)]


def line_boxes(signs, page, line_no):
    bs = []
    with open(signs, newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['page'] == page and int(r['line']) == line_no:
                bs.append((float(r['x']), float(r['w'])))
    return sorted(bs)


def est_x(k, n, boxes):
    """x centre (region px) of read position k (0-based, may be fractional) of n, scaled onto the line's boxes."""
    if not boxes:
        return None
    t = 0 if n <= 1 else k * (len(boxes) - 1) / (n - 1)
    t = min(max(t, 0), len(boxes) - 1)
    a, b = int(t), min(int(t) + 1, len(boxes) - 1)
    ca, cb = boxes[a][0] + boxes[a][1] / 2, boxes[b][0] + boxes[b][1] / 2
    return ca + (cb - ca) * (t - a)


def manifest(d):
    return json.load(open(os.path.join(d, 'manifest.json')))['iiif_lines']


def window(crops_dir, entries, band, xc, win, scale, rows_half):
    """Cut [xc-win, xc+win] from the crop of BAND whose segment holds xc most centrally; vertical: the marked line
    centre +- rows_half (S1) or the crop's band centre (S0). Returns an RGB image and the caret x in it."""
    best = None
    for e in entries:
        if e['band'] != band:
            continue
        x0, x1 = e['box'][0], e['box'][2]
        m = min(xc - x0, x1 - xc)
        if best is None or m > best[0]:
            best = (m, e)
    e = best[1]
    im = Image.open(os.path.join(crops_dir, e['crop'])).convert('RGB')
    off = e.get('marked', {}).get('margin_px', 0)
    if 'marked' in e:
        cy = e['marked']['line_centre_row']
    elif 'band_extent' in e:
        br = e['band_extent']['band_rows']
        cy = (br[0] + br[1]) // 2 - e['box'][1]
    else:
        cy = im.height // 2
    lx = int(xc - e['box'][0] + off)
    box = (max(off, lx - win), max(0, cy - rows_half), min(im.width, lx + win), min(im.height, cy + rows_half))
    w = im.crop(box)
    w = w.resize((w.width * scale, w.height * scale), Image.LANCZOS)
    return w, (lx - box[0]) * scale


def build(a):
    s0, s1 = load(a.s0), load(a.s1)
    m0, m1 = manifest(a.crops0), manifest(a.crops1)
    rng = random.Random(a.seed)
    os.makedirs(os.path.join(a.out, 'rows'), exist_ok=True)
    rows = []
    for line in sorted(set(s0) & set(s1)):
        x, y = s0[line], s1[line]
        cols = columns(x, y)
        ln = int(line.split('_L')[-1])
        boxes = line_boxes(a.signs, a.page, ln)
        last_i = -1
        for c, (i, j, sx, sy, ok) in enumerate(cols):
            if i is not None:
                last_i = i
            if ok:
                continue
            k = i if i is not None else last_i + 0.5
            left = next((cols[q][2] for q in range(c - 1, -1, -1) if cols[q][4]), 'line start')
            right = next((cols[q][2] for q in range(c + 1, len(cols)) if cols[q][4]), 'line end')
            rows.append(dict(line=line, col=c, s0=sx or '', s1=sy or '', k=k, n=len(x), band=ln,
                             xc=est_x(k, len(x), boxes), left=left, right=right))
    for n, r in enumerate(rows, 1):
        r['row'] = n
        r['sheet'] = (n - 1) // a.rows + 1 if n <= a.max_rows else 0
        opts = [('s0', r['s0']), ('s1', r['s1'])]
        rng.shuffle(opts)
        r['opt1'], r['opt2'] = opts[0], opts[1]
        if r['sheet'] and r['xc'] is not None:
            va, ca = window(a.crops0, m0, r['band'], r['xc'], a.win, a.scale, a.rows_half)
            vb, cb = window(a.crops1, m1, r['band'], r['xc'], a.win, a.scale, a.rows_half)
            W = max(va.width, vb.width) + 120
            img = Image.new('RGB', (W, va.height + vb.height + 40), (255, 255, 255))
            d = ImageDraw.Draw(img)
            img.paste(va, (110, 0)); img.paste(vb, (110, va.height + 40))
            d.text((8, va.height // 2), 'view a', fill=(0, 0, 0)); d.text((8, va.height + 40 + vb.height // 2), 'view b', fill=(0, 0, 0))
            for cx, y0 in ((110 + ca, va.height), (110 + cb, va.height + 40 + vb.height)):
                d.polygon([(cx - 12, y0 + 2), (cx + 12, y0 + 2), (cx, y0 - 14)] if y0 < img.height else
                          [(cx - 12, y0 - 1), (cx + 12, y0 - 1), (cx, y0 - 15)], fill=(220, 0, 0))
            r['img'] = os.path.join(a.out, 'rows', f'row_{n:03d}.png')
            img.save(r['img'])
    with open(os.path.join(a.out, 'key.tsv'), 'w') as f:
        f.write('row\tsheet\tline\tcol\ts0\ts1\topt1\topt2\tk\txc\n')
        for r in rows:
            f.write(f"{r['row']}\t{r['sheet']}\t{r['line']}\t{r['col']}\t{r['s0']}\t{r['s1']}\t{r['opt1'][0]}\t{r['opt2'][0]}"
                    f"\t{r['k']}\t{'' if r['xc'] is None else round(r['xc'])}\n")
    sheets = sorted({r['sheet'] for r in rows if r['sheet']})
    for s in sheets:
        p = os.path.join(a.out, f'sheet_{s:02d}.md')
        with open(p, 'w') as f:
            f.write(f'# Third look, sheet {s} (rows {", ".join(str(r["row"]) for r in rows if r["sheet"] == s)})\n\n')
            f.write('| row | image | left neighbour | right neighbour | option 1 | option 2 |\n|---|---|---|---|---|---|\n')
            for r in rows:
                if r['sheet'] != s:
                    continue
                o = lambda v: v if v else 'no sign here'
                f.write(f"| {r['row']} | {os.path.abspath(r['img'])} | {r['left']} | {r['right']} | {o(r['opt1'][1])} | "
                        f"{o(r['opt2'][1])} |\n")
    print(f'{len(rows)} disagreement rows over {len(set(s0) & set(s1))} lines; {sum(1 for r in rows if r["sheet"])} on '
          f'{len(sheets)} sheets (max {a.max_rows}); key -> {a.out}/key.tsv')
    return rows


def resolve(a):
    s0, s1 = load(a.s0), load(a.s1)
    key = {}
    with open(os.path.join(a.out, 'key.tsv'), newline='') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            key[(r['line'], int(r['col']))] = r
    ans = {}
    for p in a.answers:
        with open(p, newline='') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                ans[int(r['row'])] = r['pick'].strip()
    picks, out = [], []
    for line in sorted(set(s0) & set(s1)):
        pos = 0
        for c, (i, j, sx, sy, ok) in enumerate(columns(s0[line], s1[line])):
            if ok:
                sign, how = sx, 'agree'
            else:
                r = key[(line, c)]
                pk = ans.get(int(r['row']), '?')
                if pk in ('1', '2'):
                    who = r['opt' + pk]
                    sign, how = (sx if who == 's0' else sy), who
                elif pk.startswith('T') or pk.startswith('X_'):
                    sign, how = pk, 'third'
                else:
                    sign, how = sx, '?->s0'
                picks.append((r['row'], line, c, sx or '', sy or '', pk, how, sign or ''))
            if sign:
                pos += 1
                out.append((line, pos, sign))
    with open(a.write, 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in out:
            f.write('\t'.join(map(str, r)) + '\n')
    with open(os.path.join(a.out, 'picks.tsv'), 'w') as f:
        f.write('row\tline\tcol\ts0\ts1\tpick\tchosen\tsign\n')
        for r in picks:
            f.write('\t'.join(map(str, r)) + '\n')
    from collections import Counter
    cnt = Counter(p[6] for p in picks)
    print(f'{len(out)} signs -> {a.write}; {len(picks)} disagreements: ' + ', '.join(f'{k} {v}' for k, v in sorted(cnt.items())))
    return out, picks


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    b = sp.add_parser('build')
    for k in ('--s0', '--s1', '--crops0', '--crops1', '--signs', '--page', '--out'):
        b.add_argument(k, required=True)
    b.add_argument('--seed', type=int, default=1); b.add_argument('--rows', type=int, default=16)
    b.add_argument('--max-rows', type=int, default=48); b.add_argument('--scale', type=int, default=4)
    b.add_argument('--win', type=int, default=130, help='half window in native px (about one neighbour each side)')
    b.add_argument('--rows-half', type=int, default=80, help='half height in native px around the line centre')
    r = sp.add_parser('resolve')
    for k in ('--s0', '--s1', '--out', '--write'):
        r.add_argument(k, required=True)
    r.add_argument('--answers', nargs='+', default=[])
    a = ap.parse_args(argv)
    return build(a) if a.cmd == 'build' else resolve(a)


if __name__ == '__main__':
    main()
