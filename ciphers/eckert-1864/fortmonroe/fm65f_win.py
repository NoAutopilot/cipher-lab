#!/usr/bin/env python3
"""FM65-F: windowed word-set search of the OR I/46-47 djvu texts (scratch copies of the six IA items) for each row: report windows of 900 chars holding >= K
of the row's distinctive plain words. Second print check beside the exact-phrase grep; a miss is a search result (rule 10). Usage: fm65c_win.py DIR"""
import glob, re, sys, os
D = sys.argv[1]
W = {
 'F1 5919/2': ('Sumner Emerick mounted rifles joined ordered regiment expedition Sheldon', 4),
 'F2 5920/1': ('Wright flat cars engines commence work Beckwith Monroe Schofield', 4),
 'F3 5923/1': ('Eckert Schofield Fisher Goldsboro Morehead construction operators foreman diggers shovels', 4),
 'F4 5924/0': ('Eckert office moving accommodation precedent instigation Ord Sheldon', 4),
 'F5 5924/1': ('Sheridan Lynchburg Sherman cavalry push Schofield Beckwith Grant', 4),
 'F6 5929/1': ('Glisson Rawlins convoy pilot Roberts Babcock Beckwith Sheldon', 4),
 'F7 5929/2': ('Champion Wilmington Fayetteville Sherman scouts Eckert Sheldon', 4),
 'F8 5930/1': ('Hurlbut Charleston James Montauk Kinston Glisson Eckert', 4),
 'F9 5931/0': ('Sheldon Eckert Dealy boat Windsor deliver arrival Monroe', 4),
 'F10 5931/1': ('Gordon Emerick Beckwith gunboats cavalry Norfolk Suffolk water land Ord', 4),
 'F11 5933/0': ('Boyle guide Blackwater Broad Ford Suffolk Gordon Emerick bridges', 4),
 'F12 5933/2': ('Gordon Hartsuff district Eastern Virginia relieved command Emerick Sheldon', 4),
 'F13 5936/0': ('Sinclair Tribune Sherman Goldsboro Beaufort Elias Smith Eckert', 4),
 'F14 5941/1': ('Roanoke Chowan maps Goldsboro Porter Beckwith Russia Sherman', 4),
 'F15 5943/1': ('barges Morehead exertions James Eckert Granger Sheldon', 4),
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
