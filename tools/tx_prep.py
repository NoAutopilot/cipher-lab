#!/usr/bin/env python3
"""Tile and line-crop rendering settings for transcription readers, each a named flag measured, never assumed
(LANE TX-ENGINEER TXE-D, 9 Oct 2026; ideas O1 white space, O2 darkening, O4 colour, M4 super-resolution;
research/TX-IDEAS-2026-10-09.md). Lesson it answers: the owner's Amendment 1 -- white-space deletion, darkening and
colour alteration each become a tool flag with its parameters in a manifest, tested on the known-answer benchmark
against the plain rendering, because the taxonomy's class 3 (thin strokes) is what they are supposed to attack and
nobody had measured whether they do.

    python3 tools/tx_prep.py render --page IMAGE --boxes signs.tsv --page-name f178v [--lines 1-12] --out DIR \\
        --setting plain --setting tight [--setting ...]          # DIR/<setting>/<sid>.png + DIR/<setting>/manifest.json
    python3 tools/tx_prep.py lines --crops DIR --setting S --out DIR2 [--page IMAGE --boxes signs.tsv --page-name P]
    python3 tools/tx_prep.py proxy --tiles DIR --setting S [--setting ...] --atlas ATLAS_DIR --out DIR3 \\
        --holdout f178r_ --holdout f178v_ --holdout f179r_ [--line-read labels.tsv]
    python3 tools/tx_prep.py settings                            # list every setting and its parameters

Settings (each tile's manifest row carries the source box, the tile box, the scale and the setting's parameters):
  plain       the tile as cut today: the box grown 50% (25% a side), native scale -- the control
  tight       O1: margin measured in ink -- the box's own components re-found by a local binarisation of a
              neighbourhood (components with >= half their pixels inside the box), the tile = their union with the
              box, grown 10% (5% a side, at least 2 px), then 2x LANCZOS (a 40 px sign at about 80 px)
  gamma=G     O2: out = 255 (in/255)^(1/G); G < 1 darkens the mid-tones (G 0.5, 0.7 registered)
  stretch     O2: linear 1st-99th percentile stretch of the tile to 0..255
  thicken=N   O2: local threshold (glyph_atlas.binarise), N 1-px dilations of the ink mask, the added pixels set to
              the median ink grey and composited back on the paper
  channel=R|G|B, sep, invert, false   O4: one colour channel; ink-paper separation B - R rescaled 1-99% (sign set
              so ink is dark); 255 - x; false colour (B in red, R in green, G in blue). On a single-channel (mode L)
              source every channel equals the grey and sep is flat: the manifest says `colour_non_test: true`.
  sr2, sr4    M4: LANCZOS 2x, 4x of the plain tile. No learned SR model is importable offline in this container
              (checked: cv2.dnn_superres needs opencv-contrib plus a downloaded model; torch absent) -- `srl` not built.
  combo       tight + stretch at the tight scale (2x; the sr2 of the combination is tight's own 2x, not a second one)

proxy: the read-free reader. For each setting it re-binarises every rendered tile (the same rule for all settings,
kernel scaled with the tile scale; `invert` is binarised on 255 - x, so it is identical to plain by construction and
is reported as a non-test), keeps the components with >= half their pixels inside the source box, makes the 48x48
bitmap and the size ratios (scale-free, page median height), writes a copy of the atlas with those rows replaced and
runs `glyph_atlas.py classify --topk 3` with the given --holdout prefixes. The boxes are the atlas's own (box count
= signs.tsv's exactly: no re-segmentation), mapped to line-read positions label-blind by tx_compare.box_map (width DP,
atlas/no87_map.py costs) -- the map depends on box widths only, so it is the same for every setting. Writes
DIR3/<setting>_topk.tsv (box rows) and DIR3/<setting>_bench.tsv (line, pos, sign = top-1, k2, k3) for tools/tx_bench.py.
It never opens a truth file.

lines: the same setting on whole line crops (iiif_lines manifest.json in --crops). Tone and colour settings are
applied to the crop as is; tight/combo re-cut each crop from the source page (--page, native) with the band set to the
ink extent of the line's atlas boxes (+10%) and the segment's x range trimmed to ink, then 2x LANCZOS; a crop wider than
--max-w (2500) is split in two with --overlap (100) px of overlap at the output scale, recorded in DIR2/crops_note.md.
--segments N cuts every rendered crop into N segments named <crop>_q1..qN sharing --overlap px (TXE-D2, 9 Oct 2026: a
1250 px crop at sr4 is 5000 px, over the 2500 px reading limit; four segments of 1400 px with 200 px shared), each
<= --max-w and never re-stitched; the per-crop overlap is written to crops_note.md, never typed by hand.
Offline test: tools/tests/test_tx_prep.py.
"""
import argparse, csv, json, os, re, shutil, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
Image.MAX_IMAGE_PIXELS = None

