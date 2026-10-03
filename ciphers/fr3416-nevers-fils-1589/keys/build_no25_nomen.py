#!/usr/bin/env python3
"""build_no25_nomen.py -- reconcile two blind passes of the key no.25 nomenclator (BnF fr.3995 canvas f104, Gallica
btv1b525085665) into keys/key_no25_nomenclator.tsv. FILS-NOMEN (account 1), 3 Oct 2026.

Inputs: keys/no25_passes/passA.tsv, passB.tsv (two blind Opus passes over images/no25/c*_L*.jpg, crops only, no key);
keys/no25_passes/settle.tsv (file, row, meaning, code, note: the reconciler's decision for a split, read on the crops).
Rule (NOTES.md "FILS-NOMEN pre-registration" 2): H when A and B agree on code and meaning after normalisation
(case, u/v, i/j, accents, punctuation, superscript marks); M otherwise (settled from settle.tsv, else both readings).
Rows a pass gave as header lines are dropped. Symbol codes are compared by the settled label in settle.tsv.
Usage: python3 keys/build_no25_nomen.py [--check]   (--check: exit 1 if the committed TSV is stale; rule 7)
"""
import csv, re, sys, os, unicodedata
H = os.path.dirname(os.path.abspath(__file__))
def load(p):
    R = {}
    for r in csv.DictReader(open(os.path.join(H, p)), delimiter='\t'):
        if r['row_in_file'] == 'header' or r['meaning'].startswith('HEADER'): continue
        R.setdefault(r['file'], []).append(r)
    return R
def nm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if unicodedata.category(c) != 'Mn').replace('ſ', 's').replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z0-9]', '', s)
A, B = load('no25_passes/passA.tsv'), load('no25_passes/passB.tsv')
S = {}
for r in csv.DictReader(open(os.path.join(H, 'no25_passes/settle.tsv')), delimiter='\t'):
    S[(r['file'], r['row'])] = r
COLS = {'c1': 'Noms gnaulx', 'c2': 'Noms gnaulx / Villes', 'c3': 'Villes / Prouinces', 'c4': 'Noms Propres',
        'c5': 'Noms Propres (cont.)', 'c6': 'Motz', 'c7': 'Motz (cont.) / Dames'}
out = ['# key no.25 nomenclator, BnF fr.3995 canvas f104 (Gallica btv1b525085665, label 51r), table rotated 90 deg on the leaf.',
       '# Built by keys/build_no25_nomen.py (FILS-NOMEN, 3 Oct 2026) from two blind passes; grade H = A=B, M = split settled on the crop.',
       '# Arabic codes carry an overbar on the sheet (both passes); Roman, letter and symbol codes do not.',
       'code\tmeaning\tgrade\tsection\tsource\tnote']
for f in sorted(set(A) | set(B)):
    a, b = A.get(f, []), B.get(f, [])
    if len(a) != len(b): sys.exit('row count differs in %s: %d vs %d' % (f, len(a), len(b)))
    for i, (x, y) in enumerate(zip(a, b), 1):
        key = (f, str(i))
        same = nm(x['meaning']) == nm(y['meaning']) and nm(x['code']) == nm(y['code'])
        if key in S:
            s = S[key]; code, mean = s['code'], s['meaning']
            g = 'H' if (s.get('grade') == 'H') else 'M'
            note = s['note']
        elif same:
            code, mean, g, note = y['code'], y['meaning'], 'H', ''
        else:
            code, mean, g = x['code'], x['meaning'], 'M'
            note = 'unsettled: A %s=%s, B %s=%s' % (x['code'], x['meaning'], y['code'], y['meaning'])
        out.append('\t'.join([code, mean, g, COLS[f[:2]], '%s r%d' % (f, i), note]))
txt = '\n'.join(out) + '\n'
P = os.path.join(H, 'key_no25_nomenclator.tsv')
# f.35r code words read through the nomenclator (pre-registration rule 3: H only if the nomenclator entry is H AND the
# code is H on f.35r; the f.35r grade is read from f35r_ciphertext.tsv). Candidate code forms are the reconciler's.
NOM = {l.split('\t')[0]: l.split('\t') for l in out[4:]}
CT = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, '../f35r_ciphertext.tsv')) if not l.startswith(('#', 'line'))]
CW = [('L02', 'ciiij', 'xiiij', 'first glyph is the letter-hand x with a long lead-in tail (the "c" of NV02-READ); no c-codes exist in the table'),
      ('L10', '28', '28', 'WITHDRAWN (A1B-FILS-L10, 3 Oct 2026): two blind reads put the only free stroke with line 11 (abbreviation bar over its Z-like letter), not over figures 2 8; no code word in L10')]
WITHDRAWN = {('L10', '28')}
cw = ['# f.35r code words through key no.25 nomenclator (keys/build_no25_nomen.py, FILS-NOMEN 3 Oct 2026); grade per NOTES.md pre-reg rule 3',
      'line\ttoken_f35r\tf35r_grade\tcode_read_as\tmeaning\tnomen_grade\tgrade\tnote']
for ln, tok, code, note in CW:
    g35 = [r[3] for r in CT if r[0] == ln and r[2] == tok][0]
    e = NOM.get(code); mean, gn = (e[1], e[2]) if e else ('?', '-')
    cw.append('\t'.join([ln, tok, g35, code, mean, gn, 'withdrawn' if (ln, tok) in WITHDRAWN else ('H' if (g35 == 'H' and gn == 'H') else 'M'), note]))
cwtxt = '\n'.join(cw) + '\n'
CP = os.path.join(H, '../f35r_codewords.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(P) and open(P).read() == txt and os.path.exists(CP) and open(CP).read() == cwtxt
    print('check:', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(P, 'w').write(txt); open(CP, 'w').write(cwtxt)
g = [l.split('\t')[2] for l in out[4:]]
print('rows %d  H %d  M %d' % (len(g), g.count('H'), g.count('M')))
