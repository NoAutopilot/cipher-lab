#!/usr/bin/env python3
"""N2R-2: date + addressee window search in OR djvu texts. Usage: ms18_n2g_date.py FILE.txt|FILE.gz... A miss is a search result (rule 10)."""
import re, sys, os, gzip
Q = [('Y2 9874/1 22 Oct 1864 Brice/Forsyth/Sheridan paymasters', r'Oct(ober|\.)?\s+2[123]\W{1,4}\s*1864', ['Forsyth|Sheridan|Brice|Paymaster'], ['Paymaster|pay']),
     ('Y3 9761/1 19 Jun 1864 Sigel/Martinsburg/Beverly', r'June\s+(18|19|20)\W{1,4}\s*1864', ['Sigel|Martinsburg|Beverly'], ['Beverly|Staunton|despatches']),
     ('Y4 9913/0 10 Dec 1864 Brice paymasters Relay House', r'Dec(ember|\.)?\s+(9|10|11)\W{1,4}\s*1864', ['Relay|Brice|Paymaster'], ['Paymaster|Relay']),
     ('Y5 9800/2 24 Jul 1864 Hunter/Sixth Corps', r'July\s+(23|24|25)\W{1,4}\s*1864', ['Hunter|Sixth Corps|Wright'], ['Sixth|Corps']),
     ('Y7 9916/1 16 Dec 1864 Halleck/Canby/Hilton Head', r'Dec(ember|\.)?\s+(15|16|17)\W{1,4}\s*1864', ['Canby|Halleck|Hilton Head|Pensacola'], ['Canby|Hilton Head|Gulf']),
     ('Y8 9722/1 25 Apr 1864 Augur/Meade/Mosby/Warrenton', r'Apr(il|\.)?\s+(24|25|26)\W{1,4}\s*1864', ['Mosby|Upperville|Warrenton|Augur'], ['Mosby|Upperville|Warrenton']),
     ('Y9 9680/0 27 Feb 1864 Halleck/Grant/Hardee/Longstreet', r'Feb(ruary|\.)?\s+(26|27|28)\W{1,4}\s*1864', ['Grant|Halleck|Hardee|Longstreet'], ['Hardee|Jacksonville|Longstreet']),
     ('Y10 9725/0 27 Apr 1864 Burnside/Alexandria/Fairfax', r'Apr(il|\.)?\s+(26|27)\W{1,4}\s*1864', ['Burnside|Alexandria|Fairfax'], ['Fairfax|Alexandria']),
     ('Y11 9914/1 14 Dec 1864 Brice/Meade paymasters 6th corps', r'Dec(ember|\.)?\s+(13|14|15)\W{1,4}\s*1864', ['Meade|Brice|Paymaster'], ['Paymaster|Sixth Corps']),
     ('Y12 9681/0 29 Feb 1864 Stanton/Grant/Nashville telegraph', r'Feb(ruary|\.)?\s+(28|29)\W{1,4}\s*1864', ['Grant|Stanton|Eckert'], ['Nashville|telegraph'])]
for f in sys.argv[1:]:
    t = (gzip.open if f.endswith('.gz') else open)(f, 'rt', errors='ignore').read(); t2 = re.sub(r'\s+', ' ', t)
    for lab, dre, a, b in Q:
        n = h = 0; ex = []
        for m in re.finditer(dre, t2, flags=re.I):
            n += 1; w = t2[m.start()-150: m.end()+450]
            if all(re.search(x, w, re.I) for x in a) and all(re.search(x, w, re.I) for x in b): h += 1; ex.append(w[:300])
        if n: print(f'{os.path.basename(f)} | {lab} | date headings {n} | with terms {h}')
        for e in ex[:2]: print('    ', e)
