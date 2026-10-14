#!/usr/bin/env python3
"""C1161-V2 (lkey/PREREG-C1161-V2.md): derive lkey/ciphertext_v2.tsv (George Lasry's nomenclature digit pairs as units, greedy,
within a line) and lkey/key_v2.tsv / key_v2b.tsv from key.tsv. ciphertext.tsv and key.tsv are read only."""
import csv
from pathlib import Path
T = Path(__file__).resolve().parents[1]
NOM = {'77': 'de', '62': 'est', '55': 'que', '52': 'qui', '48': 'fait', '76': 'le', '37': 'ou', '30': 'quant', '60': 'puis', '44': 'il'}
POST = {'8': 'c', 'rc': 's', 'tz': 'l', 'c': 'f', 'L': 's'}
SRC = 'Lasry key sheet nomenclature (lasry_p073_1.png, cyphersolver dde5b0ea, CC BY 4.0); mapping by label-name identity, not two-pass (C1161-V2, 14 Oct 2026)'
rows = list(csv.DictReader(open(T / 'ciphertext.tsv'), delimiter='\t'))
out, i = [], 0
while i < len(rows):
    r = rows[i]; n = rows[i + 1] if i + 1 < len(rows) else None
    if n and n['line'] == r['line'] and r['sign'] + n['sign'] in NOM:
        conf = 'H' if r['conf'] == n['conf'] == 'H' else 'M'
        out.append({'line': r['line'], 'pos': r['pos'], 'sign': 'n' + r['sign'] + n['sign'], 'conf': conf,
                    'note': f"V2 unit from pos {r['pos']},{n['pos']}"}); i += 2
    else: out.append(r); i += 1
with open(T / 'lkey' / 'ciphertext_v2.tsv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, ['line', 'pos', 'sign', 'conf', 'note'], delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(out)
key = list(csv.DictReader(open(T / 'key.tsv'), delimiter='\t'))
for name, post in (('key_v2.tsv', {}), ('key_v2b.tsv', POST)):
    with open(T / 'lkey' / name, 'w', newline='') as fh:
        w = csv.DictWriter(fh, ['sign', 'value', 'grade', 'source'], delimiter='\t', lineterminator='\n'); w.writeheader()
        for k in key:
            k = dict(k)
            if k['sign'] in post:
                k['source'] = f"Lasry value {post[k['sign']]} (two-pass mapped, C1161-LKEY); post-hoc selection, C1161-V2; ours was {k['value']} {k['grade']}"
                k['value'], k['grade'] = post[k['sign']], 'M'
            w.writerow(k)
        for c, v in NOM.items(): w.writerow({'sign': 'n' + c, 'value': v, 'grade': 'M', 'source': SRC})
print(len(rows), '->', len(out), 'tokens;', sum(1 for r in out if r['sign'].startswith('n') and r['sign'][1:].isdigit()), 'units')
