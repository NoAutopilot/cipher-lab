#!/usr/bin/env python3
"""MANT-XTR (9 Oct 2026): writes f03NN_08/ciphertext.tsv from passA/passB + the worker's image settlements below (made before any span
or score), then spans_G1/G2.tsv from gloss1/gloss2.tsv (blind passes, used as written; NONE = no span). Run before gloss_gate.py."""
import csv, os
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# (leaf, run, pos) -> (settled, conf, note): worker eye at 2x native, digits from the image (disclosure in PREREG)
SETTLE = {
 ('0314','R03',0): ('257','med','A 254? B 254; last glyph = the leaf\'s 7 (same open-top hooked stroke as R21 187), unlike its 4 in 14 (R07, R11)'),
 ('0314','R08',0): ('257','med','A/B 254; last glyph as R03 (7 shape)'),
 ('0314','R13',0): ('257','med','A/B 254; last glyph as R03 (7 shape)'),
 ('0314','R18',0): ('257','med','A/B 254; last glyph as R03 (7 shape)'),
 ('0314','R15',2): ('190','low','A 150? B 190?; middle glyph is the y-tailed 9 of this hand (as in 198), not its s-shaped 5 (R17 150)'),
 ('0314','R11',8): ('10','med','both 10?; 1 then 0 at the strip edge, nothing after'),
 ('0312','A01',5): ('120','low','A/B 12?; a 0 under the ink blot after 12'),
 ('0312','A05',1): ('60','med','A/B 66; second glyph is a small o (0), as in A20 60'),
 ('0312','A11',0): ('198','low','last digit overwritten/blotted, 8 more likely than 6'),
 ('0312','A12',0): ('321','low','dark gutter shadow, edge'),
 ('0312','A13',3): ('21','low','under an ink stroke'),
}
for leaf in ('0314','0312'):
    D = f'{T}/f{leaf}_08'
    rd = lambda f: {r[0]: (r[1] if len(r) > 1 else '') for r in csv.reader(open(f'{D}/{f}'), delimiter='\t') if r and r[0] != 'crop'}
    A, B = rd('passA.tsv'), rd('passB.tsv')
    rows = []; n = 0
    for run in sorted(A):
        a = A[run].replace('?', '').split(); b = B.get(run, '').replace('?', '').split()
        for i in range(max(len(a), len(b))):
            n += 1; pa = a[i] if i < len(a) else ''; pb = b[i] if i < len(b) else ''
            if (leaf, run, i) in SETTLE: s, c, note = SETTLE[(leaf, run, i)]
            elif pa == pb: s, c, note = pa, 'high', 'agree'
            else: raise SystemExit(f'unsettled {leaf} {run} {i} {pa} {pb}')
            rows.append([f'T{n:03d}', run, i, pa, pb, s, c, note])
    with open(f'{D}/ciphertext.tsv', 'w') as f:
        f.write('tokid\trun\tpos\tpassA\tpassB\tsettled\tconf\tnote\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    for gp in ('1', '2'):
        G = rd(f'gloss{gp}.tsv')
        with open(f'{D}/spans_G{gp}.tsv', 'w') as f:
            f.write('span_id\tleaf\trun\tgloss\tcodes\n')
            for run in sorted(A):
                g = G.get(run, '').strip()
                if not g or g.upper().startswith('NONE'): continue
                g = ' '.join(x.strip() for x in g.split('|')).replace('?', '')
                codes = ' '.join(r[5] for r in rows if r[1] == run)
                f.write(f'G{gp}-{run}\t{leaf}\t{run}\t{g}\t{codes}\n')
    print(leaf, len(rows), 'tokens')
