#!/usr/bin/env python3
"""diff_passes.py PAGE -- per-line A/B disagreements after test2's shape map + passnorm (RUN2-ES132). Writes run2/<page>_disagreements.tsv."""
import sys, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(HERE))
from test2 import load_pass
pg = sys.argv[1]
A, B = load_pass(HERE / f'passes/{pg}_passA.tsv'), load_pass(HERE / f'passes/{pg}_passB.tsv')
rows = ['line\top\tA_pos\tA\tB']
for ln in sorted(set(A) | set(B)):
    a, b = A.get(ln, []), B.get(ln, [])
    sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != 'equal': rows.append(f'{ln}\t{op}\t{i1+1}\t{" ".join(a[i1:i2])}\t{" ".join(b[j1:j2])}')
(HERE / f'run2/{pg}_disagreements.tsv').write_text('\n'.join(rows) + '\n', encoding='utf-8')
print(len(rows) - 1, 'disagreement spans')
