#!/usr/bin/env python3
"""FM65-B (9 Oct 2026): letters-only phrase grep of the FM65-B entries' decoded phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5856/0': ['Eliza Hancox has already been sent', 'The Winants is hardly capable of going', 'also the tug D. D. Porter', 'will try to bring down a tug', 'tug D D Porter'],
 'F3 5857/1': ['orders payment to company and field officers of a second expedition', 'not mustered for December', 'I have declined as opposed to law and general orders', 'paying company and field officers except on muster rolls', 'Binney chief paymaster'],
 'F4 5858/0': ['for whom there is no transportation', 'sent in river steamers at once to your place', 'required for special service', 'you can dispense with Blackstone', 'turn over to the medical department'],
 'F5 5858/1': ['Ariel Victor Illinois General Sedgwick and Baltic were sent', 'by direction of the Quartermaster General', 'Ariel Illinois Sedgwick Victor Baltic'],
 'F6 5860/1': ['lost some place from my overcoat pocket a large package of papers', 'General Butler\'s report of the Wilmington expedition', 'inquiries made at both places', 'package of papers containing General Butler\'s report'],
 'F7 5860/2': ['The Secretary of War directs that you proceed without delay to', 'General Sherman at Savannah or wherever he may be found', 'Superintendent Military Railroads', 'McCallum Sherman Savannah proceed without delay', 'proceed without delay to General Sherman'],
 'F8 5861/1': ['if the Baltic has been ordered to Monroe consider the order as countermanded', 'let her embark troops as before ordered', 'consider the order as countermanded'],
 'F9 5861/2': ['arrived here safely will remain until tomorrow morning and then start for Savannah', 'ascertain immediately if General Butler has left Monroe', 'don\'t mention that I enquired', 'keep me posted'],
 'F10 5864/1': ['Elias Smith correspondent of the New York Tribune desires permission', 'permission to go on next boat', 'will permit me to pass him and oblige', 'Elias Smith Tribune expedition permission'],
 'F11 5866/0': ['adopt whatever method will soonest ship troops', 'perhaps there may be coal at Annapolis', 'she cannot approach the docks at Annapolis', 'coal can be taken more readily at Baltimore than Annapolis'],
 'F12 5866/2': ['were all ordered to Baltimore at 10 p.m. January 3', 'except the Baltic which was at Baltimore this morning', 'I have not heard from them since', 'Ariel General Sedgwick Victor and Illinois were all ordered'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
for p in sys.argv[1:]:
    texts[os.path.basename(p)[:-4]] = norm(open(p, errors='ignore').read())
print('volumes searched:', len(texts), ' '.join(sorted(texts)))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
