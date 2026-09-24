#!/usr/bin/env python3
"""List every f.30 sign that the key leaves without a value (grade U) and occurs at least twice, with each
occurrence in its decoded context (8 signs either side; the sign itself shown as its code in braces).
Also lists key-valued signs flagged in NOTES.md whose contexts are worth a second look (Tb, eh, H, q).
  python3 contexts_f30.py   writes unkeyed_f30.tsv from reading_f30_tokens.tsv. Values are not proposed."""
import os, collections
H = os.path.dirname(os.path.abspath(__file__))
T = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'reading_f30_tokens.tsv'), encoding='utf-8')][1:]
def show(t, focus): return '{' + t[3] + '}' if focus else ('' if t[5] == 'NULL' else '·' if t[5] == '?' else t[5] if len(t[5]) == 1 else '[' + t[5] + ']')
cnt = collections.Counter(t[3] for t in T if t[6] == 'U')
flag = ('Tb', 'eh', 'H', 'q')
out = ['sign\tgrade\tcount\tline\tposition\tcontext']
for code in [c for c, n in cnt.most_common() if n >= 2] + list(flag):
    for i, t in enumerate(T):
        if t[3] != code: continue
        ctx = ''.join(show(T[j], j == i) for j in range(max(0, i - 8), min(len(T), i + 9)))
        out.append(f'{code}\t{t[6]}\t{cnt[code] if code in cnt else sum(1 for x in T if x[3] == code)}\t{t[0]}_{t[1]}\t{t[2]}\t{ctx}')
open(os.path.join(H, 'unkeyed_f30.tsv'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(', '.join(f'{c} {n}' for c, n in cnt.most_common()))
