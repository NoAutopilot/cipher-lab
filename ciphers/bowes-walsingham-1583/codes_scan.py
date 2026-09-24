#!/usr/bin/env python3
"""Scan the Surtees 1842 OCR (corpus/) for every bare number in body text that may be a name-code.
Writes codes_scan.tsv: number, line, letter heading, context (200 chars). Excludes page headers,
'Letter-Book, p. N' lines, years 1500-1699, signature marks, and numbers followed by money/measure words."""
import re, sys
T = open('corpus/correspondenceof00bowerich_djvu.txt', encoding='utf-8').read().split('\n')
HEAD = re.compile(r'BOWES\s+CORRESPONDENCE|^\s*\d+\s+[A-Z]\s*\d*\s*$|^\s*\d+\s*$')
LET = re.compile(r'^([CLXVI]{2,}[.IL]?)\s*[.—-]')
SKIP_AFTER = re.compile(r'^\s*(l\.|li\.|lib|pounds?|crowns?|marks?|men|horse|foot|days?|years?|miles?|s\.|d\.|th\b|st\b|hundred|thousand|francs|ells|shillings)', re.I)
out = []; letter = '?'; flat = []
for i, l in enumerate(T):
    m = LET.match(l)
    if m: letter = m.group(1)
    if HEAD.search(l) or 'Letter-Book' in l or re.search(r'\bp\.\s*\d', l): continue
    flat.append((i + 1, letter, l))
text = ' '.join(l for _, _, l in flat)
pos = []; c = 0
for n, let, l in flat:
    pos.append((c, n, let)); c += len(l) + 1
import bisect
starts = [p[0] for p in pos]
for m in re.finditer(r'(?<![\w/])(\d{1,4}|1S9|8/0)(?![\w/])', text):
    num = m.group(1).replace('S', '8').replace('/', '7')
    v = int(num)
    if 1500 <= v <= 1699: continue
    after = text[m.end():m.end() + 12]
    if SKIP_AFTER.match(after): continue
    k = bisect.bisect_right(starts, m.start()) - 1
    ctx = re.sub(r'\s+', ' ', text[max(0, m.start() - 100):m.end() + 100])
    out.append((num, m.group(1), pos[k][1], pos[k][2], ctx))
with open('codes_scan.tsv', 'w') as f:
    f.write('code\tprinted\tline\tletter\tcontext\n')
    for r in out: f.write('\t'.join(map(str, r)) + '\n')
print(len(out), 'hits')
