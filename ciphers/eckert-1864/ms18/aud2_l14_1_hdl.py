#!/usr/bin/env python3
"""AUD2-LEDGER14-1 (10 Oct 2026): Huntington CONTENTdm CISOSEARCHALL (all pointers) for clear siblings of E600/E602, + IIIF leaf 9877 to scratch.
3.3 s apart; one retry after 25 s on a dropped connection."""
import json, sys, time, urllib.parse, urllib.request
UA = {"User-Agent": "Mozilla/5.0"}
n = 0
def get(url):
    global n
    for a in (0, 1):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read(); n += 1; return r
        except Exception as e:
            n += 1; print("ERR", str(e)[:60], flush=True)
            if a == 0: time.sleep(25)
    return None
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
Q = [("control 9678", "Schermerhorn Maxon Amos State agent"),
     ("E600", "Delaware cavalry furlough"), ("E600", "go home vote furlough"), ("E600", "Cannon Delaware"),
     ("E602", "embarrass operations wagons"), ("E602", "Hunters large train"), ("E602", "forage Martinsburg rebels"),
     ("E602", "Ricketts steamers")]
for lab, q in Q:
    b = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json")
    if b:
        d = json.loads(b); recs = d.get("records", [])
        print(f"{lab} | {q} | {d.get('pager',{}).get('total')} | " + " ".join(str(r.get("pointer")) for r in recs[:30]))
    time.sleep(3.3)
b = get("https://hdl.huntington.org/digital/iiif/p16003coll11/9877/full/2400,/0/default.jpg")
if b:
    open(sys.argv[1], "wb").write(b); print("leaf 9877", len(b), "bytes")
print("requests", n)
