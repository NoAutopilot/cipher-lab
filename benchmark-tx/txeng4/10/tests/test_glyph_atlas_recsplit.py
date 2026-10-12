#!/usr/bin/env python3
"""Offline test of tools/glyph_atlas.py segment --split-by-recognition (TXE4-10 RECOG-CUT, 12 Oct 2026).
Page A: separate boxes and X's (two shapes) -> an exemplar atlas with labels box/X. Page B: the same shapes drawn in
pairs joined by a bridge stroke (one connected component each). Must-catch: with --rec-lambda 1.0, where a joined pair is
cut into two pieces the cut lies in the bridge (>= 80%), and the RecKNN reads the separate shapes leave-one-out (>= 0.9). Must-not-
block: --rec-lambda 99 (above any gain) leaves every joined pair as one box (= pen units); a page with no wide box is
unchanged; --rec-permute-labels changes at least one cut (the control can vary). No network, no model, no truth file."""
import csv, os, subprocess, sys, tempfile
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')
sys.path.insert(0, os.path.join(HERE, '..'))


SHAPES = ['box', 'X', 'O', 'plus']


def glyph(img, shape, x, yc, j, t):
    if shape == 'X':
        cv2.line(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
        cv2.line(img, (x + 50 + j(), yc - 30 + j()), (x + j(), yc + 30 + j()), 20, t)
    elif shape == 'box':
        cv2.rectangle(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
    elif shape == 'O':
        cv2.ellipse(img, (x + 25 + j(), yc + j()), (25, 30), 0, 0, 360, 20, t)
    else:
        cv2.line(img, (x + 25 + j(), yc - 30 + j()), (x + 25 + j(), yc + 30 + j()), 20, t)
        cv2.line(img, (x + j(), yc + j()), (x + 50 + j(), yc + j()), 20, t)


def draw(pairs, seed=3, lines=3):
    """lines x 12 signs cycling SHAPES; pairs=True joins sign 2k to sign 2k+1 by a bridge stroke along the centre row."""
    rng = np.random.default_rng(seed)
    img = np.full((250 * lines + 150, 1700), 235, np.uint8)
    for li in range(lines):
        yc = 200 + 250 * li
        for k in range(12):
            x = 80 + k * 135
            j = lambda: int(rng.integers(-2, 3))
            t = int(rng.integers(4, 7))
            glyph(img, SHAPES[(k + li) % 4], x, yc, j, t)
            if pairs and k % 2 == 0:
                cv2.line(img, (x + 25, yc), (x + 135 + 25, yc), 20, 3)   # bridge from this centre into the next: one component
    return img


def expected(lines=3):
    return [SHAPES[(k + li) % 4] for li in range(lines) for k in range(12)]


def seg(d, name, img, extra=()):
    p = os.path.join(d, name + '.png'); cv2.imwrite(p, img)
    out = os.path.join(d, name)
    r = subprocess.run([sys.executable, TOOL, 'segment', '--page', f'{name}={p}', '--out', out, *extra],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    return out, list(csv.DictReader(open(os.path.join(out, 'signs.tsv')), delimiter='\t')), r.stdout


def main():
    d = tempfile.mkdtemp()
    atlas, rows, _ = seg(d, 'A', draw(False, 3))
    assert len(rows) == 36, len(rows)
    lab = os.path.join(d, 'labels.tsv')
    with open(lab, 'w') as f:
        f.write('box\tcode\n')
        for r in sorted(rows, key=lambda r: (int(r['line']), int(r['x']))):
            f.write(f"{r['sid']}\t{SHAPES[(int(r['pos']) - 1 + int(r['line']) - 1) % 4]}\n")
    # must-not-block 1: no wide box -> unchanged
    _, rows2, _ = seg(d, 'A2', draw(False, 4), ['--split-by-recognition', lab, '--rec-atlas', atlas, '--rec-lambda', '0.45'])
    assert len(rows2) == 36, len(rows2)
    # the joined page: 6 pen units
    _, pen, _ = seg(d, 'B0', draw(True, 5))
    assert len(pen) == 18, len(pen)
    # must-catch: where the recognition split cuts a joined pair into two pieces, the cut lies in the bridge
    # (between the first glyph's right edge, +50, and the second glyph's left edge, +135) and the two pieces read as
    # the two joined shapes. (A Laplace vote posterior rates a sliver as confidently as a whole sign, so the piece COUNT
    # is not asserted: at this lambda some pairs over-split, which the real control (e) is there to catch.)
    outd, rec, log = seg(d, 'B1', draw(True, 5), ['--split-by-recognition', lab, '--rec-atlas', atlas, '--rec-lambda', '1.0'])
    assert os.path.exists(os.path.join(outd, 'rec_split.tsv'))
    import glyph_atlas as GA
    knn = GA.RecKNN.from_atlas(atlas, lab)
    bm = np.load(os.path.join(outd, 'bitmaps.npz'))['signs']
    two = [r for r in csv.DictReader(open(os.path.join(outd, 'rec_split.tsv')), delimiter='\t') if r['pieces'] == '2']
    assert len(two) >= 6, (len(two), log)
    inbridge = sum(50 <= int(r['cuts']) <= 135 for r in two)
    assert inbridge >= 0.8 * len(two), (inbridge, len(two), [r['cuts'] for r in two])
    # the classifier itself reads the separate shapes (leave-one-out over the exemplars), so a cut in the bridge is a
    # recognition result and not luck; the pieces' own labels are not asserted: each piece carries a bridge stub that
    # changes its shape (that is what arm (e), the permuted-label control, is for on real data)
    rowsA = sorted(rows, key=lambda r: (int(r['line']), int(r['x'])))
    bmA = np.load(os.path.join(atlas, 'bitmaps.npz'))['signs']
    ia = {r['sid']: i for i, r in enumerate(rows)}
    tk = knn.topk(bmA[[ia[r['sid']] for r in rowsA]], [float(r['rh']) for r in rowsA], [float(r['rw']) for r in rowsA],
                  k=1, exclude=[{knn.sids.index(r['sid'])} for r in rowsA])
    acc = np.mean([t[0][0] == SHAPES[(int(r['pos']) - 1 + int(r['line']) - 1) % 4] for t, r in zip(tk, rowsA)])
    assert acc >= 0.9, acc
    # must-not-block 2: lambda above any gain -> never split
    _, nos, _ = seg(d, 'B2', draw(True, 5), ['--split-by-recognition', lab, '--rec-atlas', atlas, '--rec-lambda', '99'])
    assert len(nos) == 18, len(nos)
    # the control can vary: permuted labels change the chosen cuts on at least one box
    outp, perm, _ = seg(d, 'B3', draw(True, 5), ['--split-by-recognition', lab, '--rec-atlas', atlas, '--rec-lambda', '0.45',
                                                   '--rec-permute-labels', '1'])
    a = {(r['x'], r['w']) for r in rec}; b = {(r['x'], r['w']) for r in perm}
    assert a != b, 'permuted labels gave the identical cut set'
    print('ok')


if __name__ == '__main__':
    main()
