import csv, sys
from collections import OrderedDict
# usage: mktask.py draft.tsv prefix lo hi out
draft, lo, hi, out = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
L = OrderedDict()
for r in csv.DictReader(open(draft), delimiter='\t'):
    n = int(r['line'].split('_L')[1])
    if not lo <= n <= hi: continue
    L.setdefault(r['line'], []).append(r)
with open(out, 'w') as f:
    nset = 0
    for line, rows in L.items():
        if all(r['why'] == 'agree' for r in rows): continue
        toks = []
        for r in rows:
            p, s, w, alt = r['position'], r['sign'], r['why'], r['alt']
            if w == 'agree': toks.append(f'{p}:{s}')
            else:
                nset += 1
                if w == 'agree-flagged': toks.append(f'{p}:<<both={s} (a pass was unsure)>>')
                else:
                    other = alt.split(':',1)[1]; who = alt.split(':')[0]
                    a, b = (s, other) if who == 'B' else (other, s)
                    if w == 'gap': toks.append(f'{p}:<<A={a} | B={b}  ("-" = that pass saw no sign here)>>')
                    else: toks.append(f'{p}:<<A={a} | B={b}>>')
        f.write(f'{line}\n  ' + '  '.join(toks) + '\n\n')
print(out, nset)
