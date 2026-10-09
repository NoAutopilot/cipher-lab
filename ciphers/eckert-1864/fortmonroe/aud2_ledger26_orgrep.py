#!/usr/bin/env python3
"""AUD2-LEDGER-26 (9 Oct 2026): grep the djvu text of OR ser. I vol. 36 pt 3 (IA warofrebellion363unit) and Plum 1882 vol. 2
(IA militarytelegraph02plumrich) for E318's names and clauses, with the page from the nearest OCR running heads (not seen on the image).
Usage: aud2_ledger26_orgrep.py DIR  (DIR holds the two *_djvu.txt.gz files fetched by tools/print_check.py --cache DIR).
A miss is a search result (rule 10), not a novelty verdict."""
import gzip, os, re, sys
D = sys.argv[1]
def load(i): return ' '.join(gzip.open(os.path.join(D, i + '_djvu.txt.gz'), 'rt', errors='replace').read().split())
for ident, terms in [('warofrebellion363unit', ['General Halleck has given his opinion', 'telegraph route most easily', 'On consulting General Carr',
                      'Butler favors crossing', 'Embree', 'Logue', 'Glazier', 'Cowan', 'Bickford', 'circuit twice', 'regiment could', 'Gloucester route']),
                     ('militarytelegraph02plumrich', ['Embree', 'Logue', 'Glazier', 'Cowan', 'Bickford', 'Homan', 'Collings', 'Bliss', 'Mcintosh'])]:
    t = load(ident)
    heads = sorted([(m.start(), m.group(1)) for m in re.finditer(r'(\d{3}) (?:OPERATIONS IN|CORRESPONDENCE)', t)] +
                   [(m.start(), m.group(1)) for m in re.finditer(r'UNION\. (\d{3})', t)])
    for w in terms:
        ms = [m.start() for m in re.finditer(re.escape(w), t, re.I)]
        print(ident, '|', w, '|', len(ms))
        for i in ms[:3]:
            pg = ([h for h in heads if h[0] < i] or [(0, '?')])[-1][1]
            print('    head<', pg, '::', t[max(0, i - 160):i + 260])
