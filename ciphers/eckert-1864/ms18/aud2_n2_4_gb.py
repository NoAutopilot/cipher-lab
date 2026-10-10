#!/usr/bin/env python3
"""AUD2-LEDGERN2-4 (10 Oct 2026, account-4): G3 decoded-phrase pass on Google Books for N2-HF (QMG to Ingalls, 6 Aug 1864), phrases and
families FV-N2d did not run (snippets read, not totals). Key from env, country=US, never printed. Positive control first (N2-HC's printed phrase,
OR I/37 pt 2 p.573). >= 1.6 s apart. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"single and separate command will"',
     '"flag of truce boats and the boats about"', '"estimated by General Rucker"', '"capacity of 19,000 infantry"',
     '"kept in readiness for any necessary movement"', '"sent them all to City Point"', '"room for over 30,000 men"',
     'Meigs Ingalls steamboats Baltimore Philadelphia "New York" "30,000 men" 1864',
     'Meigs Ingalls "flag-of-truce boats" "Fort Monroe" August 1864 transports',
     'Quartermaster General report 1865 Rucker steamers "City Point" "Sixth Corps" "Nineteenth Corps" transports Washington',
     'Ingalls "capacity for carrying troops" transports 1864']
n = 0
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        it = d.get('items', [])
        print(q, '|', d.get('totalItems'), 'total |', len(it))
        for v in it[:8]:
            vi = v.get('volumeInfo', {}); sn = (v.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', v['id'], '|', vi.get('title', '')[:60], vi.get('publishedDate', ''), '|', v.get('accessInfo', {}).get('viewability'), '|', sn[:220])
    except Exception as e: print(q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.6)
print('googleapis requests', n)
