#!/usr/bin/env python3
"""MONL-CTL (15 Oct 2026): tiles for sort/ctl/PREREG-MONL-CTL.md: 4 c268 in-band K04-facing-d controls (L17:16, L19:2, L20:23, L20:33),
4 unsettled K04-facing-n leads (L11:14, L16:16, L17:20, L20:8) and 2 K12 references (L19:6, L20:32). Same packet format and band shifts as
sort/k04/build_k04.py (c268d band L0n = c268 L(n+13); c268c band L06 = c268 L11). Run from the folder."""
import csv, shutil
HDR = 'run\tpassage\tpos\tpassC\tA\tB\tstatus\twhy\tcandidates\tbefore\tafter\tnoteA\tnoteB\n'
D_TILES = {('L17', '16'), ('L19', '2'), ('L20', '23'), ('L20', '33'), ('L16', '16'), ('L17', '20'), ('L20', '8'), ('L19', '6'), ('L20', '32')}
C_TILES = {('L11', '14')}
def ctx(rs, i):
    return ' '.join(x['sign'] for x in rs[max(0, i - 3):i]), ' '.join(x['sign'] for x in rs[i + 1:i + 4])
def write(out, rows):
    with open(out, 'w') as o:
        o.write(HDR)
        for r in rows: o.write('\t'.join(r) + '\n')
    print(out, len(rows))
def tiles(rows, want, run, shift):
    by, t = {}, []
    for r in rows: by.setdefault(r['line'], []).append(r)
    for ln, rs in by.items():
        for i, r in enumerate(rs):
            if (ln, r['pos']) in want:
                bef, aft = ctx(rs, i)
                t.append([run, f'L{int(ln[1:]) - shift:02d}', r['pos'], r['sign'], r['sign'], '', 'check', 'sort', 'K04,K12', bef, aft, '', ''])
    return t
c268 = list(csv.DictReader(open('ciphertext_c268.tsv'), delimiter='\t'))
d = tiles(c268, D_TILES, 's268d', 13); assert len(d) == 9; write('sort/ctl/s268d_tiles.tsv', d)
c = tiles(c268, C_TILES, 's268c', 5); assert len(c) == 1; write('sort/ctl/s268c_tiles.tsv', c)
shutil.copy('sort/k04/c268d_passc.tsv', 'sort/ctl/c268d_passc.tsv'); shutil.copy('sort/k04/c268c_passc.tsv', 'sort/ctl/c268c_passc.tsv')
