"""FV-MS18h (9 Oct 2026): Huntington CONTENTdm full-text clear-copy search (p16003coll11, CISOSEARCHALL, all pointers),
one rare word per entry for E341, E342, E344 (para 1 and para 2), E348 (the four printed MS18-R4 rows). Prints hit totals and pointers; no images.
Usage: python3 ms18/fv_ms18h_hdl.py  (network; 3.3 s apart)."""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
Q = [('E341', 'Stanley'), ('E342', 'Paducah'), ('E344', 'transpires'), ('E344p2', 'Beckwith'), ('E348', 'Urbana')]
n = 0
for e, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/200/1/0/0/1/0/json"
    req = urllib.request.Request(url, headers={'User-Agent': 'cipher-lab research script (contact via repository)'})
    d = json.load(urllib.request.urlopen(req, timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{e} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs), flush=True)
    time.sleep(3.3)
print('requests', n)
