#!/usr/bin/env python3
"""N7-VIV53L: echo check of a window re-read -- how often its label equals reader A (= passC at a split), reader B, or neither.
    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53L_echo.py PAGE"""
import csv, os, sys
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lookalike53L', sys.argv[1])
t = {(r['passage'], r['pos']): r for r in csv.DictReader(open(os.path.join(d, f'53L_{sys.argv[1]}_splits_tiles.tsv')), delimiter='\t')}
c = {'A': 0, 'B': 0, 'other': 0}
for r in csv.DictReader(open(os.path.join(d, f'53L_{sys.argv[1]}_reread.tsv')), delimiter='\t'):
    x = t[(r['passage'], r['pos'])]
    c['A' if r['label'] == x['A'] else 'B' if r['label'] == x['B'] else 'other'] += 1
print(sys.argv[1], c)
