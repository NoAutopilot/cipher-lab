#!/usr/bin/env python3
"""FV-L17c (10 Oct 2026; copied from fv_l17a_hdl.py, queries for E622 E623 E624 via env Q): Huntington CONTENTdm full-text search (p16003coll11, CISOSEARCHALL, suppressfulltext=1) across ALL pointers on
distinctive clear words of E581 E582 (5862) E583 E585 (5872) E586 (5874) E587 (5883); item info for named pointers (argv 2..);
IIIF pages at 2400 px to SCRATCH for the eye check (env IMG, comma list). >= 3.2 s apart. Usage: fv_l17a_hdl.py SCRATCH [PTR ...].
A miss is a search result, not a statement about print (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [q for q in os.environ.get('Q', '').split(',') if q]
IMG = [p for p in os.environ.get('IMG', '').split(',') if p]
out = sys.argv[1]; n = 0
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/100/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        print(f'{q!r}: ERROR {e}'); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(f"{r.get('pointer')}({r.get('title')})" for r in recs))
    for r in recs:
        tr = r.get('transc') or ''
        if isinstance(tr, str) and tr:
            i = tr.lower().find(q.split()[0].lower())
            print('    ', r.get('pointer'), '::', ' '.join(tr[max(0, i-250):i+350].split()))
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.2)
for ptr in sys.argv[2:]:
    url = HB + f"dmGetItemInfo/p16003coll11/{ptr}/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
        json.dump(d, open(os.path.join(out, f'info_{ptr}.json'), 'w'))
        print('INFO', ptr, '::', d.get('title'), '::', ' '.join(str(d.get('transc') or d.get('transa') or '').split()))
    except Exception as e: print('INFO', ptr, 'ERROR', e)
    n += 1; time.sleep(3.2)
for p in IMG:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    try:
        open(os.path.join(out, f'p{p}.jpg'), 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=180).read()); print('IIIF', p, 'ok')
    except Exception as e: print('IIIF', p, 'ERROR', e)
    n += 1; time.sleep(3.2)
print('requests', n)
