#!/usr/bin/env python3
"""LS4-R1b: be-api full-text phrase search over all IA items (one request per phrase, >= 2 s apart). Prints total and up to 4
identifiers with a snippet. A miss is a search result, not a statement about print (rule 10). Usage: ls4_r1b_fts.py "phrase" ..."""
import json, re, sys, time, urllib.parse, urllib.request
for ph in sys.argv[1:]:
    url = 'https://be-api.us.archive.org/fts/v1/search?size=6&q=' + urllib.parse.quote('"' + ph + '"')
    req = urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=60))
        h = d['hits']; tot = h['total']
        print(f'{ph!r}: total {tot}')
        for x in h['hits'][:4]:
            s = re.sub(r'\s+', ' ', re.sub(r'</?[a-z]+>|\{\{\{|\}\}\}', '', ' '.join(x.get('highlight', {}).get('text', [''])[:1])))[:200]
            print('   ', x['fields']['identifier'] if 'fields' in x else x.get('_id'), '|', s)
    except Exception as e:
        print(f'{ph!r}: ERROR {e}')
    time.sleep(2.2)
