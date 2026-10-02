#!/usr/bin/env python3
"""NEVBIR-LOOKALIKE step 1 (2 Oct 2026): reader confusion map for the 1572 sign sheet, disk only.

Reads every two-reader alignment on disk (*/passC*_agreement.tsv, written by reconcile_blind.py) and counts, per
unordered label pair, how often reader A and reader B gave different sheet labels at the same aligned position
(status split*). Gaps (one reader saw no sign) are not counted. X_NEW (off-sheet) is kept as a label: a sheet sign
read as off-sheet by the other reader is a confusion too. Writes confusion_1572.tsv (label_a, label_b, n, n_target,
examples) where n_target counts the pairs seen on f.144r or f.168 (the two runs under test) and n is all leaves.
"""
import csv, glob, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
cnt, tgt, ex = collections.Counter(), collections.Counter(), collections.defaultdict(list)
tot = collections.Counter()
for f in sorted(glob.glob(str(HERE / '*/passC*_agreement.tsv'))):
    leaf = Path(f).parent.name
    for r in csv.DictReader(open(f), delimiter='\t'):
        a, b, st = r['idA'], r['idB'], r['status']
        if not a or not b:
            continue
        tot[leaf] += 1
        if not st.startswith('split') or a == b:
            continue
        k = tuple(sorted((a, b)))
        cnt[k] += 1
        if leaf in ('f144r', 'f168'):
            tgt[k] += 1
        if len(ex[k]) < 4:
            ex[k].append(f"{leaf}:{r['passage']}.{r['posA']}")
with open(HERE / 'confusion_1572.tsv', 'w') as o:
    o.write('label_a\tlabel_b\tn\tn_target\texamples\n')
    for k, n in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0])):
        o.write(f'{k[0]}\t{k[1]}\t{n}\t{tgt[k]}\t{" ".join(ex[k])}\n')
print('aligned pairs read:', sum(tot.values()), 'label swaps:', sum(cnt.values()), 'distinct pairs:', len(cnt))
