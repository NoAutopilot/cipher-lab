#!/usr/bin/env python3
"""FM65-F (10 Oct 2026): letters-only phrase grep of the FM65-F rows' readable phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5919/2': ['I was ordered to join my', 'I have joined the', 'Am I right', 'first mounted rifles', 'Sumner mounted rifles', 'Leave soon so get quick answer'],
 'F2 5920/1': ['Please have two engines and some flat cars sent here at once', 'so that Colonel Wright can commence work', 'none have arrived at this place', 'flat cars sent here at once'],
 'F3 5923/1': ['double line from here to Fort Fisher', 'double line from Morehead City to Goldsboro', 'construction parties', 'good foreman', 'difficulty of getting operators', 'do all in your power to supply'],
 'F4 5924/0': ['Please answer regarding moving office', 'very essential objection is that we may be required to move', 'if the precedent is once established', 'room for some purpose of her own'],
 'F5 5924/1': ['will push on to Lynchburg', 'push on to Lynchburg and if', 'cavalry force of about 8000', 'join you and General Sherman', 'Sheridan will push on'],
 'F6 5929/1': ['Glisson says he will send', 'Convoy is now ready', 'I leave in a few moments with', 'Captain Glisson'],
 'F7 5929/2': ['Steamship Champion arrived here from Wilmington', 'Sherman and his forces had reached Fayetteville', 'scouts of Shermans army reached Wilmington', 'no particulars could be obtained', 'Champion sailing the same day'],
 'F8 5930/1': ['go up the James River immediately', 'no news of the Montauk', 'our troops in possession of Kinston', 'Hurlbut in from Charleston', 'in possession of Kinston'],
 'F9 5931/0': ['will reach F about', 'go on board the boat on arrival', 'deliver anything you may receive in person', 'name of boat is'],
 'F10 5931/1': ['how much water can your gunboats', 'covered if necessary by gunboats', 'you can come up tonight', 'leave word where they had better land', 'send answer to Mr Emerick', 'George H Gordon'],
 'F11 5933/0': ['the guide Boyle', 'Blackwater can be crossed', 'Broad Ford is the best place', 'twentytwo miles from Suffolk', 'several bridges standing', 'ready to accompany any expedition'],
 'F12 5933/2': ['owing to matters still pending prefers that you continue in command', 'you will therefore not be relieved by', 'District of Eastern Virginia', 'prefers that you continue in command'],
 'F13 5936/0': ['Sherman occupied Goldsboro yesterday', 'Samuel Sinclair Tribune', 'Elias Smith', 'without opposition', 'for your information Beaufort'],
 'F14 5941/1': ['maps ready that illustrate the Roanoke and Chowan', 'all well at Goldsboro', 'I am coming up to see you but must get back as soon as possible', 'If Admiral Porter is there I should like to meet him', 'Steamer Russia'],
 'F15 5943/1': ['relative to barges', 'no exertions will be spared to send them', 'barges and', 'Morehead City'],
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
