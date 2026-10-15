#!/usr/bin/env python3
"""VIV-GSPLIT3D (PREREG-VIVGSPLIT3 Addendum C): look and check sheets for hand-cutting the f.191r label-g tiles by eye.

  VIVGSPLIT3_SCRATCH=DIR python3 panels191.py targets            # -> DIR/targets191.tsv: the 116 g tokens of tx/viv63_f191/rec.tsv, priority lines first
  VIVGSPLIT3_SCRATCH=DIR python3 panels191.py sheets K0 K1 OUT    # look sheet of targets K0..K1-1 (windows of the VIV-F191 crop, 10 px ruler)
  VIVGSPLIT3_SCRATCH=DIR python3 panels191.py check STAGE OUT     # check sheet: each staged eye box (gid x w) drawn on its window
Crops: DIR/f191 (the VIV-F191 command, images/p63/manifest_vivf191.json); units: DIR/atlas191 (glyph_atlas segment --median-h pool on those crops).
The pointer (a tick over the crop) comes from the token's VIV-GSPLIT map units (tx/vivgsplit/map_f191r.tsv, any op) or, when it has none, from its
nearest mapped neighbours; it only points the eye. The box is drawn by eye and logged in tx/vivgsplit3/boxes_handcut_f191r.tsv.
"""
import csv, os, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
SCR = os.environ.get('VIVGSPLIT3_SCRATCH', '')
PRI = set(range(8, 17)) | set(range(29, 33))
HALF = 170


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t', quoting=csv.QUOTE_NONE))


def band(path):
    """y, h of a box on an f.191r crop: 82 px tall from 25 px above the crop's x-height peak (row ink profile), so the g body and its lower
    loop sit inside (the f.191r crops are 215-240 px tall with the line in the middle; the other leaves' fixed band does not fit them)."""
    import numpy as np
    a = 255 - np.asarray(Image.open(path).convert('L'), float)
    y = max(0, int(np.argmax(a.mean(1))) - 25)
    return y, min(82, a.shape[0] - y)


def targets():
    rec = rd(os.path.join(FOLD, 'tx', 'viv63_f191', 'rec.tsv'))
    sg = {r['sid']: r for r in rd(os.path.join(SCR, 'atlas191', 'signs.tsv'))}
    mp = rd(os.path.join(FOLD, 'tx', 'vivgsplit', 'map_f191r.tsv'))
    man = {e['crop'][:-4]: e['box'] for e in __import__('json').load(open(os.path.join(SCR, 'f191', 'manifest.json')))['iiif_lines']}
    units = {}
    for m in mp:
        if m['sid'] in sg:
            units.setdefault((m['line'][6:], m['pos']), []).append(sg[m['sid']])
    def gx(u):  # source-x centre of a unit
        return man['c196_f191r_dr_' + u['page'][6:]][0] + int(u['x']) + int(u['w']) / 2
    byl = {}
    for r in rec:
        byl.setdefault(r['line'], []).append(r)
    out = []
    for r in rec:
        if r['sign'] != 'g':
            continue
        toks = byl[r['line']]; i = toks.index(r)
        u = units.get((r['line'], r['pos']))
        if u:
            xs = sum(gx(v) for v in u) / len(u); how = 'map'
        else:
            lo = next((gx(units[(r['line'], t['pos'])][0]) for t in reversed(toks[:i]) if (r['line'], t['pos']) in units), None)
            hi = next((gx(units[(r['line'], t['pos'])][0]) for t in toks[i + 1:] if (r['line'], t['pos']) in units), None)
            xs = (lo + hi) / 2 if lo and hi else (lo or hi); how = 'interp'
        segs = sorted(k for k in man if k.startswith('c196_f191r_dr_' + r['line'] + '_'))
        seg = min(segs, key=lambda k: abs((man[k][0] + man[k][2]) / 2 - xs) if man[k][0] + 60 <= xs <= man[k][2] - 60 else 1e9 + abs(man[k][0] - xs))
        ctx = ' '.join(('[' + t['sign'] + ']') if j == i else t['sign'] for j, t in enumerate(toks) if abs(j - i) <= 5)
        out.append(dict(gid=f"{r['line']}:{r['pos']}", line=r['line'], pos=r['pos'], crop=seg, px=int(xs - man[seg][0]), how=how, ctx=ctx,
                        pri=int(int(r['line'][1:]) in PRI)))
    out.sort(key=lambda t: (-t['pri'], int(t['line'][1:]), int(t['pos'])))
    with open(os.path.join(SCR, 'targets191.tsv'), 'w') as f:
        cols = list(out[0]); f.write('\t'.join(cols) + '\n')
        for t in out:
            f.write('\t'.join(str(t[c]) for c in cols) + '\n')
    print(len(out), 'priority', sum(t['pri'] for t in out), 'interp', sum(t['how'] == 'interp' for t in out))


