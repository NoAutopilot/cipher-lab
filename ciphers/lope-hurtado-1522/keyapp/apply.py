#!/usr/bin/env python3
"""LOPE-KEYAPP application (PREREG-LOPE-KEYAPP.md, after gate.py PASS): cifra 7 values for the code tokens Bourdeau left
unread or probable in R9634 and R9646, and the conflict codes at every occurrence (M, both values listed).
Input: r9634_cipher.txt, r9634_reading.tsv (Bourdeau, dbourdeau/cyphersolver 044576987, CC BY 4.0 / MIT, credited).
Usage: python3 apply.py [--check]   (writes ../reading_kolosova_gain.tsv; --check exits 1 if stale)."""
import csv, io, os, re, sys
from gate import tok
HERE = os.path.dirname(os.path.abspath(__file__))
k7 = {}
for r in csv.reader(io.open(os.path.join(HERE, '..', 'kolosova2024_cifra7.tsv'), encoding='utf-8'), delimiter='\t'):
    if r and not r[0].startswith('#') and r[0] != 'word':
        k7.setdefault(r[1].strip(), []).append((r[0], r[2].strip()))
ctx = {}
for line in io.open(os.path.join(HERE, 'r9634_reading.tsv'), encoding='utf-8'):
    if not line.startswith(('#', 'ref')):
        ref, _, rd = line.rstrip('\n').split('\t'); ctx[ref] = rd
cip = {}
for line in io.open(os.path.join(HERE, 'r9634_cipher.txt'), encoding='utf-8'):
    if re.match(r'1[45][rv]\d\d ', line):
        cip[line[:5]] = re.sub(r'\[.*?\]', '', line[6:]).split()
R9646_CTX = {'run1': 'escrevi a v. Mt. como el papa era concertado con el {yib} de Ferrara',
             'run4': 'respondiome que [null] a-bi-a miedo que oviese de ...',
             'run5': 'que creo que {top} dinero en[t]ra[r]a toda ...'}
# (record, line, Bourdeau group, Bourdeau's prior value, kind); kind gain = unread before, upgrade = probable before
ITEMS = [('R9634', '14v01', 'zac', 'unread', 'gain'), ('R9634', '15v06', 'ʃi', 'unread', 'gain'),
         ('R9634', '14v11', 'zub', 'alla (probable, R9656; left unread in reading)', 'upgrade'),
         ('R9634', '14v13', 'zub', 'alla (probable, R9656; left unread in reading)', 'upgrade'),
         ('R9646', 'run1', 'yib', 'duque (probable)', 'upgrade')]
# conflict codes (HYPOTHESES.md): per occurrence, which value the context admits (judged by this worker from Bourdeau's reading)
ADMITS = {'14r03': 'por', '14r06': 'por', '14v09': 'por', '14v10': 'por', '14v21': 'por', '14v23': 'por',
          'tod 14v08': 'otro ("lo otro que le queda"; otra not with lo)',
          'ʃop': 'bi (syllable inside a spelled word; tiempo breaks the word)',
          'ʃal 14r10': 'both (estan / todos muertos de miedo)', 'ʃal 14v02': 'both (toma esta / todo ∂ʇʇ&8ɣɣωHo)',
          'ʃal 14v13': 'both (es esta / toda de frontera; todo is masculine)', 'ʃal 15v10': 'both (en esta esto / en todo esto)'}
CONFLICT = {'top': ('por', 'razón (por = tog)'), 'tod': ('otro', 'otra = tud'), 'ʃop': ('bi', 'tiempo = sop'),
            'ʃal': ('esta', 'todo = sal')}

def k7val(g):
    v = k7.get(tok(g) or '', [])
    return ' / '.join(w for w, _ in v), ('M' if any(t == 'M' for _, t in v) else 'H') if v else ''

def build():
    out = ['record\tline\ttoken\tkolosova_notation\tkolosova_value\tgrade\tkind\tbourdeau_prior\tcontext']
    for rec, ln, g, prior, kind in ITEMS:
        v, gr = k7val(g)
        out.append('\t'.join([rec, ln, g, tok(g), v, gr, kind, prior, ctx.get(ln) or R9646_CTX[ln]]))
    for ln in sorted(cip):
        for g in cip[ln]:
            if g in CONFLICT:
                a, b = CONFLICT[g]
                adm = ADMITS.get(ln) if g == 'top' else ADMITS.get(f'{g} {ln}') or ADMITS.get(g)
                out.append('\t'.join(['R9634', ln, g, tok(g), b, 'M', 'conflict: context admits ' + adm, a, ctx[ln]]))
    out.append('\t'.join(['R9646', 'run5', 'top', 'top', 'razón (por = tog)', 'M', 'conflict: context admits por', 'por',
                          R9646_CTX['run5']]))
    out.append('\t'.join(['R9646', 'run4', 'ʃop', 'sop', 'tiempo = sop', 'M',
                          'conflict: context admits bi (a-bi-a)', 'bi', R9646_CTX['run4']]))
    return '\n'.join(out) + '\n'

text = build(); fn = os.path.join(HERE, '..', 'reading_kolosova_gain.tsv')
if '--check' in sys.argv:
    sys.exit(0 if io.open(fn, encoding='utf-8').read() == text else 1)
io.open(fn, 'w', encoding='utf-8').write(text)
print(text)
