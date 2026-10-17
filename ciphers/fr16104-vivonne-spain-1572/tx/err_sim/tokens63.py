#!/usr/bin/env python3
"""ERR-SIM: reading_piece63.tsv (one row per line) -> per-token TSV for tools/depth_stats.py (line, pos, sign, conf, value, grade).
    python3 tx/err_sim/tokens63.py  (writes tx/err_sim/tokens63.tsv)"""
import csv, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(os.path.dirname(H))
with open(os.path.join(H, 'tokens63.tsv'), 'w') as o:
    o.write('line\tpos\tsign\tconf\tvalue\tgrade\n')
    for r in csv.DictReader(open(os.path.join(T, 'reading_piece63.tsv')), delimiter='\t'):
        for i, (c, v, g) in enumerate(zip(r['codes'].split(), r['decode'], r['grades']), 1):
            o.write(f"{r['page']}_{r['line']}\t{i}\t{c}\t\t{'' if v == '_' else v}\t{g}\n")
