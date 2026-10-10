#!/usr/bin/env python3
"""FM65-B: dmGetItemInfo (title/descri/transc) for the other-pointer CISOSEARCHALL hits of fm65b_hdl.out. 3.3 s apart."""
import json, sys, time, urllib.request
UA={'User-Agent':'cipher-lab research script (contact via repository)'}
for p in sys.argv[1:]:
    url=f"https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16003coll11/{p}/json"
    d=json.load(urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60))
    print('=====',p,{k:(v if not isinstance(v,str) else v[:1200]) for k,v in d.items() if k in('title','descri','transc','date','creato','find')}, flush=True)
    time.sleep(3.3)