SETTINGS = {
    'plain': dict(geom='plain', scale=1, ops=[]),
    'tight': dict(geom='tight', scale=2, ops=[]),
    'gamma=0.5': dict(geom='plain', scale=1, ops=[('gamma', 0.5)]),
    'gamma=0.7': dict(geom='plain', scale=1, ops=[('gamma', 0.7)]),
    'stretch': dict(geom='plain', scale=1, ops=[('stretch', 1, 99)]),
    'thicken=1': dict(geom='plain', scale=1, ops=[('thicken', 1)]),
    'channel=R': dict(geom='plain', scale=1, ops=[('channel', 'R')]),
    'channel=G': dict(geom='plain', scale=1, ops=[('channel', 'G')]),
    'channel=B': dict(geom='plain', scale=1, ops=[('channel', 'B')]),
    'sep': dict(geom='plain', scale=1, ops=[('sep',)]),
    'invert': dict(geom='plain', scale=1, ops=[('invert',)]),
    'false': dict(geom='plain', scale=1, ops=[('false',)]),
    'sr2': dict(geom='plain', scale=2, ops=[]),
    'sr4': dict(geom='plain', scale=4, ops=[]),
    'combo': dict(geom='tight', scale=2, ops=[('stretch', 1, 99)]),
}
PLAIN_GROW = 0.25      # a side: the box grown 50%
TIGHT_GROW = 0.05      # a side: the ink extent grown 10%
COLOUR_OPS = {'channel', 'sep', 'false'}


def setting(name):
    if name in SETTINGS:
        return dict(SETTINGS[name], name=name)
    for pre, op in (('gamma=', 'gamma'), ('thicken=', 'thicken')):
        if name.startswith(pre):
            v = float(name[len(pre):]) if op == 'gamma' else int(name[len(pre):])
            return dict(geom='plain', scale=1, ops=[(op, v)], name=name)
    sys.exit(f'unknown setting {name!r}; run `tx_prep.py settings`')


# ---------------------------------------------------------------- image ops
def odd(k):
    k = int(round(k))
    return k + 1 - k % 2


def binarise(grey, rel=0.78, k=15):
    """glyph_atlas.binarise with an explicit closing kernel (tile-sized inputs need one scaled with the tile)."""
    import cv2
    bg = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, np.ones((k, k), np.uint8))
    bg = cv2.GaussianBlur(bg, (0, 0), k / 3)
    norm = grey.astype(float) / np.maximum(bg.astype(float), 1)
    return (norm < rel).astype(np.uint8)


def to_grey(im):
    return np.array(im.convert('L')) if isinstance(im, Image.Image) else im


