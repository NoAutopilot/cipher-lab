#!/usr/bin/env python3
"""AUD2-LEDGER-36: Google Books follow-ups inside Steers, The Lincoln Assassination: The Evidence (GvYpUeuPPrAC) and on the three telegrams'
decoded phrases. Key from env (never printed), country=US, 1.7 s apart. Prints only hits whose id is in the snippet set or whose snippet names the item."""
import json, os, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
QS = ['"Boulware" Seddon "King & Queen"', '"Boulware" "Dana"  assassination evidence', '"Boulware" Halleck Richmond captured',
      '"Wm. Boulware"', '"Boulware" "Judge Advocate General" 1865', '"Boulware" "Norwell"', '"Boulware" Steers evidence arrest Bingham Holt',
      '"Secretary of War directs that you arrest"', '"to report to the Judge Advocate General" Boulware',
      '"confiscating officer for the rebel government"', '"Thomas J. Campbell" Knoxville Thomas Nashville 1865 arrested',
      '"Campbell" receiver sequestration Knoxville arrested Augusta 1865',
      '"for how many horses" forage rail Sherman 1864', '"horses in excess of" Sherman forage rail 1864 McCallum']
n = 0
for q in QS:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q)
            + '&country=US&maxResults=10&key=' + os.environ.get('GOOGLE_BOOKS_KEY', ''), headers={'User-Agent': UA}), timeout=60))
    except Exception as e:
        d = {'_err': str(e)[:80]}
    n += 1; time.sleep(1.7)
    print('GB', repr(q), d.get('_err') or d.get('totalItems'))
    for it in (d.get('items') or [])[:10]:
        v = it['volumeInfo']; s = (it.get('searchInfo') or {}).get('textSnippet', '')
        print('   ', it['id'], '|', v.get('title', '')[:60], '|', v.get('publishedDate'), '|', s[:260].replace('\n', ' '))
print('requests googleapis', n)
