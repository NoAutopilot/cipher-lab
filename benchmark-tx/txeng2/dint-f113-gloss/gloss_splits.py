#!/usr/bin/env python3
"""TXP-D113: difflib word alignment of glossA.tsv vs glossB.tsv; writes gloss_splits.tsv (every non-equal opcode) and prints
per-line character agreement. Run from the repo root."""
import csv, difflib
D = 'benchmark-tx/txeng2/dint-f113-gloss'
rd = lambda p: {r['line']: r['text'] for r in csv.DictReader(open(p), delimiter='\t')}
A, B = rd(D + '/glossA.tsv'), rd(D + '/glossB.tsv')
with open(D + '/gloss_splits.tsv', 'w') as f:
    f.write('line\tword_from\tA\tB\n')
    for ln in A:
        a, b = A[ln].split(), B[ln].split()
        ca, cb = A[ln].replace(' ', '').lower(), B[ln].replace(' ', '').lower()
        sm = difflib.SequenceMatcher(None, ca, cb, autojunk=False)
        m = sum(x.size for x in sm.get_matching_blocks())
        print('%s chars agree %d/%d = %.2f' % (ln, m, max(len(ca), len(cb)), m / max(len(ca), len(cb))))
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, [w.lower() for w in a], [w.lower() for w in b], autojunk=False).get_opcodes():
            if op != 'equal':
                f.write('%s\t%d\t%s\t%s\n' % (ln, i1 + 1, ' '.join(a[i1:i2]) or '-', ' '.join(b[j1:j2]) or '-'))
