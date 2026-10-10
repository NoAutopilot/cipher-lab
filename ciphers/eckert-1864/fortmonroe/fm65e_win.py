#!/usr/bin/env python3
"""FM65-E: windowed word-set search of the OR I/46-47 djvu texts (scratch copies of the six IA items) for each row: report windows of 900 chars holding >= K
of the row's distinctive plain words. Second print check beside the exact-phrase grep; a miss is a search result (rule 10). Usage: fm65c_win.py DIR"""
import glob, re, sys, os
D = sys.argv[1]
W = {
 'F1 5898/1': ('Rhode Island patrol Cape Henry Cape Fear River vessels troops Hampton Roads', 4),
 'F2 5899/0': ('Dumbarton Cambridge Tuesday James River Sheldon vessel ready', 3),
 'F3 5902/1': ('Gordon Vogdes Eastern District Commission investigation Emerick Ord', 4),
 'F4 5902/2': ('Gordon Vogdes investigation Ord command Emerick progress quietly', 4),
 'F5 5904/1': ('Meagher Schofield Rucker Annapolis ambulances mule teams Beckwith shipped', 4),
 'F6 5905/0': ('Palmer Meagher Morehead arriving transportation Grant', 4),
 'F7 5907/1': ('Lynch torpedoes Wise Bureau Ordnance James River immediate use', 4),
 'F8 5912/1': ('Yorktown office operators telegraph Ord imperative Quartermaster', 4),
 'F9 5914/1': ('Trenchard Newbern Wilmington Cape Fear Rhode Island', 4),
 'F10 5915/0': ('Yorktown telegraph station Eckert Vincent James Ord established', 4),
 'F11 5915/1': ('Cuyler Fisher Wilmington evacuation Terry Fulton', 4),
 'F12 5917/1': ('Washburne Johnson rascal Gordon evidence Commerce Norfolk', 4),
 'F13 5918/0': ('Wilder Plato Ord Beckwith Grant Department negroes moneys', 4),
 'F14 5918/1': ('pilots monitors Bradley James River Navy furnish', 4),
 'F15 5919/1': ('Bowers Roberts scout Beckwith Roberts proceed', 4),
}
T = {}
for p in sorted(glob.glob(os.path.join(D, '*.txt'))): T[os.path.basename(p)[:-4]] = re.sub(r'\s+', ' ', open(p, errors='ignore').read())
for k, (words, K) in W.items():
    ws = words.split(); best = []
    for v, t in T.items():
        pos = sorted(m.start() for w in ws for m in re.finditer(re.escape(w), t))
        i = 0
        while i < len(pos):
            j = i; 
            while j < len(pos) and pos[j] - pos[i] <= 900: j += 1
            seg = t[pos[i]:pos[i] + 900]; got = [w for w in ws if w in seg]
            if len(got) >= K: best.append((len(got), v, pos[i], got)); i = j
            else: i += 1
    best.sort(reverse=True)
    print(k, '|', len(best), 'windows >= %d words' % K)
    for n, v, p, got in best[:3]: print('    ', n, v[:28], p, ' '.join(got), '::', T[v][max(0, p - 40):p + 260])
