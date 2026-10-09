#!/usr/bin/env python3
"""TXP-D89: passZ_pipeline.tsv = rec/ciphertext_draft.tsv with adjud_out.tsv applied (sign replaced; NONE deletes;
two labels insert two signs). CLEAR positions (clear words in the line) are dropped: passZ is the cipher-sign sequence
per line, ids f89_L01..L14, renumbered from 1. Mechanical.   python3 make_passz.py [--check]"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
rd = lambda p: list(csv.DictReader(open(p, newline=''), delimiter='\t'))
adj = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd(os.path.join(H, 'adjud_out.tsv'))}
seq = {}
for r in rd(os.path.join(H, 'rec/ciphertext_draft.tsv')):
    s = adj.get((r['line'], int(r['position'])), r['sign'])
    for t in s.split():
        if t in ('NONE', 'CLEAR', '-'):
            continue
        seq.setdefault(r['line'], []).append(t)
out = ['line\tpos\tsign']
for ln in sorted(seq):
    out += ['f89_%s\t%d\t%s' % (ln, i + 1, s) for i, s in enumerate(seq[ln])]
t = '\n'.join(out) + '\n'
p = os.path.join(H, 'passZ_pipeline.tsv')
old = open(p).read() if os.path.exists(p) else None
if '--check' in sys.argv:
    sys.exit(0 if old == t else 1)
open(p, 'w').write(t); print('passZ signs', len(out) - 1)
