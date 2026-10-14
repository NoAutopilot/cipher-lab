#!/usr/bin/env python3
"""GB-2 (14 Oct 2026, account 2, for LANE DEFAULT-A2-0911-14), the one retry after gb2_verbael.py's 503: control again, then the
metadata of the two full-view 1725 Verbael ids found by gb2_verbael.py, then date-phrase snippet searches restricted by intitle:Verbael
for Beverning's 17/27 June and 22 Aug 1653 letters and the 18 July 1653 companion (Bijdragen X p.298: Verbael No. 37, pp.252-253).
A 503/429 stops the host. >= 2 s apart; never prints the key."""
import json, os, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
VIDS = ['vZzvg46MRdEC', 'T2JVAAAAYAAJ']
Q = [('control', 'search', 'intitle:Thurloe "state papers" Birch')]
Q += [(f'meta {v}', 'meta', v) for v in VIDS]
Q += [('jul18', 'search', 'intitle:Verbael "18 Julij 1653"'),
      ('jun27', 'search', 'intitle:Verbael "27 Junij 1653"'),
      ('jun17', 'search', 'intitle:Verbael "17 Junij 1653"'),
      ('aug22', 'search', 'intitle:Verbael "22 Augusti 1653"'),
      ('griffier', 'search', 'intitle:Verbael Beverningk Nieupoort Westmunster Julij Griffier')]
n = 0
for lab, kind, q in Q:
    if kind == 'meta':
        url = f'https://www.googleapis.com/books/v1/volumes/{q}?' + urllib.parse.urlencode({'country': 'US', 'key': K})
    else:
        url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        n += 1
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    except Exception as ex:
        print(f'{lab}\t{q}\tERR {str(ex)[:60]} -- host stopped'); break
    if kind == 'meta':
        v = d.get('volumeInfo', {}); a = d.get('accessInfo', {})
        print(f'{lab}\t{v.get("title","")[:120]}\t{v.get("publishedDate")}\tpageCount {v.get("pageCount")}\t{a.get("viewability")}'
              f'\tpdf {a.get("pdf",{}).get("isAvailable")}\tepub {a.get("epub",{}).get("isAvailable")}\tpublicDomain {a.get("publicDomain")}'
              f'\t{v.get("industryIdentifiers")}\t{v.get("canonicalVolumeLink")}')
    else:
        print(f'{lab}\t{q}\ttotalItems {d.get("totalItems")}')
        for it in d.get('items', []):
            v = it.get('volumeInfo', {})
            s = ' '.join(((it.get('searchInfo') or {}).get('textSnippet', '')).split())[:400]
            print(f'  {it["id"]}\t{v.get("title","")[:70]}\t{v.get("publishedDate","")}\t{it.get("accessInfo",{}).get("viewability")}\t{s}')
        if lab == 'control' and not d.get('items'):
            print('control found nothing -- stopped'); break
    time.sleep(2)
print('# googleapis requests', n)
