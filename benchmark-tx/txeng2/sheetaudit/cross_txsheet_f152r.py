#!/usr/bin/env python3
"""TXE2-SHEETAUDIT (9 Oct 2026): cross the TX-SHEET per-hand sheet's f152r tiles (atlas/sheet_truth/sheet.tsv) against
the birago1572-f152r truth, reading truth rows ONLY at those tile positions. sid -> atlas/secure_tokens.tsv (passage, pos)
-> truth line f152r_<passage>, pos; ref_sign is printed beside the tile's code as a mapping check.
Other leaves' tiles (f139v, f144r, f162r, f174*, f175v, f184*, f185r) are on no benchmark item and are not crossable."""
import csv, os
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
A = os.path.join(R, 'ciphers/nevers-birago-fr3251-1572/atlas')
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))
sec = {r['sid']: r for r in rd(os.path.join(A, 'secure_tokens.tsv'))}
tiles = [(r['code'], s) for r in rd(os.path.join(A, 'sheet_truth/sheet.tsv')) for s in r['exemplars'].split(',') if s.startswith('f152r_')]
keys = {(f"f152r_{sec[s]['passage']}", sec[s]['pos']) for _, s in tiles}
truth = {(t['line'], t['pos']): t for t in rd(os.path.join(R, 'benchmark-tx/birago1572-f152r.truth.tsv')) if (t['line'], t['pos']) in keys}
print('sheet\tcell\tbox\ttruth_pos\tref_sign\ttruth\tplain\tstatus\tverdict')
for code, s in tiles:
    k = (f"f152r_{sec[s]['passage']}", sec[s]['pos']); t = truth.get(k)
    if t is None:
        print(f'sheet_truth\t{code}\t{s}\t{k[0]}.{k[1]}\t-\t-\t-\tno truth row\tno-truth'); continue
    tv = t['truth']
    v = 'MAPPING?' if t['ref_sign'] != code else ('no-truth (' + t['status'] + ')' if not tv else ('OK' if code in tv.split('|') else 'MISLABELLED'))
    print(f"sheet_truth\t{code}\t{s}\t{k[0]}.{k[1]}\t{t['ref_sign']}\t{tv}\t{t['plain']}\t{t['status']}\t{v}")
