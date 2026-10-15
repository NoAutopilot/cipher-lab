#!/usr/bin/env python3
"""MONL-ADH (15 Oct 2026): tiles for the value-blind sort of PREREG-MONL-ADH.md part 2 (addendum scope): the 14 c268 L11-L15 lead tokens
in the pairs of sort/adh/cells.txt, and the 7 c172 controls of PREREG-MONL-SORT. Band ids: c268c band L0n = c268 L(n+5) (regen_monll11.sh).
Writes sort/adh/{s268c,s172}_tiles.tsv (tools/lookalike_pass.py windows packet format), sort/adh/c268c_passc.tsv and
sort/adh/candidates.png (cells cut from images/keysheet_monluc1_ids.png, ids only; untracked). Run from the folder."""
import csv
from PIL import Image
PAIRS = {}
for ln in open('sort/adh/cells.txt'):
    if ln.strip() and not ln.startswith('#'):
        a, b = ln.split('\t')[0].split(',')
        PAIRS[a] = PAIRS[b] = f'{a},{b}'
PAIRS.update({'K14': 'K14,K17'})  # controls only (PREREG-MONL-SORT)
LEADS = {('L13', '10'), ('L15', '9'), ('L15', '12'), ('L15', '18'), ('L13', '7'), ('L13', '16'), ('L13', '20'), ('L13', '23'),
         ('L11', '14'), ('L11', '23'), ('L13', '14'), ('L15', '4'), ('L11', '12'), ('L13', '3')}
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
t = []
for ln, rs in by.items():
    for i, r in enumerate(rs):
        if (ln, r['pos']) in LEADS:
            bef, aft = ctx(rs, i)
            t.append(['s268c', f'L{int(ln[1:]) - 5:02d}', r['pos'], r['sign'], r['sign'], '', 'check', 'sort', PAIRS[r['sign']], bef, aft, '', ''])
assert len(t) == 14, len(t)
write('sort/adh/s268c_tiles.tsv', t)
with open('sort/adh/c268c_passc.tsv', 'w') as o:
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
write('sort/adh/s172_tiles.tsv', c)
ks = Image.open('images/keysheet_monluc1_ids.png').convert('RGB'); W, H = 136, 176
ids = ['K04', 'K12', 'K11', 'K62', 'K37', 'K43', 'K14', 'K17']
S = Image.new('RGB', (W * len(ids), H), 'white')
for j, k in enumerate(ids):
    n = int(k[1:]) - 1; col, row = n % 8, n // 8
    S.paste(ks.crop((col * W, row * H, col * W + W, row * H + H)), (j * W, 0))
S.save('sort/adh/candidates.png'); print('sort/adh/candidates.png')
