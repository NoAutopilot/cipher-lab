"""Offline test for region.json (tools/sorter_recut.py write_region / region_y; SORTER-PAGEVIEW, 4 Oct 2026): a tile's box
mapped back onto the original region (the inverse of the deskew shear) must hold its own ink. Synthetic round trip, plus
one real tile per target whose sorter/region.json and region image are on disk (skipped when absent)."""
import csv, json, sys, tempfile
from pathlib import Path
import numpy as np
from PIL import Image
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE.parent)); sys.path.insert(0, str(HERE))
import sorter_recut as sr
from test_sorter_recut import page, PITCH


def ink_back(grey, doc, pg, strip, x, y, w, h, shift=0):
    """Fraction of the tile's ink pixels (in the strip page) that are ink at the mapped region pixel too."""
    thr = (float(np.median(strip)) + float(np.percentile(strip, 0.5))) / 2; hit = tot = 0   # halfway ink..paper
    for xx in range(x, x + w):
        for yy in range(y, y + h):
            if strip[yy, xx] < thr:
                tot += 1; ry = int(round(sr.region_y(doc, pg, xx, yy))) + shift
                hit += 0 <= ry < grey.shape[0] and grey[ry, xx] < thr + 15
    return hit / max(1, tot), tot


def test_synthetic_round_trip():
    g, xs, tr = page(slope=0.08)
    with tempfile.TemporaryDirectory() as d:
        cfg = sr.Cfg(pitch=PITCH, half=80, nclu=3)
        tiles, _ = sr.run(g, [tr], ['p_L01'], [[('S1', 'S1')] * len(xs)], [xs], d, Path(d) / 'pages', cfg, region_image='x.jpg')
        doc = json.load(open(Path(d) / 'region.json'))
        assert doc['image'] == 'x.jpg' and doc['half'] == 80 and doc['W'] == g.shape[1] and len(doc['lines']['p_L01']) > 100
        strip = np.array(Image.open(Path(d) / 'pages' / 'p_L01.jpg').convert('L'))
        for t in tiles:
            f, n = ink_back(g, doc, 'p_L01', strip, t['x'], t['y'], t['w'], t['h'])
            assert n > 50 and f >= 0.95, (t['sid'], f, n)
            assert ink_back(g, doc, 'p_L01', strip, t['x'], t['y'], t['w'], t['h'], shift=60)[0] < 0.3   # the check can fail


def test_real_tiles():
    for tgt in ('fr16106-vivonne-longlee-1579', 'fr16045-pisany-rome-1585'):
        S = ROOT / 'ciphers' / tgt / 'sorter'
        if not (S / 'region.json').exists(): print('skip', tgt); continue
        doc = json.load(open(S / 'region.json')); img = ROOT / doc['image']
        if not img.exists(): print('skip', tgt, '(no region image)'); continue
        grey = np.array(Image.open(img).convert('L')); assert grey.shape == (doc['H'], doc['W'])
        rows = [r for r in csv.DictReader(open(S / 'signs.tsv'), delimiter='\t')]
        pages = sorted({r['page'] for r in rows}); done = 0
        for pg in (pages[2], pages[len(pages) // 2]):                 # one tile near the top, one mid-page (sloped lines)
            strip = np.array(Image.open(S / 'pages' / f'{pg}.jpg').convert('L'))
            r = max((r for r in rows if r['page'] == pg), key=lambda r: int(r['w']) * int(r['h']))
            f, n = ink_back(grey, doc, pg, strip, *(int(r[k]) for k in ('x', 'y', 'w', 'h')))
            assert n > 50 and f >= 0.9, (tgt, r['sid'], f, n); done += 1
            off = ink_back(grey, doc, pg, strip, *(int(r[k]) for k in ('x', 'y', 'w', 'h')), shift=doc['pitch'] // 2)[0]
            assert off < f - 0.3, (tgt, r['sid'], 'half a line off still matches', off, f)   # the check can fail
        print('ok', tgt, done, 'tiles')


if __name__ == '__main__':
    for k, f in list(globals().items()):
        if k.startswith('test_'): f(); print('ok', k)
