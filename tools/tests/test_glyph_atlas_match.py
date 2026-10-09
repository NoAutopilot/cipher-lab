#!/usr/bin/env python3
"""Offline test for tools/glyph_atlas.py match (MQS-GLYPH-MATCH, 9 Oct 2026).
Atlas = two synthetic pages of boxes and Xs (+ one excluded page of circles). Catches: a fresh page of the same two
shapes scores a higher IR than a page of triangles and circles, and ranks first. Must NOT: let an excluded page shape the
fit (the IR table is identical with the circle page excluded and with it absent from the atlas altogether), nor accept
--stored for a page still in the atlas (exit non-zero). --shuffle writes one column per seed."""
import csv, os, subprocess, sys, tempfile
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')


def page(path, shapes, seed):
    img = np.full((900, 1600), 235, np.uint8)
    rng = np.random.default_rng(seed)
    for li in range(3):
        yc = 200 + li * 250
        for k in range(12):
            x, j, t = 100 + k * 115, (lambda: int(rng.integers(-3, 4))), int(rng.integers(4, 7))
            s = shapes[k % len(shapes)]
            if s == 'X':
                cv2.line(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
                cv2.line(img, (x + 50 + j(), yc - 30 + j()), (x + j(), yc + 30 + j()), 20, t)
            elif s == 'B':
                cv2.rectangle(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
            elif s == 'O':
                cv2.circle(img, (x + 25, yc), 28 + j(), 20, t)
            else:   # triangle
                pts = np.array([[x + 25 + j(), yc - 30], [x + j(), yc + 30], [x + 50 + j(), yc + 30]], np.int32)
                cv2.polylines(img, [pts], True, 20, t)
    cv2.imwrite(path, img)
    return path


def table(p):
    return {r['leaf']: r for r in csv.DictReader(open(p), delimiter='\t')}


def main():
    d = tempfile.mkdtemp()
    run = lambda *a, check=True: subprocess.run([sys.executable, TOOL, *a], check=check, capture_output=True, text=True)
    pa, pb = page(os.path.join(d, 'a.png'), 'BX', 1), page(os.path.join(d, 'b.png'), 'XB', 2)
    pc = page(os.path.join(d, 'c.png'), 'O', 3)
    full, two = os.path.join(d, 'full'), os.path.join(d, 'two')
    run('segment', '--page', f'a={pa}', '--page', f'b={pb}', '--page', f'c={pc}', '--out', full)
    run('segment', '--page', f'a={pa}', '--page', f'b={pb}', '--out', two)
    qs = ['--page', f'same={page(os.path.join(d, "q1.png"), "BX", 7)}',
          '--page', f'other={page(os.path.join(d, "q2.png"), "TO", 8)}']
    t1, t2 = os.path.join(d, 't1.tsv'), os.path.join(d, 't2.tsv')
    out = run('match', '--out', full, '--exclude-page', 'c', '--k', '4', '--shuffle', '3', '--positive', 'same',
              '--tsv', t1, *qs).stdout
    A = table(t1)
    assert float(A['same']['ir']) > float(A['other']['ir']) and A['same']['rank'] == '1', A
    assert 'ir_s3' in A['same'] and 'margin' in out, (A, out)
    run('match', '--out', two, '--k', '4', '--shuffle', '3', '--tsv', t2, *qs)
    B = table(t2)
    assert all(A[k][c] == B[k][c] for k in A for c in A[k]), (A, B)   # excluded page never touched the fit
    r = run('match', '--out', full, '--stored', 'c', '--k', '4', '--tsv', t1, check=False)
    assert r.returncode != 0 and 'still in the atlas' in (r.stderr + r.stdout), r
    s = run('match', '--out', full, '--exclude-page', 'c', '--stored', 'c', '--k', '4', '--tsv', t1).stdout
    assert float(table(t1)['c']['ir']) < 0.5, s   # circles were excluded: they sit outside the box/X clusters
    print('ok')


if __name__ == '__main__':
    main()
