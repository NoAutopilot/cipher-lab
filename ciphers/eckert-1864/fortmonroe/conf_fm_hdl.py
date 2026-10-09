#!/usr/bin/env python3
"""CONF-FM (9 Oct 2026, account 1): fetch the Huntington CONTENTdm item record (dmGetItemInfo, p16003coll11) for the clear
copies of E250 (10490), E254 (9913), E257 (4823) and the cipher entries' own pointers 5770, 5829, 5774, and Part B's 5820, 5821.
>= 3.2 s apart, descriptive UA. Writes conf_fm_hdl.json (title, transc per pointer). Usage: python3 conf_fm_hdl.py [ptr ...]"""
import json, sys, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
ptrs = sys.argv[1:] or ['10490', '9913', '4823', '5820', '5821']
out = {}
try:
    out = json.load(open('conf_fm_hdl.json'))
except Exception:
    pass
n = 0
for p in ptrs:
    d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60))
    n += 1
    out[p] = {k: d.get(k) for k in ('title', 'transc', 'date', 'descri') if d.get(k)}
    time.sleep(3.2)
json.dump(out, open('conf_fm_hdl.json', 'w'), indent=1, ensure_ascii=False)
print('requests', n)
