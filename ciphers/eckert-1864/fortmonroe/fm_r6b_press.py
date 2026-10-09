#!/usr/bin/env python3
"""FM-R6b (9 Oct 2026): fetch ALTO full text of New-York daily tribune (sn83030213) pages for a date via loc.gov resource JSON + tile.loc.gov text service,
save to SCRATCH, grep rare words. Usage: fm_r6b_press.py DATE SCRATCH WORD... ; >= 2.5 s apart. A miss is a search result (rule 10)."""
import json, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
date, out = sys.argv[1], sys.argv[2]; words = [w.lower() for w in sys.argv[3:]]
LCN = sys.argv[0] and 'sn83030213'
def get(u):
    return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90).read()
n = 0
for sp in range(1, 9):
    try:
        d = json.loads(get(f'https://www.loc.gov/resource/{LCN}/{date}/ed-1/?sp={sp}&st=text&fo=json')); n += 1; time.sleep(2.5)
        ft = d['fulltext_service']
        t = get(ft).decode('utf8', 'ignore'); n += 1; time.sleep(2.5)
    except Exception as e:
        print('page', sp, 'ERR', str(e)[:70]); continue
    txt = re.sub(r'<[^>]+>', ' ', t) if '<' in t[:50] else t
    if '<String' in t: txt = ' '.join(re.findall(r'CONTENT="([^"]*)"', t))
    open(f'{out}/{LCN}_{date}_p{sp}.txt', 'w').write(txt)
    low = txt.lower()
    print('page', sp, len(txt), {w: low.count(w) for w in words}, flush=True)
print('requests', n)