def font(n=13):
    try:
        return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', n)
    except Exception:
        return ImageFont.load_default()


def cell(t, box=None, half=None):
    HALF = half or globals()['HALF']
    im = Image.open(os.path.join(SCR, 'f191', t['crop'] + '.jpg')).convert('RGB'); W, H = im.size
    px = int(t['px']); a = max(0, min(W - 2 * HALF, px - HALF)); c = im.crop((a, 0, a + 2 * HALF, H)).resize((2 * HALF * 3 // 2, H * 3 // 2))
    k = 1.5
    cv = Image.new('RGB', (c.size[0] + 4, c.size[1] + 52), 'white'); d = ImageDraw.Draw(cv)
    d.text((2, 0), f"{t['gid']}  {t['ctx']}", fill=(0, 0, 120), font=font())
    for xx in range(-(-a // 10) * 10, a + 2 * HALF, 10):
        X = (xx - a) * k; L = 12 if xx % 50 == 0 else 5
        d.line([(X, 34 - L), (X, 34)], fill='black')
        if xx % 50 == 0:
            d.text((X + 1, 17), str(xx), fill='black', font=ImageFont.load_default())
    d.polygon([((px - a) * k - 5, 36), ((px - a) * k + 5, 36), ((px - a) * k, 47)], fill=(0, 90, 230))
    cv.paste(c, (0, 50))
    if box:
        x, w = box; y, h = band(os.path.join(SCR, 'f191', t['crop'] + '.jpg'))
        ImageDraw.Draw(cv).rectangle([(x - a) * k, 50 + y * k, (x + w - a) * k, 50 + (y + h) * k], outline=(230, 120, 0), width=2)
    return cv


def sheet(cells, out, cols=2):
    cw = max(c.size[0] for c in cells) + 8; ch = max(c.size[1] for c in cells) + 6
    sh = Image.new('RGB', (cols * cw, -(-len(cells) // cols) * ch), 'white')
    for i, c in enumerate(cells):
        sh.paste(c, ((i % cols) * cw, (i // cols) * ch))
    sh.save(out); print(out, len(cells), sh.size)


if __name__ == '__main__':
    if sys.argv[1] == 'targets':
        targets()
    elif sys.argv[1] == 'sheets':
        tg = rd(os.path.join(SCR, 'targets191.tsv'))[int(sys.argv[2]):int(sys.argv[3])]
        sheet([cell(t) for t in tg], sys.argv[4], cols=int(sys.argv[5]) if len(sys.argv) > 5 else 3)
    elif sys.argv[1] == 'check':
        tg = {t['gid']: t for t in rd(os.path.join(SCR, 'targets191.tsv'))}
        st = [l.split() for l in open(sys.argv[2]) if l.strip() and not l.startswith('#')]
        sheet([cell(dict(tg[g], px=int(x) + int(w) // 2), (int(x), int(w)), half=90) for g, x, w, *_ in st], sys.argv[3], cols=5)
