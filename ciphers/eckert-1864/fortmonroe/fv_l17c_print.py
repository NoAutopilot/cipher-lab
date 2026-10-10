#!/usr/bin/env python3
"""FV-L17c (10 Oct 2026): fresh letters-only phrase grep (not the readers' phrases) for E622 E623 E624 over the cached print-check volumes
(OR ser. I/II, ORN, Butler Corr. III-V, O'Brien 1910, Plum). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E622': ['stop all bound for the Potomac', 'Chesapeake City to meet', 'escort the tows', 'tows down the bay', 'Van Vliet\'s list', 'three ferry-boats and three tugs',
          'ferry boats and three tugs', 'proceed at once to Fort Monroe and report to you', 'send a vessel into the bay', 'management of the fleet', 'charters by Captain Wise',
          'list of charters', 'chartered for the expedition'],
 'E623': ['correspondent of the World', 'Shore is in Baltimore', 'W. W. Shore', 'ordered out of this department', 'I want him caught', 'a man who knows him',
          'evidence against him', 'three days ago to arrest him', 'did not get the dispatch'],
 'E624': ['five miles from Bermuda', '5 miles from Bermuda', 'ready to move in the morning', 'Harrison\'s Landing to join', 'cavalry expedition crossing',
          'keep you posted', 'left General Butler\'s headquarters'],
}
texts = {os.path.basename(p)[:-12]: norm(gzip.open(p, 'rt', errors='ignore').read()) for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
