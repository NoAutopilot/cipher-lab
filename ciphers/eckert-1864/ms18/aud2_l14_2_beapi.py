#!/usr/bin/env python3
"""AUD2-LEDGER14-2 (copy of fvl14b_beapi.py): IA be-api full-text search, whole collection (no identifier unless a third column names one), on decoded/plain phrases of E611 E612 E620 E621 N2-SA.
Positive control first: FV-MS18r's whole-collection hit ('what point he should come for that purpose' -> papersofulyssess0011gran).
Snippets only, no page numbers (CLAUDE.md access item 3). >= 2 s apart. A miss is a search result (rule 10), not a novelty verdict."""
import json, sys, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [(l.split(' | ') + [''])[:3] for l in open(sys.argv[1]).read().splitlines() if l.strip()]
n = 0
for lab, q, ident in Q:
    url = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(dict({'q': q}, **({'identifier': ident} if ident else {})))
    for attempt in (1, 2):
        try:
            n += 1
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
            hits = d.get('hits', {}).get('hits', []) if isinstance(d.get('hits'), dict) else d.get('hits', [])
            print(lab, '|', q, '|', ident or 'whole', '|', len(hits), flush=True)
            for h in hits[:6]:
                src = h.get('fields', {}) or h.get('_source', {}) or {}
                print('  id', (h.get('_id') or src.get('identifier', '')).split('|')[0])
                for s in (h.get('highlight', {}) or {}).get('text', [])[:2]: print('   ', ' '.join(s.split())[:400])
            break
        except Exception as e:
            print(lab, '|', q, '| ERROR', e, flush=True)
            if attempt == 1: time.sleep(25)
    time.sleep(2.2)
print('be-api requests', n)
