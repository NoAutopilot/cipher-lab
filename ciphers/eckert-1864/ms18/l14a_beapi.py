#!/usr/bin/env python3
"""L14-A (10 Oct 2026): IA be-api full-text snippet search, whole collection (no identifier), quoted phrases from the not-located L14-A rows; >= 1.8 s apart.
A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('Y1 9835/1', '"means mischief on the Pacific coast"'), ('Y1 9835/1', '"very important to watch" "who he associates with"'),
     ('Y2 9877/1', '"to enable them to go home and vote" furlough 1864'), ('Y2 9877/1', 'furlough "go home and vote" Delaware cavalry Wallace Hurlbut'),
     ('Y4 9826/0', '"are exempt from conscription" Mosby'), ('Y4 9826/0', 'Mosby "valuable information" "capable of bearing arms" Upperville'),
     ('Y6 9777/1', '"large train was sent to the rear when he moved forward"'), ('Y6 9777/1', 'Ricketts "Pt. Depot" Baltimore steamers be met and landed 1864'),
     ('Y7 9823/3', '"Muddy Branch" cavalry "start immediately on their scout"'), ('Y7 9823/3', '"Muddy Branch" wharf Illinois cavalry August 1864 scout'),
     ('Y8 9865/1', '"be prepared to meet Hood" Thomas Schofield Kent'), ('Y8 9865/1', 'Thomas "two old regiments" Pope Ohio Indiana Nashville October 1864')]
n = 0
for lab, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
        hits = d.get('hits', {}).get('hits', [])
        print(lab, '|', q, '|', len(hits), flush=True)
        for h in hits[:4]:
            md = h.get('fields', {}).get('meta_title', h.get('fields', {}).get('identifier', ''))
            print('   ', h.get('fields', {}).get('identifier'), '|', (h.get('highlight', {}) or {}).get('text', [''])[0].replace('\n', ' ')[:260])
    except Exception as e: n += 1; print(lab, '|', q, '| ERR', str(e)[:100])
    time.sleep(1.9)
print('be-api requests', n)
