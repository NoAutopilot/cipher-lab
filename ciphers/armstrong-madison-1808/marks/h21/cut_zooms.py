#!/usr/bin/env python3
"""Campaign step H21 (28 Sept 2026): one 2x line zoom per HELD mark of marks/h18_inventory.tsv, cut from the witness
frame the holding reader used (w30 = M34-014-0030 page 1, w31/w32 = 0031/0032 pages 2-3, w33 = 0033 page 4), the pass
line number mapped through that witness's crop manifest (page 1: crops_0030 boxes 4.., the H18 sheets' own offset;
page 2: crops_003xL; page 3: crops_003xR; page 4: images/crops_h18/_p4/manifest.json from regen_sheets.py).
Writes images/crops_h21/<page>_<witness>_L<line>_<group>.jpg (untracked; images/ is at the 30 MB line -- rerun this
script to rebuild) and marks/h21/zooms.tsv listing crop, page, witness, line, group, held class.
"""
import csv, json, re
from pathlib import Path
from PIL import Image
T = Path(__file__).resolve().parents[2]; D = T/'images'; OUT = D/'crops_h21'; OUT.mkdir(exist_ok=True)
def boxes(d): return [e['box'] for e in json.load(open(D/d/'manifest.json'))['iiif_lines']]
JOB = {('p1','w30'): ('M34-014-0030.jpg', 40, 2096, boxes('crops_0030')[3:]),
       ('p2','w31'): ('M34-014-0031.jpg', 40, 1990, boxes('crops_0031L')), ('p3','w31'): ('M34-014-0031.jpg', 1880, 3968, boxes('crops_0031R')),
       ('p2','w32'): ('M34-014-0032.jpg', 40, 1990, boxes('crops_0032L')), ('p3','w32'): ('M34-014-0032.jpg', 1880, 3968, boxes('crops_0032R')),
       ('p4','w33'): ('M34-014-0033.jpg', 0, 1944, boxes('crops_h18/_p4'))}
frames = {}
rows = []
for r in csv.DictReader(open(T/'marks/h18_inventory.tsv'), delimiter='\t'):
    if r['status'] != 'held': continue
    wits = sorted(set(re.findall(r'(w3\d)/', r['details'])))
    lines = [int(x) for x in r['line'].split('/')]
    for wit in wits:
        f, x0, x1, bx = JOB[(r['page'], wit)]
        im = frames.setdefault(f, Image.open(D/f)); H = im.size[1]
        for ln in lines:
            if ln-1 >= len(bx): continue
            b = bx[ln-1]
            c = im.crop((x0, max(0, b[1]-60), x1, min(H, b[3]+25)))
            c = c.resize((c.size[0]*2, c.size[1]*2), Image.LANCZOS)
            if c.size[0] > 2400: c = c.resize((2400, int(c.size[1]*2400/c.size[0])), Image.LANCZOS)
            fn = f"{r['page']}_{wit}_L{ln:02d}_{r['group']}.jpg"; c.save(OUT/fn, quality=90)
            rows.append([fn, r['page'], wit, ln, r['group'], r['class'], r['under_digit']])
with open(T/'marks/h21/zooms.tsv', 'w') as f:
    f.write('crop\tpage\twitness\tline\tgroup\theld_class\theld_under_digit\n')
    for row in rows: f.write('\t'.join(map(str, row))+'\n')
print(len(rows), 'zooms written to', OUT)
