#!/usr/bin/env python3
"""TXE4-9 check 2 (read-free, no truth): the label pairs on which the committed f98v and f113 passes (passA/passB, Opus,
txeng2) split, and how often those same pairs occur as splits in the committed f89 passA/passB. Alignment = tx_bench.align with
empty truth sets (pure label edit distance, G 0.75). CLEAR rows dropped everywhere; '.' rows kept on f98v/f113 (their items keep
dots) and dropped on f89 (its item has no dots, RESULTS.md 'Dots dropped'). Prints the pair table and the exposure: the share of
f89 split events that fall on a calibration split pair. This is the stated power of the transfer check, computed before any read."""
import os, sys
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools'))
import tx_bench, tx_calibrate
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'txeng2')


def load(item, name, drop_dots):
    d = tx_calibrate.load_read(os.path.join(B, item, name + '.tsv'))
    return {k: [s for s in v if not (drop_dots and s == '.')] for k, v in d.items()}


def splits(a, b):
    c = Counter(); n = 0
    for ln in sorted(set(a) | set(b)):
        x, y = a.get(ln, []), b.get(ln, [])
        for ri, osg in tx_bench.align(x, [set() for _ in x], y):
            n += 1
            if ri is None:
                c[('<none>', osg)] += 1
            elif osg is None:
                c[(x[ri], '<none>')] += 1
            elif x[ri] != osg:
                c[tuple(sorted((x[ri], osg)))] += 1
    return c, n


cal = Counter(); ncal = 0
for item in ('dint-f98v-gloss', 'dint-f113-gloss'):
    c, n = splits(load(item, 'passA', False), load(item, 'passB', False)); cal += c; ncal += n
    print('%s: alignment columns %d, split columns %d, distinct pairs %d' % (item, n, sum(c.values()), len(c)))
f89, n89 = splits(load('dint-f89-gloss', 'passA', True), load('dint-f89-gloss', 'passB', True))
print('dint-f89-gloss: alignment columns %d, split columns %d, distinct pairs %d' % (n89, sum(f89.values()), len(f89)))
sub_cal = {p: k for p, k in cal.items() if '<none>' not in p}
hit = sum(f89.get(p, 0) for p in sub_cal)
tot89 = sum(k for p, k in f89.items() if '<none>' not in p)
print('calibration substitution pairs %d (events %d); f89 substitution split events %d, of which on a calibration pair %d (%.2f)'
      % (len(sub_cal), sum(sub_cal.values()), tot89, hit, hit / tot89 if tot89 else 0))
print('pair\tcalib_splits\tf89_splits')
for p, k in sorted(cal.items(), key=lambda t: -t[1]):
    print('%s~%s\t%d\t%d' % (p[0], p[1], k, f89.get(p, 0)))
print('f89 pairs not seen on the calibration pages: %d events' % (tot89 - hit))
