#!/usr/bin/env python3
"""FV-N2e (10 Oct 2026): all-pointer Huntington CONTENTdm clear-copy search (p16003coll11, CISOSEARCHALL, three words, AND)
for the three step-0 misses N2-IA, IC, IH; one positive control per entry (the row's own transcription words must return it)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
Q = [("IA", "Maryland veteran regiment"), ("IA", "Slocum Baltimore veteran"), ("IA-ctl 9701", "Veteran detained purpose"),
     ("IC", "Vicksburg Monroe gauge"), ("IC", "Vicksburg Monroe railroad"), ("IC-ctl 9755", "Shreveport grading Directors"),
     ("IH", "Canby Hurlbut Reynolds"), ("IH", "Banks Reynolds relieved"), ("IH-ctl 9739", "combined Gulf duty")]
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
