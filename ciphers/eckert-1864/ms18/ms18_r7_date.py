#!/usr/bin/env python3
"""MS18-R7: date + addressee window search in OR djvu texts (same shape as ms18_r6_date.py). Usage: ms18_r7_date.py FILE... A miss is a search result (rule 10)."""
import re, sys, os
Q = [('X1 9842/1 15 Sept 1864 Meigs/Allen/Louisville funds', r'Sept(ember|\.)?\s+1[56]\W{1,4}\s*1864', ['Allen|Louisville|Meigs|Quartermaster'], ['funds|Ferry|certificates']),
     ('X3 9878/1 28 Oct 1864 Halleck/Thomas/Rosecrans', r'Oct(ober|\.)?\s+2[78]\W{1,4}\s*1864', ['Thomas|Rosecrans|Halleck'], ['Rosecrans']),
     ('X4 9673/1 6 Feb 1864 Stanton/McCallum', r'Feb(ruary|\.)?\s+[67]\W{1,4}\s*1864', ['McCallum|Nashville|Stanton'], ['Devereux|McCallum']),
     ('X6 10013/0 19 May 1865 Rawlins/Clowry/horses', r'May\s+(19|20)\W{1,4}\s*1865', ['Clowry|Rawlins|St\\. Louis|Saint Louis'], ['horses|cavalry']),
     ('X8 9820/3 16 Aug 1864 Stanton/Dana/Horner', r'Aug(ust|\.)?\s+1[67]\W{1,4}\s*1864', ['Dana|Horner|New York|Stanton'], ['released|trade|detective']),
     ('X9 9759/1 13 June 1864 Stanton/Sherman/Burbridge', r'June\s+1[34]\W{1,4}\s*1864', ['Sherman|Stanton|Washington'], ['Burbridge|Morgan']),
     ('X11 10048/1 2 Sept 1865 Sharkey/Slocum', r'Sept(ember|\.)?\s+[23]\W{1,4}\s*1865', ['Slocum|Sharkey|Vicksburg'], ['Sharkey|militia']),
     ('X12 10003/2 7 May 1865 Brown/Wilson/Macon', r'May\s+[78]\W{1,4}\s*1865', ['Wilson|Macon|Stanton'], ['Brown|Augur'])]
for f in sys.argv[1:]:
    t = open(f, errors='ignore').read(); t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in Q:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[m.start()-150: m.end()+450]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:300])
        if n: print(f'{os.path.basename(f)} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('    ', e)