def apply_ops(im, ops, kernel):
    """im: PIL image (L or RGB). Returns (PIL image, notes dict)."""
    import cv2
    notes = {}
    for op in ops:
        kind = op[0]
        if kind in COLOUR_OPS:
            if im.mode != 'RGB':
                notes['colour_non_test'] = True
            rgb = np.array(im.convert('RGB')).astype(float)
            if kind == 'channel':
                im = Image.fromarray(rgb[..., 'RGB'.index(op[1])].astype(np.uint8), 'L')
            elif kind == 'false':
                im = Image.fromarray(rgb[..., [2, 0, 1]].astype(np.uint8), 'RGB')
            else:   # sep: B - R, rescaled 1-99%, sign chosen so ink (dark in luminance) stays dark
                d = rgb[..., 2] - rgb[..., 0]
                lum = rgb.mean(axis=2)
                if d.std() > 0 and np.corrcoef(d.ravel(), lum.ravel())[0, 1] < 0:
                    d = -d
                lo, hi = np.percentile(d, 1), np.percentile(d, 99)
                out = np.full(d.shape, 128.0) if hi <= lo else np.clip((d - lo) / (hi - lo) * 255, 0, 255)
                if hi <= lo:
                    notes['colour_non_test'] = True
                im = Image.fromarray(out.astype(np.uint8), 'L')
            continue
        g = np.array(im.convert('L')).astype(float) if im.mode != 'RGB' else None
        if kind == 'invert':
            im = Image.fromarray(255 - np.array(im), im.mode)
        elif kind == 'gamma':
            a = np.array(im).astype(float)
            im = Image.fromarray(np.clip(255 * (a / 255) ** (1 / op[1]), 0, 255).astype(np.uint8), im.mode)
        elif kind == 'stretch':
            a = np.array(im).astype(float)
            lo, hi = np.percentile(a, op[1]), np.percentile(a, op[2])
            if hi > lo:
                im = Image.fromarray(np.clip((a - lo) / (hi - lo) * 255, 0, 255).astype(np.uint8), im.mode)
        elif kind == 'thicken':
            gg = g if g is not None else np.array(im.convert('L')).astype(float)
            ink = binarise(gg.astype(np.uint8), k=kernel)
            if ink.any():
                lvl = float(np.median(gg[ink > 0]))
                dil = cv2.dilate(ink, np.ones((3, 3), np.uint8), iterations=int(op[1]))
                add = (dil > 0) & (ink == 0)
                a = np.array(im).astype(float)
                if a.ndim == 3:
                    a[add] = np.minimum(a[add], lvl)
                else:
                    a[add] = np.minimum(a[add], lvl)
                im = Image.fromarray(a.astype(np.uint8), im.mode)
                notes['thicken_ink_grey'] = round(lvl, 1)
        else:
            sys.exit(f'unknown op {kind}')
    return im, notes


def components(ink):
    import cv2
    return cv2.connectedComponentsWithStats(ink, connectivity=8)


def own_mask(ink, bx, min_side):
    """Pixels of the components with >= half their area inside box bx=(x0,y0,x1,y1) of the ink array."""
    n, lab, st, _ = components(ink)
    x0, y0, x1, y1 = bx
    keep = np.zeros_like(ink)
    for i in range(1, n):
        if st[i, 4] < max(4, min_side ** 2):
            continue
        comp = lab == i
        inside = comp[max(0, y0):y1, max(0, x0):x1].sum()
        if inside >= 0.5 * st[i, 4]:
            keep[comp] = 1
    return keep


def tight_box(grey, b, mh):
    """O1: union of the box and its own components' extent in a neighbourhood binarisation, grown 5% a side."""
    x, y, w, h = b
    H, W = grey.shape
    nx0, ny0 = max(0, int(x - 0.5 * w)), max(0, int(y - 0.5 * h))
    nx1, ny1 = min(W, int(x + 1.5 * w)), min(H, int(y + 1.5 * h))
    nb = grey[ny0:ny1, nx0:nx1]
    ink = binarise(nb, k=odd(max(15, 0.4 * mh)))
    m = own_mask(ink, (x - nx0, y - ny0, x - nx0 + w, y - ny0 + h), 0.12 * mh)
    ex0, ey0, ex1, ey1 = x, y, x + w, y + h
    if m.any():
        ys, xs = np.nonzero(m)
        ex0, ey0 = min(ex0, nx0 + xs.min()), min(ey0, ny0 + ys.min())
        ex1, ey1 = max(ex1, nx0 + xs.max() + 1), max(ey1, ny0 + ys.max() + 1)
    gx = max(2, int(round(TIGHT_GROW * (ex1 - ex0))))
    gy = max(2, int(round(TIGHT_GROW * (ey1 - ey0))))
    return (max(0, ex0 - gx), max(0, ey0 - gy), min(W, ex1 + gx), min(H, ey1 + gy)), (ex0, ey0, ex1, ey1)


