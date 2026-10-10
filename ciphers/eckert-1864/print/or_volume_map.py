#!/usr/bin/env python3
"""OR-CACHE (10 Oct 2026): read the printed title page out of each OR volume's head (or_titlepage.py output dir) and
compare with the volume the repo's list (ciphers/eckert-1862/ec18/or_volumes.tsv) claims. Usage: or_volume_map.py HEADDIR"""
import re, glob, os, csv, sys
R = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100}
def rom(s):
    s = s.upper().replace('J', 'I'); v = 0
    for a, b in zip(s, s[1:] + ' '):
        x, y = R.get(a, 0), R.get(b, 0); v += -x if x < y else x
    return v
claim = {r['ia_identifier']: r['or_vol'] for r in csv.DictReader(open('ciphers/eckert-1862/ec18/or_volumes.tsv'), delimiter='\t')}
for f in sorted(glob.glob(sys.argv[1] + '/*.head.txt')):
    i = os.path.basename(f)[:-9]; raw = open(f, errors='replace').read(); src = raw.split('\n', 1)[0]
    t = re.sub(r'\s+', ' ', raw)
    k = max(t.find('THE WAR OF THE REBELLION'), t.find('WAR OF THE REBELLION'))
    seg = t[k:k + 1500] if k >= 0 else t
    m = re.search(r'SERIES\s+([IVX]+)[^A-Z]{0,4}VOLUME\s+([IVXLjl]+)', seg)
    pm = re.search(r'PA-?RT\s+([IVXHT]+)\b', seg)
    nm = re.search(r'IN\s+(TWO|THREE|FOUR|FIVE|SIX)\s+PARTS', seg)
    part = rom(pm.group(1).replace('H', 'II').replace('T', 'I')) if pm else ''
    print('\t'.join(map(str, [i, claim.get(i, '-'), rom(m.group(1)) if m else '?', rom(m.group(2)) if m else '?', part, nm.group(1) if nm else '', src])))
