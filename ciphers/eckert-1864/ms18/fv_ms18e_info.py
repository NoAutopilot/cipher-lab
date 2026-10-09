"""FV-MS18e: item info (title + transcription head) for the near-date CONTENTdm hits of ms18/fv_ms18e_hdl.out."""
import json, time, urllib.request
P = ['10041', '10043', '9803', '9806', '9882', '10028']
for p in P:
    u = f"https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q=dmGetItemInfo/p16003coll11/{p}/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'cipher-lab research script (contact via repository)'}), timeout=60))
    t = d.get('transc') or ''
    t = t if isinstance(t, str) else ''
    print(p, '|', d.get('title'), '|', ' '.join(t.split())[:900], flush=True)
    time.sleep(3.3)
print('requests', len(P))
