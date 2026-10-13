#!/usr/bin/env python3
"""THUR-51 step 2: in the Birch vol 7 djvu text (collectionofstat07thur, sources/ia-fulltext/thurloe-gz), list every
Bamfylde letter (heading line naming Bamfylde/Bampfylde/Beauple to the next heading-like line or 120 lines), the
numeral groups in it, whether codes 45 or 87 occur, and the lines just above a numeral line that look like a printed
gloss (mostly single letters or short words spaced out). Script reads, a model judges.
python3 scan_v7_4587.py v7.txt -> TSV on stdout"""
import re, sys
L = open(sys.argv[1], encoding='utf-8', errors='replace').read().splitlines()
HEAD = re.compile(r'(bam[p]?f[iy]l?[ed]|beauple)', re.I)
NEXT = re.compile(r'^\W{0,3}(A\s+)?(letter|paper|col[.,]|colonel|mr\.|major|general|the\s+same|to\s|from\s)', re.I)
def glossy(s):
    t = s.split()
    return len(t) >= 2 and sum(len(w) <= 2 for w in t) / len(t) >= 0.5 and not re.search(r'\d', s)
print('head_line\theading\tline\tcodes\thas45\thas87\tgloss_above')
for i, l in enumerate(L):
    s = l.strip()
    if not (len(s) < 90 and HEAD.search(s) and re.search(r'(to|from|letter)', s, re.I)):
        continue
    end = min(len(L), i + 160)
    for j in range(i + 3, end):
        if len(L[j].strip()) < 90 and NEXT.match(L[j].strip()) and re.search(r'(letter|to\s+\w)', L[j], re.I):
            end = j; break
    for j in range(i, end):
        codes = re.findall(r'(?<![\d.,])\d{1,3}(?!\d)', L[j])
        groups = re.findall(r'\d{1,3}\s*[.,]\s*\d{1,3}', L[j])
        if not groups and not any(len(c) == 3 and c not in ('100',) for c in codes):
            continue
        above = ''
        for k in range(j - 1, max(i, j - 3), -1):
            if L[k].strip():
                above = L[k].strip() if glossy(L[k]) else ''
                break
        print(f'{i+1}\t{s[:50]}\t{j+1}\t{" ".join(codes)}\t{int("45" in codes)}\t{int("87" in codes)}\t{above[:80]}')
