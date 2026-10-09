#!/usr/bin/env python3
"""AUD2-LEDGER-12 (9 Oct 2026, account 4): fetch the OCR of the Chronicling America pages hit by aud2_ledger12_loc.py (resource JSON ->
fulltext_file ALTO -> words) to OUTDIR, and print a window around each search word. >= 2 s apart."""
import json, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]
PAGES = [('sn83030213/1864-11-09/ed-1', 8, ['perit', 'vermont']), ('sn83035143/1864-09-02/ed-1', 1, ['greyhound']),
         ('sn83021205/1864-08-30/ed-1', 2, ['greyhound']), ('sn83045462/1864-09-03/ed-1', 2, ['greyhound']),
         ('sn83030213/1864-08-30/ed-1', 1, ['monroe']), ('sn83045462/1864-08-29/ed-1', 2, ['monroe'])]
n = 0
for res, sp, words in PAGES:
    try:
        n += 1
        d = json.load(urllib.request.urlopen(urllib.request.Request(
            f'https://www.loc.gov/resource/{res}/?sp={sp}&fo=json&at=resource', headers=UA), timeout=90))
        time.sleep(2); n += 1
        x = urllib.request.urlopen(urllib.request.Request(d['resource']['fulltext_file'], headers=UA), timeout=90).read().decode('utf8', 'replace')
        txt = ' '.join(re.findall(r'CONTENT="([^"]*)"', x)) if 'CONTENT=' in x else re.sub(r'<[^>]+>', ' ', x)
        fn = f"{out}/{res.replace('/', '_')}_sp{sp}.txt"; open(fn, 'w').write(txt)
        print('##', res, sp, len(txt.split()), 'words')
        low = txt.lower()
        for w in words:
            for m in re.finditer(w, low):
                print('  [' + w + ']', txt[max(0, m.start() - 500): m.start() + 500].replace('\n', ' '))
    except Exception as e: print('##', res, sp, 'ERR', str(e)[:120])
    time.sleep(2)
print('requests', n)
