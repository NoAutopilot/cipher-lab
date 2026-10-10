import json,sys,time,urllib.parse,urllib.request
S=sys.argv[1]; UA={'User-Agent':'cipher-lab research script (contact via repository)'}
n=0
def get(url,binary=False):
    global n
    for att in (1,2):
        try:
            r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=90).read(); n+=1; return r
        except Exception as e:
            n+=1; print('ERR',url[-60:],str(e)[:60],flush=True)
            if att==2: print('requests',n); sys.exit('stopped')
            time.sleep(25)
HB="https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
for lab,q in [('control 9678','Schermerhorn Maxon Amos State agent'),('E600','Delaware furlough vote'),('E602','Ricketts Locust Point')]:
    d=json.loads(get(HB+"dmQuery/p16003coll11/CISOSEARCHALL%5E"+urllib.parse.quote(q)+"%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"))
    print(lab,q,d.get('pager',{}).get('total'),' '.join(str(r.get('pointer')) for r in d.get('records',[])),flush=True); time.sleep(3.3)
for p in [9877,9826,9777,9778,9823,9824,9865]:
    b=get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg')
    open(f'{S}/leaves/{p}.jpg','wb').write(b); print(p,len(b),b[:3]==b'\xff\xd8\xff',flush=True); time.sleep(3.3)
print('requests',n)
