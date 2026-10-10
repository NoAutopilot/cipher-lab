#!/usr/bin/env python3
"""OR-CACHE (10 Oct 2026): fetch IA _djvu.txt for the named ids once, gzip into sources/ia-fulltext/print-check/ (the cache the
print-check scripts read). One request per id, 1.5 s apart, skip if present. Usage: or_fetch_cache.py ID [ID...]"""
import sys, os, gzip, time, urllib.request, hashlib
D = 'sources/ia-fulltext/print-check'
for i in sys.argv[1:]:
    dst = f'{D}/{i}_djvu.txt.gz'
    if os.path.exists(dst): print(i, 'present'); continue
    rq = urllib.request.Request(f'https://archive.org/download/{i}/{i}_djvu.txt', headers={'User-Agent': 'cipher-lab research script (contact via repository)'})
    try: b = urllib.request.urlopen(rq, timeout=180).read()
    except Exception as e: print(i, 'ERR', e); time.sleep(1.5); continue
    open(dst, 'wb').write(gzip.compress(b, 9))
    print(i, len(b), hashlib.sha256(b).hexdigest()[:16], flush=True); time.sleep(1.5)
