#!/usr/bin/env python3
"""FM65-B (10 Oct 2026, account 1): IA be-api full-text snippet search for the FM65-B rows: Grant Papers 10-11, Butler's Correspondence IV-V, and four
whole-collection queries (no identifier). >= 1.8 s apart. A miss is a search result, not a statement about print (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(None, '"proceed without delay to report in person to General Sherman at Savannah"'),
     (None, '"Winants is hardly capable"'), (None, '"Eliza Hancox"  Winants'),
     (None, '"not mustered for December"'), (None, 'Brice "second expedition" paymaster mustered'),
     (None, '"dispense with Blackstone"'),
     (None, 'Sedgwick Baltic Ariel Victor Illinois Baltimore ordered "January 3"'),
     (None, '"report of the Wilmington expedition" lost overcoat'),
     (None, '"consider the order as countermanded" Baltic Monroe'),
     (None, 'Stanton "start for Savannah" "arrived here safely"'),
     (None, '"Elias Smith" Tribune expedition permission Ingalls'),
     (None, 'soonest ship troops Baltic Annapolis coal docks'),
     (None, '"has not heard from them since" Baltic Baltimore Sedgwick')]
n = 0
for ident, q in Q:
    p = {'q': q}
    if ident: p['identifier'] = ident
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        hits = d.get('hits', {}).get('hits', [])
        print(ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:4]:
            print('   ', (h.get('fields', {}) or {}).get('identifier'), (h.get('fields', {}) or {}).get('title', '')[:60] if isinstance((h.get('fields', {}) or {}).get('title', ''), str) else '')
            for s in (h.get('highlight', {}) or {}).get('text', [])[:3]: print('      ', s.replace('\n', ' ')[:300])
    except Exception as e: print(ident or '(all)', '|', q, '| ERR', str(e)[:100])
    n += 1; time.sleep(1.8)
print('be-api requests', n)
