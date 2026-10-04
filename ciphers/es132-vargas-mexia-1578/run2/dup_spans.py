#!/usr/bin/env python3
"""dup_spans.py PAGE -- list A/B disagreement spans (normalised by test2.load_pass) with span keys (line, A start index 1-based)
for writing a reconcile_<PAGE>.py decision table (A3V3-ES9396, 4 Oct 2026)."""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
pg = sys.argv[1]
A, B = load_pass(HERE / f'passes/{pg}_passA.tsv'), load_pass(HERE / f'passes/{pg}_passB.tsv')
d = n = 0
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    n += max(len(a), len(b))
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal': continue
        d += max(i2 - i1, j2 - j1)
        print(f"{ln}\t{i1+1}\tA: {' '.join(a[i1:i2]) or '-'}\tB: {' '.join(b[j1:j2]) or '-'}\t| ctx {' '.join(a[max(0,i1-2):i1])}")
print(f'# err_2reader {d}/{n} = {d/n:.3f}', file=sys.stderr)
