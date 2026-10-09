#!/usr/bin/env python3
"""SUR-0744R: split one pass's verbatim TSV (<P>/raw.tsv) into passA_sonnet_blind.tsv (alias_run.run()'s fixed filename) and
gloss_reconciled.tsv (that pass's own gloss rows, unedited), as SUR-BLIND mk.py. Notation only (rule 3): section sign -> &, em dash -> -.
Row-label fix only (pass A): A wrote its L10 gloss row under the label L09 (the second 'L09 gloss' row, directly before 'L10 cipher';
its own remark on that cipher row names the slip); relabelled L10. No sign is re-read. Usage: python3 mk.py A|B"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); p = sys.argv[1]; d = os.path.join(H, p)
rows = [l.rstrip('\n') for l in open(os.path.join(d, 'raw.tsv'), encoding='utf-8')]
rows = [r.replace('§', '&').replace('—', '-') for r in rows]
seen = set(); fixed = []
for r in rows:
    f = r.split('\t')
    if len(f) > 1 and f[1] == 'gloss':
        if (f[0], 'gloss') in seen and f[0] == 'L09': f[0] = 'L10'
        seen.add((f[0], 'gloss'))
    fixed.append('\t'.join(f))
rows = fixed
hdr = f'# SUR-0744R pass {p}: one blind Sonnet call on crops p0744R_L01-L22 (crop paths only, reader-code vocabulary, [ij]=dotted, y=undotted; no values, no key), 9 Oct 2026 00:4x UTC, after PREREG 94e16aee. Verbatim as returned (notation + row label per mk.py).\n'
open(os.path.join(d, 'passA_sonnet_blind.tsv'), 'w', encoding='utf-8').write(hdr + '\n'.join(rows) + '\n')
g = [f'# SUR-0744R pass {p}: that pass\'s own gloss rows, unedited', 'crop\tgloss\tnote']
g += [f"{r.split(chr(9))[0]}\t{r.split(chr(9))[2]}\t" for r in rows[1:] if r.split('\t')[1] == 'gloss']
open(os.path.join(d, 'gloss_reconciled.tsv'), 'w', encoding='utf-8').write('\n'.join(g) + '\n')
