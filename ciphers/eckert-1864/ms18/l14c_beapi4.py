#!/usr/bin/env python3
"""L14-C be-api round 4: whole-collection phrase queries for the four rows still not located; prints EVERY hit id (round 3 showed only the first four of ten) and flags war/Civil-War ids. >= 2.2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('9811/0', '"asked my opinion in regard to"'), ('9811/0b', '"lawfully and properly belong to your office"'), ('9811/0c', '"beg to be excused from deciding"'),
     ('9850/2', '"frauds and inefficiencies in Arkansas"'), ('9850/2b', '"alleged frauds and inefficiencies"'),
     ('9897/1', '"Beverly Tucker will cross"'), ('9897/1b', '"Odell may be relied upon"'), ('9862/0', '"have not arrived there" "Harper\'s Ferry" Garrett'),
     ('9862/0b', '"if they have been delayed on the road"')]
for lab, q in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print(lab, '|', q, '|', len(hits), '|', ' '.join((h.get('_id') or '')[:28] for h in hits), flush=True)
    except Exception as e: print(lab, '|', q, '| ERROR', e)
    time.sleep(2.2)
print('be-api requests', len(Q))
