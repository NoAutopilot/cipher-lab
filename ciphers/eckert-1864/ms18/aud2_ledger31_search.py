#!/usr/bin/env python3
"""AUD2-LEDGER-31 (9 Oct 2026): E346 second-verifier print/scholarship search: IA be-api full text inside named items and across all items,
Google Books (keyed, country=US), OpenAlex, CORE. >=1.5 s apart per host. Keys from the environment, never printed. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
def get(url, hdr=None):
    h = dict(UA); h.update(hdr or {})
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60))
    except Exception as e:
        return {'_err': str(e)[:120]}
def fts(q, ident=None):
    u = 'https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + (f'&identifier={ident}' if ident else '') + '&size=25'
    d = get(u); time.sleep(1.6)
    if '_err' in d: return f'ERR {d["_err"]}'
    hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
    tot = d.get('hits', {}).get('total') if isinstance(d.get('hits'), dict) else len(hits)
    out = []
    for h in hits[:12]:
        s = h.get('_source', h); f = h.get('fields', {})
        hl = h.get('highlight', {}).get('text', [''])
        out.append(f"{s.get('identifier') or f.get('identifier')}: {' / '.join(x.replace(chr(10),' ')[:300] for x in hl[:2])}")
    return f'{tot} | ' + ' || '.join(out)
for ident, terms in [('dynamitefiendchi0000lara', ['machinery', 'locomotives', 'Norris', 'Murray', 'Gordon', 'Bruce', 'Montreal', 'Gilpin', 'Stanton'])]:
    for t in terms: print('IA-in', ident, repr(t), fts(t, ident), flush=True)
for q in ['"Gordon, Bruce & Co"', '"Gordon Bruce" Halifax', '"Keith" locomotives Halifax Norris', '"Mitchell, Kenner"', '"Alexander Keith" locomotives', '"Keith" "Norris" locomotives 1864']:
    print('IA-all', repr(q), fts(q), flush=True)
gk = os.environ.get('GOOGLE_BOOKS_KEY', '')
for q in ['"Alexander Keith" locomotives Halifax 1864', '"Keith" locomotives Norris Halifax rebel', '"Gordon, Bruce" Keith Halifax 1864', '"Mitchell, Kenner" Montreal', 'Stanton Gilpin Keith locomotives', '"James Bruce" Halifax 1864 machinery']:
    d = get('https://www.googleapis.com/books/v1/volumes?q=' + urllib.parse.quote(q) + '&maxResults=10&country=US&key=' + gk); time.sleep(1.6)
    items = d.get('items', [])
    print('GB', repr(q), d.get('totalItems', d.get('_err')), ' || '.join(f"{i['volumeInfo'].get('title')} ({i['volumeInfo'].get('publishedDate')}): {i.get('searchInfo',{}).get('textSnippet','')[:200]}" for i in items[:8]), flush=True)
ok = os.environ.get('OPENALEX_KEY', '')
for q in ['Alexander Keith Halifax Confederate agent locomotives', 'Confederate agents Halifax Nova Scotia 1864 machinery Montreal']:
    d = get('https://api.openalex.org/works?per_page=8&search=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + ok}); time.sleep(1.6)
    print('OA', repr(q), d.get('meta', {}).get('count', d.get('_err')), ' || '.join(f"{w.get('display_name')} ({w.get('publication_year')})" for w in d.get('results', [])[:8]), flush=True)
ck = os.environ.get('CORE_API_KEY', '')
for q in ['"Alexander Keith" Halifax Confederate 1864', 'Keith locomotives Norris Confederate Halifax']:
    d = get('https://api.core.ac.uk/v3/search/works/?limit=8&q=' + urllib.parse.quote(q), {'Authorization': 'Bearer ' + ck}); time.sleep(1.6)
    print('CORE', repr(q), d.get('totalHits', d.get('_err')), ' || '.join(f"{w.get('title')} ({w.get('yearPublished')})" for w in d.get('results', [])[:8]), flush=True)
