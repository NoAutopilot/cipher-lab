#!/usr/bin/env python3
"""RIK-COVER: grep R4120 cover names in text files; one row per hit with context.
usage: cover_grep.py NAMES.tsv OUT.tsv LABEL=FILE [LABEL=FILE ...]
Hyphen line breaks are joined; match is case-insensitive on word starts."""
import re, sys, csv
names = [r for r in csv.reader((l for l in open(sys.argv[1], encoding='utf-8') if not l.startswith('#')), delimiter='\t')][1:]
out = csv.writer(open(sys.argv[2], 'w', newline='', encoding='utf-8'), delimiter='\t')
out.writerow(['source', 'line', 'name', 'kind', 'slot', 'match', 'context'])
tot = {}
for spec in sys.argv[3:]:
    label, path = spec.split('=', 1)
    txt = open(path, encoding='utf-8', errors='replace').read()
    txt = re.sub(r'-\n\s*', '', txt)
    lines = txt.split('\n')
    for n, ln in enumerate(lines, 1):
        for name, pat, kind, slot in names:
            for m in re.finditer(r'\b' + pat + r'\w*', ln, re.I):
                ctx = ' '.join(lines[max(0, n-2):n+1])[:240]
                out.writerow([label, n, name, kind, slot, m.group(0), ctx])
                tot[(label, name)] = tot.get((label, name), 0) + 1
for k, v in sorted(tot.items()):
    print(k, v)
