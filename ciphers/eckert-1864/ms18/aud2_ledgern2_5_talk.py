"""AUD2-LEDGERN2-5 (10 Oct 2026, account 4): Decoding the Civil War Talk (talk.zooniverse.org, project 2125) keyword search for O9-DC/DE/DH/DI words.
>= 2 s apart. A miss is a search result (rule 10)."""
import json, time, urllib.parse, urllib.request
UA = {'User-Agent': 'cipher-lab research script (contact via repository)', 'Accept': 'application/vnd.api+json; version=1'}
for q in ['Olcott', 'Stover', 'Van Vliet', 'Marcia', 'Brady arrest', 'Atlas Fox']:
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request('https://talk.zooniverse.org/searches?section=project-2125&page_size=20&query=' + urllib.parse.quote(q), headers=UA), timeout=60))
        hits = d.get('searches', [])
        print(repr(q), len(hits), (d.get('meta', {}).get('searches') or {}).get('count'))
        for h in hits[:20]: print('   ', h.get('type'), h.get('id'), str(h.get('body') or h.get('title') or '')[:220].replace('\n', ' '))
    except Exception as e: print(repr(q), 'ERR', str(e)[:80])
    time.sleep(2)
