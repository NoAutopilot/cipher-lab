#!/usr/bin/env python3
"""AUD2-LEDGER-22 (9 Oct 2026, account 4): (a) IA be-api full-text search inside named identifiers (snippets only, no page numbers), and
(b) Google Books API phrase queries (key from GOOGLE_BOOKS_KEY, country=US, never printed), for E291/E292 (eckert-1864); one request at a
time, >= 2 s apart. A miss is a search result for the log (rule 10), never a novelty verdict. Usage: aud2_ledger22_search.py > .out"""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
BE = [('papersofulyssess0012gran', '"Coggins"'), ('papersofulyssess0012gran', '"M. R. Morgan"'),
      ('papersofulyssess0012gran', '"Harpers Ferry"'), ('privateofficialc05butl', '"Coggins"'),
      ('papersofulyssess0011gran', '"Bickford"'), ('papersofulyssess0011gran', '"White House" telegraph')]
GB = [('E291', '"Bickford" "White House" 1864 telegraph Eckert'), ('E291', '"Bickford has a card"'),
      ('E291', '"not to build any farther"'), ('E291', '"Bickford" "card" cipher telegraph 1864'),
      ('E292', '"lines are down" "order by telegraph" Monroe'), ('E292', '"Coggins Point" "1,200 head"'),
      ('E292', '"Coggins" "Morgan" "Harpers Ferry" commissary 1864'), ('E292', '"Thomas Wilson" commissary "Coggins"')]
for ident, q in BE:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'identifier': ident})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
        print('be-api', ident, '|', q, '|', len(hits))
        for h in hits[:2]:
            for s in (h.get('highlight', {}) or {}).get('text', [])[:8]: print('   ', ' '.join(s.split())[:300])
    except Exception as e: print('be-api', ident, '|', q, '| ERROR', e)
    time.sleep(2)
key = os.environ.get('GOOGLE_BOOKS_KEY', '')
for e, q in GB:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': key})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30))
        print(f'gb {e}\t{q}\ttotal={d.get("totalItems", 0)}')
        for it in d.get('items', [])[:6]:
            v = it['volumeInfo']; s = it.get('searchInfo', {}).get('textSnippet', '')
            print(f'    {v.get("title","")} ({v.get("publishedDate","")}) [{it["accessInfo"].get("viewability")}] :: {s}')
    except Exception as ex:
        print(f'gb {e}\t{q}\tERROR {type(ex).__name__} {getattr(ex, "code", "")}')
    time.sleep(2)
print('requests: be-api', len(BE), 'google books', len(GB))
