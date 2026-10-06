#!/usr/bin/env python3
"""R11A-HAR, 6 Oct 2026: write align_f88r.tsv (passage, merged, posA, idA, idB, status) from reconcile_passes.py's
ciphertext_draft.tsv + disagreements.tsv, the column layout tools/lookalike_pass.py confusion/packet read.
status: agree | split (both readers labelled, labels differ) | gapA / gapB (one reader has no sign there)."""
import csv
from pathlib import Path
here = Path(__file__).resolve().parent
dis = {(r['line'], r['col']): r for r in csv.DictReader(open(here / 'disagreements.tsv'), delimiter='\t')}
rows, posA = [], {}
for r in csv.DictReader(open(here / 'ciphertext_draft.tsv'), delimiter='\t'):
    k = (r['line'], r['position'])
    if k in dis:
        a, b = dis[k]['A'], dis[k]['B']
        st = 'gapA' if a == '-' else 'gapB' if b == '-' else 'split'
    else:
        a = b = r['sign']; st = 'agree'
    pa = ''
    if a != '-':
        posA[r['line']] = posA.get(r['line'], 0) + 1; pa = posA[r['line']]
    rows.append(dict(passage=r['line'], merged=r['position'], posA=pa, idA=a, idB=b, status=st))
with open(here / 'align_f88r.tsv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
from collections import Counter
print(Counter(r['status'] for r in rows))
