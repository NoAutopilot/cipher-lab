#!/usr/bin/env python3
"""R7-OLDA: per-sign disagreement between two blind passes over the block A and C2 crops (PREREG_R7-OLDA.md item 3).
Normalisation is diff_pass2.py's norm_tok (PREREG_OLD-PASS2 item 2) on both sides; the pass markers '~' (struck word)
and '+' (interlinear addition) are dropped like punctuation. Agreement, not accuracy.

  python3 diff_r7olda.py passA.tsv passB.tsv [--norm-out DIR]
"""
import csv, os, sys
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diff_pass2 import norm_tok, lev
CONF = {}

def lines(path):
    d = defaultdict(list); c = defaultdict(list)
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            n = norm_tok(r['token'].replace('~', '').replace('+', ''))
            if n:
                d[(r['block'], int(r['line']))].append(n); c[(r['block'], int(r['line']))].append(r['conf'])
    CONF[path] = c
    return d

def main():
    a, b = lines(sys.argv[1]), lines(sys.argv[2])
    tot = defaultdict(lambda: [0, 0.0])
    for k in sorted(set(a) | set(b)):
        x, y = ''.join(a.get(k, [])), ''.join(b.get(k, []))
        e = lev(x, y); m = (len(x) + len(y)) / 2
        tot[k[0]][0] += e; tot[k[0]][1] += m
        print(f"{k[0]}\t{k[1]}\t{e}/{m:.0f}\tA={' '.join(a.get(k, []))}\tB={' '.join(b.get(k, []))}")
    E = N = 0
    for blk, (e, n) in sorted(tot.items()):
        print(f"BLOCK {blk}: {e}/{n:.0f} = {100*e/n:.1f}% per-sign disagreement"); E += e; N += n
    print(f"TOTAL A+C2: {E}/{N:.0f} = {100*E/N:.1f}% per-sign disagreement (agreement, not accuracy; gate 10.0%)")
    if '--norm-out' in sys.argv:
        out = sys.argv[sys.argv.index('--norm-out') + 1]
        for name, d, p in (('passA', a, sys.argv[1]), ('passB', b, sys.argv[2])):
            with open(os.path.join(out, f'norm_{name}.tsv'), 'w') as f:
                f.write('line\tpos\ttoken\tconf\n')
                for k in sorted(d):
                    for i, t in enumerate(d[k], 1):
                        f.write(f"{k[0]}_L{k[1]:02d}\t{i}\t{t}\t{CONF[p][k][i-1]}\n")

if __name__ == '__main__':
    main()
