#!/usr/bin/env python3
"""R12D-HDKV independent re-derivation (verifier, 6 Oct 2026): written without reading decode_key.py's token loop.
Usage: python3 -I keys/r12d_rederive.py ciphers/hessen-daenemark-1672 ; exit 1 on any diff from reading_tokens.tsv.
Rule used: value = exceptions.tsv value if (line,pos) listed, else key.tsv / key_gloss.tsv value; unkeyed -> '?', U.
Grade = exception grade if listed; else key grade, lowered to M when the sign's transcription conf is M (H/C/S -> M; I stays I);
'?' in value -> M (unless U)."""
import csv, sys
T = sys.argv[1]
def rows(f):
    with open(f"{T}/{f}") as fh:
        return list(csv.DictReader(fh, delimiter='\t'))
key = {}
for f in ('key.tsv', 'key_gloss.tsv'):
    for r in rows(f):
        if r['code'] in key: print('DUP', r['code'], f)
        key[r['code']] = (r['value'], r['grade'])
ex = {(r['line'], r['pos']): (r['value'], r['grade']) for r in rows('exceptions.tsv')}
out = []
for r in rows('ciphertext.tsv'):
    k = (r['line'], r['pos'])
    if k in ex:
        v, g = ex[k]
    elif r['sign'] in key:
        v, g = key[r['sign']]
        if r['conf'] == 'M' and g in 'HCS': g = 'M'
        if '?' in v and g in 'HCS': g = 'M'
    else:
        v, g = '?', 'U'
    out.append((r['line'], r['pos'], r['sign'], r['conf'], v, g))
mine = {(a, b): (v, g) for a, b, s, c, v, g in out}
theirs = {(r['line'], r['pos']): (r['value'], r['grade']) for r in rows('reading_tokens.tsv')}
from collections import Counter
print('mine', sorted(Counter(g for *_, g in out).items()))
print('committed', sorted(Counter(g for _, g in theirs.values()).items()))
diff = [(k, mine.get(k), theirs.get(k)) for k in sorted(set(mine) | set(theirs)) if mine.get(k) != theirs.get(k)]
for d in diff: print('DIFF', *d)
print('diffs', len(diff), 'value diffs', sum(1 for k, a, b in diff if (a or ('',))[0] != (b or ('',))[0]))
sys.exit(1 if diff else 0)
