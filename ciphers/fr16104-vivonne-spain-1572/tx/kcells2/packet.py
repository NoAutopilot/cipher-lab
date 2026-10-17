#!/usr/bin/env python3
"""VIV-KCELLS2 step 5: tx/kcells2/packet.tsv -- tiles for a split of reader labels c and 2 (no crops cut).

    python3 tx/kcells2/packet.py

Re-runs tx/kcells/kcells.py's target alignment (same instrument, its control PASSed 12/14) and lists every label-c position where the
clerk wrote p, every label-2 position where he wrote m, and as many c / 2 positions at e, q, u (contrast tiles, in stream order).
crop = the line's existing crops under images/ (segment not resolved; ';'-joined).
"""
import glob, os, sys
H = os.path.dirname(os.path.abspath(__file__)); TX = os.path.dirname(H); T = os.path.dirname(TX)
sys.path.insert(0, os.path.join(TX, 'kcells'))
import kcells as kc  # noqa: E402


def main():
    r = kc.run(kc.load(), kc.seedmap(kc.ckey()))
    al = [(name, lab, l, loc) for name in r for lab, l, loc in r[name][0]]
    want = {'c': 'p', '2': 'm'}
    rows = []
    for lab, X in want.items():
        hit = [a for a in al if a[1] == lab and a[2] == X]
        other = [a for a in al if a[1] == lab and a[2] in 'equ'][:len(hit)]
        rows += [(a, 'target') for a in hit] + [(a, 'contrast') for a in other]
    with open(os.path.join(H, 'packet.tsv'), 'w', encoding='utf-8') as f:
        f.write('kind\tpair\tpage\tline\tpos\tlabel\tclerk_letter\tcrop\n')
        for (name, lab, l, (pg, ln, i)), kind in rows:
            crops = ';'.join(sorted(os.path.relpath(p, T) for p in glob.glob(os.path.join(T, 'images', f'*_{pg}_{ln}_s*.jpg'))))
            f.write(f'{kind}\t{name}\t{pg}\t{ln}\t{i}\t{lab}\t{l}\t{crops}\n')
    from collections import Counter
    print(Counter((k, a[1], a[2]) for a, k in rows))


if __name__ == '__main__':
    main()
