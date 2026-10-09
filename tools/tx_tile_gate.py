#!/usr/bin/env python3
"""Per-cut quality gate: label every cut sign tile good / bad-crop / joined / blot before any reader sees it
(TXE-F, LANE TX-ENGINEER round 2, 9 Oct 2026; benchmark-tx/PREREG-txeng-2.md, TX-IDEAS row O3, the owner's item 3).

Lesson it answers (research/TX-TAXONOMY-2026-10-09.md class 2): on Birago no.87 the line band cuts 14% of the atlas
boxes (error 9.5% there vs 5.2% inside) and the segmenter glues 3% of positions 2:1. The question this tool measures is
which per-tile flags, computed from the page image alone, predict a position the line read gets wrong -- and only if
they do, whether re-cutting the flagged tiles helps. Every feature is read from the page image and the atlas boxes;
no sign label, decode or truth file is read by `score` or `recut`.

Subcommands
  score   --page P --out DIR/tiles.tsv: one row per atlas box of page P with features and a rule label fixed before
          any truth was opened (TXE-F brief step 1):
            ink_mass   ink pixels / box area (page Otsu threshold)
            aspect     h / w;  rh, rw from signs.tsv
            n_comp     8-connected ink components inside the box (>= 4 px each)
            edge       share of the box perimeter pixels that are ink of the box's own component (its largest)
            band       tx_taxonomy band_edge rule against the harvest crop band of the box's line: cut / near / in / -
            erosion    tools/tx_taxonomy.erosion_share (3x3 erosion survival)
            nb_touch   share of the own component's pixels lying inside a neighbouring box of the same line
            valleys    interior minima of the box's smoothed column ink profile that fall below half the lower of the
                       two flanking maxima
          label: joined   if w > 1.8 x page median sign width and valleys >= 2
                 bad-crop elif band == cut or edge > 0.3
                 blot     elif ink_mass > 0.6 and n_comp == 1 and 0.7 <= aspect <= 1.4 and h < 0.6 x page median h
                 good     otherwise
  gate    --unit U --tiles T1.tsv [T2.tsv] --box-pos BP.tsv: opens truth (only through tools/tx_bench.py's
          position_errors) AFTER tiles.tsv is committed: per label, positions flagged, how many of L's and pass A's
          wrong positions it holds, precision and recall; registered gate: non-good labels hold >= 50% of L's wrong
          positions at <= 15% of positions flagged.
  recut   --page P --tiles T --labels joined,bad-crop --unit U --box-pos BP --out DIR: joined -> split at the deepest
          valley into two tiles; bad-crop -> the box grown to its own component's full ink extent + 10%, cut from
          the page (not the band crop), neighbouring lines masked with tools/iiif_lines.mask_neighbours; blot ->
          dropped and logged with its features (DIR/<unit>/dropped.tsv). Tiles at 2x with one neighbour of context
          each side, sheets of at most --rows (24): DIR/<unit>/sheet_NN.png + sheet_NN.tsv (row, line, pos, L sign:
          the key, NEVER given to the reader).
  resolve --unit U --dir DIR --pass-out OUT.tsv: reads DIR/<unit>/reads_NN.tsv (row, sign_id, conf); a flagged
          position takes the re-read sign (X_NEW / ? / empty keep L); every other unit position keeps L.

Usage (repo root):
  python3 tools/tx_tile_gate.py score --page f178v --out benchmark-tx/txeng/gate/tiles_f178v.tsv
  python3 tools/tx_tile_gate.py gate --unit dev_tune --tiles benchmark-tx/txeng/gate/tiles_f178v.tsv
  python3 tools/tx_tile_gate.py recut --page f178v --unit dev_tune --tiles benchmark-tx/txeng/gate/tiles_f178v.tsv
Offline test: tools/tests/test_tx_tile_gate.py (synthetic page, no network, no model).
"""
import argparse
import csv
import json
import os
import re
import sys
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tx_taxonomy import erosion_share, page_origin  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = 'ciphers/nevers-birago-fr3251-1572'
D = dict(atlas=f'{T}/atlas', harvest=f'{T}/harvest', out='benchmark-tx/txeng/gate',
         line_read='benchmark-tx/outputs/birago1572-no87/labels.tsv', units='benchmark-tx/txeng/units/README.md',
         unit_dir='benchmark-tx/txeng/units', bench='BENCHMARK-TX.tsv', item='birago1572-no87')
