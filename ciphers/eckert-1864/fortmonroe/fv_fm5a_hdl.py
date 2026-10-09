#!/usr/bin/env python3
"""FV-FM5a (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, transcription in the result) for the
decoded substance of E210 (5637), E212 (5767), E213 (5607), E214 (5703), E216 (5743): a clear or received/sent copy elsewhere in the
Eckert papers. >= 3.2 s apart. Usage: fv_fm5a_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['royer', 'tafft', 'best maps', 'surplus', 'superintendent', 'insulators', 'bickford', 'new base', 'removing stores',
     'available transportation', 'suited service', 'embark white house']
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(f'{q!r}: ERROR {e}'); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs))
    for r in recs:
        tr = (r.get('transc') or '')
        if isinstance(tr, str) and tr:
            i = tr.lower().find(q.split()[0])
            print('    ', r.get('pointer'), '::', ' '.join(tr[max(0, i-120):i+200].split()))
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.2)
# item info (full transcription) for hits that came back without a transcription snippet, at most MAXINFO
MAXINFO = int(os.environ.get('MAXINFO', '0'))
for ptr in sys.argv[2:2 + MAXINFO]:
    url = HB + f"dmGetItemInfo/p16003coll11/{ptr}/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print('INFO', ptr, '::', d.get('title'), '::', ' '.join(str(d.get('transc') or d.get('transa') or '')[:900].split()))
    time.sleep(3.2)
print('requests', n)
