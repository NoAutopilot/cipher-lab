#!/usr/bin/env python3
"""MS18-R6: date + addressee window search in OR djvu texts. For each (label, date-regex, terms) prints the number of 'Month D, YYYY' dated telegram headings in each volume and
those whose next 400 characters hold all the terms. Usage: ms18_r6_date.py FILE... ; queries are defined below. A miss is a search result (rule 10)."""
import re, sys, os
Q = [('X6 10005/2 8 May 1865 Richmond/Caldwell/Boulware', r'May\s+8\W{1,4}\s*1865', ['Halleck|Caldwell|Richmond'], ['Boulware|Bouldware|arrest']),
     ('X9 10020/2 24 May 1865 Macon/Lines', r'May\s+2[34]\W{1,4}\s*1865', ['Macon|Wilson|Nashville'], ['Campbell|Paxton|bell|deliver']),
     ('X10 9836/1 7 Sept 1864 Horner/Masury/Whiton', r'Sept(ember|\.)?\s+[78]\W{1,4}\s*1864', ['New York|Horner|Whiton|Masury'], ['rail|Whiton|Masury'])]
for f in sys.argv[1:]:
    t = open(f, errors='ignore').read(); t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in Q:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[m.start()-150: m.end()+450]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:300])
        print(f'{os.path.basename(f)} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('    ', e)
