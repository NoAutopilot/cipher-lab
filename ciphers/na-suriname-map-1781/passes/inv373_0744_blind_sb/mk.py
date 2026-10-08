#!/usr/bin/env python3
"""SUR-BLIND: split one pass's verbatim TSV (<P>/raw.tsv) into the two files alias_run.run() reads: passA_sonnet_blind.tsv (verbatim,
with a header comment; the driver's fixed filename, whichever pass it holds) and gloss_reconciled.tsv (that pass's own gloss rows,
unedited -- PREREG: no hand re-reading of the gloss). Usage: python3 mk.py A|B"""
import os, sys
H = os.path.dirname(os.path.abspath(__file__)); p = sys.argv[1]; d = os.path.join(H, p)
rows = [l.rstrip('\n') for l in open(os.path.join(d, 'raw.tsv'), encoding='utf-8')]
# notation only (CLAUDE.md rule 3, one convention before scoring): pass B wrote the Greek glyphs and a section sign where the
# vocabulary codes are [psi] and &; dp_align already reads [lambda] as the glyph. No sign is re-read.
rows = [r.replace('ψ', '[psi]').replace('§', '&') for r in rows]
hdr = f'# SUR-BLIND pass {p}: one blind Sonnet call on crops p0744L_L01-L21 (crop paths only, reader-code vocabulary, [ij]=dotted, y=undotted; no values, no key), 8 Oct 2026 22:2x UTC, after PREREG 09cd01ce8. Verbatim as returned.\n'
open(os.path.join(d, 'passA_sonnet_blind.tsv'), 'w', encoding='utf-8').write(hdr + '\n'.join(rows) + '\n')
g = [f'# SUR-BLIND pass {p}: that pass\'s own gloss rows, unedited', 'crop\tgloss\tnote']
g += [f"{r.split(chr(9))[0]}\t{r.split(chr(9))[2]}\t" for r in rows[1:] if r.split('\t')[1] == 'gloss']
open(os.path.join(d, 'gloss_reconciled.tsv'), 'w', encoding='utf-8').write('\n'.join(g) + '\n')
