#!/usr/bin/env python3
"""FM-R3c (8-9 Oct 2026): phrase grep of the FM-R3c entries' clear/decoded phrases AND rare names/numbers in OR/ORN djvu texts
(scratch *.txt passed as arguments, plus the cached ../../../sources/ia-fulltext/print-check/*.gz). Prints volume, count and a 160-char snippet of the first hit.
A miss is a search result, not a verdict (rule 10). Usage: fm_r3c_printcheck.py VOL.txt ... [--only F4]"""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
PH = {
 'F1 5839/2': ['brasses are worn again', 'brasses worn again', 'we can not go on', 'Rodgers brasses', 'Cuyler Rodgers'],
 'F2 5734/2': ['Nothing new to communicate', 'Visited army lines', 'thought to be very strong', 'Agawam Farrar', 'Agawan'],
 'F3 5736/1': ['dispatch several gunboats from the Potomac', 'gunboats from the Potomac to York River', 'to answer calls from that quarter', 'No change in the naval situation here', 'naval situation here'],
 'F4 5760/0': ['Samuel Jones', 'equal number of rebel officers of equal rank', 'under the enemy\'s fire as long as our officers are exposed in Charleston', 'this weak and cruel act', 'Boordman', 'Mary A. Boardman', 'E. N. Strong', 'fire on the city is continued'],
 'F5 5683/0': ['no press despatches sent unless revised and approved', 'Fort Powhatan and made three successive charges', 'Powhatan and made three successive', 'ample reinforcements', 'steamer Dictator', 'steamer Manhattan at sea', 'stating loss of steamer Manhattan', 'large lot of cotton picked up near Hatteras', 'Rowe has sent in the following'],
 'F6 5831/2': ['Tullifinny Creek and Coosawatchie', 'cut opening through woods', 'knock the fits out of', 'break of communication between Charleston and Savannah', 'exchanged prisoners left Charleston Monday morning', 'steamer United States with'],
 'F7 5670/1': ['Kingsland Creek', 'Hold your position will reinforce you', 'captured a rebel courier', 'rebel courier with dispatches from Beauregard', 'Ames in position to keep Beauregard', 'not disposed to fight without reinforcements', 'Drewry\'s Bluff'],
 'F8 5729/1': ['Hanoverian named Finck', 'Finck left Charleston', 'Hanoverian', 'the city could be taken by', 'Van Duzer Carter', 'Carter Knoxville June 2'],
 'F9 5837/1': ['send off the Nereus', 'take any vessels you find for convoy', 'you have all the orders we have to give', 'send full account of your passage by mail', 'wishing you may be in time', 'Nereus'],
 'F10 5837/0': ['Captain John F. Anderson', 'with dispatches from General Sherman and General Foster', 'arrival here this morning at five o\'clock', 'detailed dispatches from General Sherman', 'John F. Anderson'],
}
def rx(ph): return re.compile(r'[\s\W]*'.join(re.escape(w) for w in re.findall(r"[A-Za-z0-9']+", ph.replace("'", ""))), re.I)
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = gzip.open(p, 'rt', errors='ignore').read()
only = None
args = sys.argv[1:]
if '--only' in args: i = args.index('--only'); only = args[i+1]; args = args[:i] + args[i+2:]
for p in args: texts[os.path.basename(p)[:-4]] = open(p, errors='ignore').read()
print('volumes searched:', len(texts))
for e, phs in PH.items():
    if only and not e.startswith(only): continue
    for ph in phs:
        r = rx(ph); res = []
        for v, t in texts.items():
            ms = list(r.finditer(t))
            if ms:
                m = ms[0]; s = re.sub(r'\s+', ' ', t[max(0, m.start()-80):m.end()+80])
                res.append(f'{v} x{len(ms)} [{s}]')
        print(e, '|', ph, '|', ' || '.join(res) or 'none')
