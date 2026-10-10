#!/usr/bin/env python3
"""MS18-R8: date + addressee window search in OR djvu texts (same shape as ms18_r6_date.py). Usage: ms18_r8_date.py FILE... A miss is a search result (rule 10)."""
import re, sys, os
Q = [('X1 10003/2 7 May 1865 Stanton/Wilson/Brown', r'May\s+[78]\W{1,4}\s*1865', ['Wilson|Macon|Stanton'], ['Brown|Augur']),
     ('X2 10048/1 2 Sept 1865 Eckert/Slocum/Sharkey', r'Sept(ember|\.)?\s+[23]\W{1,4}\s*1865', ['Slocum|Sharkey|Vicksburg'], ['Sharkey|militia']),
     ('X3 9885/1 2 Oct 1864 Dix/Horner/election proxies', r'Oct(ober|\.)?\s+[23]\W{1,4}\s*1864', ['Dix|New York|Stanton|Horner'], ['proxies|affidavit|Inspectors|fraudulent']),
     ('X4 9887/0 3 Nov 1864 Dix/Butler troops New York', r'Nov(ember|\.)?\s+[34]\W{1,4}\s*1864', ['Dix|Butler|New York'], ['Butler']),
     ('X5 9841/0 13 Sept 1864 O\'Brien/Knox Ames', r'Sept(ember|\.)?\s+1[34]\W{1,4}\s*1864', ['Knox|Ames|O.Brien|Butler'], ['Ames|promise to pay|tested']),
     ('X6 10055/0 23 Sept 1865 Alberger/Baker/Lynchburg', r'Sept(ember|\.)?\s+2[34]\W{1,4}\s*1865', ['Alberger|Lynchburg|Sampson|Baker'], ['Alberger|Lynchburg']),
     ('X7 9694/1 4 Apr 1864 Grant/Sherman', r'April\s+[45]\W{1,4}\s*1864', ['Sherman|Grant|Washington'], ['consolidated|Hooker|Granger']),
     ('X8 9903/1 2 Dec 1864 Horner/Dyer sacks', r'Dec(ember|\.)?\s+[23]\W{1,4}\s*1864', ['Dyer|Monroe|Horner|New York'], ['sacks|gunny|bags']),
     ('X9 9880/2 31 Oct 1864 Halleck/Rosecrans', r'Oct(ober|\.)?\s+31\W{1,4}\s*1864', ['Rosecrans|Halleck|Curtis'], ['McNeil|Price|Arkansas']),
     ('X10 9772/0 3-4 July 1864 Garrett/Gilmore/Wallace', r'July\s+[34]\W{1,4}\s*1864', ['Garrett|Gilmore|Wallace|Sigel|Chambersburg'], ['Sigel|Garrett|Hunter|valley'])]
for f in sys.argv[1:]:
    t = open(f, errors='ignore').read(); t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in Q:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[m.start()-150: m.end()+450]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:300])
        if n: print(f'{os.path.basename(f)} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('    ', e)
