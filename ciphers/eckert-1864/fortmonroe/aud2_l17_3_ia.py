#!/usr/bin/env python3
"""AUD2-LEDGER17-3 (10 Oct 2026): IA advancedsearch for OR ser. III vol. 4 and Grant Papers vol. 10 (metadata only)."""
import json, time, urllib.parse, urllib.request
UA = 'cipher-lab research script (contact via repository)'
QS = ['title:(war of the rebellion) AND (volume:"Ser. 3 vol. 4" OR volume:"ser.3 v.4" OR volume:"Series III" )',
      'title:(war of the rebellion official records) AND description:(series III)',
      'title:(papers of ulysses s. grant)']
for q in QS:
    u = 'https://archive.org/advancedsearch.php?' + urllib.parse.urlencode({'q': q, 'fl[]': ['identifier', 'title', 'volume', 'date'], 'rows': 60, 'output': 'json'}, doseq=True)
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': UA}), timeout=60))
        print('Q', q, d['response']['numFound'])
        for x in d['response']['docs']:
            print('  ', x.get('identifier'), '|', str(x.get('volume')), '|', str(x.get('title'))[:90])
    except Exception as e:
        print('Q', q, 'ERR', e)
    time.sleep(2)
