#!/usr/bin/env python3
"""AUD2-LEDGERN2-4 (10 Oct 2026, account-4): Google Books snippets aimed at the Quartermaster General's annual report 1865 (PhNAAAAAYAAJ /
OeuqO9UOOZIC) for N2-HF; control = AUD2-LEDGERN2-1's vessel-table hit. Key from env, country=US, never printed. >= 1.6 s apart. Output in
aud2_n2_4_gb_qmg.out. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
Q = ['"Cossack" "Collyer" side-wheel steamer quartermaster',
     'quartermaster general annual report 1865 "Sixth Corps" transported Washington "City Point" steamers 1864',
     'quartermaster general report 1865 Rucker steamboats Baltimore Philadelphia "New York" transport troops Washington 1864',
     'quartermaster general report 1865 "flag-of-truce" boats "Fort Monroe" transports']
for q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'maxResults': 10, 'country': 'US', 'key': K})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
        it = d.get('items', []); print(q, '|', d.get('totalItems'), 'total')
        for v in it[:8]:
            vi = v.get('volumeInfo', {}); sn = (v.get('searchInfo') or {}).get('textSnippet', '')
            print('   ', v['id'], '|', vi.get('title', '')[:60], vi.get('publishedDate', ''), '|', sn[:220])
    except Exception as e: print(q, '| ERR', str(e)[:100])
    time.sleep(1.6)
print('googleapis requests', len(Q))
