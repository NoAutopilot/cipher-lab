#!/usr/bin/env python3
"""Extract numeral-group runs with bracketed period decipherments from the MHS
Bowdoin and Temple Papers pt. II (Colls MHS 7th ser. vol. 6, 1907; IA collectionsofmas00mass_17 djvu.txt).
Usage: extract_bt.py DJVU_TXT > bt_pairs.tsv   (line, groups, gloss)"""
import re, sys
txt = open(sys.argv[1], encoding='utf-8', errors='replace').read()
lines = txt.split('\n')
# join text with line index map
flat = []; idx = []
for i, l in enumerate(lines):
    for ch in l + ' ':
        flat.append(ch); idx.append(i + 1)
s = ''.join(flat)
pat = re.compile(r'((?:\b\d{1,4}\s*[.,]?\s*){1,12})\[([^\]]{1,80})\]')
print('line\tgroups\tgloss')
for m in pat.finditer(s):
    groups = re.findall(r'\d{1,4}', m.group(1))
    gloss = re.sub(r'\s+', ' ', m.group(2)).strip()
    print(f"{idx[m.start()]}\t{' '.join(groups)}\t{gloss}")
