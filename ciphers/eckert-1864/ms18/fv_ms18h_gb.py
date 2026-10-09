"""FV-MS18h (9 Oct 2026): print search for E344 paragraph 2 (the Eckert cipher-office note, 14 Oct 1864), unprinted in OR.
Google Books API (country=US, key from env, never printed) and IA be-api full-text, quoted phrases. Usage: python3 ms18/fv_ms18h_gb.py"""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
GB = ['"words commencing Henry"', '"words beginning McClellan"', '"copies of all ciphers to and from"', 'Eckert "Van Duzer" "translate and deliver"']
n = 0
for q in GB:
    url = 'https://www.googleapis.com/books/v1/volumes?country=US&maxResults=10&q=' + urllib.parse.quote(q) + ('&key=' + K if K else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        items = d.get('items', [])
        print('GB', q, 'total', d.get('totalItems'), '|', ' ; '.join((i['volumeInfo'].get('title', '')[:50] + ' ' + str(i['volumeInfo'].get('publishedDate', ''))) for i in items[:5]))
    except Exception as e:
        print('GB', q, 'ERR', type(e).__name__, getattr(e, 'code', ''))
    n += 1; time.sleep(1.6)
for q in ['"words commencing Henry"', '"words beginning McClellan"']:
    url = 'https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print('IA', q, 'hits', len(hits), '|', ' ; '.join(str(h.get('fields', {}).get('identifier', h.get('_id', '')))[:60] for h in hits[:5]))
    except Exception as e:
        print('IA', q, 'ERR', type(e).__name__, getattr(e, 'code', ''))
    n += 1; time.sleep(1.6)
print('requests', n)
