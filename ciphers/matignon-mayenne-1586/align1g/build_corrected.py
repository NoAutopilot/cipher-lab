#!/usr/bin/env python3
"""bMAT1G: rebuild f.78v with the page's line structure (11 lines) from Bourdeau's f78 (dbourdeau/cyphersolver
matignon1586/f78_cipher.txt, fc0c9e8, CC BY 4.0, copied as f78_bourdeau.txt) plus the signs his transcription skips,
read from native crops by two blind passes (align1f/passA_f78v.tsv, align1g/passB_f78v.tsv; inserted segments in
passA_ins.tsv / passB_ins.tsv, reconciled by tools/reconcile_passes.py, disagreements settled on the crop in NOTES.md).
Finding: Bourdeau l.9 = page l.9 up to '.v. d' + page l.10 from 'Ze oo t ff h' to its end; Bourdeau l.10 = page l.10 up
to 'o s e' + page l.11 from 'Ze d ff' to its end. Missing: page l.9 after '.v. d' (27 signs) and page l.11 before 'Ze d ff'
(17 signs). Inserted grade: C = both passes agree, M = one pass or settled on the crop by one reader.
Writes f78_corrected.txt (token/grade, inserted tokens marked +) and f78_corrected_stream.txt (plain tokens).
--check exits 1 if the committed files are stale."""
import os, sys
h = os.path.dirname(os.path.abspath(__file__))
B = [l.split() for l in open(os.path.join(h, 'f78_bourdeau.txt')) if l.strip()]
assert len(B) == 10 and B[8][13] == 'd' and B[8][14] == 'Ze' and B[9][15] == 'e' and B[9][16] == 'Ze'
INS9 = [('w-','C'),('h','C'),('m','C'),('2','M'),('7','C'),('B','C'),('p','C'),('ff','C'),('s','C'),('w','M'),('q','C'),
        ('d','M'),('m','C'),('T','C'),('B','C'),('d','M'),('7','C'),('3','C'),('d','C'),('f','C'),('54','M'),('d','M'),
        ('U','C'),('q','C'),('1','C'),('7','M'),('6','M')]
INS11 = [('9','M'),('14','C'),('c','C'),('p','C'),('o','C'),('d','M'),('BOX2','C'),('t','C'),('f','C'),('E','C'),('h','C'),
         ('c','C'),('p','C'),('U','C'),('oo','C'),('t','C'),('d','C')]
b = lambda toks: [(t, 'B') for t in toks]
lines = [b(l) for l in B[:8]]
lines.append(b(B[8][:14]) + [(t, g + '+') for t, g in INS9])
lines.append(b(B[9][:16]) + b(B[8][14:]))
lines.append([(t, g + '+') for t, g in INS11] + b(B[9][16:]))
full = '\n'.join(' '.join(t if g == 'B' else '%s/%s' % (t, g) for t, g in l) for l in lines) + '\n'
plain = '\n'.join(' '.join(t for t, g in l) for l in lines) + '\n'
ins = [g for l in lines for t, g in l if g != 'B']
summary = 'lines %d, Bourdeau tokens %d (all kept), inserted %d (C %d, M %d)' % (len(lines), sum(len(l) for l in B), len(ins), ins.count('C+'), ins.count('M+'))
if '--check' in sys.argv:
    ok = open(os.path.join(h, 'f78_corrected.txt')).read() == full and open(os.path.join(h, 'f78_corrected_stream.txt')).read() == plain
    print(summary, 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(os.path.join(h, 'f78_corrected.txt'), 'w').write(full)
open(os.path.join(h, 'f78_corrected_stream.txt'), 'w').write(plain)
print(summary)
