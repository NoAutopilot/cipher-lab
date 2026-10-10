#!/usr/bin/env python3
"""AUD2-LEDGER14-1 (10 Oct 2026): IA be-api full-text queries, in-volume (Grant Papers 11/12) and whole-collection; 1.9 s apart."""
import json, time, urllib.parse, urllib.request
Q = [
 ("CTRL vol11", "papersofulyssess0011gran", '"Ricketts"'),
 ("E602 vol11", "papersofulyssess0011gran", '"Locust Point"'),
 ("E602 vol11", "papersofulyssess0011gran", 'Meigs Ricketts Baltimore'),
 ("E602 vol11", "papersofulyssess0011gran", '"without ambulances"'),
 ("E602 vol11", "papersofulyssess0011gran", '"Martinsburg" forage'),
 ("CTRL vol12", "papersofulyssess0012gran", '"Delaware"'),
 ("E600 vol12", "papersofulyssess0012gran", '"Delaware cavalry"'),
 ("E600 vol12", "papersofulyssess0012gran", 'furlough vote Delaware'),
 ("E600 vol12", "papersofulyssess0012gran", '"go home and vote"'),
 ("E600 all", None, '"First Delaware Cavalry" furlough vote'),
 ("E600 all", None, '"Delaware Cavalry" "go home and vote"'),
 ("E600 all", None, '"request of Governor Cannon"'),
 ("E602 all", None, '"Locust Point" Ricketts "without ambulances"'),
 ("E602 all", None, '"embarrass operations"  "animals and wagons"'),
 ("E602 all", None, '"Hunter\'s large train"'),
]
for lab, ident, q in Q:
    qq = q + (f" AND identifier:{ident}" if ident else "")
    url = "https://be-api.us.archive.org/fts/v1/search?q=" + urllib.parse.quote(qq) + "&size=8"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=40))
    except Exception as e:
        print(f"{lab} | {q} | ERROR {type(e).__name__} {e}"); time.sleep(1.9); continue
    hits = d.get("hits", {}).get("hits", [])
    print(f"{lab} | {q} | {d.get('hits',{}).get('total')}")
    for h in hits[:8]:
        f = h.get("fields", {}); hl = h.get("highlight", {})
        snip = " ... ".join(" ".join(x.split()) for v in hl.values() for x in v)[:400]
        print(f"    {f.get('identifier')} | {str(f.get('title'))[:60]} | {snip}")
    time.sleep(1.9)
