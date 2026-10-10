#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026): Chronicling America page text for E572 by the loc.gov resource JSON (www.loc.gov ?fo=json) -> tile.loc.gov
word-coordinates full text (chroniclingamerica.loc.gov ocr.txt answered 403, not retried). Prints each paragraph naming the Champion.
>= 2 s apart. Usage: fv_l15b_loc2.py SCRATCH"""
import json, os, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
P = [('sn83045462', '1865-03-16', 1), ('sn83030313', '1865-03-16', 1), ('sn83026172', '1865-03-16', 3), ('sn83030213', '1865-03-16', 4), ('sn86053570', '1865-03-17', 4)]
out = sys.argv[1]; n = 0
get = lambda u: urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read().decode('utf-8', 'ignore')
for lccn, d, s in P:
    try:
        j = get(f'https://www.loc.gov/resource/{lccn}/{d}/ed-1/?sp={s}&fo=json'); n += 1; time.sleep(2)
        u = sorted(set(re.findall(r'https://tile\.loc\.gov/text-services/word-coordinates-service\?segment=[^"]*?&format=alto_xml&full_text=1', j)))[0]
        t = get(u); n += 1; open(os.path.join(out, f'{lccn}_{d}_{s}.txt'), 'w').write(t)
        t = re.sub(r'<[^>]+>', ' ', t).replace('\\n', ' ')
        hits = list(re.finditer(r'Champion', t))
        print(f'{lccn} {d} seq-{s}: {len(hits)} Champion')
        for m in hits[:3]: print('   ', ' '.join(t[max(0, m.start()-500):m.end()+900].split())); print()
    except Exception as e: print(lccn, d, s, 'ERR', str(e)[:80])
    time.sleep(2)
print('loc.gov + tile.loc.gov requests', n)
