#!/usr/bin/env python3
"""FM-R6a (9 Oct 2026): be-api positive control + retries for the Sherman 16 Oct 1864 Ship's Gap dispatch (F4) in OR I/39 pt 3 (warofrebellion393unit).
A zero is a search result, not a verdict (rule 10)."""
import json,urllib.parse,urllib.request,time
for ident,q in [('warofrebellion393unit','Whiton Adna Anderson Inspector-General'),('warofrebellion393unit','Snake Creek Gap Sherman Hood'),('warofrebellion393unit','Resaca tunnel railroad repair Sherman'),('warofrebellion393unit','Roddy Tuscumbia')]:
    u='https://be-api.us.archive.org/fts/v1/search?'+urllib.parse.urlencode({'q':q,'identifier':ident})
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'cipher-lab research script (contact via repository)'}),timeout=60))
        h=d.get('hits',{}).get('hits',[]); print(ident,'|',q,'|',len(h))
        for x in h[:3]:
            for s in (x.get('highlight',{}) or {}).get('text',[])[:2]: print('  ',s[:250].replace('\n',' '))
    except Exception as e: print(ident,'|',q,'| ERR',str(e)[:80])
    time.sleep(2)
