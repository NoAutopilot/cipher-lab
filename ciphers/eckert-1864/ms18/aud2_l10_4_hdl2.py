#!/usr/bin/env python3
"""AUD2-LEDGER10-4: dmGetItemInfo for the gauge/guage and Meigs-Canby hits not on disk (10451 10469 7815 9564); prints title and the text around 'gau'/'Canby'."""
import json, time, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16003coll11/{}/json"
for p in (10451, 10469, 7815, 9564):
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(HB.format(p), headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=60))
        t = d.get("transc") or ""; t = t if isinstance(t, str) else ""; i = max(t.lower().find("gau"), t.find("Canby"))
        print(p, "|", d.get("title"), "|", t[max(0, i - 350):i + 350].replace("\n", " "), flush=True)
    except Exception as e:
        print(p, "ERR", str(e)[:80], flush=True)
    time.sleep(3.3)
print("requests 4")
