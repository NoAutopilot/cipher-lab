#!/usr/bin/env python3
"""Offline test for tools/glyph_atlas.py: a synthetic page of 3 lines x 12 signs of two shapes (a box and an X, jittered in size and stroke);
every X carries a small ring above it. Segment must find 36 signs and 18 marks, each mark attached to an X;
cluster with k=6 must give pure clusters (over-split, merged by the labels); atlas must write two codes."""
import csv, json, os, subprocess, sys, tempfile
import numpy as np, cv2

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')


def main():
    d = tempfile.mkdtemp()
    img = np.full((900, 1600), 235, np.uint8)
    rng = np.random.default_rng(1)
    for li in range(3):
        yc = 200 + li * 250
        for k in range(12):
            x = 100 + k * 115
            j = lambda: int(rng.integers(-2, 3))
            t = int(rng.integers(4, 7))
            if k % 2:
                cv2.line(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
                cv2.line(img, (x + 50 + j(), yc - 30 + j()), (x + j(), yc + 30 + j()), 20, t)
                cv2.circle(img, (x + 25, yc - 60), 8, 20, 3)
            else:
                cv2.rectangle(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
    p = os.path.join(d, 'page.png')
    cv2.imwrite(p, img)
    run = lambda *a: subprocess.run([sys.executable, TOOL, *a], check=True, capture_output=True, text=True).stdout
    run('segment', '--page', f'p1={p}', '--out', d)
    S = list(csv.DictReader(open(os.path.join(d, 'signs.tsv')), delimiter='\t'))
    M = list(csv.DictReader(open(os.path.join(d, 'marks.tsv')), delimiter='\t'))
    assert len(S) == 36, len(S)
    assert len(M) == 18, len(M)
    marked = {s['sid'] for s in S if s['marks']}
    assert len(marked) == 18 and all(int(s['pos']) % 2 == 0 for s in S if s['sid'] in marked)
    run('cluster', '--out', d, '--k', '6', '--k-marks', '1', '--pca-scale', 'shared')
    C = {r['id']: r['cluster'] for r in csv.DictReader(open(os.path.join(d, 'clusters.tsv')), delimiter='\t') if r['kind'] == 'sign'}
    xs = {C[s['sid']] for s in S if s['sid'] in marked}
    bs = {C[s['sid']] for s in S if s['sid'] not in marked}
    assert not xs & bs, (xs, bs)   # over-split is fine (merged by labels), mixed clusters are not
    lab = {'signs': {**{c: 'X' for c in xs}, **{c: 'B' for c in bs}}, 'marks': {'0': 'o'}}
    json.dump(lab, open(os.path.join(d, 'labels.json'), 'w'))
    out = run('atlas', '--out', d, '--labels', os.path.join(d, 'labels.json'))
    A = list(csv.DictReader(open(os.path.join(d, 'atlas.tsv')), delimiter='\t'))
    assert {r['code'] for r in A} == {'X', 'B'} and all(r['count'] == '18' for r in A), A
    assert [r['marks_seen'] for r in A if r['code'] == 'X'] == ['o:18']
    assert os.path.exists(os.path.join(d, 'atlas.png'))
    bx = os.path.join(d, 'boxes.tsv')
    run('classify', '--out', d, '--labels', os.path.join(d, 'labels.json'), '--page', 'p1', '--tsv', bx,
        '--knn', '3', '--pca-scale', 'shared', '--strips', os.path.join(d, 'strips'), '--max-w', '800')
    B = list(csv.DictReader(open(bx), delimiter='\t'))
    assert len(B) == 36 and all(r['code'] == ('X' if r['box'] in marked else 'B') for r in B), B
    assert all(r['marks'] == ('o' if r['box'] in marked else '') for r in B)
    assert len(os.listdir(os.path.join(d, 'strips'))) == 6   # 3 lines x 2 parts

    # merge-vgap: two dust specks far apart vertically, same x-range, no other line nearby --
    # must NOT be chained into one giant box (the fr3151-seure-1558 f75L bug, 24 Sept 2026).
    d2 = tempfile.mkdtemp()
    img2 = np.full((900, 400), 235, np.uint8)
    cv2.rectangle(img2, (100, 90), (150, 150), 20, 5)   # one real sign, sets mh
    cv2.rectangle(img2, (100, 200), (110, 210), 20, 3)  # dust speck A, same x range
    cv2.rectangle(img2, (100, 700), (110, 710), 20, 3)  # dust speck B, far below, same x range
    p2 = os.path.join(d2, 'page.png')
    cv2.imwrite(p2, img2)
    run('segment', '--page', f'p2={p2}', '--out', d2, '--min-area', '0.05')
    S2 = list(csv.DictReader(open(os.path.join(d2, 'signs.tsv')), delimiter='\t'))
    assert max(int(s['h']) for s in S2) < 400, [(s['sid'], s['h']) for s in S2]
    print('ok')


if __name__ == '__main__':
    main()
