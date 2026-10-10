#!/usr/bin/env python3
"""FM65-C: windowed word-set search of the OR I/46-47 djvu texts (scratch copies of the six IA items) for each row: report windows of 900 chars holding >= K
of the row's distinctive plain words. Second print check beside the exact-phrase grep; a miss is a search result (rule 10). Usage: fm65c_win.py DIR"""
import glob, re, sys, os
D = sys.argv[1]
W = {
 'F1 5867/0': ('Robie Cosgrove cracks bearings journal Wilmington breakdown', 4),
 'F2 5868/0': ('Baltic Annapolis coal Monroe countermand Newport orders', 4),
 'F3 5867/2': ('Emerick Abbott vessels forage Sheldon sailed', 4),
 'F4 5869/1': ('Butler relieved resign Eastville Carney Janeway White Norfolk', 4),
 'F5 5870/0': ('Ariel Sedgwick Baltimore arrived delay forage vessels Beckwith', 4),
 'F6 5871/0': ('Ericsson Puritan shaft buoys lighted weather Beaufort Wednesday Rodgers', 4),
 'F7 5871/1': ('Sedgwick Ariel Ashland sailed perfect order Morgan Beckwith Rawlins', 4),
 'F8 5873/1': ('Suwo Nada Oriental sailed half hour Morgan Rawlins ordered', 4),
 'F9 5877/0': ('Bradley mule teams complete rations Beckwith Monroe transportation', 4),
 'F10 5877/1': ('Varuna Fisher siege guns landed entrenched weather splendid Sheldon', 4),
 'F11 5877/2': ('Dupont Thames Haze Sentinel teams Small Monroe Grant directs rations Morgan', 4),
 'F12 5878/1': ('Rawlins vessels returned expedition disabled wagons mortars Fisher Quartermaster telegraphed', 4),
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
