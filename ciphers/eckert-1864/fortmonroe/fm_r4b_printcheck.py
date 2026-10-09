#!/usr/bin/env python3
"""FM-R4b (9 Oct 2026): letters-only phrase grep of the FM-R4b entries' decoded phrases AND rare names/numbers in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5787/1': ['City of Hudson', 'Ingalls City of Hudson', 'No such orders were received', 'answered him to this effect', 'almost destitute of water', 'destitute of water', 'Hudson ordered to report'],
 'F2 5629/1': ['Captain Farquhar requires', 'Farquhar requires mules', 'mules for pontoon train', 'mules for the pontoon train', 'pontoon train when can they be furnished', 'additional wagons and teams complete', 'wagons and teams complete', 'I made requisition for'],
 'F3 5741/0': ['arriving here in considerable numbers', 'indicates work for us this side of James', 'cable for James River', 'cable for Appomattox', 'Butler has asked again for one', 'ready for short notice', 'send hoe man here'],
 'F4 5812/0': ['send all empty steamers to Washington', 'empty steamers to Washington to bring down', 'as fast as they arrive and become light', 'estimates are prepared of material', 'buildings already in process of erection', 'Colonel Bradley to send', 'Captain William T Howell', 'William T Howell'],
 'F5 5610/1': ['I am ordered to New York to await decision', 'await decision upon an application to leave the Department of the South', 'application to leave the Department of the South', 'appear before the investigating committee', 'visit Washington that I may appear', 'Seymour ordered to New York'],
 'F6 5822/1': ['Mendota and Miami', 'Canonicus and Mahopac', 'Canonicus Mahopac Hampton Roads', 'three Manitous', 'Aikens Landing below Dutch Gap', 'moved all the vessels to Aikens Landing', 'proceed down the river as you command', 'Parker Porter Mendota'],
 'F7 5609/2': ['additional shelter tents are needed here', 'shelter tents are needed here instead of', 'shelter tents instead of 20000', 'required by Lieutenant Webster', 'required by Lieutenant Webster', 'let me know if I can count on the amount of water', 'count on the amount of water'],
 'F8 5790/0': ['Keyport', 'left here at 1 PM on the Keyport', 'wish you to meet him at the wharf on arrival at Monroe', 'deliver any telegrams that may be sent you for him', 'tell him that I directed you to do so', 'get anything he may have', 'meet him at the wharf on arrival'],
 'F9 5742/1': ['put afloat all the 3 and 2 inch plank', 'afloat all the 3 and 2 inch plank you can', 'dont want scantling', 'do not want scantling', 'dont start vessel up until you get further orders', 'Colonel Shaffer chief of staff please hurry me an operator', 'hurry me an operator', 'send me an operator'],
 'F10 5775/1': ['remove York River light vessel', 'authority is received to remove York River light vessel', 'York River light vessel', 'take her to Hampton Roads', 'light house inspector', 'McGarvey light house inspector', 'J W Sampson'],
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
