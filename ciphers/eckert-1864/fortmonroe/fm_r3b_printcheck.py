#!/usr/bin/env python3
"""FM-R3b (9 Oct 2026): letters-only phrase grep of the FM-R3b entries' decoded phrases AND rare names/numbers in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5811/2': ['H Livingston', 'Louisa Moore', 'Louisa Moore Idaho', 'Weybosset', 'Montauk and Beaufort', 'Sedgwick Massachusetts'],
 'F3 5747/1': ['send up all ferry boats', 'ferry boats immediately', 'lumber to Fort Powhatan', 'lumber to Fort Powhatan'],
 'F4 5823/2': ['Barns', 'Charles McCormick medical director', 'taken the', 'B Deford', 'Baltic'],
 'F5 5701/1': ['Captain Farquhar', 'Farquhar report to', 'Farquhar chief engineer', 'Farquhar ordered to report to General Smith'],
 'F6 5626/0': ['Longstreet at Charlottesville', 'Longstreet Charlottesville 5000', 'John I Davenport', 'Davenport our man', 'our man reports Longstreet'],
 'F7 5748/0': ['mail boats to Charles City', 'Charles City landing', 'send the mail boats', 'H B Blood'],
 'F8 5808/1': ['D Stinson', 'Ninth Vermont will leave', 'Captain Stinson', 'William L James', 'Perit'],
 'F9 5814/1': ['torpedoes invented by Mr Woods', 'invented by Mr Woods', 'Bureau of Ordnance torpedoes', 'Woods torpedoes'],
 'F10 5833/0': ['Pocotaligo bridge been destroyed', 'Press despatch New York Herald', 'Foster had not communicated with General Sherman', 'Herald of the 13th about General Foster is wrong', 'Pocotaligo'],
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
