#!/usr/bin/env python3
"""MONL-K04 (15 Oct 2026): tiles for sort/k04/PREREG-MONL-K04.md: 8 c268 K04-facing-n leads (L11:14, L16:11, L16:16, L17:20, L18:18,
L20:8, L20:27, L20:37), 2 c268 K12 references (L19:6, L20:32) and 2 c172 K04 controls (L03:26, L04:13). Band ids: c268d band L0n =
c268 L(n+13) (regen_monll16.sh); c268c band L06 = c268 L11 (regen_monll11.sh). Writes sort/k04/{s268d,s268c,s172}_tiles.tsv
(tools/lookalike_pass.py windows packet format) and sort/k04/{c268d,c268c}_passc.tsv. Run from the folder."""
import csv
HDR = 'run\tpassage\tpos\tpassC\tA\tB\tstatus\twhy\tcandidates\tbefore\tafter\tnoteA\tnoteB\n'
D_TILES = {('L16', '11'), ('L16', '16'), ('L17', '20'), ('L18', '18'), ('L20', '8'), ('L20', '27'), ('L20', '37'), ('L19', '6'), ('L20', '32')}
C_TILES = {('L11', '14')}
CTL = {('L03', '26'), ('L04', '13')}
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
d = tiles(c268, D_TILES, 's268d', 13); assert len(d) == 9; write('sort/k04/s268d_tiles.tsv', d)
c = tiles(c268, C_TILES, 's268c', 5); assert len(c) == 1; write('sort/k04/s268c_tiles.tsv', c)
k = tiles(list(csv.DictReader(open('ciphertext_c172.tsv'), delimiter='\t')), CTL, 's172', 0); assert len(k) == 2
write('sort/k04/s172_tiles.tsv', k)
for name, lo, shift in (('c268d', 14, 13), ('c268c', 6, 5)):
    with open(f'sort/k04/{name}_passc.tsv', 'w') as o:
        o.write('passage\tpos\tsign_id\n')
        for r in c268:
            if int(r['line'][1:]) >= lo: o.write(f"L{int(r['line'][1:]) - shift:02d}\t{r['pos']}\t{r['sign']}\n")
from PIL import Image
ks = Image.open('images/keysheet_monluc1_ids.png').convert('RGB'); W, H = 136, 176
S = Image.new('RGB', (W * 2, H), 'white')
for j, k in enumerate(['K04', 'K12']):
    n = int(k[1:]) - 1; col, row = n % 8, n // 8
    S.paste(ks.crop((col * W, row * H, col * W + W, row * H + H)), (j * W, 0))
S.save('sort/k04/candidates.png'); print('sort/k04/candidates.png')
