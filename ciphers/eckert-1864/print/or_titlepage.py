#!/usr/bin/env python3
"""OR-CACHE: print the title-page head of IA OR volumes. Local gz cache first (no request); else a Range GET of
the first 40000 bytes of <id>_djvu.txt (1.5 s apart). Usage: or_titlepage.py OUTDIR ID [ID...]"""
import sys, os, gzip, time, urllib.request
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
cache = 'sources/ia-fulltext/print-check'
for i in sys.argv[2:]:
    dst = os.path.join(out, i + '.head.txt')
    if os.path.exists(dst): continue
    g = os.path.join(cache, i + '_djvu.txt.gz')
    if os.path.exists(g):
        t = gzip.open(g, 'rt', errors='replace').read(40000); src = 'local-cache'
    else:
        rq = urllib.request.Request(f'https://archive.org/download/{i}/{i}_djvu.txt',
            headers={'Range': 'bytes=0-39999', 'User-Agent': 'cipher-lab research script (contact via repository)'})
        try: t = urllib.request.urlopen(rq, timeout=60).read().decode('utf-8', 'replace'); src = 'archive.org'
        except Exception as e: t = 'ERR %s' % e; src = 'archive.org-ERR'
        time.sleep(1.5)
    open(dst, 'w').write(src + '\n' + t)
    print(i, src, len(t))
