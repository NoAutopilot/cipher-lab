#!/usr/bin/env python3
"""SYL-NOM (13 Oct 2026): do fr.15576 f.2's codes fall inside the no.54 nomenclator's code range and format?

Counts and lists only; no reading, no decode. Reads f2_fr15576/ciphertext_body.tsv (D4-15576 reconciled body,
C01-C21) and key_no54_nomenclator.tsv + key_no54.tsv (syllabary). Prints a format census of both sides and the
overlap of plain numeric values. Exit 0 always (a census, not a gate).
  python3 ciphers/fr15575-syllabic-1592-95/nomen_range_check.py
"""
import csv, os, re, collections
H = os.path.dirname(os.path.abspath(__file__))

def fmt(code):
    c = re.sub(r'[^0-9A-Za-z]', '', code)
    if not c: return 'symbol'
    if c.isdigit(): return f'{len(c)}-digit'
    if c.isalpha(): return 'letters'
    return 'mixed'

f2 = []
for r in csv.DictReader(open(os.path.join(H, 'f2_fr15576/ciphertext_body.tsv')), delimiter='\t'):
    f2 += r['tokens'].split()
f2c = collections.Counter(fmt(t) for t in f2)
f2num = collections.Counter(re.sub(r'\D', '', t) for t in f2 if re.sub(r'\D', '', t))
print(f'fr.15576 f.2 body: {len(f2)} tokens; formats {dict(f2c)}')
n3 = sorted(int(v) for v in f2num if len(v) == 3)
print(f'  3-digit distinct values {len(n3)}, range {n3[0]}-{n3[-1]}')
print('  non-numeric tokens:', dict(collections.Counter(t for t in f2 if not re.sub(r"\D", "", t))))

nom = list(csv.DictReader((l for l in open(os.path.join(H, 'key_no54_nomenclator.tsv')) if not l.startswith('#')), delimiter='\t'))
codes = []
for r in nom:
    for alt in re.split(r'\s+(?:ou|et)\s+', r['code']):
        if '?' not in alt: codes.append((alt, r['entry'], r['conf']))
nc = collections.Counter(fmt(c) for c, _, _ in codes)
print(f'no.54 nomenclator: {len(nom)} entries, {len(codes)} codes; formats {dict(nc)}')
nnum = {re.sub(r'\D', '', c): (e, g) for c, e, g in codes if fmt(c).endswith('digit')}
for k in sorted(nnum, key=lambda x: (len(x), x)):
    print(f'  numeric code {k}: {nnum[k][0]} ({nnum[k][1]})')
syl = {r['code'] for r in csv.DictReader((l for l in open(os.path.join(H, 'key_no54.tsv')) if not l.startswith('#')), delimiter='\t')}
shared3 = sorted(v for v in nnum if len(v) == 3 and v in f2num)
print(f'3-digit nomenclator codes also on f.2: {len(shared3)} {[(v, nnum[v][0], f2num[v]) for v in shared3]}')
print(f'f.2 3-digit values outside every no.54 code (syllabary + nomenclator): {sum(1 for v in n3 if str(v) not in nnum and str(v) not in syl)} of {len(n3)}')
print('f.2 values 700-709:', {v: f2num[v] for v in sorted(f2num) if v.startswith('70') and len(v) == 3}, '; sheet codes with 70x digits:', [(c, e) for c, e, g in codes if re.sub(r'\D', '', c).startswith('70')])
lettersf2 = {t for t in f2 if fmt(t) == 'letters'}
nomlet = {re.sub(r'[^A-Za-z]', '', c).lower() for c, _, _ in codes if fmt(c) == 'letters'}
print(f'f.2 letter tokens that equal a nomenclator letter code: {sorted(lettersf2 & nomlet)}')
