#!/usr/bin/env python3
"""AUD2-LEDGER-15 (9 Oct 2026, account 4): print search for E251 E252 E253 E256 E258.

Fetches each volume's djvu text once from archive.org to a scratch directory (argv[1], default ./_aud2_l15),
2 s apart, checks its title page, and prints the lines around each pattern. Images and texts stay out of the repo.
Volumes: OR I/43 pt 1 (warofrebellion014301rootrich -- NOT the cached warofrebellion431unit, which is I/47 pt 2),
OR I/42 pt 2-3, OR I/40 pt 1-2, OR I/35 pt 2, Plum Military Telegraph II, Davis History of the 104th Pa. (1866),
Butler Private and Official Correspondence V.
"""
import os, re, sys, time, urllib.request

OUT = sys.argv[1] if len(sys.argv) > 1 else '_aud2_l15'
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
VOLS = {
    'warofrebellion014301rootrich': ['One hundred and fourth Pennsyl', 'One hundred and fourth\\s+Regiment', 'steamer Fulton',
                                     'Hart, Thompson D', 'Foster, John G'],
    'warofrebellion422unit': ['hundred and fourth Penn', 'steamer Fulton', 'Hilton Head'],
    'warofrebellion423unit': ['Bartonsville', 'Stephen Barton', 'Carney'],
    'warofrebellion401unit': ['Dealy', 'Bridge was taken up', 'Jamestown Island 1'],
    'warofrebellion402unit': ['Dealy', 'Channing Clapp', 'Pettes'],
    'warofrebellion352unit': ['regiment sent on the Fulton', 'August 2[6-8], 1864'],
    'militarytelegraph02plumrich': ['Douglas Kent', 'close the lines'],
    'historyof104thpe00davi': ['landed from the', 'last of August several'],
    'privateofficialc05butl': ['Bartonsville', 'Provost Marshal', 'Geo. C. Carney'],
}
os.makedirs(OUT, exist_ok=True)
for ident, pats in VOLS.items():
    p = os.path.join(OUT, ident + '.txt')
    if not os.path.exists(p):
        data = urllib.request.urlopen(urllib.request.Request(
            f'https://archive.org/download/{ident}/{ident}_djvu.txt', headers=UA), timeout=180).read()
        open(p, 'wb').write(data)
        time.sleep(2)
    lines = [re.sub(r' +', ' ', l) for l in open(p, encoding='utf-8', errors='replace').read().split('\n')]
    head = ' '.join(lines[:400])
    m = re.search(r'(SERIES I.{0,40}VOLUME [XLVI]+.{0,40}PART [IV]+)', head)
    print('=' * 8, ident, '|', m.group(1) if m else head[:0] or '(no OR title)')
    for pat in pats:
        hits = [i for i, l in enumerate(lines) if re.search(pat, l)]
        print(f'-- {pat!r}: {len(hits)} hit(s)')
        for i in hits[:4]:
            print('   ', ' / '.join(x.strip() for x in lines[max(0, i - 3):i + 6] if x.strip())[:600])
