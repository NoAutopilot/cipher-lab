#!/usr/bin/env python3
"""COS-1167B (10 Oct 2026): fill copy_words, groups_per_word and flag in align/cos1167_spans.tsv from align/cos1167b_copy.tsv
(copy words = whitespace tokens of the span's copy text, sigla one word each) against COS-1167's reference range 0.615-1.053
(align/cos1167_ref.py, mis-cut span excluded). Usage: python3 align/cos1167b_fill.py [--check]  (run from the folder; --check
exits 1 if the committed spans table differs from what this script writes)."""
import csv, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LO, HI = 0.615, 1.053
SPANS = os.path.join(HERE, 'cos1167_spans.tsv')
copy = {r['span']: r for r in csv.DictReader(open(os.path.join(HERE, 'cos1167b_copy.tsv')), delimiter='\t')}
rows = list(csv.reader(open(SPANS), delimiter='\t'))
head = rows[0]
ig, iw, ir, iflag = 5, 6, 7, 8
out = io.StringIO(); w = csv.writer(out, delimiter='\t', lineterminator='\n'); w.writerow(head)
for r in rows[1:]:
    s = r[0]
    if s in copy:
        n = len(list(copy[s].values())[2].split()); g = int(r[ig])
        r[iw] = str(n); q = g / n; r[ir] = f'{q:.3f}'
        if s == 'a1':
            r[iflag] = 'not bounded: P1 cipher tail uncounted; copy words are an upper bound'
        else:
            r[iflag] = 'in range' if LO <= q <= HI else ('above range' if q > HI else 'below range')
    w.writerow(r)
new = out.getvalue()
if '--check' in sys.argv:
    sys.exit(0 if open(SPANS).read() == new else 1)
open(SPANS, 'w').write(new); print(new)
