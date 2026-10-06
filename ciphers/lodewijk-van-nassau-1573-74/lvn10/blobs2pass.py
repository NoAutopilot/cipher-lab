#!/usr/bin/env python3
"""R14-LVN10C (6 Oct 2026): turn a per-tile read file (reads_<P>.tsv: label<TAB>reading, the reader's output for the
lvn10/tokcrops.py contact sheets) into lvn10/pass<P>.tsv in page order (blobs.tsv page_order), one numeral per row,
'|' for a word, the reader's '?' kept. A tile the reader skipped yields nothing. Usage: blobs2pass.py A6 (needs blobs.tsv
and reads_A6.tsv beside this script). Offline."""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__)); P = sys.argv[1]
bl = {r['label']: r for r in csv.DictReader(open(os.path.join(H, 'blobs.tsv')), delimiter='\t')}
rd = {}
for line in open(os.path.join(H, 'reads_%s.tsv' % P)):
    f = line.rstrip('\n').split('\t')
    if len(f) < 2 or f[0] not in bl: continue
    rd[f[0]] = f[1]
rows = []
for lab, r in sorted(bl.items(), key=lambda kv: int(kv[1]['page_order'])):
    for t in [x for x in rd.get(lab, '').replace(',', ' ').split() if x != '-']:
        rows.append(('L%02d' % int(r['phys']), lab, t))
with open(os.path.join(H, 'pass%s.tsv' % P), 'w') as f:
    f.write('line\tidx\ttoken\n')
    for i, (L, lab, t) in enumerate(rows): f.write(f'{L}\t{i + 1}\t{t}\n')
print(P, len(rd), 'tiles read of', len(bl), ';', sum(1 for x in rows if x[2] != '|'), 'numeral tokens')
