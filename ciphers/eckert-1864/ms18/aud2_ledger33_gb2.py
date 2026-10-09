#!/usr/bin/env python3
"""AUD2-LEDGER-33 (9 Oct 2026): Google Books follow-ups for E358 on the leads of aud2_ledger33_search.out (Katz, 'The Mysterious Prisoner', Civil War Times
Illustrated 21 (7), 1982; Life and Adventures of Gen. W.A.C. Ryan, 1876; Papers of Andrew Johnson, the Ryan protest, M619 roll 359): phrase queries on the
telegram's own clear words. Key from env, never printed; country=US; >= 1.7 s apart. A miss is a search result, never a verdict."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
n = 0
for q in ['"close and secure custody" Ryan', '"publication signed" Canada Ryan', '"substance or purport" papers Ryan Memphis', '"mysterious prisoner" Ryan Memphis Stanton telegram',
          '"Ryan" Memphis 1865 "M619" ironed parole', '"Jonathan George Ryan"', '"J. G. Ryan" Memphis 1865 Surratt', '"Barton" Memphis Ryan Surratt 1865 Stanton']:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&country=US&maxResults=8&key=' + os.environ.get('GOOGLE_BOOKS_KEY', ''), headers={'User-Agent': UA}), timeout=60))
    except Exception as e:
        d = {'_err': str(e)[:80]}
    n += 1; time.sleep(1.7)
    print('GB', repr(q), d.get('_err') or d.get('totalItems'))
    for it in (d.get('items') or [])[:8]:
        v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
        print('   ', it['id'], '|', v.get('title', '')[:70], '|', v.get('publishedDate'), '|', (it.get('accessInfo') or {}).get('viewability'), '|', s[:260].replace('\n', ' '))
print('requests', n)
