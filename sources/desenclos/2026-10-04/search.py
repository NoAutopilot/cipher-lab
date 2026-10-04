#!/usr/bin/env python3
"""Grep Desenclos's open full texts (raw/ft/*.txt) for each target's terms (terms.tsv); write search-log.tsv.
DESENCLOS-PREMISE, 4 Oct 2026. Hits are listed with context; 'real' hits are judged by eye in README.md."""
import re, glob, csv
files = sorted(glob.glob('raw/ft/*.txt'))
out = csv.writer(open('search-log.tsv', 'w'), delimiter='\t', lineterminator='\n')
out.writerow(['target', 'searched_for', 'regex', 'files_searched', 'raw_matches', 'match_files', 'first_context'])
for t, rx, what in list(csv.reader(open('terms.tsv'), delimiter='\t'))[1:]:
    hits = []
    for f in files:
        txt = re.sub(r'\s+', ' ', open(f, errors='ignore').read())
        for m in re.finditer(rx, txt, flags=re.I):
            hits.append((f.split('/')[-1], txt[max(0, m.start()-80):m.end()+80]))
    out.writerow([t, what, rx, len(files), len(hits), ','.join(sorted({h[0] for h in hits})), hits[0][1] if hits else ''])
