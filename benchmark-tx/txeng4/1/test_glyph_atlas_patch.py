#!/usr/bin/env python3
"""Offline test of benchmark-tx/txeng4/1/glyph_atlas.patch (TXE4-1, 12 Oct 2026): applies the patch to a temp copy of
tools/glyph_atlas.py and checks the three new atlas options on a synthetic page. No network, no model, no truth.
Must catch: (1) the canonical cut is exactly the drawing's box (pixel-equal to the numpy slice); (2) --shuffle-rows gives a
derangement (no row shows its own tiles) and the same seed gives the same image bytes; a different seed differs.
Must NOT block: --from-tokens writes the same sheet as --from-truth on the same TSV (byte-identical)."""
import csv, hashlib, os, shutil, subprocess, sys, tempfile
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def main():
    d = tempfile.mkdtemp()
    shutil.copy(os.path.join(ROOT, 'tools/glyph_atlas.py'), d)
    r = subprocess.run(['patch', '-p1', '-d', d, '-i', os.path.join(HERE, 'glyph_atlas.patch')], capture_output=True, text=True)
    if r.returncode:
        r = subprocess.run(['patch', '-p0', '-d', d, 'glyph_atlas.py', '-i', os.path.join(HERE, 'glyph_atlas.patch')],
                           capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    tool = os.path.join(d, 'glyph_atlas.py')
    # synthetic page: 3 lines x 12 signs, boxes (even k) and crosses (odd k), as tools/tests/test_glyph_atlas.py
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
            else:
                cv2.rectangle(img, (x + j(), yc - 30 + j()), (x + 50 + j(), yc + 30 + j()), 20, t)
    pg = os.path.join(d, 'pg.png'); cv2.imwrite(pg, img)
    out = os.path.join(d, 'atlas')
    r = subprocess.run([sys.executable, tool, 'segment', '--out', out, '--page', f'pg={pg}'], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    signs = list(csv.DictReader(open(os.path.join(out, 'signs.tsv')), delimiter='\t'))
    assert len(signs) >= 30, len(signs)
    # tokens by shape: a box is wider than tall by construction? both 50x60; use x parity of the grid instead
    with open(os.path.join(d, 'tokens.tsv'), 'w') as f:
        f.write('sid\tcode\n')
        for s in signs:
            k = round((int(s['x']) - 100) / 115)
            f.write(f"{s['sid']}\t{'X' if k % 2 else 'B'}\n")
    # a drawing with two cells and a boxes file
    draw = np.full((60, 140), 255, np.uint8)
    cv2.rectangle(draw, (10, 10), (50, 50), 0, 3)
    cv2.line(draw, (80, 10), (120, 50), 0, 3); cv2.line(draw, (120, 10), (80, 50), 0, 3)
    cv2.imwrite(os.path.join(d, 'draw.png'), draw)
    open(os.path.join(d, 'boxes.tsv'), 'w').write('token\tdrawing\tx0\ty0\tx1\ty1\nB\tdraw.png\t5\t5\t55\t55\nX\tdraw.png\t75\t5\t125\t55\n')
    sys.path.insert(0, d)
    import glyph_atlas as GA
    canon = GA.load_canonical_boxes(os.path.join(d, 'boxes.tsv'), d)
    assert np.array_equal(canon['B'], draw[5:55, 5:55]) and np.array_equal(canon['X'], draw[5:55, 75:125]), 'canonical cut != box'

    def build(name, extra):
        sd = os.path.join(d, name); os.makedirs(sd, exist_ok=True)
        r = subprocess.run([sys.executable, tool, 'atlas', '--out', out, '--canonical-boxes', os.path.join(d, 'boxes.tsv'),
                            '--canonical-dir', d, '--per', '4', '--spread', '--trim', '0.2', '--sheet-dir', sd] + extra,
                           capture_output=True, text=True)
        assert r.returncode == 0, r.stdout + r.stderr
        return sd
    a = build('truth', ['--from-truth', os.path.join(d, 'tokens.tsv')])
    b = build('tokens', ['--from-tokens', os.path.join(d, 'tokens.tsv')])
    assert sha(os.path.join(a, 'sheet_truth_01.png')) == sha(os.path.join(b, 'sheet_truth_01.png')), '--from-tokens differs from --from-truth'
    s1 = build('shuf1', ['--from-tokens', os.path.join(d, 'tokens.tsv'), '--shuffle-rows', '7'])
    s1b = build('shuf1b', ['--from-tokens', os.path.join(d, 'tokens.tsv'), '--shuffle-rows', '7'])
    rows = list(csv.DictReader(open(os.path.join(s1, 'sheet_truth.tsv')), delimiter='\t'))
    hand = [r for r in rows if r['shown'] == 'hand']
    assert len(hand) == 2 and all(r['tiles_from'] != r['code'] for r in hand), rows
    assert sha(os.path.join(s1, 'sheet_truth_01.png')) == sha(os.path.join(s1b, 'sheet_truth_01.png')), 'same seed, different image'
    assert sha(os.path.join(s1, 'sheet_truth_01.png')) != sha(os.path.join(a, 'sheet_truth_01.png')), 'shuffle changed nothing'
    # the derangement helper on more rows: never a fixed point, deterministic
    codes = list('abcdefg')
    m = GA.derange(codes, 20261012)
    assert all(m[c] != c for c in codes) and sorted(m.values()) == codes and m == GA.derange(codes, 20261012)
    print('ok: canonical cut equals the box; --from-tokens == --from-truth; derangement with no fixed row, seed-stable')
    shutil.rmtree(d)


if __name__ == '__main__':
    main()
