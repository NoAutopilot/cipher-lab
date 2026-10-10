#!/usr/bin/env python3
"""FV-L15n (10 Oct 2026): leaf images (to a scratch dir, argv[1]) and one CISOSEARCHALL per entry, p16003coll11, 3.2 s apart, under the hdl token."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {"User-Agent": "cipher-lab research script (contact via repository)"}
out = sys.argv[1]; n = 0
def get(u):
    global n; n += 1
    r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read(); time.sleep(3.2); return r
for p in ["5883", "5888", "5919", "5779"]:
    open(f"{out}/p{p}.jpg", "wb").write(get(f"https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg"))
for e, q in [("E537", "Varina Blair"), ("E544", "Palmer accordingly"), ("E565", "scout Roberts"), ("E171", "Arago Heine")]:
    d = json.loads(get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"))
    recs = d.get("records", [])
    print(e, q, "total", d.get("pager", {}).get("total"), [(r.get("pointer"), (r.get("title") or "")[:40]) for r in recs][:10])
print("requests", n)
