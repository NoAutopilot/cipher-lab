#!/usr/bin/env python3
"""ECK-S65G (11 Oct 2026, account 1, for LANE DEFAULT-A1-1840): units 1 and 3 of the FM-S65B Remaining gaps.
Unit 1: the three IA be-api whole-collection phrase checks that answered HTTP 502 twice on 10 Oct (E590 Seward, E592 Cammann,
E593 ponchos), with a positive control first (the Anderson telegram query that hit OR I/47 pt 2 on 10 Oct).
Unit 3: the Sherman family letters (Thorndike 1894): IA advancedsearch for the identifier, metadata title check, then be-api
inside that identifier for E594 (Sherman to John Sherman, Fort Monroe 27 Mar 1865).
>= 2 s apart, one request at a time, descriptive UA, one retry after a pause on 5xx then stop. A miss is a search result (rule 10).
Usage: eck_s65g_beapi.py unit1|find|unit3 [IDENT]"""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
N = {'be-api': 0, 'archive.org': 0}

def get(url, host):
    for attempt in (1, 2):
        N[host] += 1
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        except Exception as e:
            print('   ERR', host, str(e)[:80], '(attempt', attempt, ')')
            if attempt == 1 and ('50' in str(e)):
                time.sleep(20); continue
            return None
        finally:
            time.sleep(2)

def beapi(q, ident=None):
    p = {'q': q}
    if ident: p['identifier'] = ident
    d = get('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p), 'be-api')
    if d is None: print(ident or '(all)', '|', q, '| UNCHECKED'); return
    hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
    print(ident or '(all)', '|', q, '|', len(hits), 'hits')
    for h in hits[:6]:
        src = h.get('fields', {}) or h.get('_source', {}) or {}
        print('   id', src.get('identifier') or h.get('_id'))
        for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('      ', ' '.join(s.split())[:300])

mode = sys.argv[1]
G13, G14 = 'papersofulyssess0013gran', 'papersofulyssess0014gran'
if mode == 'meta':  # title/volume check of the IA ids before searching inside them
    for ident in (G13, G14):
        d = get(f'https://archive.org/metadata/{ident}/metadata', 'archive.org')
        r = (d or {}).get('result', {})
        print(ident, '|', r.get('title'), '|', r.get('volume'), '|', r.get('date'), '|', r.get('collection'))
elif mode == 'unit1':
    beapi('"dispatches for you from Major-General Sherman"')  # positive control (hit on 10 Oct)
    beapi('"ponchos" Ingalls')  # FV-L17b's one unchecked whole-collection query (502 twice)
    beapi('ponchos Ingalls Sheridan 1865')
elif mode == 'g13':  # Grant Papers vol. 13 (Nov 1864 - 20 Feb 1865): the volume for E589-E592, unchecked (Google Books 429)
    beapi('"six vessels"', G13)  # positive control: FM-S65B's vol. 13 Google Books hit for E531
    beapi('Monohansett', G13)                       # E589
    beapi('"retained no copy"', G13)                # E590
    beapi('"staff officer" Seward', G13)            # E590
    beapi('Radford torpedoes', G13)                 # E591
    beapi('Lynch torpedoes', G13)                   # E591
    beapi('Camman', G13)                            # E592
    beapi('"sell gold"', G13)                       # E592
    beapi('Cashier "National Bank" Norfolk', G13)   # 5914/2 (vol. 14 hit on 10 Oct; vol. 13 for completeness)
print('requests', N)
# appended 11 Oct 2026 19:0x UTC: the page of FM-S65B's 5914/2 hit, through vol. 14's own snippets (running heads / index lines carry page numbers)
if mode == 'page5914':
    N['be-api'] = 0
    beapi('"Gordon\'s Commission"', G14)
    beapi('Gordon commission Norfolk', G14)
    beapi('"Cashier of the National Bank"', G14)
    print('requests', N)
