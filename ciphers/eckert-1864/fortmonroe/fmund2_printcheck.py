#!/usr/bin/env python3
"""FM-UND2 (10 Oct 2026): letters-only phrase grep (same cache and norm as fmund_printcheck.py) for the E622 head and 5658/0 telegram 2. A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E622 head': ['Rucker will send an officer in a steamer down the Potomac', 'stop all vessels first despatched', 'you should send a vessel in to the bay to stop all bound for the Potomac', 'change their destination to Fortress Monroe', 'Van Vliet\'s list is not yet received', 'have already orders for Fortress Monroe', 'Captain Wise has gone to New York', 'to join you at Fortress Monroe and assist you in the management of the fleet', 'Highland Light', 'Key Port', 'Tallaca', 'steam tugs are on their way to you', 'Briggs Chief Quartermaster', 'vessels chartered for the expedition', 'Matilda George Weems', 'ferry boats and tugs are on their way'],
 'tel2 5658/0': ['I left General Butler\'s headquarters', 'miles from Bermuda landing', 'all quiet and ready to move in the morning', 'crossing at Harrison\'s landing to join us', 'I will start tomorrow all working fine', 'will endeavor to keep you posted', 'Harrison\'s Landing to join us', 'all working fine'],
}
texts = {os.path.basename(p)[:-12]: norm(gzip.open(p, 'rt', errors='ignore').read()) for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        print(e, '|', ph, '|', ','.join(v for v, t in texts.items() if norm(ph) in t) or 'none')
