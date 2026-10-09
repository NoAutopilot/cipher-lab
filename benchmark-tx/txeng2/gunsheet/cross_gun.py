#!/usr/bin/env python3
"""TXE2-GUNSHEET (PREREG-txeng2-9 GS1): cross the gunther8246-p2 p.1 calibration sheet against the whole-letter
Japikse alignment through the 5109-rebuilt key, exemplar by exemplar. Reads p.1 rows of align_letter.tsv ONLY
(never a p2 row, never a pass). Writes cross.tsv beside this script; corrects nothing.
Verdicts: OK (label's key value = the print's aligned letter), MISLABELLED (keyed, value differs), no-alignment
(aligner gave no single-letter chunk), OK (u/v notation) (the key folds v->u, the print text does
not; counted with OK after one-convention normalisation, listed separately), off-key (label not a C row of key.tsv)."""
import csv, os, sys
R = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(R, '..', '..', '..'))
P = os.path.join(ROOT, 'benchmark-tx/txpool/gunther8246-p2')
F = os.path.join(ROOT, 'ciphers/gunther-van-schwarzburg-1561')


def rd(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def key():  # same normalisation as benchmark-tx/build_gunther8246p2.py key()
    k = {}
    for r in rd(os.path.join(F, 'key.tsv')):
        if r['grade'] == 'C':
            k[r['sign']] = 'q' if r['value'] == 'König' else r['value'].lower().replace('v', 'u').replace('w', 'u')
    return k


ct = rd(os.path.join(F, 'ciphertext.tsv'))
al = rd(os.path.join(P, 'align_letter.tsv'))
assert len(ct) == len(al)
p1 = {}
for c, a in zip(ct, al):
    if c['line'].startswith('p1'):          # p.1 rows only; p2 rows are never kept
        p1.setdefault(c['line'], []).append((c['sign'], a['plain_chunk']))
kv = key()
cal = rd(os.path.join(P, 'sheet/calibration.tsv'))
rows, n = [], {}
for i, r in enumerate(cal):
    line = 'p1L%02d' % (i + 2)               # crop p1cal_L01 = committed line p1L02 (RESULTS.md: p1L02-L11)
    labels = r['labels'].split()
    pos = p1[line]
    assert [s for s, _ in pos] == labels, (r['crop'], line)
    for j, (lab, ch) in enumerate(zip(labels, [c for _, c in pos]), 1):
        v = kv.get(lab, '')
        if not v:
            verd = 'off-key'
        elif ch == v:
            verd = 'OK'
        elif ch.replace('v', 'u') == v:      # key.tsv folds v->u, the print text does not (CLAUDE.md rule 3, PX-BRODEC)
            verd = 'OK (u/v notation)'
        elif len(ch) != 1:
            verd = 'no-alignment'
        else:
            verd = 'MISLABELLED'
        n[verd] = n.get(verd, 0) + 1
        rows.append((r['crop'], j, line, lab, v or '-', ch or '-', verd))
with open(os.path.join(R, 'cross.tsv'), 'w', encoding='utf-8') as f:
    f.write('crop\ttile\tline\tlabel\tkey_value\tprint_letter\tverdict\n')
    f.writelines('\t'.join(map(str, x)) + '\n' for x in rows)
print(len(rows), n)
for x in rows:
    if x[-1] != 'OK':
        print('\t'.join(map(str, x)))
