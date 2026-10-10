#!/usr/bin/env python3
"""AUD2-LEDGER17-2 (10 Oct 2026): IA be-api full-text queries (whole collection) for E594 and E591, control first, 2 s apart, one retry
after 25 s on an error, then the query is logged unchecked. A miss is a search result, not a novelty verdict (rule 10).
Usage: aud2_l17_2_beapi.py > aud2_l17_2_beapi.out"""
import json, sys, time, urllib.parse, urllib.request
Q = ['"Wait at Fort Monroe until I get there"',
     '"telegraphed to my brother, Senator Sherman"',
     '"Senator Sherman" "Old Point" Wednesday Goldsboro',
     '"John Sherman" "Fortress Monroe" "Bat" Newbern 1865',
     '"expect to go back to Goldsboro"',
     '"Dominick Lynch" torpedoes',
     '"submarine torpedoes" Radford Lynch',
     '"no torpedoes on hand" Bureau']
for q in Q:
    u = 'https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode({'q': q, 'size': 10})
    for a in (1, 2):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60) as f:
                d = json.load(f); break
        except Exception as e:
            print(q, '| ERROR', getattr(e, 'code', e), 'attempt', a); sys.stdout.flush()
            d = None
            if a == 1: time.sleep(25)
    if d is None: print(q, '| UNCHECKED'); continue
    hits = d.get('hits', {}).get('hits', [])
    print(q, '| hits', d.get('hits', {}).get('total'), len(hits))
    for h in hits:
        s = h.get('fields', {}); hl = h.get('highlight', {})
        print('   ', s.get('identifier'), '|', str(s.get('title'))[:60], '|', s.get('year'), '|', ' '.join(' '.join(sum(hl.values(), [])).split())[:300])
    sys.stdout.flush(); time.sleep(2)
