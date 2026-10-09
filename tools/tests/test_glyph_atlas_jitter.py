#!/usr/bin/env python3
"""Offline test of `glyph_atlas.py classify --jitter` (TXE-J, 9 Oct 2026). A synthetic atlas: class A = a blob filling
its box, class B = the same blob cut by a 1-2 px shift of the window. Two query boxes on one page: a 6 px blob (a 2 px
shift cuts a third of it -> its jittered top-1 flips to B: low stab) and a 60 px blob (a 2 px shift cuts 3% -> still A:
stab 1.0). Also checks the unjittered re-cut reproduces the stored top-1 and that --jitter leaves code/k1 unchanged."""
import csv, json, os, subprocess, sys, tempfile
import numpy as np
import cv2

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')
sys.path.insert(0, os.path.join(HERE, '..'))
import glyph_atlas as G  # noqa: E402


def main():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'crops'))
    mh = 20.0
    page = np.full((100, 200), 255, np.uint8)
    page[30:36, 20:26] = 0            # small blob, box 20,30 6x6
    page[20:80, 100:160] = 0          # big blob, box 100,20 60x60
    cv2.imwrite(os.path.join(d, 'crops', 'q.png'), page)
    json.dump({'q': {'image': '', 'box': None, 'median_h': mh}, 't': {'image': '', 'box': None, 'median_h': mh}},
              open(os.path.join(d, 'pages.json'), 'w'))
    rows, bms, clus = [], [], []

    def add(page_, sid, x, y, w, h, bm, cluster):
        rows.append(dict(sid=sid, page=page_, line=1, pos=len(rows) + 1, x=x, y=y, w=w, h=h, rh=h / mh, rw=w / mh,
                         dy=0, marks=''))
        bms.append(bm); clus.append((sid, cluster))

    def cut(n, dx, dy):              # an n x n blob seen through an n x n window shifted by dx, dy
        m = np.zeros((n, n), np.uint8)
        m[max(0, -dy):n - max(0, dy), max(0, -dx):n - max(0, dx)] = 1
        return G.bitmap(m)
    k = 0
    for n in (6, 60):
        for _ in range(6):
            k += 1; add('t', f't_A{k}', 0, 0, n, n, cut(n, 0, 0), 'cA')
        sh = [(dx, dy) for dx in (-2, -1, 0, 1, 2) for dy in (-2, -1, 0, 1, 2) if (dx, dy) != (0, 0)] if n == 6 \
            else [(dx, dy) for dx in (-20, 20) for dy in (-20, 0, 20)]
        for dx, dy in sh:
            k += 1; add('t', f't_B{k}', 0, 0, n, n, cut(n, dx, dy), 'cB')
    add('q', 'q_01_001', 20, 30, 6, 6, cut(6, 0, 0), 'cQ')
    add('q', 'q_01_002', 100, 20, 60, 60, cut(60, 0, 0), 'cQ')
    cols = ['sid', 'page', 'line', 'pos', 'x', 'y', 'w', 'h', 'rh', 'rw', 'dy', 'marks']
    with open(os.path.join(d, 'signs.tsv'), 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    open(os.path.join(d, 'marks.tsv'), 'w').write('mid\tpage\tline\tx\ty\tw\th\trh\trw\tsid\n')
    with open(os.path.join(d, 'clusters.tsv'), 'w') as f:
        f.write('kind\tid\tcluster\n')
        for sid, c in clus:
            f.write(f'sign\t{sid}\t{c}\n')
    np.savez(os.path.join(d, 'bitmaps.npz'), signs=np.array(bms))
    json.dump({'signs': {'cA': 'A', 'cB': 'B', 'cQ': '_'}, 'marks': {}}, open(os.path.join(d, 'labels.json'), 'w'))
    base = ['classify', '--out', d, '--labels', os.path.join(d, 'labels.json'), '--page', 'q', '--exclude-page',
            '--topk', '3', '--knn', '3', '--pca-scale', 'shared']   # 'unit' blows up the null components of a 44-row set
    plain, jit = os.path.join(d, 'plain.tsv'), os.path.join(d, 'jit.tsv')
    subprocess.run([sys.executable, TOOL] + base + ['--tsv', plain], check=True, capture_output=True)
    subprocess.run([sys.executable, TOOL] + base + ['--tsv', jit, '--jitter', '5', '--jitter-seed', '3'], check=True,
                   capture_output=True)
    P = list(csv.DictReader(open(plain), delimiter='\t'))
    J = {r['box']: r for r in csv.DictReader(open(jit), delimiter='\t')}
    assert 'stab' not in P[0]
    for r in P:                      # --jitter adds columns, never changes the unjittered answer
        assert all(J[r['box']][c] == r[c] for c in r), r['box']
        assert r['code'] == 'A', r
        assert J[r['box']]['k1_0'] == r['code']   # the unjittered re-cut reproduces the stored top-1
    small, big = float(J['q_01_001']['stab']), float(J['q_01_002']['stab'])
    assert big == 1.0, big
    assert small <= 0.6, small       # the 6 px box flips to B under most 2 px shifts
    assert J['q_01_001']['k1_j'] == 'B' or small >= 0.4
    print(f'ok (stab small {small:.2f}, big {big:.2f})')


if __name__ == '__main__':
    main()
