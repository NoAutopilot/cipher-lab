#!/usr/bin/env python3
"""Campaign step H21 (28 Sept 2026): merge the second reader's zoom verdicts (marks/h21/reader_p14.tsv, reader_p23.tsv)
with the H18 held marks. A held mark whose zoom verdict is MARK in the same class is written as a second source into
marks/h18_passes/<page>_<witness>_C.tsv (the H18 reconciler then counts it accepted); MARK in a different class is
kept held and noted; NONE drops the mark (marks/h21/drops.tsv, honoured by h18_inventory.py); UNSURE keeps it held.
Writes marks/h21/verdicts.tsv, then the caller re-runs marks/h18_inventory.py."""
import csv, collections
from pathlib import Path
H = Path(__file__).resolve().parent; M = H.parent
zooms = list(csv.DictReader(open(H/'zooms.tsv'), delimiter='\t'))
held = {(z['crop']): z for z in zooms}
reads = []
for f in ('reader_p14.tsv', 'reader_p23.tsv'):
    if (H/f).exists(): reads += list(csv.DictReader(open(H/f), delimiter='\t'))
byc = collections.defaultdict(list)
for r in reads: byc[r['crop'].strip()].append(r)
verdicts = []; passfiles = collections.defaultdict(list); drops = []
# a held mark may have two zooms (two lines or two witnesses): promoted if ANY zoom says MARK in the held class,
# dropped only if EVERY zoom says NONE, else held
bykey = collections.defaultdict(list)
for z in zooms: bykey[(z['page'], z['group'], z['held_class'])].append(z)
for key, zs in bykey.items():
    page, group, cls = key
    rs = [r for z in zs for r in byc.get(z['crop'], [])]
    vs = [r['verdict'].strip().upper() for r in rs]
    same = [r for r in rs if r['verdict'].strip().upper() == 'MARK' and r['class'].strip().upper()[:4] == cls]
    other = [r for r in rs if r['verdict'].strip().upper() == 'MARK' and r['class'].strip().upper()[:4] != cls]
    if same:
        st = 'promoted'; r = same[0]; z = [z for z in zs if z['crop'] == r['crop']][0]
        passfiles[(page, z['witness'])].append((z['line'], group, cls, r['what_it_is'], r['confidence']))
    elif other: st = 'held (mark seen, other class: %s)' % other[0]['class']
    elif vs and all(v == 'NONE' for v in vs): st = 'dropped'; drops.append((page, group, cls, rs[0]['what_it_is']))
    elif not rs: st = 'held (no zoom read)'
    else: st = 'held (unsure)'
    verdicts.append((page, group, cls, ' / '.join(z['line'] for z in zs), '; '.join(f"{r['verdict']}:{r['class']}:{r['under_digit']}:{r['what_it_is']} ({r['confidence']})" for r in rs), st))
with open(H/'verdicts.tsv', 'w') as f:
    f.write('page\tgroup\theld_class\tlines\tsecond_reader\tresult\n')
    for v in verdicts: f.write('\t'.join(v)+'\n')
with open(H/'drops.tsv', 'w') as f:
    f.write('page\tgroup\tclass\tzoom_reading\n')
    for d in drops: f.write('\t'.join(d)+'\n')
for (page, wit), items in passfiles.items():
    with open(M/'h18_passes'/f'{page}_{wit}_C.tsv', 'w') as f:
        f.write('# H21 second reader (zoom per group), promoted marks only; format as the H18 passes\n')
        for ln, g, cls, det, conf in items: f.write(f'line{ln}\tZOOM\t{g}:{cls}:{det} [H21 zoom]\t{conf}\n')
c = collections.Counter(v[5].split(' ')[0] for v in verdicts)
print('held marks judged:', len(verdicts), dict(c)); print('pass files written:', [f'{p}_{w}_C.tsv' for p, w in passfiles])
