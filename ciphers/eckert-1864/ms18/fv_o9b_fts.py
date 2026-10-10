"""FV-O9b (10 Oct 2026, for LANE LEDGER-10), copied from fv_o9a_fts.py: be-api.us.archive.org full-text phrase queries (all items). Usage: fv_n2a_fts.py QUERY... A miss is a search result (rule 10)."""
import json,sys,time,urllib.parse,urllib.request
UA={'User-Agent':'cipher-lab research script (contact via repository)'}
for q in sys.argv[1:]:
    u='https://be-api.us.archive.org/fts/v1/search?q='+urllib.parse.quote(q)+'&size=15'
    try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=90))
    except Exception as e: print('==',q,'ERR',e); time.sleep(2); continue
    h=d['hits']; print('==',q,'total',h['total'])
    for x in h['hits']:
        f=x['fields']; hl=x.get('highlight',{}).get('text',[''])
        print('  ',f['identifier'][0],f.get('meta_year',f.get('year','')),'|',' ... '.join(hl)[:300].replace('\n',' '))
    time.sleep(2)
