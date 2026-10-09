#!/usr/bin/env python3
"""MANT-0309 (9 Oct 2026; after f0314_08/build_spans.py, MANT-XTR): writes ciphertext.tsv from passA/passB + the worker's image settlements
below (made before any span or score), then spans_G1/G2.tsv from gloss1/gloss2.tsv (blind passes, used as written; NONE = no span).
R05b continues R05 on the next line: its codes join R05's span (fixed in PREREG-MANT0309.md). Run before gloss_gate.py."""
import csv, os
D = os.path.dirname(os.path.abspath(__file__)); leaf = '0309'
# (run, pos) -> (settled, conf, note): worker eye at 3x native, digits from the image (disclosure in PREREG)
SETTLE = {
 ('R06', 0): ('9', 'med', 'A NONE (4? at edge) B NONE (4?); one y-tailed glyph + point, same form as the last digit of R05 29 and R08 29 (both passes 29)'),
 ('R09', 0): ('9', 'med', 'A 4? B NONE; one y-tailed glyph + point, as R06'),
 ('R16', 0): ('9', 'med', 'A 4? B NONE (e 9?); one y-tailed glyph + point, as R06'),
 ('R04', 1): ('259', 'med', 'A 259? B 259; y-tailed last digit (4|9 glyph question as 254/257 on 0314; read 9 as in R05 29)'),
}
rd = lambda f: {r[0]: (r[1] if len(r) > 1 else '') for r in csv.reader(open(f'{D}/{f}'), delimiter='\t') if r and r[0] != 'crop'}
A, B = rd('passA.tsv'), rd('passB.tsv')
runs = [r['run'] for r in csv.DictReader(open(f'{D}/runs.tsv'), delimiter='\t')]
rows = []; n = 0
for run in runs:
    tok = lambda s: [] if s.strip().upper().startswith('NONE') else s.replace('?', '').split()
    a, b = tok(A[run]), tok(B.get(run, ''))
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
