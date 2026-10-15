#!/usr/bin/env python3
"""MONL-VB (15 Oct 2026): tiles for a value-blind sort of the c268 L06-L10 K04/K12/K14/K34 tokens into the cell pairs K04|K12,
K14|K17, K34|K53 (MONL-C268B's recurring contradictions), the c268 L04:6/L04:8 K12 tokens into K12|K22 (MONL-EYE's lead), and the 7
c172 controls of PREREG-MONL-SORT (4 K04, 3 gloss-confirmed K14). L01-L05 K12/K14/K34 tokens were sorted by MONL-SORT and are skipped.
Writes sort/vb/{s268b,s268a,s172}_tiles.tsv (tools/lookalike_pass.py windows packet format), sort/vb/c268b_passc.tsv (L06-L10 renumbered
to the regen_monlc268b.sh band ids L01-L05) and sort/vb/candidates.png (cells cut from images/keysheet_monluc1_ids.png, ids only;
untracked). Run from the folder: python3 sort/vb/build_vb.py"""
import csv
from PIL import Image
PAIRS = {'K12': 'K04,K12', 'K04': 'K04,K12', 'K14': 'K14,K17', 'K17': 'K14,K17', 'K34': 'K34,K53', 'K53': 'K34,K53'}
HDR = 'run\tpassage\tpos\tpassC\tA\tB\tstatus\twhy\tcandidates\tbefore\tafter\tnoteA\tnoteB\n'
def ctx(rs, i):
    return ' '.join(x['sign'] for x in rs[max(0, i - 3):i]), ' '.join(x['sign'] for x in rs[i + 1:i + 4])
def write(out, rows):
    with open(out, 'w') as o:
        o.write(HDR)
        for r in rows: o.write('\t'.join(r) + '\n')
    print(out, len(rows))
c268 = list(csv.DictReader(open('ciphertext_c268.tsv'), delimiter='\t'))
by = {}
for r in c268: by.setdefault(r['line'], []).append(r)
b, a = [], []
for ln, rs in by.items():
    n = int(ln[1:])
    for i, r in enumerate(rs):
        bef, aft = ctx(rs, i)
        if n >= 6 and r['sign'] in PAIRS:
            b.append(['s268b', f'L{n - 5:02d}', r['pos'], r['sign'], r['sign'], '', 'check', 'sort', PAIRS[r['sign']], bef, aft, '', ''])
        if ln == 'L04' and r['pos'] in ('6', '8'):
            a.append(['s268a', ln, r['pos'], r['sign'], r['sign'], '', 'check', 'sort', 'K12,K22', bef, aft, '', ''])
write('sort/vb/s268b_tiles.tsv', b); write('sort/vb/s268a_tiles.tsv', a)
with open('sort/vb/c268b_passc.tsv', 'w') as o:
    o.write('passage\tpos\tsign_id\n')
    for r in c268:
        if int(r['line'][1:]) >= 6: o.write(f"L{int(r['line'][1:]) - 5:02d}\t{r['pos']}\t{r['sign']}\n")
CTL = {('L03', '26'), ('L03', '52'), ('L04', '13'), ('L04', '19'), ('L02', '48'), ('L02', '54'), ('L03', '40')}
c172 = list(csv.DictReader(open('ciphertext_c172.tsv'), delimiter='\t'))
by = {}
for r in c172: by.setdefault(r['line'], []).append(r)
c = []
for ln, rs in by.items():
    for i, r in enumerate(rs):
        if (ln, r['pos']) in CTL:
            bef, aft = ctx(rs, i)
            c.append(['s172', ln, r['pos'], r['sign'], r['sign'], '', 'check', 'sort', PAIRS[r['sign']], bef, aft, '', ''])
write('sort/vb/s172_tiles.tsv', c)
ks = Image.open('images/keysheet_monluc1_ids.png').convert('RGB'); W, H = 136, 176
ids = ['K04', 'K12', 'K14', 'K17', 'K22', 'K34', 'K53']
S = Image.new('RGB', (W * len(ids), H), 'white')
for j, k in enumerate(ids):
    n = int(k[1:]) - 1; col, row = n % 8, n // 8
    S.paste(ks.crop((col * W, row * H, col * W + W, row * H + H)), (j * W, 0))
S.save('sort/vb/candidates.png'); print('sort/vb/candidates.png')
