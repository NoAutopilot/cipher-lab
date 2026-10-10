#!/usr/bin/env python3
"""FV-FM65b (10 Oct 2026): loc.gov Chronicling America JSON search (press of the day), Jan 1865, for ship names in E507 E512 E530.
>= 2 s apart. Hit lists are leads to read, not verdicts (rule 10)."""
import json, time, urllib.parse, urllib.request
for q in ['Winants Hancox', 'steamer Russia flag ship', 'Sedgwick Ariel Ashland sailed']:
    url = 'https://www.loc.gov/collections/chronicling-america/?' + urllib.parse.urlencode({'q': q, 'fo': 'json', 'dates': '1865-01-01/1865-01-31', 'c': 10})
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=90))
        r = d.get('results', [])
        print(q, '| results', d.get('pagination', {}).get('of'))
        for x in r[:8]: print('   ', x.get('date'), (x.get('title') or '')[:80], x.get('id'))
    except Exception as e: print(q, '| ERR', str(e)[:100])
    time.sleep(2)
