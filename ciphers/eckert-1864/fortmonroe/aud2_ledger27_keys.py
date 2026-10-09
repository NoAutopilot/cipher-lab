#!/usr/bin/env python3
"""AUD2-LEDGER-27 (9 Oct 2026; copy of aud2_ledger25_keys.py): independent key look-up of every word of E319 (5695), E320 (5702) and E321 (5782) against key.md rows (all sections),
case-insensitive; prints each body word that is a key row with its meaning(s) and the key's page/line. A look-up, not a decode."""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..')
key = {}
for l in open(os.path.join(T, 'key.md')):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if l.startswith('|') and len(c) >= 3 and c[0] and not set(c[0]) <= set('-: ') and c[0].lower() != 'word':
        key.setdefault(c[0].lower(), []).append((c[1], c[2], c[3] if len(c) > 3 else ''))
txt = open(os.path.join(T, 'ciphertext.txt')).read()
for E in ('E319', 'E320', 'E321'):
    body = txt.split('### ' + E + ' ', 1)[1].split('\n### ', 1)[0]
    print('=====', E); print(body.strip()); print('-----')
    hits = 0
    for i, w in enumerate(re.findall(r"[A-Za-z']+", body.split('\n', 1)[1])):
        k = key.get(w.lower())
        if k:
            hits += 1; print(i, w, '=', ' / '.join(f'{m} ({g}, {s})' for m, g, s in k))
    print(E, 'key-row words:', hits)
