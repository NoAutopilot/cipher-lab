#!/usr/bin/env python3
"""N5-VIV54 pre-clean of the blind passes before tools/reconcile_passes.py (NOTES "N5-VIV54").

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54_clean.py f173r f173v

Reads tx/<page>_pass{A,B}.tsv, writes tx/<page>_pass{A,B}_c.tsv: [PLAIN:...] stretches removed (L02/L03 of f.173r are
plain and duplicate crops; the plain head of f.173r L04 and the "Il non" group both readers wrote as plain are dropped,
as N5-VIVK did), pass A's 'π' written as SIGNS.md's P. Nothing else is changed.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for page in sys.argv[1:]:
    for p in 'AB':
        out = []
        for ln in open(os.path.join(HERE, f'{page}_pass{p}.tsv'), encoding='utf-8'):
            if ln.startswith('row\t') or not ln.strip():
                continue
            row, codes = (ln.rstrip('\n').split('\t', 1) + [''])[:2]
            codes = re.sub(r'\[PLAIN:[^\]]*\]', ' ', codes)
            toks = ['P' + t[1:] if t.startswith('π') else t for t in codes.split()]
            if toks:
                out.append(f'{row}\t{" ".join(toks)}')
        with open(os.path.join(HERE, f'{page}_pass{p}_c.tsv'), 'w', encoding='utf-8') as f:
            f.write('row\tcodes\n' + '\n'.join(out) + '\n')
        print(page, p, len(out), 'rows')
