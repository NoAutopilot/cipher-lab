#!/usr/bin/env python3
"""ECK-S65G (11 Oct 2026, account 1, for LANE DEFAULT-A1-1840): Google Books API (keyed, country=US) snippet sweep of The Papers of Ulysses
S. Grant vol. 13 (Nov 1864 - 20 Feb 1865; not on the Internet Archive) for E589-E592, the volume FM-S65B and FV-L17b could not search (503/429).
Control first (FM-S65B's vol. 13 hit for E531, '"six vessels" Oriental'); if the control errors, stop (one try per query, 503/429 stops the host).
Hit = a snippet from a vol. 13 id whose bolded words cover >= 3 of the query's content words. >= 2 s apart; never prints the key."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}
P = [('control E531', '"six vessels" Oriental'),
     ('E589', 'Monohansett Beckwith Sheldon Monroe'),
     ('E590', '"retained no copy" staff officer Seward'),
     ('E591', 'Radford torpedoes Lynch Bureau of Ordnance Ironsides'),
     ('E592', 'Camman gold Cooper naval officer')]
STOP = {'the', 'and', 'for', 'are', 'was', 'with', 'from', 'not', 'his', 'has', 'all', 'her', 'off', 'bureau'}
n = 0
for e, q in P:
    words = {w.lower() for w in re.findall(r"[A-Za-z0-9']+", q) if len(w) > 2 and w.lower() not in STOP}
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q + ' intitle:Grant', 'country': 'US', 'maxResults': 20, 'key': K})
    try:
        n += 1
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    except Exception as ex:
        print(f'{e}\t{q}\tERR {str(ex)[:60]} -- host stopped'); break
    hits = []
    for it in d.get('items', []):
        if it.get('id') not in V13: continue
        s = (it.get('searchInfo') or {}).get('textSnippet', '')
        bold = {b.lower() for b in re.findall(r'<b>([^<]+)</b>', s)}
        cov = sum(1 for w in words if any(w in b for b in bold))
        hits.append((it['id'], cov, s))
    if not hits: print(f'{e}\t{q}\tNO vol.13 HIT (totalItems {d.get("totalItems")})')
    for vid, cov, s in hits: print(f'{e}\t{q}\tv13 {vid}\tcov {cov}/{len(words)}\t{" ".join(s.split())[:400]}')
    time.sleep(2)
print('# googleapis requests', n)
