#!/usr/bin/env python3
"""Campaign step H19 (28 Sept 2026): known-answer test of the printed modifier rule on Armstrong's own office letter.

Monroe Papers reel 9 frame 956 (a printed 1,700-entry cipher form; NOTES.md step H14) prints: "^ under the last figure
doubles the last letter of those represented by that n°" and "ʃ under a figure withdraws the letter corresponding".
Armstrong's 15 Feb 1808 THE=972 office letter (NARA M34-014 frames 0024/0025, step H4) carries a small mark under the
last digit of a few groups.  Known plaintext: Bourdeau's decode (tools/data/uscodes-1800/decodes/armstrong_1808-02-15.txt)
and his THE=972 table.  This script aligns the letter's numeric sequence (tools/data/uscodes-1800/stats.py
THE972_USAGE['1808-02-15'], 243 tokens) to the decode tokens (difflib on table words) and prints, for every marked
group and for the unmarked occurrences of the same values, the table reading in context -- so the reader can see
whether "double the last letter" is what the word needs.  Writes h19_known_answer.tsv.  No decoding beyond Bourdeau's.
"""
import csv, difflib, importlib.util, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[2]; U = ROOT/'tools/data/uscodes-1800'
spec = importlib.util.spec_from_file_location('u', U/'stats.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
toks = m.THE972_USAGE['1808-02-15'].split()
rows = list(csv.reader(open(U/'THE972_bourdeau.tsv'), delimiter='\t'))
tab = {r[0]: r[1] for r in rows[1:] if len(r) > 1}
words = [tab.get(t, '{'+t+'}') for t in toks]
body = open(U/'decodes/armstrong_1808-02-15.txt').read().split('\n', 1)[1]
dt = [t.strip() for t in re.split(r'\s\.\s', body) if t.strip()]
sm = difflib.SequenceMatcher(None, [w.lower() for w in words], [d.lower() for d in dt], autojunk=False)
amap = {}
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        for k in range(i2-i1): amap[i1+k] = j1+k
# marked groups: position in the sequence, read from frame 0024 by this runner (H4, H19 zooms)
MARKED = {55: '817', 89: '741', 121: '741', 158: '662', 164: '624', 199: '1165'}
out = []
def rec(i, kind):
    assert toks[i] == MARKED.get(i, toks[i])
    ctx = ' '.join(f'{toks[k]}={words[k]}' for k in range(max(0, i-3), min(len(toks), i+4)))
    j = amap.get(i); dec = ' '.join(dt[max(0, j-3):j+4]) if j is not None else '(not aligned)'
    out.append((kind, i, toks[i], words[i], ctx, dec))
for i in sorted(MARKED): rec(i, 'marked')
for i, t in enumerate(toks):
    if t in MARKED.values() and i not in MARKED: rec(i, 'unmarked-control')
with open(HERE/'h19_known_answer.tsv', 'w') as f:
    f.write('kind\tpos\tgroup\ttable\ttable_context\tdecode_context\n')
    for r in out: f.write('\t'.join(map(str, r))+'\n')
for r in out: print(' | '.join(map(str, r)))
