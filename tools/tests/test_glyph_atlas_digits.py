#!/usr/bin/env python3
"""Offline test for tools/glyph_atlas.py digits / cut_digits (MANT-CUT, 15 Oct 2026).
Synthetic strip: numeral groups drawn with cv2.putText, separated by filled dots, a clear word at the left end and a
neighbour line of ink above. Catches: each digit's box centre falls inside the drawn digit's own x-span (>= 90% of
digits), the clear word and the neighbour line are not taken as digits. Must NOT: place a digit of a token that is not
on the strip (a tokens list longer than the strip leaves the extra token's digits None, never a neighbour's box).
Also runs the `digits` subcommand end to end on the same strip."""
import csv, os, subprocess, sys, tempfile
import numpy as np, cv2
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import glyph_atlas as G


def strip(path):
    img = np.full((90, 1100), 235, np.uint8)
    cv2.putText(img, 'lorem ipsum dolor sit amet consectetur', (5, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.6, 20, 2)
    x, spans = 20, []
    cv2.putText(img, 'dans', (x, 62), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 20, 2)
    x += 110
    for tok in ['54', '66', '103', '19', '4', '27']:
        for d in tok:
            cv2.putText(img, d, (x, 66), cv2.FONT_HERSHEY_SIMPLEX, 1.6, 20, 3)
            spans.append((x, x + 34))
            x += 36
        x += 8
        cv2.circle(img, (x, 60), 5, 20, -1)
        x += 18
    cv2.imwrite(path, img)
    return img, spans


def main():
    d = tempfile.mkdtemp()
    p = os.path.join(d, 's.png')
    img, spans = strip(p)
    toks = ['54', '66', '103', '19', '4', '27']
    bx, hd = G.cut_digits(img, toks)
    ok = sum(1 for b, (a, e) in zip(bx, spans) if b and a - 3 <= b[0] + b[2] / 2 <= e + 3)
    assert ok >= 0.9 * len(spans), (ok, len(spans), bx)
    assert all(b is None or b[1] > 20 for b in bx), 'a box reached the neighbour line'
    bx2, _ = G.cut_digits(img, toks + ['888'])
    assert len(bx2) == len(spans) + 3
    assert all(b is None for b in bx2[-3:]) or sum(b is not None for b in bx2[-3:]) == 0, bx2[-3:]
    t = os.path.join(d, 'in.tsv')
    open(t, 'w').write('strip\ttokens\n%s\t%s\n' % (p, ' '.join(toks)))
    o = os.path.join(d, 'out.tsv')
    subprocess.run([sys.executable, os.path.join(HERE, '..', 'glyph_atlas.py'), 'digits', '--strips', t, '--tsv', o], check=True)
    rows = list(csv.DictReader(open(o), delimiter='\t'))
    assert len(rows) == len(spans) and ''.join(r['digit'] for r in rows) == ''.join(toks)
    print('ok: %d/%d digits inside their own span; unmatched token left empty; digits subcommand OK' % (ok, len(spans)))


if __name__ == '__main__':
    main()
