#!/usr/bin/env python3
"""Apply the sign sorter's fixed cuts ("Fix the cut", SORTER-NUDGE 4 Oct 2026) to a sorter folder.

  python3 tools/sorter_apply_recuts.py --recuts recuts.tsv --signs signs.tsv --pages PAGES_DIR --tiles TILES_DIR
      [--signs-out FILE] [--force] [--dry-run]

recuts.tsv is what tools/sign_sorter_apply.py writes from the page's db collection 'recuts' (tile, page, old_x old_y old_w
old_h, new_x new_y new_w new_h, at, and since 5 Oct 2026 quad and mask; source line-image pixels, the x y w h of
signs.tsv). For each row this:
  - re-crops the tile from PAGES_DIR/<page>.(png|jpg|jpeg) at the new box, with tools/sign_sorter.py's margins (0.9 h
    above, 0.35 h below, 5 px each side), into TILES_DIR/<tile>.jpg; the crop it replaces is kept once as
    <tile>.orig.jpg (cut at the old box if no <tile>.jpg existed), never overwritten by a second run;
  - sets the tile's x y w h in signs.tsv to the new box (in place unless --signs-out).
Free corners and stray ink (SORTER-QUAD, owner 5 Oct 2026: on a wide looped sign the sheared box could not cover the sign
without a neighbour's ink): a row whose quad cell holds four corners [[x, y], ...] (TL, TR, BR, BL) is cut by
bilinearly warping that quadrilateral (Image.QUAD; projective until 6 Oct 2026) to an upright tile W x H (W the longer of the top and bottom edges, H the longer of
the left and right ones), with the same margins taken around it in the warped frame (pixels that fall off the page are
white); new_x .. new_h are the quad's bounding box and are what signs.tsv gets. A mask cell [{r, pts: [[x, y], ...]}, ...]
lists brush strokes (radius r, source pixels) over a neighbour's ink: they are painted white on the source before the cut,
quad or plain box. A row without a quad cell (recuts.tsv written before 5 Oct 2026, or an {x, y, w, h} recut) is cut
exactly as before.
A row whose signs.tsv box is neither the recut's old box nor already its new box is skipped and reported (the folder was
re-cut since the page was built, e.g. recut.py run again) unless --force; a row already at its new box is re-cropped but
counts as already applied, so the tool can be run again after a rebuild that re-ran recut.py. Exit 0 when every row
applied or was already applied, 2 when any was skipped (stale or missing tile/page), 1 on bad input.
Only boxes move: a recut tile keeps its sign label and pile (labels.tsv untouched). One tile = one box; the page has no
"split here". Offline. Test: tools/tests/test_sorter_apply_recuts.py.
"""
import argparse, csv, json, os, sys

import numpy as np
from PIL import Image, ImageDraw

PAPER = 255   # masked ink and off-page pixels become paper white


def crop_box(im, x, y, w, h):
    top, bot, side = max(10, int(.9 * h)), max(6, int(.35 * h)), 5
    return im.crop((max(0, x - side), max(0, y - top), min(im.width, x + w + side), min(im.height, y + h + bot)))


def margins(w, h):
    """tools/sign_sorter.py's margins around a w x h box: (top, bottom, side)."""
    return max(10, int(.9 * h)), max(6, int(.35 * h)), 5


def quad_size(q):
    """Upright size (W, H) of quad q [[x, y]] x 4 (TL, TR, BR, BL): the longer top/bottom edge, the longer left/right edge."""
    d = lambda a, b: float(np.hypot(q[a][0] - q[b][0], q[a][1] - q[b][1]))
    return max(1, int(round(max(d(0, 1), d(3, 2))))), max(1, int(round(max(d(0, 3), d(1, 2)))))


def homography(src, dst):
    """The 8 coefficients (a..h) of the projective map src[i] -> dst[i] (4 point pairs): x' = (a x + b y + c) / (g x + h y + 1),
    y' = (d x + e y + f) / (g x + h y + 1); the order Pillow's Image.PERSPECTIVE takes (output -> input)."""
    A, B = [], []
    for (x, y), (u, v) in zip(src, dst):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return [float(c) for c in np.linalg.solve(np.array(A, float), np.array(B, float))]


def crop_quad(im, q):
    """Warp quad q (source pixels, TL TR BR BL) to an upright tile with sign_sorter.py's margins around it."""
    W, H = quad_size(q); top, bot, side = margins(W, H)
    # bilinear (Image.QUAD), not projective (6 Oct 2026): a perspective map flips sign inside the margins of a strongly
    # sheared quad and cuts only paper; the margin corners are the bilinear map of the quad extended past [0, 1]
    at = lambda s, t: tuple((1 - s) * (1 - t) * q[0][c] + s * (1 - t) * q[1][c] + s * t * q[2][c] + (1 - s) * t * q[3][c]
                            for c in (0, 1))
    s0, s1, t0, t1 = -side / W, 1 + side / W, -top / H, 1 + bot / H
    data = at(s0, t0) + at(s0, t1) + at(s1, t1) + at(s1, t0)   # Image.QUAD order: upper left, lower left, lower right, upper right
    return im.transform((W + 2 * side, H + top + bot), Image.QUAD, data, Image.BILINEAR, fillcolor=PAPER)


