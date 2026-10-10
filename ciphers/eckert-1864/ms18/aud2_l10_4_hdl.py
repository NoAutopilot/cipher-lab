#!/usr/bin/env python3
"""AUD2-LEDGER10-4 (10 Oct 2026): all-pointer Huntington CONTENTdm search for any clear copy, repeat or answer of N2-IC (9755); control = own row."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
Q = [("IC", "guage"), ("IC", "gauge"), ("IC", "grading Shreveport"), ("IC", "Directors report Monroe"), ("IC", "Meigs Canby railroad"), ("IC-ctl 9755", "rebellion guage annual")]
n = 0
for tag, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    for attempt in (1, 2):
        try:
            n += 1
            d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=60))
            recs = d.get("records", [])
            print(f"{tag}\t{q!r}\t{d.get('pager', {}).get('total')} hits\t" + " ".join(str(r.get("pointer")) for r in recs[:50]), flush=True); break
        except Exception as e:
            print(f"{tag}\t{q!r}\tattempt {attempt} ERR {str(e)[:60]}", flush=True); time.sleep(25)
    time.sleep(3.3)
print("requests", n)
