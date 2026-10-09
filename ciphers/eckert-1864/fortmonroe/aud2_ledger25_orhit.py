#!/usr/bin/env python3
"""AUD2-LEDGER-25 (9 Oct 2026): follow-up on print_check hits for E309 phrases: IA be-api highlights (across IA) and Google Books
searchInfo snippets (country=US, key from GOOGLE_BOOKS_KEY, never printed), to see whether the OR hits are this telegram. 2 s apart."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
def get(u): return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=90))
for q in ['"all the steamers that can possibly be spared"', '"the Illinois is nearly discharged"']:
    try:
        d = get('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q}))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print('BE-API', q, len(hits))
        for h in hits[:6]:
            src = h.get('fields', {}) or h.get('_source', {}) or {}
            print('  id', h.get('_id') or src.get('identifier'))
            for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('    ', ' '.join(s.split())[:400])
    except Exception as e: print('BE-API', q, 'ERROR', e)
    time.sleep(2)
    try:
        d = get('https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10, 'key': os.environ.get('GOOGLE_BOOKS_KEY', '')}))
        print('GB', q, d.get('totalItems'))
        for i in d.get('items', [])[:5]:
            v = i['volumeInfo']; print('   ', i['id'], v.get('title', '')[:60], v.get('publishedDate'), '|', i.get('searchInfo', {}).get('textSnippet', '')[:300])
    except Exception as e: print('GB', q, 'ERROR', e)
    time.sleep(2)
