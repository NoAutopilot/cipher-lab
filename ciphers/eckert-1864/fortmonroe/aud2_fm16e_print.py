#!/usr/bin/env python3
"""AUD2-FM16e (11 Oct 2026, for LANE DEFAULT-A1-0540): letters-only phrase grep over the cached print-check volumes
(sources/ia-fulltext/print-check/*_djvu.txt.gz, 215 on 11 Oct; FV-L16e had 191) for E443 E445 E446 E448, fresh phrases
(none of fv_l16e_print.py's); KWIC per hit. A miss is a search result, not a statement about print (rule 10)."""
import gzip, glob, re
Q = {
 'E443': ['prevailing to considerable extent', 'prevailing to a considerable extent at', 'thought best to notify you', 'surgeon charles mcdougall',
          'surgeon mcdougall', 'yellow fever at newbern', 'yellow fever at new berne', 'yellow fever prevailing at', 'e mcclellan', 'john horner'],
 'E445': ['baird will arrive', 'have him sent here', 'sent here with his instruments', 'arrive tomorrow morning on the', 'city of hendron', 'r o brien'],
 'E446': ['dunn formerly', 'same w a dunn', 'formerly employed in the american', 'american telegraph office at baltimore', 'operator at cherrystone',
          'answer quick i dont know', 'desires to know if the operator'],
 'E448': ['dont fail to be at', 'do not fail to be at the wharf', 'dont mention his coming', 'mention his coming to', 'bates has posted you',
          'posted you fully', 'manhattan arrives', 'w j dealy'],
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
            if n:
                for m in list(re.finditer(re.escape(nq), t))[:3]:
                    print(f'{e}\t{q}\t{vid}\t{n}\t...{t[max(0,m.start()-160):m.end()+160]}...')
