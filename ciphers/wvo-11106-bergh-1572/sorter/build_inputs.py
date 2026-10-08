#!/usr/bin/env python3
"""GLY-11106 (8 Oct 2026): sign-sorter inputs for WVO 11106 p.2 from the glyph atlas (atlas/) and the reconciled
transcription. Writes sorter/labels.tsv (sid, sign, family, cluster), sorter/focus.tsv (box sid, question) and
sorter/cipher_lines.tsv. A box's pile is the reconciled label of the position atlas/map_tx.py matched it to; a box
carrying two joined signs goes to pile 'joined' (the person cuts or names it), an unmatched box to its shape cluster's
majority pile when that cluster's firm matches give one label >= 50% and >= 3 times (family 'shape-guess'), else to
'unmatched', a
fragment (dot, descender piece) to 'fragment'. Each tx/focus.tsv question (line:pos) points at the box matched to that
position; a position with no box of its own is listed in sorter/focus_unplaced.tsv. Run from anywhere."""
import csv
from pathlib import Path
here = Path(__file__).resolve().parent; root = here.parent
cl = {r['id']: r['cluster'] for r in csv.DictReader(open(root / 'atlas/clusters.tsv'), delimiter='\t') if r['kind'] == 'sign'}
bm = list(csv.DictReader(open(root / 'atlas/boxmap.tsv'), delimiter='\t'))
fam = lambda s: 'digit' if s[:1].isdigit() else ('letter' if s[:1].isalpha() else 'other')
from collections import Counter, defaultdict
maj = defaultdict(Counter)
for r in bm:
    if r['firm'] == '1' and r['kind'] == 'cipher': maj[cl.get(r['sid'])][r['label']] += 1
def guess(c):
    if not maj[c]: return None
    l, n = maj[c].most_common(1)[0]
    return l if n >= 3 and n / sum(maj[c].values()) >= 0.5 else None
lab, where = [], {}
for r in bm:
    if r['kind'] == 'fragment': s, f = 'fragment', 'other'
    elif not r['pos']:
        g = guess(cl.get(r['sid'])); s, f = (g, 'shape-guess') if g else ('unmatched', 'other')
    elif r['joined'] == '1': s, f = 'joined', 'other'
    elif r['kind'] == 'struck': s, f = r['label'], 'struck'
    else: s, f = r['label'], fam(r['label'])
    lab.append((r['sid'], s, f, cl.get(r['sid'], '')))
    for p in r['pos'].split('+'):
        if p: where.setdefault(f"{r['line']}:{p}", (r['sid'], r['joined'] == '1'))
with open(here / 'labels.tsv', 'w') as o:
    o.write('sid\tsign\tfamily\tcluster\n'); o.writelines('\t'.join(x) + '\n' for x in lab)
foc, unpl = [], []
for q in csv.DictReader(open(root / 'tx/focus.tsv'), delimiter='\t'):
    hit = where.get(q['sid']); text = q['question'].split(' (crop')[0]
    if hit: foc.append((hit[0], f"{q['sid']}: {text}" + (' (box holds two signs: cut it first)' if hit[1] else '')))
    else: unpl.append((q['sid'], text))
with open(here / 'focus.tsv', 'w') as o:
    o.write('sid\tquestion\n'); o.writelines(f'{a}\t{b}\n' for a, b in foc)
with open(here / 'focus_unplaced.tsv', 'w') as o:
    o.write('tx_sid\tquestion\n'); o.writelines(f'{a}\t{b}\n' for a, b in unpl)
with open(here / 'cipher_lines.tsv', 'w') as o:
    o.write('page\n'); o.writelines(f'L{i:02d}\n' for i in range(1, 23))
print(f'{len(lab)} tiles, {len(foc)} focus tiles, {len(unpl)} focus positions without a box of their own')
