#!/usr/bin/env python3
"""FM-S65B (10 Oct 2026): letters-only phrase grep of the FM-S65B rows' readable phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5892/1': ['Monohansett will leave for Monroe', 'Monohansett will leave', 'wishes you to meet him on arrival', 'Major Eckert wishes'],
 'F2 5893/1': ['Did the Bruno come with the Bolivia', 'Bruno come with the Bolivia'],
 'F3 5896/0': ['I have sent the letter referred to in our dispatch', 'by the hands of a staff officer to be delivered to you', 'I retained no copy', 'letter referred to in my dispatch'],
 'F4 5896/1': ['I arrived here today with despatches for you from General Sherman', 'will be in Annapolis tomorrow morning', 'despatches for you from General Sherman', 'Jay F. Anderson'],
 'F5 5908/0': ['No torpedoes on hand', 'have telegraphed the Bureau of Ordnance for', 'will forward immediately on receipt', 'Radford New Ironsides', 'New Ironsides torpedoes'],
 'F6 5910/1': ['Sell gold to fall', 'Camman and Company', 'Cammann and Company', 'he is naval officer'],
 'F7 5914/2': ['if Gordon\'s commission has not yet adjourned', 'Gordons commission has not yet adjourned', 'to call before it the Cashier', 'Cashier of the National Bank'],
 'F9 5936/2': ['ponchos are not on hand at present', 'ponchos are not on hand', 'Canby is shoed'],
 'F10 5941/2': ['I am going to see Grant at City Point', 'expect to go back to Goldsboro by way of Newbern', 'go back to Goldsboro by Newbern', 'from Old Point on Wednesday', 'Old Point on Wednesday'],
 'F11 5942/1': ['furlough Adams is hampered'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
