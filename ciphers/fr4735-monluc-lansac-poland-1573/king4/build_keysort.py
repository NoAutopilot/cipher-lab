#!/usr/bin/env python3
"""SORTER-KING (23 Oct 2026): key-rebuild sign-sorter for the c258 (f.133) look-alike pairs in king4/focus.tsv.
No fresh page crops: king4/strips/ (occurrence tiles) is untracked and regenerating it needs openapi.bnf.fr, which
this job's hosts exclude (Gallica has answered 403 since 20 Oct) -- and the "image-check" escalation step
(NOTES.md MONL-KING4 line ~2424) is already marked done (the 124-tile look-alike window re-read). The remaining
escalation step is "key-rebuild": the owner reviews the KEYSHEET's own candidate cells for the 17 K-id-vs-K-id
pairs focus.tsv disputes (20 distinct ids; the other 5 focus rows are word pairs or off-sheet shapes with no
keysheet cell, listed but not tiled). Cells are cut from images/keysheet_monluc1_ids.png with the same grid
build_tiles.py already uses (136x176 cells, 8 columns, i = int(k[1:]) - 1), one tile per distinct id, starting
in its own pile (blind: the pile name is the shape id, never a letter value or a decode guess). Writes
king4/sorter_pages/keysheet.png (page copy), king4/keysort_signs.tsv, king4/keysort_labels.tsv,
king4/keysort_focus.tsv. Run from the repo root: python3 ciphers/fr4735-monluc-lansac-poland-1573/king4/build_keysort.py
"""
import csv, re, os, shutil
from collections import defaultdict

D = 'ciphers/fr4735-monluc-lansac-poland-1573'
K = D + '/king4'
CW, CH, NC = 136, 176, 8

os.makedirs(K + '/sorter_pages', exist_ok=True)
open(K + '/sorter_pages/.gitignore', 'w').write('*\n!.gitignore\n')
shutil.copy(D + '/images/keysheet_monluc1_ids.png', K + '/sorter_pages/keysheet.png')

rows = [l.rstrip('\n').split('\t') for l in open(K + '/focus.tsv') if l.strip()]
kpairs, other = [], []
for sid, q in rows:
    m = re.search(r'which of (.+?), (.+?)\?$', q)
    a, b = m.group(1), m.group(2)
    (kpairs if a.startswith('K') and b.startswith('K') else other).append((sid, q, a, b))

by_id = defaultdict(list)   # id -> list of (partner, sid-as-position)
for sid, q, a, b in kpairs:
    pos = sid.replace('c258_', '').replace('_', '.', 1).replace('L0', 'L').replace('L', 'L0', 1) if False else sid
    m = re.match(r'c258_(L\d+)_(\d+)', sid)
    pos = f'{m.group(1)}.{m.group(2)}'
    by_id[a].append((b, pos)); by_id[b].append((a, pos))

ids = sorted(by_id, key=lambda s: int(s[1:]))

with open(K + '/keysort_signs.tsv', 'w', newline='') as o:
    w = csv.writer(o, delimiter='\t', lineterminator='\n')
    w.writerow(['sid', 'page', 'x', 'y', 'w', 'h'])
    for k in ids:
        i = int(k[1:]) - 1
        w.writerow([k, 'keysheet', (i % NC) * CW, (i // NC) * CH, CW, CH])

with open(K + '/keysort_labels.tsv', 'w', newline='') as o:
    w = csv.writer(o, delimiter='\t', lineterminator='\n')
    w.writerow(['sid', 'sign'])
    for k in ids:
        w.writerow([k, k])

with open(K + '/keysort_focus.tsv', 'w', newline='') as o:
    for k in ids:
        partners = defaultdict(list)
        for other_id, pos in by_id[k]:
            partners[other_id].append(pos)
        parts = [f'{oid} at {", ".join(sorted(ps))}' for oid, ps in sorted(partners.items())]
        q = f'{k}: a disputed alternative with ' + '; '.join(parts) + ' on f.133. Same drawn shape as its partner(s), or different?'
        o.write(f'{k}\t{q}\n')

print(f'ids {len(ids)}: {ids}')
print(f'K-id pairs {len(kpairs)}, other (word/off-sheet, not tiled) {len(other)}: {[r[0] for r in other]}')
