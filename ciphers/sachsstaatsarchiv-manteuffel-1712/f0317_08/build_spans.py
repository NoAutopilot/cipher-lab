#!/usr/bin/env python3
"""MANT-0317 (9 Oct 2026; copied from f0309_08/build_spans.py, MANT-0309): writes ciphertext.tsv from passA/passB + the worker's image settlements
below (made before any span or score), then spans_G1/G2.tsv from gloss1/gloss2.tsv (blind passes, used as written; NONE = no span).
No continuation runs on this leaf (PREREG-MANT0317.md). Run before gloss_gate.py."""
import csv, os
D = os.path.dirname(os.path.abspath(__file__)); leaf = '0317'
# (run, pos) -> (settled, conf, note): worker eye at 3x native, digits from the image (disclosure in PREREG)
SETTLE = {
 ('R02', 2): ('66', 'low', 'A 06 (note: may be 66) B 06?; 3x zoom: second glyph a 6 (b-form), first a small closed loop without the 6 ascender; 06 is not a group form on these leaves -- read 66 low, and gate.out is re-run with 06 as a sensitivity row'),
 ('R03', 3): ('28', 'med', 'A 282 (one group) B 28 2; 3x zoom: a point after the 8 before the 2 (28.2)'),
 ('R03', 4): ('2', 'med', 'A (in 282) B 2; as R03 pos 3'),
 ('R06', 0): ('292', 'med', 'A 242? B 242?; middle glyph y-tailed (4|9 glyph question, MANT-YCEN); read 9 as on 0309 (R05/R08 29)'),
 ('R11', 4): ('57', 'med', 'A 57? B 54?; second digit a y-tailed glyph of the same form as the next token, which both passes read 7'),
}
rd = lambda f: {r[0]: (r[1] if len(r) > 1 else '') for r in csv.reader(open(f'{D}/{f}'), delimiter='\t') if r and r[0] != 'crop'}
A, B = rd('passA.tsv'), rd('passB.tsv')
runs = [r['run'] for r in csv.DictReader(open(f'{D}/runs.tsv'), delimiter='\t')]
rows = []; n = 0
for run in runs:
    tok = lambda s: [] if s.strip().upper().startswith('NONE') else s.replace('?', '').split()
    a, b = tok(A[run]), tok(B.get(run, ''))
    if run == 'R03' and a[3:4] == ['282']: a = a[:3] + ['282', ''] + a[4:]  # A joined 28.2 into one group: keep positions aligned with B
    for i in range(max(len(a), len(b), 1 if (run, 0) in SETTLE else 0)):
        n += 1; pa = a[i] if i < len(a) else ''; pb = b[i] if i < len(b) else ''
        if (run, i) in SETTLE: s, c, note = SETTLE[(run, i)]
        elif pa == pb: s, c, note = pa, 'high', 'agree'
        else: raise SystemExit(f'unsettled {run} {i} {pa} {pb}')
        rows.append([f'T{n:03d}', run, i, pa, pb, s, c, note])
with open(f'{D}/ciphertext.tsv', 'w') as f:
    f.write('tokid\trun\tpos\tpassA\tpassB\tsettled\tconf\tnote\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
for gp in ('1', '2'):
    G = rd(f'gloss{gp}.tsv')
    with open(f'{D}/spans_G{gp}.tsv', 'w') as f:
        f.write('span_id\tleaf\trun\tgloss\tcodes\n')
        for run in runs:
            if run == 'R05b': continue
            g = G.get(run, '').strip()
            if not g or g.upper().startswith('NONE'): continue
            g = g.replace('?', '')
            codes = ' '.join(r[5] for r in rows if r[1] == run or (run == 'R05' and r[1] == 'R05b'))
            f.write(f'G{gp}-{run}\t{leaf}\t{run}\t{g}\t{codes}\n')
print(leaf, len(rows), 'tokens')
