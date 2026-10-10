"""FV-MS18n: Chronicling America (loc.gov JSON) by date window for E375 (Isaac Surratt, Baltimore, Oct 1865) and Google Books (key, country=US) phrase
queries on decoded phrases of E371 E374 E375 (G3). >= 2 s apart. A miss is a search result (rule 10)."""
import json, os, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n = 0
for q, dr in [('Isaac Surratt Baltimore', '1865-10-15/1865-11-30'), ('Isaac Surratt arrested', '1865-10-15/1865-12-31'), ('Surratt Baker Baltimore', '1865-10-15/1865-11-30')]:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://www.loc.gov/collections/chronicling-america/?fo=json&c=15&dates=' + dr + '&q=' + urllib.parse.quote(q), headers=UA), timeout=90))
    except Exception as e:
        d = {'_err': str(e)[:100]}
    n += 1; time.sleep(2)
    print('CA', repr(q), dr, d.get('_err') or (d.get('pagination') or {}).get('of'), flush=True)
    for r in (d.get('results') or [])[:10]:
        print('   ', str(r.get('date')), '|', str(r.get('partof_title') or r.get('title'))[:60], '|', r.get('id', '')[-55:], '|', ' '.join(r.get('description') or [])[:200].replace('\n', ' '), flush=True)
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in ['"close watch on the man referred to"', '"Isaac Surratt" "close watch" 1865', '"withdraw from Colonel Ferry"', '"Ferry" "all Government funds" Louisville 1864',
          '"Devereux should leave his present duties"', '"Devereux" McCallum Anderson "February 6, 1864"']:
    u = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 10}) + ('&key=' + K if K else '')
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
    except Exception as e:
        d = {'_err': str(e)[:80]}
    n += 1; time.sleep(2)
    print('GB', q, d.get('_err') or d.get('totalItems'), flush=True)
    for it in (d.get('items') or [])[:8]:
        v = it['volumeInfo']; print('   ', str(v.get('title'))[:60], v.get('publishedDate'), '|', str((it.get('searchInfo') or {}).get('textSnippet'))[:200], flush=True)
print('requests', n)
