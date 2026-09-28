#!/usr/bin/env python3
"""Known-answer check of the printed Bowdoin-Temple (pt. II) bracketed decipherments against WE028
(Monroe's cypher, tools/data/uscodes-1800/WE028.tsv), and write the groups as a screen.py input.
Usage: we028_check.py  (reads bt_pairs.tsv, writes bt_we028_check.tsv and bt_groups.tsv)"""
import csv, re, pathlib
H = pathlib.Path(__file__).resolve().parent
R = H.parents[2]
we = {}
for row in csv.DictReader(open(R/'tools/data/uscodes-1800/WE028.tsv'), delimiter='\t'):
    we[int(row['value'])] = row['plaintext']
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
out = open(H/'bt_we028_check.tsv', 'w'); grp = open(H/'bt_groups.tsv', 'w')
out.write('line\tgroups\tprinted_gloss\twe028_reading\tverdict\n')
n = ok = 0
for row in csv.DictReader(open(H/'bt_pairs.tsv'), delimiter='\t'):
    gs = [int(g) for g in row['groups'].split()]
    rd = ''.join(we.get(g, '?') for g in gs)
    a, b = norm(rd), norm(row['gloss'].split('|')[0])
    # agreement: share of gloss letters covered in order (OCR noise tolerated)
    import difflib
    r = difflib.SequenceMatcher(None, a, b).ratio()
    v = 'MATCH' if r >= 0.75 else ('PART' if r >= 0.5 else 'MISS')
    n += 1; ok += v == 'MATCH'
    out.write(f"{row['line']}\t{row['groups']}\t{row['gloss']}\t{rd}\t{v} {r:.2f}\n")
    grp.write(f"bt{row['line']}\t{row['groups']}\n")
print(f'{ok}/{n} bracketed runs read MATCH under WE028')
