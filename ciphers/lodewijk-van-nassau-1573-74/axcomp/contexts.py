#!/usr/bin/env python3
"""AX-COMP: print every code > 120 of letter N with 5 aligned tokens either side (value[plain chunk]).
    python3 axcomp/contexts.py N > axcomp/contexts_N.txt"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, 'align_%s.tsv' % sys.argv[1]), encoding='utf-8'), delimiter='\t'))
for i, r in enumerate(rows):
    if r['kind'] == 'num' and int(r['value']) > 120:
        ctx = ' '.join('%s[%s]' % (x['value'] or x['raw'], x['plain_chunk']) for x in rows[max(0, i - 5):i + 6])
        print('%s\t%s\t%s' % (r['value'], r['cipher_line'], ctx))
