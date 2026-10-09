#!/usr/bin/env python3
"""AUD2-LEDGER-23 (9 Oct 2026): independent key look-up of every word of E302 (pointer 5697/1) against key.md rows (all sections),
case-insensitive; prints each body word that is a key row with its meaning(s) and the key's page/line. A look-up, not a decode."""
import os, re
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..')
key = {}
for l in open(os.path.join(T, 'key.md')):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if l.startswith('|') and len(c) >= 3 and c[0] and not set(c[0]) <= set('-: ') and c[0].lower() != 'word':
        key.setdefault(c[0].lower(), []).append((c[1], c[2], c[3] if len(c) > 3 else ''))
txt = open(os.path.join(T, 'ciphertext.txt')).read()
body = txt.split('### E302 ', 1)[1].split('\n### ', 1)[0].split('\n', 1)[1]
hits = 0
for i, w in enumerate(re.findall(r"[A-Za-z']+", body)):
    k = key.get(w.lower())
    if k:
        hits += 1; print(i, w, '=', ' / '.join(f'{m} ({g}, {s})' for m, g, s in k))
print('key-row words:', hits)
