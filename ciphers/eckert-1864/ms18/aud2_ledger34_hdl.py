#!/usr/bin/env python3
"""AUD2-LEDGER-34 (10 Oct 2026): second-audit CONTENTdm pass for E351 E355 E356 (p16003coll11). Full catalogue record (every non-empty field)
for the three own pointers, then CISOSEARCHALL (suppressfulltext=1) on words the first audit did not query. >= 3.3 s apart.
Usage: aud2_ledger34_hdl.py [--queries-only] (the retry after the first run's dropped connection). A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
PTR = ['10065', '9863', '9729']
Q = ['Cluer', 'Clancey', 'Goodman Boston', 'Woolley minors', 'Sands Kirkland', 'Stiner Herald', 'minors habeas']
n = 0
if '--queries-only' in sys.argv: PTR = []
for p in PTR:
    d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60)); n += 1
    keep = {k: v for k, v in d.items() if isinstance(v, str) and v.strip() and k not in ('transc', 'full')}
    print('INFO', p, json.dumps(keep)[:3000], flush=True); time.sleep(3.3)
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!date/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(f"{r.get('pointer')}({str(r.get('date'))[:10]})" for r in recs[:50]), flush=True)
    time.sleep(3.3)
print('requests', n)