def paint_mask(im, mask):
    """A copy of im with each brush stroke {r, pts} painted paper white (round caps and joins, as the page draws them)."""
    if not mask:
        return im
    im = im.copy(); g = ImageDraw.Draw(im)
    for st in mask:
        r, pts = float(st['r']), [(float(x), float(y)) for x, y in st['pts']]
        for x, y in pts:
            g.ellipse((x - r, y - r, x + r, y + r), fill=PAPER)
        if len(pts) > 1:
            g.line(pts, fill=PAPER, width=max(1, int(round(2 * r))))
    return im


def parse_quad(cell):
    """recuts.tsv quad cell -> [[x, y]] x 4 or None (empty = an old {x, y, w, h} row); ValueError when malformed."""
    if not (cell or '').strip():
        return None
    q = json.loads(cell)
    if not (isinstance(q, list) and len(q) == 4 and all(isinstance(p, list) and len(p) == 2 for p in q)):
        raise ValueError('quad needs four [x, y] corners')
    return [[float(p[0]), float(p[1])] for p in q]


def parse_mask(cell):
    """recuts.tsv mask cell -> [{r, pts}] ([] when empty); ValueError when malformed."""
    if not (cell or '').strip():
        return []
    m = json.loads(cell)
    if not isinstance(m, list) or not all(isinstance(s, dict) and float(s['r']) > 0 and isinstance(s['pts'], list) and
                                          all(len(p) == 2 for p in s['pts']) for s in m):
        raise ValueError('mask needs [{r, pts: [[x, y], ...]}, ...]')
    return m


def find_page(pages, page):
    for e in ('.png', '.jpg', '.jpeg'):
        p = os.path.join(pages, page + e)
        if os.path.exists(p):
            return p
    return None


def run(recuts, signs, pages, tiles, signs_out=None, force=False, dry=False):
    rows = list(csv.DictReader(open(recuts, newline=''), delimiter='\t'))
    with open(signs, newline='') as f:
        rd = csv.DictReader(f, delimiter='\t'); cols = rd.fieldnames; srows = list(rd)
    if not cols or not {'sid', 'page', 'x', 'y', 'w', 'h'} <= set(cols):
        raise SystemExit('signs.tsv needs sid page x y w h columns')
    by = {r['sid']: r for r in srows}
    os.makedirs(tiles, exist_ok=True)
    rep = {'applied': [], 'already': [], 'skipped': []}
    ims = {}
    for r in rows:
        sid = r['tile']; s = by.get(sid)
        try:
            new = [int(r[k]) for k in ('new_x', 'new_y', 'new_w', 'new_h')]
            old = [int(r[k]) for k in ('old_x', 'old_y', 'old_w', 'old_h')] if r.get('old_x', '') != '' else None
            quad, mask = parse_quad(r.get('quad')), parse_mask(r.get('mask'))
        except (KeyError, ValueError, TypeError):
            rep['skipped'].append((sid, 'bad box')); continue
        if not s:
            rep['skipped'].append((sid, 'not in signs.tsv')); continue
        cur = [int(s[k]) for k in ('x', 'y', 'w', 'h')]
        state = 'already' if cur == new else 'applied' if (cur == old or force) else None
        if state is None:
            rep['skipped'].append((sid, 'signs.tsv box %s is neither old %s nor new %s' % (cur, old, new))); continue
        page = s['page']; pp = find_page(pages, page)
        if not pp:
            rep['skipped'].append((sid, 'no page image ' + page)); continue
        if not dry:
            im = ims.get(pp) or ims.setdefault(pp, Image.open(pp).convert('L'))
            t, o = os.path.join(tiles, sid + '.jpg'), os.path.join(tiles, sid + '.orig.jpg')
            if not os.path.exists(o):
                if os.path.exists(t):
                    os.replace(t, o)
                else:
                    crop_box(im, *(old or cur)).save(o, 'JPEG', quality=90)
            src = paint_mask(im, mask)
            (crop_quad(src, quad) if quad else crop_box(src, *new)).save(t, 'JPEG', quality=90)
            s.update({'x': str(new[0]), 'y': str(new[1]), 'w': str(new[2]), 'h': str(new[3])})
        rep[state].append(sid)
    if not dry and (rep['applied'] or rep['already']):
        with open(signs_out or signs, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=cols, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(srows)
    return rep


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0], epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--recuts', required=True); ap.add_argument('--signs', required=True)
    ap.add_argument('--pages', required=True, help='the line/page images signs.tsv x y refer to')
    ap.add_argument('--tiles', required=True, help='folder of per-tile crops (<tile>.jpg; the old crop kept as <tile>.orig.jpg)')
    ap.add_argument('--signs-out', help='write the updated signs.tsv here instead of in place')
    ap.add_argument('--force', action='store_true', help='apply even when signs.tsv no longer holds the old box')
    ap.add_argument('--dry-run', action='store_true')
    a = ap.parse_args(argv)
    rep = run(a.recuts, a.signs, a.pages, a.tiles, a.signs_out, a.force, a.dry_run)
    print('applied %d, already applied %d, skipped %d' % (len(rep['applied']), len(rep['already']), len(rep['skipped'])))
    for sid, why in rep['skipped']:
        print('SKIP %s: %s' % (sid, why))
    return 2 if rep['skipped'] else 0


if __name__ == '__main__':
    sys.exit(main())
