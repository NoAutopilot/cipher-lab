#!/usr/bin/env python3
"""TXP-B23: gloss.tsv = the two blind gloss reads (glossA/glossB.tsv) with every difflib word split settled by the one Sonnet
look (gloss_splits_out.tsv). Baseline text only: words written above another word (the 'above' column) are kept in
gloss.tsv's 'above' column, not merged into the aligned text. Line ids f23r_L01..L08 (G0n = above cipher line L0n)."""
import csv, difflib, os
D = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))
A = {r['line']: r for r in rd(os.path.join(D, 'glossA.tsv'))}
B = {r['line']: r for r in rd(os.path.join(D, 'glossB.tsv'))}
S = {(r['line'], int(r['word_pos'])): r for r in rd(os.path.join(D, 'gloss_splits_out.tsv'))}
with open(os.path.join(D, 'gloss.tsv'), 'w', encoding='utf-8') as f:
    f.write('line\ttext\tabove\tconf\n')
    for g in sorted(A):
        a, b = A[g]['text'].split(), B[g]['text'].split()
        sm = difflib.SequenceMatcher(None, [w.lower() for w in a], [w.lower() for w in b], autojunk=False)
        words, conf = [], 'H'
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                words += a[i1:i2]
            else:
                s = S[(g, i1 + 1)]
                words += s['reading'].split()
                conf = max(conf, s['conf'], key='HML'.index)
        above = S[(g, 0)]['reading'] if (g, 0) in S else A[g]['above']
        f.write('f23r_L%s\t%s\t%s\t%s\n' % (g[1:], ' '.join(words), above, conf))
