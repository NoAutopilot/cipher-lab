#!/usr/bin/env python3
"""AUD2-LEDGER-34 (10 Oct 2026): IA be-api full-text search. stdin: one query per line, optional TAB identifier (else global). Appends to argv[1]. 1.6 s apart."""
import json,sys,time,urllib.parse,urllib.request
UA='cipher-lab research script (contact via repository)'
out=open(sys.argv[1],'a')
for line in sys.stdin:
    line=line.rstrip('\n')
    if not line: continue
    q,_,ident=line.partition('\t')
    url='https://be-api.us.archive.org/fts/v1/search?q='+urllib.parse.quote(q)+('&identifier='+ident if ident else '')
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=60))
        hits=d.get('hits',{}).get('hits',[]); tot=d.get('hits',{}).get('total',len(hits))
        tot=tot.get('value') if isinstance(tot,dict) else tot
        det=' ; '.join(f"{h['fields'].get('identifier',['?'])[0]} ({(h['fields'].get('meta_title') or ['?'])[0][:45]}) {str(h.get('highlight',{}).get('text',[''])[0])[:160]!r}" for h in hits[:6])
        r=f"{q}\t{ident or 'global'}\t{tot}\t{det}"
    except Exception as e:
        r=f"{q}\t{ident or 'global'}\tERR {e}\t"
    print(r[:1200]); out.write(r+'\n'); time.sleep(1.6)
