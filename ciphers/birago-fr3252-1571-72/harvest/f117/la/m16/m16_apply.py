#!/usr/bin/env python3
"""D2-B117M step 1 rule (m16/PREREG-M16.md): S iff the window read is firm (H/M), equals top-1, and no firm earlier third read
disagrees. Appends exception rows (values unchanged, grade S) to kapc/exceptions_kapc_f117.tsv. Run from harvest/f117/la."""
import csv
T = {(r['passage'], r['pos']): r for r in csv.DictReader(open('m16/m16_in_tiles.tsv'), delimiter='\t')}
K = {(r['line'], r['pos']): r for r in csv.DictReader(open('kapc/m_to_s.tsv'), delimiter='\t')}
V = {(r['line'], r['pos']): r for r in csv.DictReader(open('kapc/reading_f117_kapc_tokens.tsv'), delimiter='\t')}
ex = open('kapc/exceptions_kapc_f117.tsv').read()
rows, log = [], []
for r in csv.DictReader(open('m16/m16_reread.tsv'), delimiter='\t'):
    k = (r['passage'], r['pos']); t = T[k]; m = K[k]
    firm3 = m['note_3r'] in ('lookalike 2-of-3', 'lookalike confirms') and m['sign_3r'] != t['passC']
    s = r['conf'] in ('H', 'M') and r['label'] == t['passC'] and not firm3
    log.append((*k, t['passC'], m['sign_3r'], m['note_3r'], r['label'], r['conf'], 'S' if s else 'M'))
    if s:
        tok = V[('f117_' + k[0], k[1])] if ('f117_' + k[0], k[1]) in V else V[k]
        rows.append(f"f117\t{k[0]}\t{k[1]}\t{tok['value']}\tS\tD2-B117M S: top-1 {t['passC']} and m16 value-blind window read ({r['conf']}) agree\n")
with open('m16/m16_grades.tsv', 'w') as f:
    f.write('line\tpos\ttop1\tsign_3r\tnote_3r\tm16_label\tm16_conf\tnew_grade\n')
    for l in log: f.write('\t'.join(l) + '\n')
if 'D2-B117M' not in ex:
    open('kapc/exceptions_kapc_f117.tsv', 'a').writelines(rows)
print('S', len(rows), 'of', len(log))
