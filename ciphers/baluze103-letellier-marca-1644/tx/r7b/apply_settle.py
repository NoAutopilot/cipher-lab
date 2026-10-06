#!/usr/bin/env python3
"""R7B-BAL103R, 6 Oct 2026: apply the crop settlements to the two-pass drafts and write ciphertext.tsv.

  python3 tx/r7b/apply_settle.py            (rewrites ciphertext.tsv from tx/r7b/rec_[rv]/ciphertext_draft.tsv
                                             + tx/r7b/settle_{r1,r2,v}.tsv; the pass files are untouched)
Settled sign: confidence H if the settler read it H, else M; '?' -> L; '-' drops the column; 'a+b' becomes two signs.
Positions are renumbered per line; 'alt' keeps the draft's column and both pass readings (never a silent repair).
"""
import csv, os
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(D))
settle = {}
for n in ('settle_r1.tsv', 'settle_r2.tsv', 'settle_v.tsv'):
    for r in csv.DictReader(open(os.path.join(D, n)), delimiter='\t'):
        settle[(r['line'].strip(), r['position'].strip())] = r
rows, used = [], set()
for page in ('rec_r', 'rec_v'):
    for r in csv.DictReader(open(os.path.join(D, page, 'ciphertext_draft.tsv')), delimiter='\t'):
        k = (r['line'], r['position'])
        if r['why'] == 'agree' or k not in settle:
            rows.append((r['line'], r['sign'], r['confidence'], r['alt'], r['why'])); continue
        s = settle[k]; used.add(k)
        orig = f"col{r['position']} draft={r['sign']} {r['alt']}".strip()
        sign, conf = s['sign'].strip(), s['conf'].strip().upper()
        why = 'settled-' + ('H' if conf == 'H' else 'M')
        if sign == '-': continue
        for part in sign.split('+'):
            c = 'L' if part == '?' else ('H' if conf == 'H' else 'M')
            rows.append((r['line'], part, c, orig, why))
missing = [k for k in settle if k not in used]
assert not missing, f'settlement rows matching no draft column: {missing[:5]}'
with open(os.path.join(T, 'ciphertext.tsv'), 'w') as f:
    f.write('line\tposition\tsign\tconfidence\talt\twhy\n'); pos, cur = 0, None
    for line, sign, conf, alt, why in rows:
        pos = pos + 1 if line == cur else 1; cur = line
        f.write(f'{line}\t{pos}\t{sign}\t{conf}\t{alt}\t{why}\n')
print('ciphertext.tsv', len(rows), 'signs;', len(used), 'settled columns')