def plain_box(shape, b):
    x, y, w, h = b
    H, W = shape
    gx, gy = int(round(PLAIN_GROW * w)), int(round(PLAIN_GROW * h))
    return (max(0, x - gx), max(0, y - gy), min(W, x + w + gx), min(H, y + h + gy))


def render_tile(page_im, grey, b, st, mh):
    """-> (PIL tile, manifest row) for box b=(x,y,w,h) under setting st."""
    ink_extent = None
    if st['geom'] == 'tight':
        tb, ink_extent = tight_box(grey, b, mh)
    else:
        tb = plain_box(grey.shape, b)
    tile = page_im.crop(tb)
    sc = st['scale']
    kern = odd(max(15, 0.4 * mh))
    tile, notes = apply_ops(tile, st['ops'], kern)
    if sc != 1:
        tile = tile.resize((tile.width * sc, tile.height * sc), Image.LANCZOS)
    row = dict(source_box=list(map(int, b)), tile_box=list(map(int, tb)), scale=sc, **notes)
    if ink_extent:
        row['ink_extent'] = list(map(int, ink_extent))
    return tile, row


def read_tsv(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader((ln for ln in f if not ln.startswith('#')), delimiter='\t'))


def parse_lines(s):
    if not s:
        return None
    out = set()
    for part in s.split(','):
        a, _, b = part.partition('-')
        out |= set(range(int(a), int(b or a) + 1))
    return out


def params(st):
    return dict(geom=st['geom'], scale=st['scale'], ops=[list(o) for o in st['ops']],
                plain_grow_a_side=PLAIN_GROW, tight_grow_a_side=TIGHT_GROW, resample='LANCZOS')


# ---------------------------------------------------------------- render
def cmd_render(a):
    page_im = Image.open(a.page)
    page_im.load()
    grey = np.array(page_im.convert('L'))
    rows = [r for r in read_tsv(a.boxes) if r['page'] == a.page_name]
    want = parse_lines(a.lines)
    if want:
        rows = [r for r in rows if int(r['line']) in want]
    mh = a.median_h or float(np.median([int(r['h']) for r in rows]))
    for name in a.setting:
        st = setting(name)
        d = os.path.join(a.out, name)
        os.makedirs(d, exist_ok=True)
        man = dict(setting=name, parameters=params(st), page=a.page, page_name=a.page_name, source_mode=page_im.mode,
                   median_h=mh, tiles={})
        for r in rows:
            b = (int(r['x']), int(r['y']), int(r['w']), int(r['h']))
            tile, row = render_tile(page_im, grey, b, st, mh)
            tile.save(os.path.join(d, r['sid'] + '.png'))
            man['tiles'][r['sid']] = row
        if any(v.get('colour_non_test') for v in man['tiles'].values()):
            man['colour_non_test'] = True
        json.dump(man, open(os.path.join(d, 'manifest.json'), 'w'), indent=1)
        print(f'{name}: {len(rows)} tiles -> {d}' + (' (colour_non_test: source is single-channel)'
                                                     if man.get('colour_non_test') else ''))


