#!/usr/bin/env python3
"""FV-L15b (10 Oct 2026): fetch Chronicling America page OCR (chroniclingamerica.loc.gov .../ocr.txt) for the E572 press hits listed in
fv_l15b_beapi.out to SCRATCH and print every paragraph naming the Champion. >= 2 s apart. Usage: fv_l15b_loc.py SCRATCH"""
import os, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
P = [('sn83045462', '1865-03-16', 1), ('sn83045462', '1865-03-16', 2), ('sn83030313', '1865-03-16', 1), ('sn83026172', '1865-03-16', 3),
     ('sn83030213', '1865-03-16', 4), ('sn86053570', '1865-03-17', 4), ('sn83030213', '1865-03-15', 4)]
out = sys.argv[1]; n = 0
for lccn, d, s in P:
    url = f'https://chroniclingamerica.loc.gov/lccn/{lccn}/{d}/ed-1/seq-{s}/ocr.txt'
    fn = os.path.join(out, f'{lccn}_{d}_{s}.txt')
    try:
        t = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read().decode('utf-8', 'ignore'); open(fn, 'w').write(t)
    except Exception as e: print(url, 'ERR', str(e)[:80]); n += 1; time.sleep(2); continue
    n += 1
    for m in re.finditer(r'Champion', t):
        print(f'{lccn} {d} seq-{s} ::', ' '.join(t[max(0, m.start()-700):m.end()+700].split())); print()
    time.sleep(2)
print('chroniclingamerica requests', n)
