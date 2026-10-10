#!/usr/bin/env python3
"""LS-R7 (8 Oct 2026): grep verbatim ledger phrases of E66-E74 in the cached Official Records djvu texts
(sources/ia-fulltext/print-check/, nothing added). Letters only, spaces removed, so line breaks and hyphens do not matter.
A miss is a search result for the log, not a verdict (rule 10)."""
import gzip, re, sys, os
D = os.path.join(os.path.dirname(__file__), '..', '..', 'sources', 'ia-fulltext', 'print-check')
# OR-CACHE 10 Oct 2026: 'warofrebellion431unit' below is OR I/47 pt 2 (title page), NOT I/43 pt 1 (that is warofrebellion431unit_0, cached 10 Oct 2026); list left as run.
VOLS = ['warofrebellion33unit', 'warofrebellion362unit', 'warofrebellion372unit', 'warofrebellion431unit',
        'warofrebellion432unit', 'warofrebellion452unit']
PH = {
 'E66': ['has called on you for', 'should have full coal and water for', 'dispatch them unless', 'take plug promise'],
 'E67': ['everything is being done', 'with utmost vigor', 'to assist in fitting out the', 'let me know'],
 'E68': ['will please see surgeon ferry', 'send its substance by', 'under adequate', 'take care he does not escape'],
 'E70': ['four hundred rounds assorted', 'there must be no delay', 'with implements and', 'issue immediately to'],
 'N2-BN/E71': ['will be completed ready for use today', 'being placed on each', 'the additional wagons'],
 'E72': ['will you see that', 'on their arrival at your', 'all facilities for a rapid march'],
 'E73': ['to make all important signals by adding a number', 'subtracting the same number from signal numbers received'],
 'E74': ['was an enormous blunder', 'it cannot happen again', 'until too late'],
}
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
texts = {}
for v in VOLS:
    p = os.path.join(D, v + '_djvu.txt.gz')
    if os.path.exists(p):
        texts[v] = norm(gzip.open(p, 'rt', errors='ignore').read())
    else:
        print('missing', v, file=sys.stderr)
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
