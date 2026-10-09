#!/usr/bin/env python3
"""Offline test for tools/tx_compare.py tiles / tiles-resolve (TXE-L, M7, 9 Oct 2026): a synthetic page of 6 signs on
2 lines. ordered keeps line order; shuffled is a seeded permutation of the same tiles (same seed -> same key, different
seed -> different order); every tile blanks its neighbours; tiles-resolve maps reads back through the key and falls back
to the line read on '?', X_NEW, missing and unmapped positions. No network, no model."""
import csv, os, sys, tempfile
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_compare as tc  # noqa: E402


def w(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def main():
    d = tempfile.mkdtemp()
    at = os.path.join(d, 'atlas'); os.makedirs(os.path.join(at, 'crops'))
    im = Image.new('L', (400, 200), 255); dr = ImageDraw.Draw(im)
    signs, bp, L = [], [], []
    for li in (1, 2):
        for i in range(3):
            x, y = 20 + 120 * i, 20 + 100 * (li - 1)
            dr.rectangle((x, y, x + 40, y + 50), fill=0)
            sid = f'pg_{li:02d}_{i + 1:03d}'
            signs.append((sid, 'pg', li, i + 1, x, y, 40, 50, 1, 1, 0, ''))
            bp.append((sid, f'pg_L{li:02d}', i + 1, '1:1'))
            L.append((f'pg_L{li:02d}', i + 1, f'T{10 * li + i}'))
    bp.append(('', 'pg_L02', 4, 'skiptok')); L.append(('pg_L02', 4, 'T99'))
    im.save(os.path.join(at, 'crops', 'pg.png'))
    w(os.path.join(at, 'signs.tsv'), 'sid page line pos x y w h rh rw dy marks'.split(), signs)
    w(os.path.join(d, 'bp.tsv'), ['sid', 'line', 'pos', 'op'], bp)
    w(os.path.join(d, 'L.tsv'), ['line', 'pos', 'sign'], L)
    lines = ['pg_L02', 'pg_L01']
    base = ['tiles', '--atlas', at, '--box-pos', os.path.join(d, 'bp.tsv'), '--lines', *lines, '--per-sheet', '4']
    ko = tc.main(base + ['--order', 'ordered', '--out-dir', os.path.join(d, 'o')])
    assert [(k['line'], k['pos']) for k in ko] == [('pg_L02', '1'), ('pg_L02', '2'), ('pg_L02', '3'),
                                                  ('pg_L01', '1'), ('pg_L01', '2'), ('pg_L01', '3')], ko
    assert os.path.exists(os.path.join(d, 'o', 'sheet_02.png')) and not os.path.exists(os.path.join(d, 'o', 'sheet_03.png'))
    assert rd(os.path.join(d, 'o', 'unmapped.tsv'))[0]['pos'] == '4'
    k1 = tc.main(base + ['--order', 'shuffled', '--out-dir', os.path.join(d, 's1'), '--seed', 'a'])
    k2 = tc.main(base + ['--order', 'shuffled', '--out-dir', os.path.join(d, 's2'), '--seed', 'a'])
    k3 = tc.main(base + ['--order', 'shuffled', '--out-dir', os.path.join(d, 's3'), '--seed', 'zz'])
    assert k1 == k2, 'same seed must give the same key'
    assert sorted((k['line'], k['pos']) for k in k1) == sorted((k['line'], k['pos']) for k in ko)
    assert [k['sid'] for k in k1] != [k['sid'] for k in ko] or [k['sid'] for k in k3] != [k['sid'] for k in ko]
    # no neighbour ink: a tile of a 40-px box grown 25% from a 120-px pitch row holds only its own block
    t = tc.sign_tile(tc.Pages(at), {s[0]: dict(zip('sid page line pos x y w h'.split(), map(str, s[:8]))) for s in signs},
                     {}, 'pg_01_002', 50, 1.6)
    px = t.load(); dark_cols = {x for x in range(t.width) for y in range(t.height) if px[x, y] < 128}
    assert max(dark_cols) - min(dark_cols) <= 45, 'neighbour ink must be blanked'
    # resolve through the shuffled key
    rdir = os.path.join(d, 'reads'); os.makedirs(rdir)
    by = {(k['line'], str(k['pos'])): k['tile'] for k in k1}
    w(os.path.join(rdir, 'reads_01.tsv'), ['tile', 'sign_id', 'conf'],
      [(f"#{by[('pg_L01', '1')]}", 'T77', 'H'), (by[('pg_L01', '2')], '?', 'L'), (by[('pg_L01', '3')], 'X_NEW', 'L'),
       (by[('pg_L02', '1')], 'T20', 'M')])
    out = tc.main(['tiles-resolve', '--line-read', os.path.join(d, 'L.tsv'), '--lines', *lines,
                   '--key', os.path.join(d, 's1', 'key.tsv'), '--reads-dir', rdir,
                   '--pass-out', os.path.join(d, 'P.tsv'), '--fallback-out', os.path.join(d, 'fb.tsv')])
    got = {(r['line'], r['pos']): r['sign'] for r in out}
    assert got[('pg_L01', '1')] == 'T77' and got[('pg_L01', '2')] == 'T11' and got[('pg_L01', '3')] == 'T12', got
    assert got[('pg_L02', '1')] == 'T20' and got[('pg_L02', '4')] == 'T99'
    fb = {r['why'] for r in rd(os.path.join(d, 'fb.tsv'))}
    assert fb == {'?', 'X_NEW', 'missing', 'unmapped'}, fb
    print('test_tx_compare_tiles: OK')


if __name__ == '__main__':
    main()
