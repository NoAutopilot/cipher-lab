#!/usr/bin/env python3
"""GB-PASS2 (15 Oct 2026, account 2, for LANE DEFAULT-A2-0209-15): Google Books for the Baluze 169 f.22r phrases of VER-BAL22's
phrases.txt (5 of 6 answered HTTP 503 on 14 Oct). Control first: an Avenel volume by title (the canonical series for these letters);
if the control finds nothing or errors, no phrase query runs. Each phrase is sent quoted, then two targeted keyword queries.
A hit is reported with its snippet and the count of query words the API bolded; a snippet hit is a location, not a reading.
A 503/429 stops the run (exit 2). Keyed, country=US, >= 2 s apart; never prints the key."""
import json, os, re, sys, time, urllib.parse, urllib.request, urllib.error
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
HERE = os.path.dirname(os.path.abspath(__file__))
PH = [l.strip() for l in open(os.path.join(HERE, 'phrases.txt'), encoding='utf-8') if l.strip() and not l.startswith('#')]
Q = [('control', 'intitle:Richelieu "Lettres, instructions diplomatiques"')]
Q += [(f'phrase {i+1}', f'"{p}"') for i, p in enumerate(PH)]
Q += [('kw Milandre Ransau', 'Milandre Ransau commandement 1639'), ('kw Melander Rantzau', 'Melander Rantzau Hesse 1639 Avaux Bouthillier')]
n = 0
for lab, q in Q:
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q, 'country': 'US', 'maxResults': 20, 'key': K})
    n += 1
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    except urllib.error.HTTPError as ex:
        print(f'{lab}\t{q}\tHTTP {ex.code} -- host stopped'); print('# googleapis requests', n); sys.exit(2)
    except Exception as ex:
        print(f'{lab}\t{q}\tERR {str(ex)[:60]} -- host stopped'); print('# googleapis requests', n); sys.exit(2)
    words = {w.lower() for w in re.findall(r"[A-Za-zÀ-ÿ']+", q) if len(w) > 3 and not w.startswith('intitle')}
    print(f'{lab}\t{q}\ttotalItems {d.get("totalItems")}')
    for it in d.get('items', [])[:20]:
        v = it.get('volumeInfo', {})
        s = ' '.join(((it.get('searchInfo') or {}).get('textSnippet', '')).split())
        bold = {b.lower() for b in re.findall(r'<b>([^<]+)</b>', s)}
        cov = sum(1 for w in words if any(w in b or b in w for b in bold))
        print(f'  {it["id"]}\t{v.get("title","")[:70]}\t{v.get("publishedDate","")}\t{it.get("accessInfo",{}).get("viewability")}\tcov {cov}/{len(words)}\t{s[:300]}')
    if lab == 'control' and not d.get('items'):
        print('control found nothing -- stopped'); print('# googleapis requests', n); sys.exit(3)
    time.sleep(2)
print('# googleapis requests', n)
