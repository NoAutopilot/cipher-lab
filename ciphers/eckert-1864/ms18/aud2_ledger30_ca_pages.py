#!/usr/bin/env python3
"""AUD2-LEDGER-30 (9 Oct 2026): read the OCR full text of named Chronicling America pages (loc.gov resource JSON -> fulltext_file) and print
each passage around the given terms. Usage: aud2_ledger30_ca_pages.py OUT_DIR 'TERM|TERM' LCCN/DATE/SP ... ; >= 2 s apart. OCR-dependent:
a miss is a weak search result, never a verdict."""
import json, os, re, sys, time, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out, terms, pages = sys.argv[1], re.compile(sys.argv[2], re.I), sys.argv[3:]; n = 0
for pg in pages:
    lccn, date, sp = pg.split('/')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(f'https://www.loc.gov/resource/{lccn}/{date}/ed-1/?sp={sp}&fo=json', headers=UA), timeout=90)); n += 1; time.sleep(2)
        x = urllib.request.urlopen(urllib.request.Request(d['resource']['fulltext_file'], headers=UA), timeout=90).read().decode('utf-8', 'replace'); n += 1; time.sleep(2)
    except Exception as e:
        print(pg, 'ERR', str(e)[:80]); continue
    t = ' '.join(re.findall(r'CONTENT="([^"]*)"', x)) or re.sub(r'<[^>]+>', ' ', x)
    open(os.path.join(out, pg.replace('/', '_') + '.txt'), 'w').write(t)
    hits = [m.start() for m in terms.finditer(t)]
    print(f'== {pg} words={len(t.split())} hits={len(hits)}')
    last = -9999
    for h in hits:
        if h - last < 600: continue
        last = h; print('   ...', re.sub(r'\s+', ' ', t[max(0, h - 350):h + 450]), '...')
print('requests', n)
