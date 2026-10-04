#!/usr/bin/env python3
"""Turn moves the owner made on earlier-pick tiles (--refs, green check) on the no.87 sorter into rows of
../owner-sort-2026-10-04/corrections.tsv (owner, 4 Oct 2026: "give me a way to fix, I might make mistakes").

    python3 ciphers/nevers-birago-fr3251-1572/sorter/no87/ref_corrections.py DB_DIR

DB_DIR is the ArtifactData export of the no.87 page (moves/<sid>.json). Each move whose sid is in refs.tsv becomes one
row: owner_sid (refs.tsv), atlas sid, from = the pile it was shown in, to = the pile placed in (OUT/ASIDE -> UNPLACED,
BAD-CUT kept). Rows already present (same atlas sid and to) are not repeated. Prints what it added."""
import csv, json, sys, time
from pathlib import Path
H = Path(__file__).resolve().parent
CORR = H.parent / 'owner-sort-2026-10-04' / 'corrections.tsv'
if len(sys.argv) != 2: sys.exit(__doc__)
refs = {r['sid']: r for r in csv.DictReader(open(H / 'refs.tsv'), delimiter='\t')}
have = set()
if CORR.exists():
    have = {(r['atlas_sid'], r['to_pile']) for r in csv.DictReader(open(CORR), delimiter='\t')}
else:
    CORR.write_text('date_utc\towner_sid\tatlas_sid\tfrom_pile\tto_pile\tsource\n')
now, added = time.strftime('%Y-%m-%d %H:%M', time.gmtime()), []
for f in sorted((Path(sys.argv[1]) / 'moves').glob('*.json')):
    d = json.load(open(f)); d = d.get('data', d); sid = d.get('sid', f.stem); to = d.get('to')
    if sid not in refs or not to: continue
    to = 'UNPLACED' if to in ('OUT', 'ASIDE') else to
    if to == refs[sid]['sign'] or (sid, to) in have: continue
    added.append([now, refs[sid]['owner_sid'], sid, refs[sid]['sign'], to, 'owner, no.87 sorter (earlier pick corrected)'])
with open(CORR, 'a') as fh:
    for r in added: fh.write('\t'.join(r) + '\n')
print('added %d correction(s) to %s' % (len(added), CORR)); [print(' ', *r[1:5]) for r in added]
