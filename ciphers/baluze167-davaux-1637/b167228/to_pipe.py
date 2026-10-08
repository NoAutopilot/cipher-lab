#!/usr/bin/env python3
"""B167-228: passes/reconciled_b170f228{r,v}.tsv (bare shape classes) -> ciphertext_b170f228.txt (pipe format, tools/decode_key.py).
Letter values are the f.229 ones (same letter, 25 Aug 1640): the majority letter per shape in passes/reconciled_b170f229{r,v}.tsv,
computed here, never set from f.228's own context. Shapes with no f.229 attestation stay unread as s:<shape> (U). Every letter sign
carries '?' (M), as on f.229. Numerals as seen; {clear} -> w:word. Prints the shape map used.
Usage: python3 b167228/to_pipe.py   (run from the target folder)"""
import re, collections
LET = set('abcdefghilmnopqrstuxyz')
TOK = re.compile(r'\{[^}]*\}|\S+')
votes = collections.defaultdict(collections.Counter)
for f in ('passes/reconciled_b170f229r.tsv', 'passes/reconciled_b170f229v.tsv'):
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        for t in TOK.findall(ln.split('\t', 1)[1]):
            t = t.rstrip('?')
            if t.startswith('s:') and '=' in t:
                shape, _, let = t[2:].partition('=')
                if let in LET:
                    votes[shape][let] += 1
SHAPE = {s: c.most_common(1)[0][0] for s, c in votes.items()}
for s, c in sorted(votes.items()):
    print('f229 shape', s, dict(c), '->', SHAPE[s])
out = ['# Baluze 170 f.228r-v (same letter as f.229, 25 Aug 1640, Amiens, bare cipher passage), reconciled by D1-BAL170/D1-BAL170B',
       '# (passes/reconciled_b170f228{r,v}.tsv). B167-228, 8 Oct 2026: letter shapes given the f.229 values (majority per shape,',
       '# b167228/to_pipe.py); L:x? = letter sign, M; s:<shape> = shape with no f.229 value (unread). Numerals as seen.']
unread = collections.Counter()
for f in ('passes/reconciled_b170f228r.tsv', 'passes/reconciled_b170f228v.tsv'):
    for ln in open(f, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t') or not ln.strip():
            continue
        lid, toks = ln.rstrip('\n').split('\t')
        page, line = lid.split('_', 1)
        res = []
        for t in TOK.findall(toks):
            if t.startswith('{'):
                res += ['w:' + w for w in t[1:-1].split()]
                continue
            q = '?' if t.endswith('?') else ''
            t = t.rstrip('?')
            if t.startswith('s:'):
                shape = t[2:]
                if shape in SHAPE:
                    res.append('L:' + SHAPE[shape] + '?')
                else:
                    unread[shape] += 1
                    res.append('s:' + re.sub(r'[^A-Za-z0-9+|_]', '', shape) + '?')
            else:
                res.append(t + q)
        out.append(f'{page} {line} | ' + ' '.join(res))
open('ciphertext_b170f228.txt', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 3, 'lines; unread shapes', dict(unread))
