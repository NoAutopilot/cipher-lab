#!/usr/bin/env python3
"""NO9-L (10 Oct 2026): letters-only phrase grep of the ten NO9-L rows' decoded phrases in the cached OR/ORN djvu texts (sources/ia-fulltext/print-check/*.gz, plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 '9699/0': ['forty thousand bushels of grain and seven hundred tons of hay', 'under sealed orders to report at', 'their cargoes which will not be discharged unless needed there', 'for the steam propellers needed'],
 '9694/2': ['Cahawba', 'Weybossett', 'transport colored', 'fully coaled and watered as soon as the storm is over', 'capacity of vessels sailing under this order'],
 '9845/0': ['whether the draft will be suspended or enforced', 'modifies it to the extent of one man', 'wavers in its execution', 'effect the recall of', 'to Governor Morton'],
 '9679/0': ['Ned Price', 'prize fighter and send him here immediately', 'Superintendent Metropolitan Police'],
 '9725/1': ['by special messenger to Major-General Steele', 'return yourself immediately to', 'left under command of the senior officer', 'if Shreveport has been taken'],
 '9762/1': ['sent by General Grant to open communication', 'by way of Charlottesville', 'returned to York River without effecting his object', 'not to be caught by the'],
 '9761/0': ['telegraph to Ordnance Department and it will be immediately sent to you by an express train', 'take every precaution in convoying the train', 'all possible despatch in carrying out'],
 '9862/1': ['scheme of the insurgents for capturing', 'going on board as officers and crew', 'take proper measures towards thwarting the same', 'a northern port'],
 '9770/2': ['advise him of the condition of affairs and take his orders in regard to your dispositions', 'ordered General Hunter to the line of', 'with all his available forces'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
isor = lambda v: 'warofrebellion' in v or 'officialrecord' in v or v.startswith('navalwar') or 'privateofficial' in v
print('volumes searched:', len(texts), 'OR/ORN/Butler:', ' '.join(sorted(v for v in texts if isor(v))))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t and isor(v)]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
