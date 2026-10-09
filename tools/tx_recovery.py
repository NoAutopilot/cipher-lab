#!/usr/bin/env python3
"""tx_recovery.py -- document-recovery renderings of a faint scan, and their read-free atlas proxy (TXE-G, 9 Oct 2026).

Lesson it answers (research/TX-RECOVERY-PRACTICE-2026-10-09.md; LANE TX-ENGINEER idea O5): the owner asked what expert
document-recovery teams do with a faint page, so the lane tests their methods rather than inventing its own. Three
greyscale methods from the document-image-analysis literature are flags here; each is measured, never assumed:

  sauvola   local binarisation (Sauvola & Pietikainen 2000; the DIBCO baseline family), window = odd(0.5 x the page's
            median sign height), k = 0.2 -- the hand's thin strokes get a threshold from their own neighbourhood
  clahe     contrast-limited adaptive histogram equalisation, clip 2.0, 8x8 tiles (the parameters reported best for
            handwritten characters), then the atlas's own background-normalised threshold
  swn       adaptive stroke-width normalisation: after the atlas threshold, a box whose stroke width (2 x the median
            distance-transform value on its ink) is under the page's median is dilated once (3x3); others untouched
            (the reliability-driven / thin-only variant reported better than thickening everything)
  plain     the control: the atlas's own threshold (glyph_atlas.binarise, rel 0.78, background by closing)

Colour methods (ink/paper channel separation, decorrelation stretch, Tonazzini-style colour decorrelation for
bleed-through) need colour: the Birago no.87 sources on disk are greyscale (mode L; harvest crops R=G=B), so they
are not flags here -- a grey image passed to them would test nothing.

Subcommands
  render --image IN --setting S --out OUT.png [--median-h PX]
        the setting applied to a page or line crop, written as a greyscale PNG (ink black on white) for a reader.
  proxy  --atlas DIR --setting S [--setting S ...] --work DIR --holdout PREFIX [...] --prefix PREFIX [...]
        read-free proxy: for each setting, every box of DIR/signs.tsv gets its 48x48 bitmap re-derived from its page
        (DIR/pages.json) under the setting -- same boxes, so plain and each setting are paired position by position --
        then tools/glyph_atlas.py classify (--topk 3, the holdouts) runs on a copy of the atlas with those bitmaps;
        writes WORK/<setting>/topk.tsv and WORK/<setting>/bench.tsv (boxes whose id starts with a --prefix, per line in
        x order, '_' dropped, k1 as the sign: the atlas/topk/no87_heldout_bench.tsv recipe; label-blind, never a truth
        column). Score bench.tsv with tools/tx_bench.py --paired WORK/plain/bench.tsv AFTER committing the topk files.

Every box (plain included) is re-derived the same way -- all ink of the box under the setting's mask -- so the plain
control here differs slightly from the stored atlas bitmaps (which keep only the box's own components); the paired
comparison is between settings of this tool, never against the stored bitmaps.

Offline test: tools/tests/test_tx_recovery.py. Disk only, no network, no model.
"""
import argparse, csv, json, os, shutil, subprocess, sys
import numpy as np
import cv2
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SETTINGS = ('plain', 'sauvola', 'clahe', 'swn')
PARAMS = {'plain': dict(rel=0.78), 'sauvola': dict(window='odd(0.5*median_h)', k=0.2),
          'clahe': dict(clip=2.0, tiles=8, rel=0.78), 'swn': dict(rel=0.78, dilate='3x3 once if box sw < page median')}


def atlas_binarise(grey, rel=0.78):
    """glyph_atlas.binarise, repeated here so the tool runs without the atlas module's heavy imports."""
    k = max(15, int(min(grey.shape) / 40) | 1)
    bg = cv2.morphologyEx(grey, cv2.MORPH_CLOSE, np.ones((k, k), np.uint8))
    bg = cv2.GaussianBlur(bg, (0, 0), k / 3)
    norm = grey.astype(float) / np.maximum(bg.astype(float), 1)
    return (norm < rel).astype(np.uint8)


def sauvola_mask(grey, median_h, k=0.2):
    from skimage.filters import threshold_sauvola
    w = max(15, int(0.5 * median_h)) | 1
    return (grey < threshold_sauvola(grey, window_size=w, k=k)).astype(np.uint8)


def clahe_grey(grey, clip=2.0, tiles=8):
    return cv2.createCLAHE(clipLimit=clip, tileGridSize=(tiles, tiles)).apply(grey)


def stroke_width(mask):
    """2 x the median distance-transform value over ink pixels (0 when no ink)."""
    if not mask.any():
        return 0.0
    dt = cv2.distanceTransform(mask.astype(np.uint8), cv2.DIST_L2, 3)
    return 2.0 * float(np.median(dt[mask > 0]))


def page_mask(grey, setting, median_h):
    """Binary ink mask of a page under a setting (swn's per-box step happens in box_masks)."""
    if setting == 'sauvola':
        m = sauvola_mask(grey, median_h)
    elif setting == 'clahe':
        m = atlas_binarise(clahe_grey(grey))
    else:
        m = atlas_binarise(grey)
    if min(grey.shape) > 2500:          # glyph_atlas.segment_page's own speck opening on large pages
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
    return m


def box_masks(mask, boxes, setting):
    out = [mask[y:y + h, x:x + w].copy() for x, y, w, h in boxes]
    if setting == 'swn' and out:
        sw = np.array([stroke_width(m) for m in out])
        med = float(np.median(sw[sw > 0])) if (sw > 0).any() else 0.0
        out = [cv2.dilate(m, np.ones((3, 3), np.uint8)) if 0 < s < med else m for m, s in zip(out, sw)]
    return out


