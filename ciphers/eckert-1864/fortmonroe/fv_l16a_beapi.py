#!/usr/bin/env python3
"""FV-L16a (10 Oct 2026): IA be-api whole-collection phrase queries (no identifier) for E509 E511 E514 E506 E508 E521, positive control
'"Suwo Nada"' in OR I/46 pt 2 by identifier first; >= 1.8 s apart. A miss is a search result, not a novelty verdict (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
BE = [('warofrebellion014602rootrich', '"Suwo Nada"'), (None, '"Ben De Ford is not here"'), (None, '"Western Metropolis" Alliance Montauk'),
      (None, '"light draft steamers" "Eliza Hancox"'), (None, '"Eliza Hancox" Winants'), (None, '"in time to sail with the rest"'),
      (None, '"over to the medical department" Blackstone'), (None, '"reported from Jamestown"'), (None, '"C. C. Leary is just in"'),
      (None, '"Leary" "ten days coal"'), (None, '"if General Butler has left"'), (None, '"mention that I inquired"')]
for ident, q in BE:
    p = {'q': q}
    if ident: p['identifier'] = ident
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://be-api.us.archive.org/fts/v1/search?' + urllib.parse.urlencode(p), headers=UA), timeout=90))
        hits = d.get('hits', {}).get('hits', [])
        print('BE', ident or '(all)', '|', q, '|', len(hits))
        for h in hits[:5]:
            f = h.get('fields', {}) or {}; hl = h.get('highlight', {}) or {}
            print('      ', f.get('identifier'), '::', ' '.join(' '.join(x if isinstance(x, str) else str(x) for x in (hl.get('text') or [])).split())[:300])
    except Exception as ex: print('BE', ident or '(all)', '|', q, '| ERR', str(ex)[:80])
    time.sleep(1.8)
