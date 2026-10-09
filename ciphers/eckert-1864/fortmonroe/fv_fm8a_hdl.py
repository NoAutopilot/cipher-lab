#!/usr/bin/env python3
"""FV-FM8a (9 Oct 2026): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, transcription in the result) for the
decoded substance of E254 (5829), E270 (5801), E272 (5768), E275 (5824), E277 (5802): a clear or received/sent copy elsewhere in the
Eckert papers. >= 3.2 s apart. Usage: fv_fm8a_hdl.py SCRATCH_DIR. A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['paymaster binney', 'brice binney', 'officers designated', 'leave for washington tonight', 'terry varina', 'repeat this to', 'nineteenth corps', '19th corps', 'shaffer rawlins', 'shaffer chief of staff', 'boots of any kind', 'allen quartermaster', 'fred martin', 'chief of artillery', 'style of gun', 'each battery']
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
# IIIF page images (2400 px) for the eye check of lines the reading turns on (E254 E270 E272 E275 E277 lines)
for ptr in ('5829', '5801', '5768', '5824', '5802'):
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{ptr}/full/2400,/0/default.jpg'
    try:
        open(os.path.join(out, f'p{ptr}.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
        print('IIIF', ptr, 'ok')
    except Exception as e:
        print('IIIF', ptr, 'ERROR', e)
    n += 1; time.sleep(3.2)
print('requests', n)
