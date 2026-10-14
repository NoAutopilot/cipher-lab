#!/usr/bin/env python3
"""GB-PASS (14 Oct 2026, account 1, for LANE DEFAULT-A1-1840-14): eck_gb2_gb.py with a second-form control first, per GB-2's
Remaining gaps item 1. Control A is the E531 query WITHOUT `intitle:Grant` (tells host load apart from a query-form 503); control B is
GB-2's own form (with `intitle:Grant`). The target queries run in the form of whichever control returned a vol. 13 hit (B's form if both).
If neither control hits, no target query runs. One try per query; 503/429 stops the host. Hit = a snippet from a vol. 13 id
(mnRjmhe3QLoC / ij8fAQAAMAAJ). >= 2 s apart; never prints the key."""
import json, os, re, sys, time, urllib.parse, urllib.request, urllib.error
K = os.environ.get('GOOGLE_BOOKS_KEY', '')
V13 = {'mnRjmhe3QLoC', 'ij8fAQAAMAAJ'}
T = [('E590', '"retained no copy" staff officer Seward'),
     ('E591', 'Radford torpedoes Lynch Bureau of Ordnance Ironsides'),
     ('E592', 'Camman gold Cooper naval officer'),
     ('E589 looser', 'Monohansett Monroe')]
STOP = {'the', 'and', 'for', 'are', 'was', 'with', 'from', 'not', 'his', 'has', 'all', 'her', 'off', 'bureau'}
n = 0
def run(e, q, suffix):
    global n
    words = {w.lower() for w in re.findall(r"[A-Za-z0-9']+", q) if len(w) > 2 and w.lower() not in STOP}
    url = 'https://www.googleapis.com/books/v1/volumes?' + urllib.parse.urlencode({'q': q + suffix, 'country': 'US', 'maxResults': 20, 'key': K})
    n += 1
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=60))
    except urllib.error.HTTPError as ex:
        print(f'{e}\t{q}{suffix}\tHTTP {ex.code}'); time.sleep(2); return None
    except Exception as ex:
        print(f'{e}\t{q}{suffix}\tERR {str(ex)[:60]}'); time.sleep(2); return None
    hits = []
    for it in d.get('items', []):
        if it.get('id') not in V13: continue
        s = (it.get('searchInfo') or {}).get('textSnippet', '')
        bold = {b.lower() for b in re.findall(r'<b>([^<]+)</b>', s)}
        hits.append((it['id'], sum(1 for w in words if any(w in b for b in bold)), s))
    if not hits: print(f'{e}\t{q}{suffix}\tNO vol.13 HIT (totalItems {d.get("totalItems")})')
    for vid, cov, s in hits: print(f'{e}\t{q}{suffix}\tv13 {vid}\tcov {cov}/{len(words)}\t{" ".join(s.split())[:400]}')
    time.sleep(2)
    return bool(hits)
a = run('control A (no intitle)', '"six vessels" Oriental', '')
b = run('control B (GB-2 form)', '"six vessels" Oriental', ' intitle:Grant')
if a is None and b is None:
    print('# both controls errored -- host stopped'); print('# googleapis requests', n); sys.exit(2)
suffix = ' intitle:Grant' if b else ('' if a else None)
if suffix is None:
    print('# no control returned a vol. 13 hit -- no target query run'); print('# googleapis requests', n); sys.exit(3)
for e, q in T:
    if run(e, q, suffix) is None:
        print('# host error -- stopped'); break
print('# googleapis requests', n)
