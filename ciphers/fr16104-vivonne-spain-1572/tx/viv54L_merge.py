#!/usr/bin/env python3
"""N7-VIV54L addendum A: build the reread file reconcile sees -- window re-read rows for split tiles, the first instrument's (void, conf L)
rows for one-pass-gap tiles -- then run `lookalike_pass.py reconcile` per page -> tx/lookalike54/viv54L_<page>_passD.tsv + focus.tsv.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_merge.py
"""
import csv, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LA = os.path.join(HERE, 'lookalike54')
TOOL = os.path.join(HERE, '..', '..', '..', 'tools', 'lookalike_pass.py')
F = ['passage', 'pos', 'label', 'conf', 'second', 'note']
for page in ('f173r', 'f173v'):
    rd = lambda p: list(csv.DictReader(open(os.path.join(LA, p)), delimiter='\t'))
    win = {(r['passage'], r['pos']): r for r in rd(f'viv54L_{page}_win_reread.tsv')}
    void = {(r['passage'], r['pos']): r for r in rd(f'viv54L_{page}_reread_used.tsv')}
    tiles = rd(f'viv54L_{page}_tiles.tsv')
    out = os.path.join(LA, f'viv54L_{page}_reread_merged.tsv')
    with open(out, 'w') as o:
        o.write('\t'.join(F) + '\n')
        for t in tiles:
            k = (t['passage'], t['pos'])
            r = win[k] if t['status'] == 'split' else void[k]
            o.write('\t'.join((r.get(f) or '').replace('\t', ' ') for f in F) + '\n')
    res = subprocess.run([sys.executable, TOOL, 'reconcile', '--tiles', os.path.join(LA, f'viv54L_{page}_tiles.tsv'),
                          '--passc', os.path.join(LA, 'align', page, 'passC.tsv'), '--reread', out,
                          '--out', os.path.join(LA, f'viv54L_{page}_passD.tsv'), '--focus', os.path.join(LA, f'viv54L_{page}_focus.tsv'),
                          '--run', f'viv54L_{page}'], capture_output=True, text=True)
    print(page, res.stdout.strip(), res.stderr.strip())
