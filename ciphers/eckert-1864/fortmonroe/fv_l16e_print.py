#!/usr/bin/env python3
"""FV-L16e (10 Oct 2026, for LANE LEDGER-16): letters-only phrase grep over the cached print-check volumes
(sources/ia-fulltext/print-check/*_djvu.txt.gz) for the nine 1864 Fort Monroe entries; KWIC per hit."""
import gzip, glob, re, sys
Q = {
 'E447': ['saugus six miles above', 'miles above city point', 'will start down at daylight', 'start down at daylight', 'e r colhoun', 'colhoun commander', 'saugus'],
 'E470': ['mahopac canonicus and saugus', 'canonicus and saugus are ready', 'are ready for service', 'three monitors'],
 'E445': ['mr baird', 'with his instruments', 'baird will arrive', 'city of hudson'],
 'E468': ['meet you and the admiral', 'admiral there at', 'meet you at fortress monroe', 'meet you at fort monroe tomorrow'],
 'E474': ['has general butlers fleet left', 'butlers fleet left', 'has the fleet left', 'fleet left yet'],
 'E443': ['yellow fever is prevailing', 'mcdougall', 'notify you at once', 'considerable extent at new berne', 'considerable extent at newbern'],
 'E471': ['till the cable is repaired', 'cable is repaired', 'nothing heard from kilpatrick', 'send no ciphers'],
 'E446': ['w a dunn', 'operator at cherrystone', 'operator at cherry stone', 'american office at baltimore'],
 'E448': ['when the manhattan arrives', 'secretary of war on board', 'dealy', 'be at the wharf when'],
}
def norm(s): return re.sub(r'[^a-z]+', ' ', s.lower())
files = sorted(glob.glob('sources/ia-fulltext/print-check/*_djvu.txt.gz'))
print('volumes', len(files))
for f in files:
    vid = f.split('/')[-1].replace('_djvu.txt.gz', '')
    t = norm(gzip.open(f, 'rt', errors='ignore').read())
    for e, qs in Q.items():
        for q in qs:
            nq = ' ' + norm(q).strip() + ' '
            n = t.count(nq)
            if n and (n <= 6 or len(nq) > 14):
                for m in list(re.finditer(re.escape(nq), t))[:4]:
                    print(f'{e}\t{q}\t{vid}\t{n}\t...{t[max(0,m.start()-160):m.end()+160]}...')
