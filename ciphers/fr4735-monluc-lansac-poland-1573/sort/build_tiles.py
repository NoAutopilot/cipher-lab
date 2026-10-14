#!/usr/bin/env python3
"""MONL-SORT (14 Oct 2026): tiles for a value-blind sort of every K12/K14/K34 token (c268 L01-L05, c172 L02-L04)
into the key-sheet cell pairs K04|K12, K14|K17, K34|K53, plus the c172 K04 tokens as in-set controls.
Writes sort/c268_tiles.tsv, sort/c172_tiles.tsv (tools/lookalike_pass.py windows packet format) and sort/candidates.png
(cells cut from images/keysheet_monluc1_ids.png, ids only). Run from the folder."""
import csv
from PIL import Image
PAIRS = {'K12': 'K04,K12', 'K04': 'K04,K12', 'K14': 'K14,K17', 'K34': 'K34,K53'}
HDR = 'run\tpassage\tpos\tpassC\tA\tB\tstatus\twhy\tcandidates\tbefore\tafter\tnoteA\tnoteB\n'
def tiles(src, run, signs, out):
    rows = list(csv.DictReader(open(src), delimiter='\t'))
    by = {}
    for r in rows:
        by.setdefault(r['line'], []).append(r)
    n = 0
    with open(out, 'w') as o:
        o.write(HDR)
        for ln, rs in by.items():
            for i, r in enumerate(rs):
                if r['sign'] not in signs:
                    continue
                bef = ' '.join(x['sign'] for x in rs[max(0, i - 3):i]); aft = ' '.join(x['sign'] for x in rs[i + 1:i + 4])
                o.write(f"{run}\t{ln}\t{r['pos']}\t{r['sign']}\t{r['sign']}\t\tcheck\tsort\t{PAIRS[r['sign']]}\t{bef}\t{aft}\t\t\n"); n += 1
    print(out, n)
tiles('ciphertext_c268.tsv', 's268', {'K12', 'K14', 'K34'}, 'sort/c268_tiles.tsv')
tiles('ciphertext_c172.tsv', 's172', {'K12', 'K14', 'K34', 'K04'}, 'sort/c172_tiles.tsv')
ks = Image.open('images/keysheet_monluc1_ids.png').convert('RGB'); W, H = 136, 176
ids = ['K04', 'K12', 'K14', 'K17', 'K34', 'K53']
S = Image.new('RGB', (W * 6, H), 'white')
for j, k in enumerate(ids):
    n = int(k[1:]) - 1; c, r = n % 8, n // 8
    S.paste(ks.crop((c * W, r * H, c * W + W, r * H + H)), (j * W, 0))
S.save('sort/candidates.png'); print('sort/candidates.png')
