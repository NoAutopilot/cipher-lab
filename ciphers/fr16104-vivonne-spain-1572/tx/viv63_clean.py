#!/usr/bin/env python3
"""N6-VIV63 pre-clean of the blind passes before tools/reconcile_passes.py (NOTES "N6-VIV63"); viv54_clean.py plus DUP rows and '[...]'.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63_clean.py f190r f190v f191r f191v

Reads tx/<page>_pass{A,B}.tsv, writes tx/<page>_pass{A,B}_c.tsv: rows marked DUP dropped, [PLAIN:...] stretches and unreadable '[...]'
stretches removed, 'π' written as SIGNS.md's P. Nothing else is changed. Prints per-pass counts (rows kept, DUP rows, PLAIN stretches).
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
for page in sys.argv[1:]:
    for p in 'AB':
        out, dup, plain, unread = [], 0, 0, 0
        for ln in open(os.path.join(HERE, f'{page}_pass{p}.tsv'), encoding='utf-8'):
            if ln.startswith('row\t') or not ln.strip():
                continue
            row, codes = (ln.rstrip('\n').split('\t', 1) + [''])[:2]
            if codes.strip().upper() == 'DUP':
                dup += 1; continue
            plain += len(re.findall(r'\[PLAIN:[^\]]*\]', codes))
            codes = re.sub(r'\[PLAIN:[^\]]*\]', ' ', codes)
            unread += len(re.findall(r'\[[^\]]*\]', codes))
            codes = re.sub(r'\[[^\]]*\]', ' ', codes)
            toks = ['P' + t[1:] if t.startswith('π') else t for t in codes.split()]
            if toks:
                out.append(f'{row}\t{" ".join(toks)}')
        with open(os.path.join(HERE, f'{page}_pass{p}_c.tsv'), 'w', encoding='utf-8') as f:
            f.write('row\tcodes\n' + '\n'.join(out) + '\n')
        print(page, p, len(out), 'rows kept;', dup, 'DUP;', plain, 'PLAIN stretches;', unread, "'[...]' stretches")