def bitmap(mask, size=48):
    """glyph_atlas.bitmap: square canvas, centred, INTER_AREA to size x size."""
    h, w = mask.shape
    s = max(h, w, 1)
    can = np.zeros((s, s), np.uint8)
    can[(s - h) // 2:(s - h) // 2 + h, (s - w) // 2:(s - w) // 2 + w] = mask * 255
    return cv2.resize(can, (size, size), interpolation=cv2.INTER_AREA)


def render(grey, setting, median_h=60.0):
    """A reader-facing rendering: ink black on white (uint8)."""
    if setting == 'clahe':
        return clahe_grey(grey)
    if setting == 'plain':
        return grey
    m = page_mask(grey, setting, median_h)
    if setting == 'swn':
        sw = stroke_width(m)
        # whole-image form: dilate where the local stroke is under the image median (component by component)
        n, lab, st, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
        widths = {i: stroke_width((lab[st[i, 1]:st[i, 1] + st[i, 3], st[i, 0]:st[i, 0] + st[i, 2]] == i).astype(np.uint8))
                  for i in range(1, n) if st[i, 4] >= 4}
        thin = np.isin(lab, [i for i, s in widths.items() if 0 < s < (np.median(list(widths.values())) if widths else sw)])
        m = np.where(cv2.dilate(thin.astype(np.uint8), np.ones((3, 3), np.uint8)) > 0, 1, m)
    return np.where(m > 0, 0, 255).astype(np.uint8)


def read_tsv(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def cmd_render(a):
    grey = np.array(Image.open(a.image).convert('L'))
    Image.fromarray(render(grey, a.setting, a.median_h)).save(a.out)
    print(f'{a.setting} -> {a.out} ({grey.shape[1]}x{grey.shape[0]}; params {json.dumps(PARAMS[a.setting])})')


def bitmaps_for(atlas, rows, setting):
    pages = json.load(open(os.path.join(atlas, 'pages.json')))
    by = {}
    for i, r in enumerate(rows):
        by.setdefault(r['page'], []).append(i)
    bm = np.zeros((len(rows), 48, 48), np.uint8)
    for pg, idx in by.items():
        info = pages[pg]
        grey = np.array(Image.open(os.path.join(ROOT, info['image'])).convert('L'))
        if info.get('box'):
            x0, y0, x1, y1 = info['box']
            grey = grey[y0:y1, x0:x1]
        m = page_mask(grey, setting, float(info['median_h']))
        boxes = [(int(rows[i]['x']), int(rows[i]['y']), int(rows[i]['w']), int(rows[i]['h'])) for i in idx]
        for i, bmask in zip(idx, box_masks(m, boxes, setting)):
            bm[i] = bitmap(bmask)
    return bm


def bench(topk, prefixes, out):
    rows = [r for r in read_tsv(topk) if r['box'].startswith(tuple(prefixes)) and r['k1'] != '_']
    with open(out, 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in sorted(rows, key=lambda r: (r['page'], int(r['line']), int(r['x']))):
            f.write(f"{r['page']}_L{int(r['line']):02d}\t{r['x']}\t{r['k1']}\n")
    return len(rows)


def cmd_proxy(a):
    rows = read_tsv(os.path.join(a.atlas, 'signs.tsv'))
    labels = a.labels or os.path.join(a.atlas, 'labels.json')
    for s in a.setting:
        d = os.path.join(a.work, s)
        os.makedirs(d, exist_ok=True)
        for fn in ('signs.tsv', 'marks.tsv', 'clusters.tsv', 'pages.json'):
            shutil.copy(os.path.join(a.atlas, fn), d)
        marks = np.load(os.path.join(a.atlas, 'bitmaps.npz'))['marks']
        np.savez_compressed(os.path.join(d, 'bitmaps.npz'), signs=bitmaps_for(a.atlas, rows, s), marks=marks)
        cmd = [sys.executable, os.path.join(ROOT, 'tools', 'glyph_atlas.py'), 'classify', '--out', d, '--labels', labels,
               '--page', 'all', '--tsv', os.path.join(d, 'topk.tsv'), '--topk', '3']
        for h in a.holdout or ():
            cmd += ['--holdout', h]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        n = bench(os.path.join(d, 'topk.tsv'), a.prefix, os.path.join(d, 'bench.tsv'))
        json.dump(dict(setting=s, params=PARAMS[s], boxes=len(rows), bench_rows=n, holdout=a.holdout, prefix=a.prefix),
                  open(os.path.join(d, 'manifest.json'), 'w'), indent=1)
        for fn in ('signs.tsv', 'marks.tsv', 'clusters.tsv', 'pages.json', 'bitmaps.npz'):
            os.remove(os.path.join(d, fn))      # regenerable; keep only topk/bench/manifest
        print(f'{s}: {len(rows)} boxes re-derived, {n} bench rows -> {d}/bench.tsv')


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = p.add_subparsers(dest='cmd', required=True)
    r = sp.add_parser('render')
    r.add_argument('--image', required=True)
    r.add_argument('--setting', choices=SETTINGS, required=True)
    r.add_argument('--out', required=True)
    r.add_argument('--median-h', type=float, default=60.0, help='sign height in px (sauvola window); default 60')
    x = sp.add_parser('proxy')
    x.add_argument('--atlas', required=True)
    x.add_argument('--labels')
    x.add_argument('--setting', action='append', choices=SETTINGS, required=True)
    x.add_argument('--work', required=True)
    x.add_argument('--holdout', action='append')
    x.add_argument('--prefix', action='append', required=True, help='box-id prefix of the scored unit (repeatable)')
    a = p.parse_args(argv)
    (cmd_render if a.cmd == 'render' else cmd_proxy)(a)


if __name__ == '__main__':
    main()
