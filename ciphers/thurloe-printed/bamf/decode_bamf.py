#!/usr/bin/env python3
"""THUR-BAMF decode (rule 7): apply the vol 4 1655 Bamfylde gloss table (gate_bamf.json 'table', built from
pairs_vol4.tsv) to the 24 letter codes of Birch vol 6 p.160 (ct_p160.txt). Grades (PREREG-THUR-BAMF.md): C = code's
letter attested >= 2 times consistently in the printed gloss, M = attested once or with a dissenting gloss, U = not in the
table. V-BAMF (verifier, 11 Oct 2026) corrected the earlier 'strict majority' rule to the PREREG's 'consistently': code 30
(e 8, y 1, r 1) is M; code 72 (u 3, v 1) stays C because u and v are one letter in the print (pairs_vol4.tsv p232 run 6).
Word/name codes >= 100 (937, 745, 356) are left unread by the gate table; THUR-BAMF2 (11 Oct 2026) adds values from
additions_bamf2.tsv (vol 5 print gloss, graded there) for codes absent from the table; the gate (gate_bamf.json) is not re-scored.
   python3 decode_bamf.py [--check]"""
import json, sys
from pathlib import Path
H = Path(__file__).resolve().parent
T = json.loads((H / 'gate_bamf.json').read_text())['table']
A = {int(r.split('\t')[0]): r.split('\t')[1:3] for r in (H / 'additions_bamf2.tsv').read_text().splitlines()
     if r and not r.startswith(('#', 'code'))}
ct = [l for l in (H / 'ct_p160.txt').read_text().splitlines() if l and not l.startswith('#')][0]
UV = {72}  # dissenting gloss is v, the same letter as u (V-BAMF)
rows, txt, counts = ['code\tletter\tgrade\tattested'], [], {'C': 0, 'M': 0, 'U': 0}
for seg in ct.split('|'):
    w = ''
    for x in seg.split():
        c = int(x)
        if c >= 100:
            if c in A:
                v, g = A[c]; w += f'[{c}={v if g == "C" else v.upper()}]'; rows.append(f'{c}\t{v}\tcode-{g}\tadditions_bamf2')
            else:
                w += f'[{c}]'; rows.append(f'{c}\t\tcode-U\t')
            continue
        t = T.get(str(c))
        if not t and c in A:
            L, g = A[c]; counts[g] += 1; w += L if g == 'C' else L.upper()
            rows.append(f'{c}\t{L}\t{g}\tadditions_bamf2'); continue
        g = 'U' if not t else ('C' if t['agree'] >= 2 and (t['agree'] == t['n'] or c in UV) else 'M')
        counts[g] += 1; L = t['letter'] if t else '?'
        w += L if g == 'C' else (L.upper() if g == 'M' else '?')
        rows.append(f"{c}\t{L}\t{g}\t{t['agree'] if t else 0}/{t['n'] if t else 0}")
    txt.append(w)
out = ('# Birch vol 6 p.160 l.19092 (Bamfylde, Paris, April 7/17 1657), decode under the vol 4 1655 gloss table.\n'
       '# lower case = C, upper = M, ? = U, [n] = word/name code unread, [n=v] word/name code from additions_bamf2.tsv (upper = M). Gate: gate_bamf.json (PASS); D1 at most.\n'
       + ' | '.join(txt) + f"\n# grades: C {counts['C']} M {counts['M']} U {counts['U']} of 24 letter codes\n\n" + '\n'.join(rows) + '\n')
f = H / 'reading_bamf_p160.txt'
if '--check' in sys.argv:
    ok = f.exists() and f.read_text() == out; print('reading_bamf_p160.txt', 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
f.write_text(out); print(out)
