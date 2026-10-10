import json, time, urllib.parse, urllib.request, re
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n=0
def get(u):
    global n; n+=1
    try: return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
    except Exception as e: return {'_err': str(e)[:80]}
    finally: time.sleep(3.3)
time.sleep(20)
d=get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote('Brady Lafayette') + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json")
print("'Brady Lafayette' (one retry after 20 s)", d.get('_err') or d.get('pager',{}).get('total'), ' '.join(str(r.get('pointer')) for r in d.get('records',[])))
for p in ['4492','10193','10194','10203','4477']:
    d=get(HB+f"dmGetItemInfo/p16003coll11/{p}/json")
    t=str(d.get('transc'))
    hits=[m.start() for m in re.finditer(r'Olcott|Fox|Brady|Stover|Lafayette',t)]
    print('INFO',p,d.get('_err') or ('title='+str(d.get('title'))[:60]+' | len='+str(len(t))+' | '+' || '.join(t[max(0,h-250):h+350].replace('\n',' ') for h in hits[:3])))
print('requests',n)
