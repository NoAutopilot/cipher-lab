"""FV-N2d (10 Oct 2026): G3 phrase pass for N2-HF (Meigs to Ingalls, 6 Aug 1864) on Google Books (keyed, country=US) and IA be-api all items.
Positive control: N2-HC's printed phrase. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
P = ['"single and separate command will"', '"flag of truce boats and the boats about Fort Monroe"', '"capacity of 19,000 infantry"',
     '"room for over 30,000 men"', '"to move 12 or 13,000 men"']
n = 0
for q in P:
    u = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'key': os.environ.get('GOOGLE_BOOKS_KEY', '')})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        its = d.get('items', [])
        print('gbooks |', q, '|', d.get('totalItems'), '|', '; '.join((i['volumeInfo'].get('title', '')[:50] + ' ' + str(i['volumeInfo'].get('publishedDate', ''))) for i in its[:4]))
    except Exception as e: print('gbooks |', q, '| ERR', str(e)[:80])
    n += 1; time.sleep(1.8)
    u = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
        hs = d.get('hits', {}).get('hits', [])
        print('be-api |', q, '|', len(hs), '|', '; '.join(h.get('fields', {}).get('identifier', [''])[0] if isinstance(h.get('fields', {}).get('identifier'), list) else str(h.get('_id', '')) for h in hs[:5]))
    except Exception as e: print('be-api |', q, '| ERR', str(e)[:80])
    n += 1; time.sleep(1.8)
print('requests', n)
