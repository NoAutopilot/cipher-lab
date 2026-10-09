#!/usr/bin/env python3
"""SUR-0745: split one pass's verbatim TSV (<P>/raw.tsv) into passA_sonnet_blind.tsv (alias_run's fixed filename) and
gloss_reconciled.tsv (that pass's own gloss rows, unedited), as SUR-0744R mk.py. Notation only (rule 3): section sign -> &,
em dash -> -, glyph psi/lambda/delta -> vocabulary code. No sign is re-read. Usage: python3 mk.py A|B"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); p = sys.argv[1]; d = os.path.join(H, p)
NOTE = {'§': '&', '—': '-', 'ψ': '[psi]', 'λ': '[lambda]', 'δ': '[delta]', 'Δ': '[delta]'}
rows = [l.rstrip('\n') for l in open(os.path.join(d, 'raw.tsv'), encoding='utf-8') if l.strip()]
def fix(r):
    f = r.split('\t')
    if len(f) > 2 and f[1] == 'cipher':
        for a, b in NOTE.items(): f[2] = f[2].replace(a, b)
    return '\t'.join(f)
rows = [fix(r) for r in rows]
hdr = f'# SUR-0745 pass {p}: one blind Sonnet call on crops p0745L_L01-L22 (crop paths only, reader-code vocabulary, [ij]=dotted, y=undotted; no values, no key), 9 Oct 2026 02:2x UTC, after PREREG 6cb5b6299. Verbatim as returned (notation per mk.py).\n'
open(os.path.join(d, 'passA_sonnet_blind.tsv'), 'w', encoding='utf-8').write(hdr + '\n'.join(rows) + '\n')
g = [f'# SUR-0745 pass {p}: that pass\'s own gloss rows, unedited', 'crop\tgloss\tnote']
g += [f"{r.split(chr(9))[0]}\t{r.split(chr(9))[2]}\t" for r in rows[1:] if len(r.split('\t')) > 2 and r.split('\t')[1] == 'gloss']
open(os.path.join(d, 'gloss_reconciled.tsv'), 'w', encoding='utf-8').write('\n'.join(g) + '\n')
