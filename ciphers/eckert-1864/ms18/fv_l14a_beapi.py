import json, time, urllib.parse, urllib.request, sys
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q=[('E600',None,'"First Delaware Cavalry" furlough vote 1864'),
   ('E600','collectedworksof0008royp_b4p3_8','Delaware cavalry furlough vote'),
   ('E600',None,'"without prejudice to the public service" furlough vote Delaware'),
   ('E602',None,'"Ricketts" "Locust Point" "ambulances" Thomas quartermaster July 1864'),
   ('E602',None,'"embarrass operations by collecting too many animals"'),
   ('E602',None,'Meigs Thomas Baltimore Ricketts "forage collected at Martinsburg"'),
   ('CTRL-E601',None,'"those who join Mosby are exempt"'),
   ('CTRL-E601','warofrebellion014301rootrich','Mosby exempt Upperville')]
for lab,ident,q in Q:
    p={'q':q}
    if ident: p['identifier']=ident
    url='https://be-api.us.archive.org/fts/v1/search?'+urllib.parse.urlencode(p)
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60))
        hits=d.get('hits',{}).get('hits',[]); print(lab,ident,'|',q,'|',len(hits),flush=True)
        for h in hits[:4]: print('   ',h.get('fields',{}).get('identifier'),'|',(h.get('highlight',{}) or {}).get('text',[''])[0].replace('\n',' ')[:240])
    except Exception as e: print(lab,'|',q,'| ERR',str(e)[:100])
    time.sleep(1.9)
