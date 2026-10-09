#!/usr/bin/env python3
"""AUD2-LEDGER-32 (9 Oct 2026): Google Books snippet follow-ups (key from env, never printed, country=US) on the volumes the first pass surfaced:
the Army and Navy Official Gazette Crane orders (date and wording), Army and Navy Journal 1864/1865 (Crane, Brackett), The Last Battle of Winchester
(2013) and Summers, The Baltimore and Ohio in the Civil War (1951) on Grant's car. Snippets only; a miss is a search result."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
Q = ['"relieve Colonel J. C. Crane"', '"Colonel J. C. Crane" "Disbursing Officer"', '"Crane" "Inspector Quartermaster" "Military Railroads" September 1864',
     '"Last Battle of Winchester" Grant "Relay House" secret car', '"Relay House" Grant "special car" Monocacy Hunter 1864', 'Smith "Baltimore and Ohio" Grant Monocacy "special car" 1864 secret',
     '"Brackett" "Special Inspector of Cavalry"', '"Price" "Brackett" "Cavalry Bureau" 1864 St. Louis Grierson remount']
n = 0
for q in Q:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=10&key=' + os.environ.get('GOOGLE_BOOKS_KEY', ''), headers={'User-Agent': UA}), timeout=60))
    except Exception as e:
        d = {'_err': str(e)[:80]}
    n += 1; time.sleep(1.7)
    print('GB', repr(q), d.get('_err') or d.get('totalItems'))
    for it in (d.get('items') or [])[:10]:
        v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
        print('   ', it['id'], '|', v.get('title', '')[:60], '|', v.get('publishedDate'), '|', s[:300].replace('\n', ' '))
print('requests', n)
