#!/usr/bin/env python3
"""AUD2-LEDGERN2-3 (10 Oct 2026): positive controls on IA be-api for papersofulyssess0013gran (Grant Papers vol. 13, Nov 16 1864-Feb 20 1865) and its
metadata. Words that must occur in that volume: Savannah, Nashville, Thomas, Butler. 0 hits on all = the volume is not indexed (non-test)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
for q in ['Nashville', 'Butler']:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': 'papersofulyssess0013gran'})
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90))
    print('papersofulyssess0013gran |', q, '|', d.get('hits', {}).get('total')); time.sleep(1.8)
m = json.load(urllib.request.urlopen(urllib.request.Request('https://archive.org/metadata/papersofulyssess0013gran/metadata', headers=UA), timeout=60))
r = m.get('result', {}); print('metadata:', r.get('title'), '|', r.get('volume'), '|', r.get('date'), '|', r.get('collection'))
print('requests 3 (2 be-api, 1 archive.org)')
