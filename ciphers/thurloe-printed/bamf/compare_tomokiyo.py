#!/usr/bin/env python3
"""THUR-BAMF2 (rule 7): compare our 51-code Bamfylde table (gate_bamf.json 'table', from Birch vol 4 1655 gloss) with
Tomokiyo's First Cipher table (tomokiyo/bamp1_table.tsv, transcribed from his bamp1.jpg) code by code.
status: agree (our letter is his value or one of his alternatives), disagree, absent_ours, absent_his, his_dash (he gives '-').
Writes compare_bamp1.tsv.   python3 compare_tomokiyo.py [--check]"""
import json, sys
from pathlib import Path
H = Path(__file__).resolve().parent
T = json.loads((H / 'gate_bamf.json').read_text())['table']
tom = {}
for l in (H / 'tomokiyo' / 'bamp1_table.tsv').read_text().splitlines():
    if l and not l.startswith('#') and not l.startswith('code'):
        c, v = l.split('\t'); tom[int(c)] = v
rows, n = ['code\tours\tours_attested\ttomokiyo\tstatus'], {}
for c in sorted(set(tom) | {int(k) for k in T}):
    o = T.get(str(c)); t = tom.get(c)
    if o is None: s = 'absent_ours'
    elif t is None: s = 'absent_his'
    elif t == '-': s = 'his_dash'
    else: s = 'agree' if o['letter'].lower() in t.split('/') else 'disagree'
    n[s] = n.get(s, 0) + 1
    rows.append(f"{c}\t{o['letter'] if o else ''}\t{str(o['agree'])+'/'+str(o['n']) if o else ''}\t{t or ''}\t{s}")
out = '\n'.join(rows) + '\n# counts: ' + ', '.join(f'{k} {v}' for k, v in sorted(n.items())) + '\n'
f = H / 'compare_bamp1.tsv'
if '--check' in sys.argv:
    ok = f.exists() and f.read_text() == out; print('compare_bamp1.tsv', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
f.write_text(out); print(out)
