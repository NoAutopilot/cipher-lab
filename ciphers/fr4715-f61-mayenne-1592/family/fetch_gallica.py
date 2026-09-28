#!/usr/bin/env python3
"""F61-FAMILY (28 Sept 2026): fetch Gallica IIIF images for the Mayenne cipher family, one request at a time, 2 s
apart, browser UA (as the H19 fetches recorded), every request appended to family/requests.log with status and
sha1. Usage: python3 fetch_gallica.py ARK CANVAS SIZE OUT   (SIZE = 'full' or a pixel width like 1200)
Never a retry loop: one retry after a 5 s pause on a network error, then stop."""
import hashlib, sys, time, urllib.request, os, pathlib
ark, canvas, size, out = sys.argv[1:5]
sz = 'full' if size == 'full' else f'{size},'
url = f'https://gallica.bnf.fr/iiif/ark:/12148/{ark}/f{canvas}/full/{sz}/0/native.jpg'
log = pathlib.Path(__file__).parent / 'requests.log'
if os.path.exists(out) and os.path.getsize(out) > 1000:
    print('cached', out); sys.exit(0)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'})
status = 'ERR'; data = b''
for attempt in range(2):
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            data = r.read(); status = str(r.status); ctype = r.headers.get('Content-Type', '')
        break
    except Exception as e:
        status = f'ERR {e}'[:80]
        if attempt == 0: time.sleep(5)
if data[:2] == b'\xff\xd8':
    open(out, 'wb').write(data); sha = hashlib.sha1(data).hexdigest()
else:
    sha = '-'; status += ' (not a JPEG: %r)' % data[:60]
with open(log, 'a') as f:
    f.write(f'{time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}\tGET\t{url}\t{status}\t{len(data)}\t{sha}\t{out}\n')
print(status, len(data), sha, out)
time.sleep(2.0)
sys.exit(0 if sha != '-' else 1)