# ---------------------------------------------------------------- proxy
def tile_bitmap(tile_path, row, mh, invert=False):
    """Re-binarise a rendered tile; -> (48x48 bitmap, rh, rw)."""
    import glyph_atlas
    sc = row['scale']
    g = np.array(Image.open(tile_path).convert('L'))
    if invert:
        g = 255 - g
    ink = binarise(g, k=odd(max(15, 0.4 * mh * sc)))
    tx0, ty0 = row['tile_box'][:2]
    x, y, w, h = row['source_box']
    bx = ((x - tx0) * sc - 2 * sc, (y - ty0) * sc - 2 * sc, (x - tx0 + w) * sc + 2 * sc, (y - ty0 + h) * sc + 2 * sc)
    m = own_mask(ink, tuple(int(v) for v in bx), 0.12 * mh * sc)
    if not m.any():
        bx0, by0, bx1, by1 = (max(0, int(v)) for v in bx)
        m = np.zeros_like(ink)
        m[by0:by1, bx0:bx1] = ink[by0:by1, bx0:bx1]
    if not m.any():
        return np.zeros((glyph_atlas.BM, glyph_atlas.BM), np.uint8), h / mh, w / mh
    ys, xs = np.nonzero(m)
    sub = m[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    return glyph_atlas.bitmap(sub), sub.shape[0] / (mh * sc), sub.shape[1] / (mh * sc)


def cmd_proxy(a):
    import glyph_atlas, tx_compare
    signs = read_tsv(os.path.join(a.atlas, 'signs.tsv'))
    idx = {r['sid']: i for i, r in enumerate(signs)}
    bms = np.load(os.path.join(a.atlas, 'bitmaps.npz'))
    os.makedirs(a.out, exist_ok=True)
    L = read_tsv(a.line_read)
    for name in a.setting:
        d = os.path.join(a.tiles, name)
        man = json.load(open(os.path.join(d, 'manifest.json')))
        mh = man['median_h']
        tmp = tempfile.mkdtemp(prefix='txprep_')
        try:
            S = np.array(bms['signs'])
            rows = [dict(r) for r in signs]
            for sid, row in man['tiles'].items():
                bm, rh, rw = tile_bitmap(os.path.join(d, sid + '.png'), row, mh, invert=(name == 'invert'))
                i = idx[sid]
                S[i] = bm
                rows[i]['rh'], rows[i]['rw'] = f'{rh:.3f}', f'{rw:.3f}'
            np.savez_compressed(os.path.join(tmp, 'bitmaps.npz'), signs=S, marks=bms['marks'])
            cols = list(signs[0].keys())
            with open(os.path.join(tmp, 'signs.tsv'), 'w') as f:
                f.write('\t'.join(cols) + '\n')
                for r in rows:
                    f.write('\t'.join(str(r[c]) for c in cols) + '\n')
            for fn in ('marks.tsv', 'clusters.tsv'):
                shutil.copy(os.path.join(a.atlas, fn), tmp)
            topk = os.path.join(a.out, f'{name}_topk.tsv')
            argv = ['classify', '--out', tmp, '--labels', a.labels or os.path.join(a.atlas, 'labels.json'),
                    '--page', man['page_name'], '--tsv', topk, '--topk', '3']
            for h in a.holdout or []:
                argv += ['--holdout', h]
            glyph_atlas.main(argv)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)
        tk = {r['box']: r for r in read_tsv(topk)}
        # only the rendered boxes' lines: the other lines of the page keep the stored bitmaps and are not this run's
        lines = sorted({f"{man['page_name']}_L{int(tk[s]['line']):02d}" for s in man['tiles'] if s in tk}
                       & {r['line'] for r in L})
        bp = tx_compare.box_map(signs, L, lines)
        out = []
        for r in bp:
            if not r['sid']:
                continue
            sids = r['sid'].split('+')
            sid = max(sids, key=lambda s: int(signs[idx[s]]['w']))   # 2:1 -> the wider box's code
            t = tk.get(sid)
            if t is None:
                continue
            out.append(dict(line=r['line'], pos=r['pos'], sign=t['k1'], k2=t.get('k2', ''), k3=t.get('k3', ''),
                            box=sid, op=r['op']))
        bench = os.path.join(a.out, f'{name}_bench.tsv')
        with open(bench, 'w') as f:
            f.write('line\tpos\tsign\tk2\tk3\tbox\top\n')
            for r in out:
                f.write('\t'.join(str(r[c]) for c in ('line', 'pos', 'sign', 'k2', 'k3', 'box', 'op')) + '\n')
        print(f'{name}: {len(tk)} boxes, {len(out)} positions -> {bench}')


