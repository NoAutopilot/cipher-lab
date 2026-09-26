#!/usr/bin/env python3
"""AX-4612TR2: write ax4612tr/settle.tsv (page, line, pos, A, B, settled, why) for every value-1-120
numeral disagreement the content-level realignment (realign.py) found, cross-referenced against
build_v2.py's SETTLEMENTS dict (the crops actually checked against images_wv2/crops_4612)."""
import csv, sys
sys.path.insert(0, 'ax4612tr')
from build_v2 import SETTLEMENTS

def is_numeral(tok):
    t = tok.lstrip('=').strip()
    return t[:1].isdigit()

rows_out = []
for page in ('p1', 'p2'):
    rows = list(csv.DictReader(open(f'ax4612tr/{page}_disagreements.tsv', encoding='utf-8'), delimiter='\t'))
    for r in rows:
        if r['kind'] != 'numeral':
            continue
        line = r['a_line'] or r['b_line']
        pos = r['a_pos'] or r['b_pos']
        key = (page, r['a_line'], int(r['a_pos'])) if r['a_line'] else None
        settled = SETTLEMENTS.get(key) if key else None
        if settled:
            value, why = settled
        else:
            value, why = '?', 'unsettled -- ambiguous or not checked against image within the box'
        rows_out.append({
            'page': page, 'line': line, 'pos': pos,
            'A': r['a_tok'] or '(none)', 'B': r['b_tok'] or '(none)',
            'settled': value, 'why': why,
        })

with open('ax4612tr/settle.tsv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['page', 'line', 'pos', 'A', 'B', 'settled', 'why'], delimiter='\t')
    w.writeheader()
    for r in rows_out:
        w.writerow(r)

n = len(rows_out)
settled_n = sum(1 for r in rows_out if r['settled'] != '?')
print(f'settle.tsv: {n} numeral disagreements, {settled_n} settled against the image, {n - settled_n} unsettled')
