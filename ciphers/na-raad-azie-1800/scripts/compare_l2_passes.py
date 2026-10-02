#!/usr/bin/env python3
"""Compare two blind passes of invnr 209 leaf 2 (right page) cipher columns, line by line.

  python3 scripts/compare_l2_passes.py data/l2passes/passA.tsv data/l2passes/passB.tsv [--out data/l2passes/compare.tsv]

Pass TSVs: line, pos, top, bottom, kind (c/x/gap/p/w), note. Only kind c columns are aligned (difflib on the
'top/bottom' strings per line). Prints per-line column counts, top-digit and pair agreement over aligned columns, and
writes every aligned or unaligned column with an 'agree' flag so the reconciler settles only the disagreements from
the crops (images/crops209/l2r_L??.jpg).
"""
import csv, sys, difflib, argparse
from collections import defaultdict


def load(path):
    d = defaultdict(list)
    with open(path) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['kind'].strip() == 'c':
                d[r['line'].strip()].append((r['top'].strip(), r['bottom'].strip()))
    return d


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('a'); ap.add_argument('b'); ap.add_argument('--out')
    a_ = ap.parse_args()
    A, B = load(a_.a), load(a_.b)
    rows = []
    tot = dict(n=0, top=0, pair=0, na=0, nb=0)
    print('line\tnA\tnB\taligned\ttop_agree\tpair_agree')
    for line in sorted(set(A) | set(B)):
        a, b = A.get(line, []), B.get(line, [])
        sa = [t for t, _ in a]; sb = [t for t, _ in b]
        sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
        n = top = pair = 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op in ('equal', 'replace') and (i2 - i1) == (j2 - j1):
                for k in range(i2 - i1):
                    x, y = a[i1 + k], b[j1 + k]
                    n += 1; top += x[0] == y[0]; pair += x == y
                    rows.append((line, i1 + k + 1, j1 + k + 1, x[0], x[1], y[0], y[1], int(x == y)))
            else:
                for k in range(i1, i2):
                    rows.append((line, k + 1, '', a[k][0], a[k][1], '', '', 0))
                for k in range(j1, j2):
                    rows.append((line, '', k + 1, '', '', b[k][0], b[k][1], 0))
        print(f'{line}\t{len(a)}\t{len(b)}\t{n}\t{top}\t{pair}')
        tot['n'] += n; tot['top'] += top; tot['pair'] += pair; tot['na'] += len(a); tot['nb'] += len(b)
    n = max(tot['n'], 1)
    print(f"TOTAL\t{tot['na']}\t{tot['nb']}\t{tot['n']}\t{tot['top']} ({tot['top']/n:.1%})\t{tot['pair']} ({tot['pair']/n:.1%})")
    if a_.out:
        with open(a_.out, 'w') as f:
            w = csv.writer(f, delimiter='\t')
            w.writerow(['line', 'posA', 'posB', 'topA', 'botA', 'topB', 'botB', 'agree'])
            w.writerows(rows)


if __name__ == '__main__':
    main()
