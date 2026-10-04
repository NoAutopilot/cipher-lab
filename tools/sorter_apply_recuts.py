#!/usr/bin/env python3
"""Apply the sign sorter's fixed cuts ("Fix the cut", SORTER-NUDGE 4 Oct 2026) to a sorter folder.

  python3 tools/sorter_apply_recuts.py --recuts recuts.tsv --signs signs.tsv --pages PAGES_DIR --tiles TILES_DIR
      [--signs-out FILE] [--force] [--dry-run]

recuts.tsv is what tools/sign_sorter_apply.py writes from the page's db collection 'recuts' (tile, page, old_x old_y old_w
old_h, new_x new_y new_w new_h, at; source line-image pixels, the x y w h of signs.tsv). For each row this:
  - re-crops the tile from PAGES_DIR/<page>.(png|jpg|jpeg) at the new box, with tools/sign_sorter.py's margins (0.9 h
    above, 0.35 h below, 5 px each side), into TILES_DIR/<tile>.jpg; the crop it replaces is kept once as
    <tile>.orig.jpg (cut at the old box if no <tile>.jpg existed), never overwritten by a second run;
  - sets the tile's x y w h in signs.tsv to the new box (in place unless --signs-out).
A row whose signs.tsv box is neither the recut's old box nor already its new box is skipped and reported (the folder was
re-cut since the page was built, e.g. recut.py run again) unless --force; a row already at its new box is re-cropped but
counts as already applied, so the tool can be run again after a rebuild that re-ran recut.py. Exit 0 when every row
applied or was already applied, 2 when any was skipped (stale or missing tile/page), 1 on bad input.
Only boxes move: a recut tile keeps its sign label and pile (labels.tsv untouched). One tile = one box; the page has no
"split here". Offline. Test: tools/tests/test_sorter_apply_recuts.py.
"""
import argparse, csv, os, sys

from PIL import Image


def crop_box(im, x, y, w, h):
    top, bot, side = max(10, int(.9 * h)), max(6, int(.35 * h)), 5
    return im.crop((max(0, x - side), max(0, y - top), min(im.width, x + w + side), min(im.height, y + h + bot)))


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
        except (KeyError, ValueError):
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
            crop_box(im, *new).save(t, 'JPEG', quality=90)
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
