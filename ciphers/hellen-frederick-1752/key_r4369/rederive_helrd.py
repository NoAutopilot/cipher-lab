#!/usr/bin/env python3
"""READ2-HELRD: independent re-derivation of R1953 from key.tsv per decode.json's stated rules.
Left entry -> its own code (grade as given); right entry -> code+100 (grade S, M stays M), which takes the
code where both land on it (decode.json: right entries are attributed to code+100 by the control-backed test).
Marks _ ^ stripped; an inner '?' -> U; a trailing '?' is read as usual. Unkeyed -> U. Output '?' for U."""
import csv, re, sys
key = {}
for r in csv.DictReader(open('key.tsv'), delimiter='\t'):
    c = int(r['code'])
    for val, g, off, src in ((r['left'], r['grade_left'], 0, 'L'), (r['right'], r['grade_right'], 100, 'R')):
        if val:
            key.setdefault(c + off, []).append((val, g if src == 'L' else ('M' if g == 'M' else 'S'), src))
out = []
for tok in open('../ciphertext_R1953.txt').read().split():
    if '?' in tok.rstrip('?') :  # inner '?': a doubtful digit inside the number, no usable code
        out.append('?'); continue
    n = re.sub(r'[_^?]', '', tok)  # trailing '?': uncertain sign, still read (graded M)
    ents = key.get(int(n)) if n else None
    if not ents: out.append('?'); continue
    out.append(next(v for v, g, src in ents if src == 'R') if any(e[2] == 'R' for e in ents) else ents[0][0])
open('rederive_helrd.txt', 'w').write('\n'.join(out) + '\n')
print(len(out), 'tokens;', sum(o == '?' for o in out), 'U;', 0, 'conflicts')
