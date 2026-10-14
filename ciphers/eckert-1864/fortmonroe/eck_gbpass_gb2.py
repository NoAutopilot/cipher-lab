#!/usr/bin/env python3
"""GB-PASS (14 Oct 2026, account 1), step 2 after eck_gbpass_gb.py's two controls answered 200 without a vol. 13 hit (A: 351 items,
vol. 13 not in the top 20; B, the 12 Oct hitting form: totalItems 0). Control C: the vol. 13 id's own record (does the API still serve
mnRjmhe3QLoC). Control D: a rarer word from the same E531 snippet, '"Suwo Nada"' (no intitle). Targets run without intitle only if D hits
vol. 13. One try per query, 503/429 stops. >= 2 s apart; never prints the key."""
import json, os, re, sys, time, urllib.parse, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(__file__))
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}
def get(url):
    try:
        return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    except urllib.error.HTTPError as ex: return f'HTTP {ex.code}'
    except Exception as ex: return f'ERR {str(ex)[:60]}'
n = 0
for vid in ['mnRjmhe3QLoC']:
    d = get(f'https://www.googleapis.com/books/v1/volumes/{vid}?' + urllib.parse.urlencode({'country': 'US', 'key': K})); n += 1
    if isinstance(d, str): print(f'control C meta {vid}\t{d}'); print('# googleapis requests', n); sys.exit(2)
    v = d.get('volumeInfo', {}); a = d.get('accessInfo', {})
    print(f'control C meta {vid}\t{v.get("title")} {v.get("subtitle","")}\t{v.get("publishedDate")}\tpageCount {v.get("pageCount")}\t{a.get("viewability")}\ttextToSpeech/search {a.get("textToSpeechPermission")}')
    time.sleep(2)
def search(lab, q):
    global n
    d = get('https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 40, 'key': K})); n += 1
    time.sleep(2)
    if isinstance(d, str): print(f'{lab}\t{q}\t{d}'); return None
    hits = [(it['id'], ' '.join(((it.get('searchInfo') or {}).get('textSnippet', '')).split())[:400]) for it in d.get('items', []) if it.get('id') in V13]
    if not hits: print(f'{lab}\t{q}\tNO vol.13 HIT (totalItems {d.get("totalItems")}; ids {[it["id"] for it in d.get("items", [])][:8]})')
    for vid, s in hits: print(f'{lab}\t{q}\tv13 {vid}\t{s}')
    return bool(hits)
d = search('control D', '"Suwo Nada"')
if d:
    for e, q in [('E590', '"retained no copy" staff officer Seward'), ('E591', 'Radford torpedoes Lynch Bureau of Ordnance Ironsides'),
                 ('E592', 'Camman gold Cooper naval officer'), ('E589 looser', 'Monohansett Monroe')]:
        if search(e, q) is None: print('# host error -- stopped'); break
else:
    print('# control D did not hit vol. 13 -- no target query run')
print('# googleapis requests', n)