# ---------------------------------------------------------------- lines
def cmd_lines(a):
    st = setting(a.setting)
    man = json.load(open(os.path.join(a.crops, 'manifest.json')))
    entries = man['iiif_lines'] if isinstance(man, dict) and 'iiif_lines' in man else man
    if a.only:
        entries = [e for e in entries if any(e['crop'].startswith(p) for p in a.only)]
    os.makedirs(a.out, exist_ok=True)
    out_man, notes = [], []
    page_im = grey = boxes = None
    if st['geom'] == 'tight':
        if not (a.page and a.boxes and a.page_name):
            sys.exit('lines --setting tight/combo needs --page, --boxes and --page-name (re-cut from the native page)')
        page_im = Image.open(a.page)
        page_im.load()
        grey = np.array(page_im.convert('L'))
        boxes = [r for r in read_tsv(a.boxes) if r['page'] == a.page_name]
    for e in entries:
        src = os.path.join(a.crops, e['crop'])
        stem = os.path.splitext(e['crop'])[0]
        if st['geom'] != 'tight':
            im = Image.open(src)
            im, nt = apply_ops(im, st['ops'], odd(15 * max(1, im.height / 70)))
            if st['scale'] != 1:
                im = im.resize((im.width * st['scale'], im.height * st['scale']), Image.LANCZOS)
            parts = [(im, None)]
        else:
            # native coords: the crop box minus the source region's offset (iiif_lines manifest)
            mo = re.search(r'/(\d+),(\d+),\d+,\d+/full/', e.get('source_url', ''))
            ox, oy = (int(mo.group(1)), int(mo.group(2))) if mo else (0, 0)
            x0, y0, x1, y1 = e['box']
            x0, x1, y0, y1 = x0 - ox, x1 - ox, y0 - oy, y1 - oy
            sx0, sx1 = x0, x1
            line_no = int(stem.split('_L')[1][:2])
            lb = [r for r in boxes if int(r['line']) == line_no]
            seg = [r for r in lb if int(r['x']) + int(r['w']) > sx0 and int(r['x']) < sx1]
            if seg:
                ey0 = min(int(r['y']) for r in lb)
                ey1 = max(int(r['y']) + int(r['h']) for r in lb)
                gy = max(2, int(round(TIGHT_GROW * (ey1 - ey0))))
                ex0 = max(sx0, min(int(r['x']) for r in seg) - 4)
                ex1 = min(sx1, max(int(r['x']) + int(r['w']) for r in seg) + 4)
                tb = (ex0, max(0, ey0 - gy), ex1, min(grey.shape[0], ey1 + gy))
            else:
                tb = (sx0, y0, sx1, y1)
            im = page_im.crop(tb)
            im, nt = apply_ops(im, st['ops'], odd(15))
            im = im.resize((im.width * st['scale'], im.height * st['scale']), Image.LANCZOS)
            parts = [(im, tb)]
        if a.segments and a.segments > 1:
            # TXE-D2: N equal segments sharing --overlap px each, every one under --max-w (never re-stitched)
            im, n = parts[0][0], a.segments
            w = -(-(im.width + (n - 1) * a.overlap) // n)
            if w > a.max_w:
                sys.exit(f'{stem}: {n} segments of {w} px exceed --max-w {a.max_w}; raise --segments')
            xs = [min(k * (w - a.overlap), im.width - w) for k in range(n)]
            parts = [(im.crop((x, 0, x + w, im.height)), f'_q{k + 1}') for k, x in enumerate(xs)]
            notes.append(f'{stem}: {im.width} px at the output scale cut into {n} segments {stem}_q1..q{n} of {w} px, '
                         f'neighbours sharing {w - (xs[1] - xs[0])}-{w - (xs[-1] - xs[-2])} px '
                         f'({(w - (xs[-1] - xs[-2])) / st["scale"]:.0f}-{(w - (xs[1] - xs[0])) / st["scale"]:.0f} px native)')
        elif parts[0][0].width > a.max_w:
            im = parts[0][0]
            half = (im.width + a.overlap) // 2
            parts = [(im.crop((0, 0, half, im.height)), 'a'), (im.crop((im.width - half, 0, im.width, im.height)), 'b')]
            notes.append(f'{stem}: {im.width} px at the output scale > {a.max_w}; split into {stem}a/{stem}b with '
                         f'{a.overlap} px overlap ({a.overlap / st["scale"]:.0f} px native)')
        for k, (im, tag) in enumerate(parts):
            fn = stem + (tag if isinstance(tag, str) else '') + '.png'
            im.save(os.path.join(a.out, fn))
            out_man.append(dict(crop=fn, source_crop=e['crop'], setting=a.setting, parameters=params(st),
                                width=im.width, height=im.height,
                                native_box=list(map(int, parts[0][1])) if isinstance(parts[0][1], tuple) else None))
    json.dump(out_man, open(os.path.join(a.out, 'manifest.json'), 'w'), indent=1)
    with open(os.path.join(a.out, 'crops_note.md'), 'w') as f:
        f.write(f'Crops rendered with tools/tx_prep.py lines --setting {a.setting} ({len(out_man)} files).\n')
        f.write(f'Scale: {st["scale"]}x native' + (' (band re-cut to the ink extent of the line)' if st['geom'] == 'tight'
                                                    else ' relative to the input crops') + '.\n')
        for n in notes:
            f.write(n + '\n')
    print(f'lines {a.setting}: {len(out_man)} crops -> {a.out}; {len(notes)} split')


def cmd_settings(a):
    for k, v in SETTINGS.items():
        print(f'{k}\t{json.dumps(params(dict(v, name=k)))}')


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)
    r = sp.add_parser('render')
    r.add_argument('--page', required=True); r.add_argument('--boxes', required=True)
    r.add_argument('--page-name', required=True); r.add_argument('--out', required=True)
    r.add_argument('--setting', action='append', required=True)
    r.add_argument('--lines', help='line numbers, e.g. 1-12 (default all)')
    r.add_argument('--median-h', type=float, help='page median sign height px (default: median box height)')
    p = sp.add_parser('proxy')
    p.add_argument('--tiles', required=True); p.add_argument('--setting', action='append', required=True)
    p.add_argument('--atlas', required=True); p.add_argument('--labels')
    p.add_argument('--out', required=True); p.add_argument('--holdout', action='append')
    p.add_argument('--line-read', default='benchmark-tx/outputs/birago1572-no87/labels.tsv')
    li = sp.add_parser('lines')
    li.add_argument('--crops', required=True); li.add_argument('--setting', required=True)
    li.add_argument('--out', required=True); li.add_argument('--only', action='append', help='crop name prefix')
    li.add_argument('--page'); li.add_argument('--boxes'); li.add_argument('--page-name')
    li.add_argument('--max-w', type=int, default=2500); li.add_argument('--overlap', type=int, default=100)
    li.add_argument('--segments', type=int, default=0,
                    help='cut every rendered crop into N segments sharing --overlap px (TXE-D2: 4 at sr4), each <= --max-w')
    sp.add_parser('settings')
    a = ap.parse_args(argv)
    return {'render': cmd_render, 'proxy': cmd_proxy, 'lines': cmd_lines, 'settings': cmd_settings}[a.cmd](a)


if __name__ == '__main__':
    main()
