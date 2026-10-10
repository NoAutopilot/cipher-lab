#!/usr/bin/env python3
"""FV-L14a (10 Oct 2026): fetch two OR djvu texts not in the print-check cache (OR I/43 pt 1 = warofrebellion014301rootrich; OR I/39 pt 3 =
warofrebellion393unit) to a scratch dir and print the KWIC of the printed texts of E601, E603, E604 msg 1 with the nearest running heads.
Usage: fv_l14a_print.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import re, sys, time, urllib.request
S = sys.argv[1]; UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
V = {'or431': 'warofrebellion014301rootrich', 'or393': 'warofrebellion393unit'}
K = [('E601', 'or431', 'reliable Union man'), ('E603', 'or431', 'Lazelle, with his'), ('E604', 'or393', 'compunction')]
T = {}
for k, ident in V.items():
    raw = urllib.request.urlopen(urllib.request.Request(f'https://archive.org/download/{ident}/{ident}_djvu.txt', headers=UA), timeout=120).read().decode('utf8', 'replace')
    T[k] = re.sub(r'\s+', ' ', raw); time.sleep(2)
for e, k, key in K:
    t = T[k]; i = t.find(key)
    heads = [(m.start() - i, m.group(0)) for m in re.finditer(r'\d{3,4} (?:OPERATIONS IN|KY\.)|CORRESPONDENCE[^\d]{0,15}\d{3,4}', t[max(0, i - 9000):i + 6000])]
    print(e, k, 'found' if i >= 0 else 'MISS', '|', t[max(0, i - 900):i + 700] if i >= 0 else '')
    print('   running heads (offset from key):', [(o - 9000 if i >= 9000 else o, h) for o, h in heads])
