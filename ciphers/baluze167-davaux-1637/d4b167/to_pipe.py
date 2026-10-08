#!/usr/bin/env python3
"""D4-B167: passes/reconciled_b170f229{r,v}.tsv (shape=letter tokens) -> ciphertext_b170f229.txt (pipe format for tools/decode_key.py).
s:<shape>=<letter>[?] -> L:<letter>[?] when the letter is a key letter, else the sign is kept unread as s:<shape>[?]; {clear} -> w:word.
Usage: python3 d4b167/to_pipe.py   (run from the target folder)"""
import re
LET = set('abcdefghilmnopqrstuxyz')
out = ['# Baluze 170 ff.229r-v (letter of 25 Aug 1640, Amiens, bare cipher passage), reconciled by D4-B167 (8 Oct 2026) from two blind',
       '# Sonnet passes (split 0.233 / 0.255, above the 0.10 gate) and the native crops; see passes/reconciled_b170f229*.tsv for shapes.',
       '# Letter signs: L:x = letter settled from context in this letter (all graded M by their ?).']
for f in ('passes/reconciled_b170f229r.tsv', 'passes/reconciled_b170f229v.tsv'):
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        lid, toks = ln.rstrip('\n').split('\t')
        page, line = lid.split('_')
        res = []
        for t in re.findall(r'\{[^}]*\}|\S+', toks):
            if t.startswith('{'):
                res += ['w:' + w for w in t[1:-1].split()]
                continue
            q = '?' if t.endswith('?') else ''
            t = t.rstrip('?')
            if t.startswith('s:'):
                shape, _, let = t[2:].partition('=')
                res.append(('L:' + let if let in LET else 's:' + shape) + q)
            else:
                res.append(t + q)
        out.append(f'{page} {line} | ' + ' '.join(res))
open('ciphertext_b170f229.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'lines')
