#!/usr/bin/env python3
"""LVN-L1 (15 Oct 2026): settle the missing 4611 p3 first line (unit p3L00) under the LVN-L1 addendum of lvn4611/PREREG-LVN-4611.md.
Reads lvn4611/reads_p3L00.tsv (two blind Sonnet calls A, B; 19 targets + 10 controls) and writes lvn4611/insert_p3L00.tsv, which
../settle.py inserts ahead of the first p3_L01 row of ciphertext_4611.tsv. Gate per call >= 8/10 controls exact; A == B (no '?') -> H
when a key_full.tsv code, else M; otherwise the reconcile below (worker's one Opus look), graded M.
DEVIATION (logged, a downgrade only): T11 (position 12) -- the tight crop cut off the leading '1' that the context crop shows ("1 27."),
so both readers saw only "27"; a placement defect, not a reading, so the agreed 27 is not settled H: entered 127 by the reconcile, M.
--check: exit 1 if insert_p3L00.tsv is stale (rule 7)."""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
codes = {r['code'] for r in rd(os.path.join(T, 'key_full.tsv'))}
R = rd(os.path.join(H, 'reads_p3L00.tsv'))
RECONCILE = {'T10': ('138', "A 128 / B 138; middle digit is the flat-topped 3 of the controls' 38"),
             'T11': ('127', "A 27 = B 27 on a tight crop that cut off the leading 1; context crop reads 1 27. (crop defect, PREREG deviation)")}
gate = {c: sum(r['read' + c] == r['sign'] for r in R if r['role'] == 'control') for c in 'AB'}
ok = all(v >= 8 for v in gate.values())
print('p3L00 control A %d/10, B %d/10, gate %s' % (gate['A'], gate['B'], 'PASS' if ok else 'FAIL'))
rows = [['p3_L00', '1', '=diy', 'M', '', 'LVN-L1 by eye at 300 dpi (clear word, not read)']]
for r in R:
    if r['role'] != 'target': continue
    a, b = r['readA'], r['readB']
    if ok and a == b and '?' not in a and r['tid'] not in RECONCILE:
        rows.append([r['line'], r['position'], a, 'H' if a in codes else 'M', '',
                     'LVN-L1 per-token 300-dpi read A %s = B %s (%s; controls %d/%d)' % (a, b, r['tid'], gate['A'], gate['B'])])
    else:
        v, why = RECONCILE.get(r['tid'], (a if a == b else '?', 'not reconciled'))
        rows.append([r['line'], r['position'], v, 'M', 'A:%s B:%s' % (a, b), 'LVN-L1 reconcile (%s): %s' % (r['tid'], why)])
# VER-LVN (15 Oct 2026, verifier, AUDIT.md "VER-LVN"): one Opus eye at 300 dpi on the full physical line beside the hand's 1s.
# /12: the leading 1 stands clear of "27." as in 116 and 12 on the same line, so the reconcile's 127 is confirmed by a second eye; no
# blind read contradicts it (both saw only "27" on the defective crop) -> S, as R15-LVNCTL graded two agreeing image looks.
# /11 138: eye agrees with B and the reconcile, but blind A read 128 -> stays M. /14 61 H: eye reads 61 (the 6 of 116), no change.
EYE = {('p3_L00', '12'): ('127', 'S', 'VER-LVN eye confirms the leading 1 (second image look agreeing with the reconcile)')}
for x in rows:
    e = EYE.get((x[0], x[1]))
    if e:
        assert x[2] == e[0], (x, e)
        x[3] = e[1]; x[5] += '; ' + e[2]
s = io.StringIO(); s.write('line\tposition\tsign\tconfidence\talt\twhy\n')
for x in rows: s.write('\t'.join(x) + '\n')
p = os.path.join(H, 'insert_p3L00.tsv')
if '--check' in sys.argv:
    if not os.path.exists(p) or open(p).read() != s.getvalue(): print('STALE', p); sys.exit(1)
else:
    open(p, 'w').write(s.getvalue())
print(sum(x[3] == 'H' for x in rows), 'H,', sum(x[3] == 'M' for x in rows), 'M of', len(rows), 'rows')
