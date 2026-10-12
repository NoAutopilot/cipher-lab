#!/usr/bin/env python3
"""TXE4-2: normalise a f.128 reader pass (A2-DIN format: line seg order gloss signs note) into tx_bench format, exactly as
benchmark-tx/build_dint128.py's build() does for the committed passes (that loop is inline in build(), which also opens the
print-alignment files, so it is repeated here on top of build_dint128.rd rather than called). Step 1 of PREREG-txeng4-2 checks
this on the committed f128/passA.tsv and passB.tsv: byte-identical to outputs/dint-f128-print/pass{A,B}.tsv but for the header
comment line.    python3 norm.py IN.tsv OUT.tsv "comment"      /  python3 norm.py --check"""
import os, sys
from collections import defaultdict
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(R, 'benchmark-tx'))
from build_dint128 import rd  # noqa: E402


def normalise(path, comment):
    lines = defaultdict(list)
    for r in rd(path):
        if r['gloss'].startswith('CLEAR:'):
            continue
        lines[r['line']] += [x for x in r['signs'].split() if x != '-']
    out = ['# ' + comment, 'line\tpos\tsign']
    for ln in sorted(lines):
        out += ['f128_%s\t%d\t%s' % (ln, i + 1, s) for i, s in enumerate(lines[ln])]
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    if sys.argv[1] == '--check':
        ok = True
        for P in 'AB':
            got = normalise(os.path.join(R, 'ciphers/fr3621-dinteville-1592/f128/pass%s.tsv' % P), 'x').split('\n', 1)[1]
            want = open(os.path.join(R, 'benchmark-tx/outputs/dint-f128-print/pass%s.tsv' % P)).read().split('\n', 1)[1]
            print('pass%s: %s' % (P, 'byte-identical below the comment line' if got == want else 'DIFFERS'))
            ok &= got == want
        sys.exit(0 if ok else 1)
    open(sys.argv[2], 'w').write(normalise(sys.argv[1], sys.argv[3]))
