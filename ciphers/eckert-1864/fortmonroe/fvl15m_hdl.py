#!/usr/bin/env python3
"""FV-L15m (10 Oct 2026, for LANE LEDGER-15): dmGetItemInfo of CLEAR-SWEEP's holder clear-copy pointers (+ FV-L15c's Glisson pointers for E571) and the
seven ledger leaves at 2400 px (to a scratch dir, argv[1]); p16003coll11, 3.2 s apart, under the hdl token."""
import json, sys, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {"User-Agent": "cipher-lab research script (contact via repository)"}
out = sys.argv[1]; n = 0
def get(u):
    global n; n += 1
    r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read(); time.sleep(3.2); return r
for p in ["7722", "7741", "8561", "7787", "4788", "7802", "8486", "7818", "8622"]:
    d = json.loads(get(HB + f"dmGetItemInfo/p16003coll11/{p}/json"))
    print(f"## {p} title={d.get('title')!r}")
    print("   transc:", " ".join(str(d.get("transc") or d.get("transcript") or "").split()))
for p in ["5887", "5888", "5895", "5897", "5917", "5929", "5768"]:
    open(f"{out}/p{p}.jpg", "wb").write(get(f"https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg"))
print("requests", n)
