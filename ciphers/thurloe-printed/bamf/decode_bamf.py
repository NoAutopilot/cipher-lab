#!/usr/bin/env python3
"""THUR-BAMF decode (rule 7): apply the vol 4 1655 Bamfylde gloss table (gate_bamf.json 'table', built from
pairs_vol4.tsv) to the 24 letter codes of Birch vol 6 p.160 (ct_p160.txt). Grades (PREREG-THUR-BAMF.md): C = code's
letter attested >= 2 times in the printed gloss with a strict majority, M = attested once, U = not in the table.
Word/name codes >= 100 (937, 745, 356) are left unread.   python3 decode_bamf.py [--check]"""
import json, sys
from pathlib import Path
H = Path(__file__).resolve().parent
T = json.loads((H / 'gate_bamf.json').read_text())['table']
ct = [l for l in (H / 'ct_p160.txt').read_text().splitlines() if l and not l.startswith('#')][0]
rows, txt, counts = ['code\tletter\tgrade\tattested'], [], {'C': 0, 'M': 0, 'U': 0}
for seg in ct.split('|'):
    w = ''
    for x in seg.split():
        c = int(x)
        if c >= 100:
            w += f'[{c}]'; rows.append(f'{c}\t\tcode\t'); continue
        t = T.get(str(c))
        g = 'U' if not t else ('C' if t['agree'] >= 2 else 'M')
        counts[g] += 1; L = t['letter'] if t else '?'
        w += L if g == 'C' else (L.upper() if g == 'M' else '?')
        rows.append(f"{c}\t{L}\t{g}\t{t['agree'] if t else 0}/{t['n'] if t else 0}")
    txt.append(w)
out = ('# Birch vol 6 p.160 l.19092 (Bamfylde, Paris, April 7/17 1657), decode under the vol 4 1655 gloss table.\n'
       '# lower case = C, upper = M, ? = U, [n] = word/name code unread. Gate: gate_bamf.json (PASS); D1 at most.\n'
       + ' | '.join(txt) + f"\n# grades: C {counts['C']} M {counts['M']} U {counts['U']} of 24 letter codes\n\n" + '\n'.join(rows) + '\n')
f = H / 'reading_bamf_p160.txt'
if '--check' in sys.argv:
    ok = f.exists() and f.read_text() == out; print('reading_bamf_p160.txt', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
f.write_text(out); print(out)
