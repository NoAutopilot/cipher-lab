#!/usr/bin/env python3
"""GB-2 (14 Oct 2026, account 2, for LANE DEFAULT-A2-0911-14): Google Books API (keyed, country=US) for the 1725 Verbael
(Beverningh/Nieupoort/Jongestall/Van de Perre's London embassy journal, 1653-54). Control first: a query for a volume known to be
on Google Books (Birch's Thurloe State Papers); if the control errors or finds nothing, stop. One try per query; a 503/429 stops the
host (the job's one retry after 60 s is run by re-invoking this script). >= 2 s apart; never prints the key.
Prints, per query: totalItems and, per item, id, title, date, viewability, and the snippet."""
import json, os, sys, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
P = [('control', 'intitle:Thurloe "state papers" Birch'),
     ('verbael-1', '"Verbael gehouden door de Heeren"'),
     ('verbael-2', 'Verbael Beverningh Nieupoort Jongestal Perre Engelant 1653'),
     ('verbael-3', 'intitle:Verbael Beverning')]
P += [(a, b) for a, b in (x.split('=', 1) for x in sys.argv[1:])]
n = 0
for lab, q in P:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        n += 1
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    except Exception as ex:
        print(f'{lab}\t{q}\tERR {str(ex)[:60]} -- host stopped'); break
    print(f'{lab}\t{q}\ttotalItems {d.get("totalItems")}')
    for it in d.get('items', []):
        v = it.get('volumeInfo', {}); a = it.get('accessInfo', {})
        s = ' '.join(((it.get('searchInfo') or {}).get('textSnippet', '')).split())[:300]
        print(f'  {it["id"]}\t{v.get("title","")[:90]}\t{v.get("publishedDate","")}\t{a.get("viewability")}\t{s}')
    if lab == 'control' and not d.get('items'):
        print('control found nothing -- stopped'); break
    time.sleep(2)
print('# googleapis requests', n)
