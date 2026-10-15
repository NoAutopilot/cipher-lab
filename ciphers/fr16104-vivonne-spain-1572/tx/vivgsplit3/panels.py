#!/usr/bin/env python3
"""VIV-GSPLIT3 (PREREG-VIVGSPLIT3.md): targets (label-g truth-f + seeded truth-r sample) and look sheets for hand-cutting by eye.

  VIVGSPLIT3_SCRATCH=DIR python3 panels.py targets          # -> tx/vivgsplit3/targets.tsv (no image read)
  VIVGSPLIT3_SCRATCH=DIR python3 panels.py sheets --cls f   # look sheets: a window of the line crop per target, ruler every 20 px
The window only points the eye (proportional x estimate from the token's position in its truth line); the box is drawn by eye and
logged in boxes_handcut.tsv in the crop's own pixel coordinates. f.211r crops: band L10 of the cut duplicated L09 and was dropped, so
truth L10 = crop L11 (images/manifest.json "viv70"). f.202r crops live in $VIVGSPLIT3_SCRATCH/p67c (manifest "viv67c").
"""
import csv, collections, json, os, random, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
REPO = os.path.abspath(os.path.join(FOLD, '..', '..')); BT = os.path.join(REPO, 'benchmark-tx'); IM = os.path.join(FOLD, 'images')
SCR = os.environ.get('VIVGSPLIT3_SCRATCH', '')
SEED, RCAP = 20261015, 20
TRUTH = {'f102r': 'vivonne1573-f102r-dev2', 'f103r': 'vivonne1573-f103r-confirm2', 'f201r': 'vivonne1573-f201r-dev',
         'f201v': 'vivonne1573-f201v-dev', 'f211r': 'vivonne1573-f211r-dev', 'f202r': 'vivonne1573-f202r-dev', 'f211v': 'vivonne1573-f211v-dev'}
LEAVES = list(TRUTH)


def crops(leaf):
    """{line: [(seg, path, x0, x1, scale)]} in source-x coordinates."""
    d, man, pre = {'f102r': (IM, 'manifest.json', 'c105_f102r'), 'f103r': (IM, 'manifest.json', 'c106_f103r'),
                   'f201r': (os.path.join(IM, 'p67', 'cut'), 'manifest.json', 'c206_f201r'),
                   'f201v': (os.path.join(IM, 'p67b'), 'manifest.json', 'c207_f201v'),
                   'f211r': (os.path.join(IM, 'p70'), 'manifest.json', 'c216_f211r'),
                   'f202r': (os.path.join(SCR, 'p67c'), 'manifest.json', 'c207_f202r'),
                   'f211v': (os.path.join(IM, 'p70c'), 'manifest.json', 'c217_f211v')}[leaf]
    ents = json.load(open(os.path.join(d, man)))['iiif_lines']
    out = collections.defaultdict(list)
    for e in ents:
        c = e['crop']
        if not c.startswith(pre + '_L'):
            continue
        ln = int(c.split('_L')[1][:2]); sg = int(c.split('_s')[-1].split('.')[0])
        if leaf == 'f211r':
            if ln == 10:
                continue
            if ln > 10:
                ln -= 1
        p = os.path.join(d, c)
        w = Image.open(p).size[0]
        x0, x1 = e['box'][0], e['box'][2]
        out[ln].append((sg, p, x0, x1, w / (x1 - x0)))
    for ln in out:
        out[ln].sort()
    return out


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def targets():
    rows = []
    for leaf in LEAVES:
        t = rd(os.path.join(BT, TRUTH[leaf] + '.truth.tsv'))
        f = [r for r in t if r['ref_sign'] == 'g' and r['plain'] == 'f']
        r_ = sorted([r for r in t if r['ref_sign'] == 'g' and r['status'] == 'scored' and not r['flag'] and r['plain'] == 'r'],
                    key=lambda r: (r['line'], float(r['pos'])))
        if len(r_) > RCAP:
            r_ = random.Random(SEED).sample(r_, RCAP)
        for c, lst in (('f', f), ('r', sorted(r_, key=lambda r: (r['line'], float(r['pos']))))):
            for r in lst:
                rows.append(dict(leaf=leaf, line=r['line'], tpos=r['pos'], cls=c, plain=r['plain']))
    with open(os.path.join(HERE, 'targets.tsv'), 'w') as fh:
        fh.write('tid\tleaf\tline\ttpos\tcls\tplain\n')
        for i, r in enumerate(rows):
            fh.write(f"{r['cls']}{i:03d}\t{r['leaf']}\t{r['line']}\t{r['tpos']}\t{r['cls']}\t{r['plain']}\n")
    print(collections.Counter((r['leaf'], r['cls']) for r in rows))


