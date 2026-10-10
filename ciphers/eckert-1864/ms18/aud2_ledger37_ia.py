#!/usr/bin/env python3
"""AUD2-LEDGER-37 (10 Oct 2026): second-verifier IA advancedsearch for the editions FV-MS18n did not reach (OR ser. III vols 4-5, Trial of John H.
Surratt 1867, Baker's History of the U.S. Secret Service 1867, railroad histories), then be-api full-text queries given as ident::query args after 'be'.
>= 1.7 s apart. A miss is a search result (rule 10), never a novelty verdict."""
import json, sys, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
def get(url):
    try: return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=90))
    except Exception as e: return {'_err': str(e)[:80]}
n = {}
def tick(h): n[h] = n.get(h, 0) + 1; time.sleep(1.7)
a = sys.argv[1:]
if 'be' in a:
    for ident, q in [x.split('::') for x in a[a.index('be') + 1:]]:
        d = get('https://be-api.us.archive.org/fts/v1/search?q=' + urllib.parse.quote(q) + '&identifier=' + ident); tick('be-api')
        hits = (d.get('hits') or {}).get('hits') or []
        print('BE', ident, repr(q), d.get('_err') or (d.get('hits') or {}).get('total'))
        for h in hits[:3]:
            hl = (h.get('highlight') or {}).get('text') or []
            print('    ', ' || '.join(x.replace('\n', ' ')[:400] for x in hl[:4]))
else:
    for q in a:
        d = get('https://archive.org/advancedsearch.php?q=' + urllib.parse.quote(q) + '&fl[]=identifier&fl[]=title&fl[]=volume&fl[]=date&rows=25&output=json'); tick('archive.org')
        print('IA', repr(q), d.get('_err') or [(x.get('identifier'), str(x.get('title'))[:50], x.get('volume'), str(x.get('date'))[:4]) for x in (d.get('response') or {}).get('docs', [])])
print('requests', n)
