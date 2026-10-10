#!/usr/bin/env python3
"""L14-C: Huntington CONTENTdm clear-copy queries (p16003coll11, CISOSEARCHALL, all pointers): positive control 9678 once, then one query per row (rare plain words of the row). >= 3.3 s apart. Usage: l14c_hdl.py"""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
import sys
Q = [('control 9678', 'Inspector Inquiry evidence'),
 ('9869/4', 'Paducah Meredith judicious Washburne'), ('9764/1', 'Stahel Lynchburg repulsed retreat caution'),
 ('9897/1', 'Beverly Tucker Odell falls discretion'), ('9862/0', 'Garrett Harpers delayed delay afternoon'),
 ('9885/3', 'settled trouble departure assigned order'), ('9848/0', 'veteran regiment prisoners detailed await retain'),
 ('9811/0', 'frankly freely excused lawfully properly decide'), ('9688/0', 'furloughs veteran expire wagons transportation'),
 ('9850/2', 'frauds inefficiencies investigate discretion Indian Territory')]
n = 0
ONLY = sys.argv[1:]
for lab, q in Q:
    if ONLY and lab.split()[0] not in ONLY: continue
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    except Exception as e:
        print(lab, 'ERROR', e); time.sleep(25); break
    print(f'{lab} | {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