LABELS = ('joined', 'bad-crop', 'blot', 'good')
COLS = ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'ink_mass', 'aspect', 'n_comp', 'edge', 'band',
        'erosion', 'nb_touch', 'valleys', 'own_x', 'own_y', 'own_w', 'own_h', 'label']


def path(p):
    return p if os.path.isabs(p) else os.path.join(ROOT, p)


def rd(p):
    with open(path(p), newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    os.makedirs(os.path.dirname(path(p)) or '.', exist_ok=True)
    with open(path(p), 'w', newline='') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


# ---------------------------------------------------------------- geometry
def otsu(gray):
    h = np.bincount(gray.ravel(), minlength=256).astype(float)
    p = h / h.sum()
    w0 = np.cumsum(p); m = np.cumsum(p * np.arange(256)); mt = m[-1]
    with np.errstate(divide='ignore', invalid='ignore'):
        sb = (mt * w0 - m) ** 2 / (w0 * (1 - w0))
    sb = np.nan_to_num(sb, nan=-1.0)
    top = np.where(sb >= sb.max() - 1e-9)[0]               # a flat optimum (a binary image): take its middle
    return int(round(top.mean()))


def components(mask):
    from iiif_lines import label_components
    return label_components(mask)


def col_valleys(ink, smooth=3):
    """(count, deepest column) of interior minima of the column ink profile below half the lower flanking maximum."""
    prof = ink.sum(0).astype(float)
    if len(prof) < 5:
        return 0, None
    k = np.ones(smooth) / smooth
    s = np.convolve(prof, k, mode='same')
    n, best, bestd = 0, None, -1.0
    i, W = 1, len(s)
    while i < W - 1:
        if s[i] < s[i - 1] and s[i] <= s[i + 1]:
            j = i
            while j + 1 < W and s[j + 1] == s[i]:
                j += 1
            c = (i + j) // 2
            lm, rm = s[:i].max(), s[j + 1:].max() if j + 1 < W else 0.0
            if s[c] < 0.5 * min(lm, rm):
                n += 1
                d = min(lm, rm) - s[c]
                if d > bestd:
                    bestd, best = d, c
            i = j + 1
        else:
            i += 1
    return n, best


def line_bands(harvest, page):
    """{line number: [(x0, y0, x1, y1) crop boxes in page-image coordinates]} from harvest/<page>/manifest.json."""
    mp = os.path.join(path(harvest), page, 'manifest.json')
    out = defaultdict(list)
    if not os.path.exists(mp):
        return out
    ox = oy = None
    for e in json.load(open(mp))['iiif_lines']:
        if ox is None:
            ox, oy = page_origin(e.get('source_file', ''))
        m = re.match(r'^.+_L(\d+)_s\d+\.jpg$', e['crop'])
        if m:
            x0, y0, x1, y1 = e['box']
            out[int(m.group(1))].append((x0 - ox, y0 - oy, x1 - ox, y1 - oy))
    return out


def band_rule(x, y, w, h, segs, edge_frac=0.15):
    """tools/tx_taxonomy.py geo_features' band_edge rule, on the crops of the box's own line."""
    if not segs:
        return '-'
    cx = x + w / 2.0
    holding = [s for s in segs if s[0] <= cx <= s[2]]
    s = holding[0] if holding else segs[0]
    if y < s[1] or y + h > s[3]:
        return 'cut'
    if min(y - s[1], s[3] - (y + h)) < edge_frac * (s[3] - s[1]):
        return 'near'
    return 'in'


def rule_label(f, med_w, med_h):
    if f['w'] > 1.8 * med_w and f['valleys'] >= 2:
        return 'joined'
    if f['band'] == 'cut' or f['edge'] > 0.3:
        return 'bad-crop'
    if f['ink_mass'] > 0.6 and f['n_comp'] == 1 and 0.7 <= f['aspect'] <= 1.4 and f['h'] < 0.6 * med_h:
        return 'blot'
    return 'good'


def tile_features(gray, thr, box, neighbours, segs):
    x, y, w, h = box
    H, W = gray.shape
    mg = max(w, h)                                          # context window: the own component may run outside the box
    X0, Y0, X1, Y1 = max(0, x - mg), max(0, y - mg), min(W, x + w + mg), min(H, y + h + mg)
    win = gray[Y0:Y1, X0:X1] < thr
    lab, n = components(win)
    bx0, by0 = x - X0, y - Y0
    inbox = lab[by0:by0 + h, bx0:bx0 + w]
    ink = inbox > 0
    f = dict(ink_mass=float(ink.mean()) if ink.size else 0.0, aspect=h / max(1, w))
    sub_lab, sub_n = components(win[by0:by0 + h, bx0:bx0 + w])
    sizes = np.bincount(sub_lab.ravel(), minlength=sub_n + 1)[1:]
    f['n_comp'] = int((sizes >= 4).sum())
    ids = np.bincount(inbox.ravel(), minlength=n + 1); ids[0] = 0
    own = int(ids.argmax()) if ids.sum() else 0
    if own:
        o = inbox == own
        per = np.concatenate([o[0], o[-1], o[1:-1, 0], o[1:-1, -1]]) if h > 1 and w > 1 else o.ravel()
        f['edge'] = float(per.mean())
        om = lab == own
        tot = om.sum()
        touch = 0
        for nx, ny, nw, nh in neighbours:
            a0, b0 = max(0, nx - X0), max(0, ny - Y0)
            a1, b1 = max(0, min(X1, nx + nw) - X0), max(0, min(Y1, ny + nh) - Y0)
            if a1 > a0 and b1 > b0:
                reg = om[b0:b1, a0:a1].copy()
                # pixels shared with the own box are not "into the neighbour"
                ox0, oy0 = max(a0, bx0), max(b0, by0)
                ox1, oy1 = min(a1, bx0 + w), min(b1, by0 + h)
                if ox1 > ox0 and oy1 > oy0:
                    reg[oy0 - b0:oy1 - b0, ox0 - a0:ox1 - a0] = False
                touch += int(reg.sum())
        f['nb_touch'] = touch / max(1, tot)
        ys, xs = np.where(om)
        f['own_x'], f['own_y'] = int(xs.min() + X0), int(ys.min() + Y0)
        f['own_w'], f['own_h'] = int(xs.max() - xs.min() + 1), int(ys.max() - ys.min() + 1)
    else:
        f.update(edge=0.0, nb_touch=0.0, own_x=x, own_y=y, own_w=w, own_h=h)
    f['valleys'] = col_valleys(ink)[0]
    f['erosion'] = erosion_share(gray, x, y, w, h)
    f['band'] = band_rule(x, y, w, h, segs)
    return f


def load_page(harvest, page):
    from PIL import Image
    d = os.path.join(path(harvest), page)
    src = sorted(f for f in os.listdir(d) if f.startswith('src_') and f.endswith('.jpg'))
    return np.asarray(Image.open(os.path.join(d, src[0])).convert('L'))


def score_page(signs, gray, bands):
    thr = otsu(gray)
    med_w = float(np.median([int(s['w']) for s in signs]))
    med_h = float(np.median([int(s['h']) for s in signs]))
    by_line = defaultdict(list)
    for s in signs:
        by_line[int(s['line'])].append(s)
    rows = []
    for li in sorted(by_line):
        ln = sorted(by_line[li], key=lambda s: int(s['x']))
        for i, s in enumerate(ln):
            box = tuple(int(s[k]) for k in ('x', 'y', 'w', 'h'))
            nb = [tuple(int(ln[j][k]) for k in ('x', 'y', 'w', 'h')) for j in (i - 1, i + 1) if 0 <= j < len(ln)]
            f = tile_features(gray, thr, box, nb, bands.get(li, []))
            f.update(sid=s['sid'], page=s['page'], line=s['line'], pos=s.get('pos', ''), x=box[0], y=box[1], w=box[2],
                     h=box[3], rh=s.get('rh', ''), rw=s.get('rw', ''))
            f['label'] = rule_label(f, med_w, med_h)
            rows.append(f)
    return rows, dict(thr=thr, med_w=med_w, med_h=med_h)


def fmt(r):
    o = dict(r)
    for k in ('ink_mass', 'aspect', 'edge', 'nb_touch', 'erosion'):
        v = o.get(k)
        o[k] = '' if v is None else '%.3f' % v
    return o


def cmd_score(a):
    signs = [s for s in rd(os.path.join(a.atlas, 'signs.tsv')) if s['page'] == a.page]
    if not signs:
        sys.exit('tx_tile_gate: no atlas boxes for page %s' % a.page)
    gray = load_page(a.harvest, a.page)
    rows, meta = score_page(signs, gray, line_bands(a.harvest, a.page))
    wr(a.out, COLS, [fmt(r) for r in rows])
    c = Counter(r['label'] for r in rows)
    print('score %s: %d boxes (otsu %d, median w %.0f h %.0f) -> %s' % (a.page, len(rows), meta['thr'], meta['med_w'],
                                                                         meta['med_h'], a.out))
    print('  labels: ' + ', '.join('%s %d (%.1f%%)' % (k, c[k], 100.0 * c[k] / len(rows)) for k in LABELS))
    return rows


# ---------------------------------------------------------------- positions
def unit_lines(readme, unit):
    from tx_compare import unit_lines as ul
    return ul(path(readme), unit)


def box_positions(a, lines):
    """Label-blind box <-> position map (tools/tx_compare.py box_map: DP over box widths only)."""
    from tx_compare import box_map
    if a.box_pos and os.path.exists(path(a.box_pos)):
        rows = rd(a.box_pos)
        if set(lines) <= {r['line'] for r in rows}:
            return [r for r in rows if r['line'] in lines]
    signs = rd(os.path.join(a.atlas, 'signs.tsv'))
    L = rd(a.line_read)
    rows = box_map(signs, L, sorted({r['line'] for r in L}))       # every line of the line read, once
    if a.box_pos:
        wr(a.box_pos, ['sid', 'line', 'pos', 'op'], rows)
    return [r for r in rows if r['line'] in lines]


def position_labels(bp, tiles):
    """{(line, pos): label} -- a 2:1 position takes the first non-good of its boxes (LABELS order); no box -> '-'."""
    lab = {r['sid']: r['label'] for r in tiles}
    out = {}
    for r in bp:
        ls = [lab.get(s) for s in r['sid'].split('+') if s]
        ls = [x for x in ls if x]
        out[(r['line'], r['pos'])] = min(ls, key=LABELS.index) if ls else '-'
    return out


def cmd_gate(a):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import tx_bench
    lines = set(unit_lines(a.units, a.unit))
    tiles = [r for t in a.tiles for r in rd(t)]
    bp = box_positions(a, lines)
    plab = position_labels(bp, tiles)
    truth = [r for r in tx_bench.read_tsv(path(os.path.join(os.path.dirname(a.bench), next(
        i['truth'] for i in tx_bench.read_tsv(path(a.bench)) if i['item'] == a.item))))]
    res = {}
    out = []
    for name, f in (('L', os.path.join(a.unit_dir, f'labels_{a.unit}.tsv')),
                    ('A', os.path.join(a.unit_dir, f'passA_{a.unit}.tsv'))):
        ol = tx_bench.load_output([path(f)])
        e = {k: v for k, v in tx_bench.position_errors(truth, ol).items() if k[0] in lines}
        res[name] = e
    n = len(res['L'])
    out.append(f'gate {a.unit}: {n} scored positions; L wrong {sum(res["L"].values())}, A wrong {sum(res["A"].values())}')
    out.append('| label | flagged | % of positions | L wrong held | L precision | L recall | A wrong held | A precision | A recall |')
    out.append('|---|---|---|---|---|---|---|---|---|')
    summary = {}
    groups = [(k, {k}) for k in LABELS] + [('non-good', {'joined', 'bad-crop', 'blot'}), ('no box', {'-'})]
    for name, ss in groups:
        ks = [k for k in res['L'] if plab.get(k, '-') in ss]
        row = [name, str(len(ks)), '%.1f' % (100.0 * len(ks) / max(1, n))]
        for p in ('L', 'A'):
            e = res[p]
            held = sum(1 for k in ks if e.get(k))
            tot = sum(e.values())
            row += [str(held), '%.3f' % (held / len(ks)) if ks else '-', '%.3f' % (held / tot) if tot else '-']
        out.append('| ' + ' | '.join(row) + ' |')
        summary[name] = dict(flagged=len(ks), L_held=sum(1 for k in ks if res['L'].get(k)),
                             A_held=sum(1 for k in ks if res['A'].get(k)))
    ng = summary['non-good']
    lt = sum(res['L'].values())
    rec, share = ng['L_held'] / max(1, lt), ng['flagged'] / max(1, n)
    met = rec >= 0.5 and share <= 0.15
    out.append(f'registered gate (non-good hold >= 50% of L wrong at <= 15% flagged): recall {rec:.3f}, '
               f'flagged {share:.3f} -> {"MET" if met else "NOT MET"}')
    print('\n'.join(out))
    if a.write:
        wr(a.write, ['line', 'pos', 'label', 'L_wrong', 'A_wrong'],
           [dict(line=k[0], pos=k[1], label=plab.get(k, '-'), L_wrong=int(res['L'][k]), A_wrong=int(res['A'].get(k, 0)))
            for k in sorted(res['L'], key=lambda k: (k[0], float(k[1])))])
    return met, summary


# ---------------------------------------------------------------- recut
def recut_box(gray, thr, t):
    """-> list of (x, y, w, h, part) page boxes for one flagged tile row t."""
    x, y, w, h = (int(t[k]) for k in ('x', 'y', 'w', 'h'))
    if t['label'] == 'joined':
        ink = gray[y:y + h, x:x + w] < thr
        _, c = col_valleys(ink)
        c = w // 2 if c is None else c
        return [(x, y, c, h, 'a'), (x + c, y, w - c, h, 'b')]
    ox, oy, ow, oh = (int(t[k]) for k in ('own_x', 'own_y', 'own_w', 'own_h'))
    x0, y0 = min(x, ox), min(y, oy)
    x1, y1 = max(x + w, ox + ow), max(y + h, oy + oh)
    gx, gy = int(round(0.05 * (x1 - x0))), int(round(0.05 * (y1 - y0)))     # +10% overall, half each side
    H, W = gray.shape
    return [(max(0, x0 - gx), max(0, y0 - gy), min(W, x1 + gx) - max(0, x0 - gx), min(H, y1 + gy) - max(0, y0 - gy), '')]


def render_tile(page_img, thr, box, nbs, scale=2):
    """The box with one neighbour of context each side, neighbouring lines masked, target framed, at `scale`x."""
    from PIL import Image, ImageDraw
    from iiif_lines import mask_neighbours
    x, y, w, h = box
    xs = [x] + [b[0] for b in nbs]; xe = [x + w] + [b[0] + b[2] for b in nbs]
    ys = [y] + [b[1] for b in nbs]; ye = [y + h] + [b[1] + b[3] for b in nbs]
    pad = max(6, h // 4)
    X0, Y0 = max(0, min(xs) - pad), max(0, min(ys) - pad)
    X1, Y1 = min(page_img.width, max(xe) + pad), min(page_img.height, max(ye) + pad)
    crop = page_img.crop((X0, Y0, X1, Y1))
    band_top, band_bot = min(ys) - Y0, max(ye) - Y0
    crop, _, _ = mask_neighbours(crop, band_top, band_bot, thr)
    crop = crop.resize((crop.width * scale, crop.height * scale), Image.BICUBIC).convert('RGB')
    d = ImageDraw.Draw(crop)
    d.rectangle(((x - X0) * scale - 3, (y - Y0) * scale - 3, (x - X0 + w) * scale + 3, (y - Y0 + h) * scale + 3),
                outline=(0, 0, 0), width=3)
    return crop


def make_sheets(rows, out_dir, max_rows):
    from PIL import Image, ImageDraw, ImageFont
    try:
        font = ImageFont.truetype('DejaVuSans-Bold.ttf', 28)
    except OSError:
        font = ImageFont.load_default()
    sheets = []
    os.makedirs(path(out_dir), exist_ok=True)
    for si in range(0, len(rows), max_rows):
        chunk = rows[si:si + max_rows]
        for i, r in enumerate(chunk):                          # rows are numbered from 1 on every sheet
            r['row'] = i + 1
        lw = 90
        width = lw + max(r['img'].width for r in chunk) + 20
        height = sum(r['img'].height + 16 for r in chunk) + 10
        sh = Image.new('RGB', (width, height), (255, 255, 255))
        d = ImageDraw.Draw(sh)
        yy = 5
        for r in chunk:
            d.text((8, yy + r['img'].height // 2 - 14), '%02d' % r['row'], fill=(0, 0, 0), font=font)
            sh.paste(r['img'], (lw, yy))
            yy += r['img'].height + 8
            d.line((0, yy, width, yy), fill=(170, 170, 170), width=1)
            yy += 8
        k = len(sheets) + 1
        sp = os.path.join(out_dir, 'sheet_%02d.png' % k)
        sh.save(path(sp))
        wr(os.path.join(out_dir, 'sheet_%02d.tsv' % k), ['row', 'line', 'pos', 'L_sign', 'sid', 'label', 'part'],
           chunk)
        sheets.append(sp)
    return sheets


def cmd_recut(a):
    from PIL import Image
    want = set(a.labels.split(','))
    tiles = rd(a.tiles)
    gray = load_page(a.harvest, a.page)
    thr = otsu(gray)
    page_img = Image.fromarray(gray)
    lines = set(unit_lines(a.units, a.unit)) if a.unit else None
    unit = a.unit or a.page
    out_dir = os.path.join(a.out, unit)
    os.makedirs(path(out_dir), exist_ok=True)
    pos_of = defaultdict(list)
    L = {}
    if lines is not None:
        for r in box_positions(a, lines):
            for s in r['sid'].split('+'):
                if s:
                    pos_of[s].append((r['line'], r['pos']))
        L = {(r['line'], r['pos']): r['sign'] for r in rd(a.line_read) if r['line'] in lines}
    by_line = defaultdict(list)
    for t in tiles:
        by_line[t['line']].append(t)
    for v in by_line.values():
        v.sort(key=lambda t: int(t['x']))
    rows, dropped = [], []
    for t in tiles:
        if lines is not None and not pos_of.get(t['sid']):
            continue
        if t['label'] == 'blot' and 'blot' not in want:
            dropped.append(dict(t, positions=';'.join('%s.%s' % p for p in pos_of.get(t['sid'], []))))
            continue
        if t['label'] not in want:
            continue
        ln = by_line[t['line']]
        i = [u['sid'] for u in ln].index(t['sid'])
        nbs = [tuple(int(ln[j][k]) for k in ('x', 'y', 'w', 'h')) for j in (i - 1, i + 1) if 0 <= j < len(ln)]
        ps = pos_of.get(t['sid']) or [('', '')]
        parts = recut_box(gray, thr, t)
        for pi, (x, y, w, h, part) in enumerate(parts):
            # a joined box split in two over a 1:2 mapping: part a -> first position, b -> second
            lp = ps[pi] if len(ps) == len(parts) else ps[0]
            rows.append(dict(line=lp[0], pos=lp[1], L_sign=L.get(lp, ''), sid=t['sid'], label=t['label'], part=part,
                             img=render_tile(page_img, thr, (x, y, w, h), nbs, a.scale)))
    rows.sort(key=lambda r: (r['line'], float(r['pos'] or 0), r['part']))
    sheets = make_sheets(rows, out_dir, a.rows) if rows else []
    wr(os.path.join(out_dir, 'dropped.tsv'), COLS + ['positions'], dropped)
    print('recut %s: %d tiles (%s) on %d sheets, %d blots dropped -> %s' % (
        unit, len(rows), dict(Counter(r['label'] + ('/' + r['part'] if r['part'] else '') for r in rows)), len(sheets),
        len(dropped), out_dir))
    return rows, dropped, sheets


# ---------------------------------------------------------------- resolve
def cmd_resolve(a):
    lines = set(unit_lines(a.units, a.unit))
    L = [r for r in rd(a.line_read) if r['line'] in lines]
    d = os.path.join(a.dir, a.unit)
    new = {}
    for f in sorted(os.listdir(path(d))):
        m = re.match(r'sheet_(\d+)\.tsv$', f)
        if not m:
            continue
        key = {r['row']: r for r in rd(os.path.join(d, f))}
        rp = os.path.join(d, 'reads_%s.tsv' % m.group(1))
        if not os.path.exists(path(rp)):
            sys.exit('tx_tile_gate: missing %s' % rp)
        for r in rd(rp):
            k = key.get(str(int(r['row'])))
            s = (r.get('sign_id') or '').strip()
            if k and s and s not in ('?', 'X_NEW') and re.match(r'^T\d+$', s) and k.get('part', '') in ('', 'a'):
                new[(k['line'], k['pos'])] = s
    out = [dict(line=r['line'], pos=r['pos'], sign=new.get((r['line'], r['pos']), r['sign'])) for r in L]
    wr(a.pass_out, ['line', 'pos', 'sign'], out)
    ch = sum(1 for r in L if new.get((r['line'], r['pos']), r['sign']) != r['sign'])
    print('resolve %s: %d positions, %d re-read, %d changed -> %s' % (a.unit, len(out), len(new), ch, a.pass_out))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split('\n\n', 1)[1])
    sub = ap.add_subparsers(dest='cmd', required=True)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--atlas', default=D['atlas']); common.add_argument('--harvest', default=D['harvest'])
    common.add_argument('--line-read', default=D['line_read']); common.add_argument('--units', default=D['units'])
    common.add_argument('--box-pos', default=os.path.join(D['out'], 'box_pos.tsv'),
                        help='label-blind box<->position map (made with tx_compare.box_map if absent)')
    s = sub.add_parser('score', parents=[common]); s.add_argument('--page', required=True); s.add_argument('--out', required=True)
    g = sub.add_parser('gate', parents=[common]); g.add_argument('--unit', required=True)
    g.add_argument('--tiles', nargs='+', required=True); g.add_argument('--unit-dir', default=D['unit_dir'])
    g.add_argument('--bench', default=D['bench']); g.add_argument('--item', default=D['item'])
    g.add_argument('--write', help='per-position TSV (line, pos, label, L_wrong, A_wrong)')
    r = sub.add_parser('recut', parents=[common]); r.add_argument('--page', required=True); r.add_argument('--tiles', required=True)
    r.add_argument('--unit'); r.add_argument('--labels', default='joined,bad-crop')
    r.add_argument('--out', default=D['out']); r.add_argument('--rows', type=int, default=24)
    r.add_argument('--scale', type=int, default=2)
    v = sub.add_parser('resolve', parents=[common]); v.add_argument('--unit', required=True)
    v.add_argument('--dir', default=D['out']); v.add_argument('--pass-out', required=True)
    a = ap.parse_args(argv)
    return {'score': cmd_score, 'gate': cmd_gate, 'recut': cmd_recut, 'resolve': cmd_resolve}[a.cmd](a)


if __name__ == '__main__':
    main()
