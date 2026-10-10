#!/usr/bin/env python3
"""OR-CACHE2 (10 Oct 2026): fetch each missing ser. I part's _djvu.txt once (archive.org, 1.5 s apart, one retry after 25 s on a
dropped connection, then stop), gzip into sources/ia-fulltext/print-check/, and print the title-page lines (first 3 kB) for the
volume/part check. Extends or_fetch_cache.py (same cache, same User-Agent). Usage: or_cache2_fetch.py ID [ID...]"""
import sys, os, gzip, time, urllib.request, hashlib, re
D = 'sources/ia-fulltext/print-check'
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n = 0
for i in sys.argv[1:]:
    dst = f'{D}/{i}_djvu.txt.gz'
    if os.path.exists(dst): print(i, 'present'); continue
    b = None
    for attempt in (1, 2):
        n += 1
        try:
            b = urllib.request.urlopen(urllib.request.Request(f'https://archive.org/download/{i}/{i}_djvu.txt', headers=UA), timeout=240).read(); break
        except Exception as e:
            print(i, 'ERR', attempt, e, flush=True)
            if attempt == 1: time.sleep(25)
    if b is None: print('STOP: two failures on', i); break
    open(dst, 'wb').write(gzip.compress(b, 9))
    head = re.sub(r'\s+', ' ', b[:3500].decode('utf8', 'replace'))
    print(i, len(b), hashlib.sha256(b).hexdigest()[:16], '| HEAD:', head[:260], flush=True)
    time.sleep(1.5)
print('requests', n)
