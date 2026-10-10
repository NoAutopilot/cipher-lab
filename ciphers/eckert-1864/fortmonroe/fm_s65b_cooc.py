#!/usr/bin/env python3
"""FM-S65B (10 Oct 2026): loose co-occurrence (all terms within 800 chars) over the cached OR/ORN djvu texts for the filing candidates. Hits are leads, read in context (rule 10)."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = {'5892/1': ['monohansett'], '5896/0': ['retained no copy'], '5908/0': ['radford', 'torpedo', 'ironsides'], '5910/1': ['cammann'], '5914/2': ['gordon', 'commission', 'cashier'],
     '5936/2': ['ponchos', 'canby'], '5941/2': ['goldsboro', 'old point', 'wednesday'], '5941/2b': ['sherman', 'city point', 'newbern', 'old point']}
for p in sorted(glob.glob(D + '/*_djvu.txt.gz')):
    t = re.sub(r'\s+', ' ', gzip.open(p, 'rt', errors='ignore').read().lower()); v = os.path.basename(p)[:-12]
    for k, terms in Q.items():
        first = terms[0]; n = 0
        for m in re.finditer(re.escape(first), t):
            w = t[max(0, m.start() - 800): m.start() + 800]
            if all(x in w for x in terms[1:]):
                n += 1
                if n <= 2: print(k, v, '|', t[max(0, m.start() - 150): m.start() + 250])
        if n > 2: print(k, v, f'... {n} windows')
