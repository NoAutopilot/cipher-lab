#!/usr/bin/env python3
"""FM65-D (10 Oct 2026): letters-only phrase grep of the FM65-D rows' readable phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5879/0': ['Fort Fisher is ours', 'all the adjacent defences of New Inlet', 'a well sustained assault', 'nothing could withstand the bravery of our troops', 'bright flash was seen to proceed', 'greatest anxiety prevailed on board the Vanderbilt', 'powder magazine just outside', 'Tribune Special Correspondent'],
 'F2 5883/0': ['remain at Varina until Mr. Blair arrives', 'Blair arrives and is passed through the lines', 'notify Colonel Mulford'],
 'F3 5885/0': ['has started this evening on his return', 'I send today the El Cid and Ranger', 'Cassandria is just here', 'El Cid and Ranger'],
 'F4 5885/1': ['torpedoes of 900 pounds each with insulating wire', 'send immediately by the Phlox', 'I have immediate use for them', 'Captain Lynch commanding ordnance ship'],
 'F5 5886/0': ['torpedoes of 900 pounds each with insulating wire', 'are required by Commander Parker', 'twelve torpedoes of 900 pounds'],
 'F6 5887/0': ['Nevada will be at Monroe', 'order her to City Point immediately after they have landed', 'will take months to prepare them', 'Bureau does not know for what purpose these are intended', 'torpedoes of the kind you name are not available'],
 'F7 5887/1': ['Saugus left this morning for Washington', 'General Grant needs her at once', 'let a message meet her and turn her back'],
 'F8 5888/1': ['I shall leave here tomorrow to be absent several days', 'return to your headquarters in the field', 'take charge of army operations from here', 'in case of contingency you will be on hand'],
 'F9 5888/2': ['all asked for has been ordered', 'not less than 6000 men will report to you', 'prepare accordingly'],
 'F10 5889/2': ['Send one battery with each division and let the others follow', 'bring transportation from Washington to follow the troops', 'If good mules cannot be obtained in Washington', 'bring those from Kentucky'],
 'F11 5890/2': ['Ship ordered to Portsmouth New Hampshire', 'I do not wish to go', 'have me detached here by telegraph', 'my executive officer Lieutenant Commander Parker can take ship'],
 'F12 5891/1': ['very sorry I missed train by forgetting cipher book', 'too many pupils about office'],
 'F13 5895/2': ['by what boat the President left Annapolis', 'time the boat passes Point Lookout', 'ascertain immediately by what boat'],
 'F14 5896/2': ['called on Colonel Stager for cipher operator', 'need construction corps and some operators', 'meet General Schofield at Monroe to accompany him'],
 'F15 5897/0': ['important despatches for him from General Sherman', 'should he arrive in Annapolis tonight'],
 'F16 5861/2b': ['ascertain immediately if General Butler has left Monroe', 'don\'t mention that I enquired', 'keep me posted'],
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
