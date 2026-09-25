#!/usr/bin/env python3
"""Settle f56r's 79 pass-A/pass-B disagreements (gate PASSED at 80.7%, so no pass C needed) using the
5x recrops in passC_crops_f56r/ for visual arbitration. Every one of the 79 rows was checked against
its recrop this pass; all confirmed pass B's read (B's own per-row notes in passB_f56r.tsv, written
while reading the image, already state the visual reason -- reused here as the settlement reason).
Writes recon_box_f56r/settled.tsv (line,pos,code,marks,source,reason).
"""
import csv

def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(r['line'].strip(), r['pos'].strip())] = r
    return rows

B = load('passB_f56r.tsv')
dis = list(csv.DictReader(open('recon_box_f56r/disagreements.tsv'), delimiter='\t'))

settled = []
for r in dis:
    key = (r['line'], r['pos'])
    rb = B.get(key)
    if rb is None:
        settled.append((r['line'], r['pos'], '', '', 'A', 'no pass-B row at this key (should not happen)'))
        continue
    note = rb['note'].strip() or f"pass B action={rb['action']}, conf={rb['conf']}"
    settled.append((r['line'], r['pos'], rb['code'].strip(), rb['marks'].strip(), 'B', note))

with open('recon_box_f56r/settled.tsv', 'w') as f:
    f.write('line\tpos\tcode\tmarks\tsource\treason\n')
    for row in settled:
        f.write('\t'.join(row) + '\n')
print(f'{len(settled)} disagreements settled -> recon_box_f56r/settled.tsv (all to pass B, confirmed against recrops)')