def window(leaf, line, tpos, cr, truth, nb=6):
    toks = sorted([r for r in truth if r['line'] == line], key=lambda r: float(r['pos']))
    idx = [i for i, r in enumerate(toks) if r['pos'] == tpos][0]
    ln = int(line.split('_L')[1])
    segs = cr[ln]
    lo, hi = segs[0][2], segs[-1][3]
    xs = lo + (idx + 0.5) / len(toks) * (hi - lo)
    best = min(segs, key=lambda s: abs((s[2] + s[3]) / 2 - xs) if s[2] <= xs <= s[3] else 1e9 + abs(s[2] - xs))
    sg, p, x0, x1, sc = best
    cx = (xs - x0) * sc
    ctx = ' '.join(('[' + r['ref_sign'] + ']') if i == idx else r['ref_sign'] for i, r in enumerate(toks) if abs(i - idx) <= nb)
    pl = ''.join(('[' + (r['plain'] or '.') + ']') if i == idx else (r['plain'] or '.') for i, r in enumerate(toks) if abs(i - idx) <= nb)
    return p, cx, ctx, pl


def sheets(cls, per=8, half=330, cols=1):
    tg = [r for r in rd(os.path.join(HERE, 'targets.tsv')) if r['cls'] == cls]
    if cls == 'r':  # interleave leaves so a stopped run keeps every leaf represented
        byl = collections.defaultdict(list)
        for r in tg:
            byl[r['leaf']].append(r)
        tg = [byl[l][i] for i in range(RCAP) for l in LEAVES if i < len(byl[l])]
    cache, tcache = {}, {}
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 14)
    except Exception:
        font = ImageFont.load_default()
    out = os.path.join(SCR, 'sheets'); os.makedirs(out, exist_ok=True)
    win = []
    for r in tg:
        if r['leaf'] not in cache:
            cache[r['leaf']] = crops(r['leaf']); tcache[r['leaf']] = rd(os.path.join(BT, TRUTH[r['leaf']] + '.truth.tsv'))
        p, cx, ctx, pl = window(r["leaf"], r["line"], r["tpos"], cache[r["leaf"]], tcache[r["leaf"]], 6 if half > 300 else 4)
        im = Image.open(p).convert('RGB'); w, h = im.size
        a = int(max(0, min(w - 2 * half, cx - half))); b = min(w, a + 2 * half)
        win.append((r, p, a, im.crop((a, 0, b, h)), ctx, pl))
    for k in range(0, len(win), per):
        part = win[k:k + per]
        rowsH = [max(x[3].size[1] + 58 for x in part[j:j + cols]) for j in range(0, len(part), cols)]
        sh = Image.new('RGB', (cols * (2 * half + 14), sum(rowsH)), 'white'); d = ImageDraw.Draw(sh)
        for j, (r, p, a, c, ctx, pl) in enumerate(part):
            X = (j % cols) * (2 * half + 14); y = sum(rowsH[:j // cols])
            d = ImageDraw.Draw(sh)
            _panel(sh, d, X, y, r, p, a, c, ctx, pl, font)
        fn = os.path.join(out, f'sheet_{cls}_{k // per + 1:02d}.png'); sh.save(fn); print(fn, len(part))


def _panel(sh, d, X, y, r, p, a, c, ctx, pl, font):
        if True:
            d.text((X + 4, y + 2), f"{r['tid']} {r['line']}:{r['tpos']} {os.path.basename(p)[:-4]}", fill='black', font=font)
            d.text((X + 4, y + 20), f"{ctx} | {pl}", fill=(0, 0, 120), font=font)
            y0 = y + 40
            for cxx in range(-(-a // 20) * 20, a + c.size[0], 20):
                xx = cxx - a
                L = 16 if cxx % 100 == 0 else 6
                d.line([(X + xx, y0 + 16 - L), (X + xx, y0 + 16)], fill=(0, 0, 0))
                if cxx % 100 == 0:
                    d.text((X + xx + 2, y0), str(cxx), fill='black', font=ImageFont.load_default())
            sh.paste(c, (X, y0 + 18))
            for yy in range(0, c.size[1], 20):
                d.line([(X + c.size[0], y0 + 18 + yy), (X + c.size[0] + (8 if yy % 100 == 0 else 4), y0 + 18 + yy)], fill='black')


if __name__ == '__main__':
    if sys.argv[1] == 'targets':
        targets()
    else:
        c = sys.argv[3] if len(sys.argv) > 3 else 'f'
        sheets(c, *((16, 200, 2) if c == 'r' else ()))
