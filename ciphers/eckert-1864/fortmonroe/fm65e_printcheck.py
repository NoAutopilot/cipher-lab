#!/usr/bin/env python3
"""FM65-E (10 Oct 2026): letters-only phrase grep of the FM65-E rows' readable phrases in the cached OR/ORN djvu texts
(sources/ia-fulltext/print-check/*.gz plus scratch *.txt given as arguments). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'F1 5898/1': ['exclusive of the Rhode Island', 'vessels exclusive of the Rhode Island', 'patrol from Cape Henry', 'Cape Henry to Cape Fear', 'whilst troops are moving south'],
 'F2 5899/0': ['the Dumbarton ready', 'we have but one vessel', 'Cambridge will be available', 'Cambridge will be ready on Tuesday', 'convey him up the James River'],
 'F3 5902/1': ['placing the Command of the Eastern District', 'temporarily in the hands of General Vogdes', 'purposes of the Commission', 'devoted to the investigation', 'General Vogdes'],
 'F4 5902/2': ['investigation can progress quietly', 'take the command for the present', 'you will have to take the command'],
 'F5 5904/1': ['Meagher shipped from here and Annapolis', 'about 10,000 men', '306 mule teams', 'will sail from here tomorrow morning', 'ambulances and ditto', 'Rucker'],
 'F6 5905/0 ': ['Meagher are just arriving at Morehead', 'just arriving at Morehead', 'They have no transportation', 'just been received from Palmer'],
 'F7 5907/1': ['mentioned in Bureau letter of 25th ultimo', 'have not been received', 'required for immediate use on James River', 'Lynch Commander and Inspector of Ordnance'],
 'F8 5912/1': ['requires an office at Yorktown at once', 'anxious inquiry about office', 'Can you supply these operators', 'one at Yorktown is considered imperative'],
 'F9 5914/1': ['Newbern has arrived from Cape Fear', 'within four miles of Wilmington', 'Trenchard'],
 'F10 5915/0': ['telegraph station be established at Yorktown', 'establish the office as speedily as practicable', 'respectfully forwarded to Major Eckert', 'Acting Chief Quartermaster'],
 'F11 5915/1': ['Cuyler arrived this morning from Fort Fisher', 'evacuation of Wilmington on the night of the 21st', 'neglected to destroy'],
 'F12 5917/1': ['I sent for Johnson to try him', 'greatest rascal should escape', 'do not let him turn State evidence', 'send him to you under guard', 'Do you want him', 'Washburne Chairman Committee of Commerce'],
 'F13 5918/0': ['order I gave Wilder to report for duty', 'Wilder is directed to report in person', 'receiving moneys from negroes', 'retain Captain Wilder until proper inquiry', 'prevent my holding him responsible'],
 'F14 5918/1': ['entirely out of pilots', 'furnish the Navy with two pilots', 'monitors to go up James River'],
 'F15 5919/1': ['cannot find the scout that was to report', 'ready to proceed in two hours', 'Shall I go without him', 'Colonel Roberts 139th New York', 'Lieutenant Colonel Bowers'],
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
