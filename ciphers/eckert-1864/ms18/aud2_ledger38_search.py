#!/usr/bin/env python3
"""AUD2-LEDGER-38 (10 Oct 2026): phrase searches for E378 (16 Aug 1864, Princess/Keith) and E381 (27 July 1865, Ryan witness).
Google Books (key + country=US), IA global full text (be-api), IA advancedsearch for OR/ORN volume ids, be-api per-volume terms.
Usage: aud2_ledger38_search.py > aud2_ledger38_search.out. 1.6 s between requests. A miss is a search result, never a novelty verdict (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
KEY = os.environ.get('GOOGLE_BOOKS_KEY', '')
n = {}
def get(url, host):
    n[host] = n.get(host, 0) + 1
    try: return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e: return {'_err': str(e)[:80]}
    finally: time.sleep(1.6)
GB = ['"with malice toward none"',  # positive control
      '"may be released and allowed to proceed"', '"detectives along to observe"', '"observe the course of trade"',
      '"schooner Princess" Keith 1864', '"Princess" Keith Halifax detectives Dana', '"Keith\'s message"',
      '"action in respect to Ryan"', '"send forward the witness"', '"allow no communication by or with him"',
      '"spare no pains to find" witness Ryan', 'Barton Memphis Ryan witness Stanton 1865']
for q in GB:
    d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&maxResults=10&country=US&key=' + KEY, 'googleapis')
    if '_err' in d: print('GB', q, 'ERR', d['_err'].replace(KEY, '<key>') if KEY else d['_err']); continue
    items = d.get('items', [])
    print('GB', q, d.get('totalItems'), '|', ' || '.join(f"{i['volumeInfo'].get('title','?')[:50]} ({i['volumeInfo'].get('publishedDate','?')}; {i['id']}): {i.get('searchInfo',{}).get('textSnippet','')[:140]}" for i in items[:6]))
IA = ['with malice toward none', 'may be released and allowed to proceed', 'detectives along to observe', 'schooner Princess Keith',
      'action in respect to Ryan', 'send forward the witness mentioned', 'allow no communication by or with him']
for ph in IA:
    d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(f'"{ph}"'), 'be-api')
    if '_err' in d: print('IA', ph, 'ERR', d['_err']); continue
    h = d.get('hits', {}).get('hits', []); t = d.get('hits', {}).get('total', len(h)); t = t.get('value') if isinstance(t, dict) else t
    print('IA', repr(ph), t, '|', '; '.join(f"{x['fields'].get('identifier',['?'])[0]} ({(x['fields'].get('meta_title') or ['?'])[0][:50]})" for x in h[:6]))
# volume ids
for q in ['title:("official records of the union and confederate navies") AND volume:3', 'identifier:officialrecordso*']:
    d = get('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(q) + '&fl[]=identifier&fl[]=title&fl[]=volume&rows=60&output=json', 'archive.org')
    print('ADV', q, ' '.join(f"{r['identifier']}[{r.get('volume','')}]" for r in d.get('response', {}).get('docs', [])))
VOLS = {'warofrebellion0304rootrich': ['Princess', 'Keith', 'Ryan'], 'warofrebellion0305rootrich': ['Ryan', 'Barton'],
        'officialrecordso0003unse': ['Princess', 'Keith']}
for ident, terms in VOLS.items():
    for t in terms:
        d = get(f'https://be-api.us.archive.org/fts/v1/search?q={urllib.parse.quote(t)}&identifier={ident}', 'be-api')
        if '_err' in d: print('VOL', ident, t, 'ERR', d['_err']); continue
        h = d.get('hits', {}).get('hits', [])
        sn = ' ... '.join(' '.join(x.get('highlight', {}).get('text', [])[:3]) for x in h[:1])[:400]
        print('VOL', ident, repr(t), len(h), '|', sn)
print('requests', n)
