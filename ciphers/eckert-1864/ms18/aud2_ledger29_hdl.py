#!/usr/bin/env python3
"""AUD2-LEDGER-29 (9 Oct 2026): second-verifier all-pointer CONTENTdm clear-copy search (p16003coll11, CISOSEARCHALL, suppressfulltext=1) on clear words of
E326-E330, item info for hit pointers not yet seen, and IIIF pages for the eye check. >= 3.3 s apart. Usage: fv_ms18c_hdl.py SCRATCH_DIR [--img P ...].
A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = ['Tunstall', 'Van Duzer Miller', 'seizure of his papers', 'rebel agents arrest', 'Dana arrest Nashville', 'Secretary of War directs the arrest', 'Thos T', 'Van Duzer Tunstall', 'Bruch Garrett', 'Sampson Hamilton arrest']
out = sys.argv[1]; n = 0
args = sys.argv[2:]
if '--img' in args:
    for p in args[args.index('--img') + 1:]:
        fp = os.path.join(out, f'p{p}.jpg')
        url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
        open(fp, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); n += 1
        print('img', p, os.path.getsize(fp), flush=True); time.sleep(3.3)
    print('requests', n); sys.exit()
if '--info' in args:
    for p in args[args.index('--info') + 1:]:
        d = json.load(urllib.request.urlopen(urllib.request.Request(HB + f"dmGetItemInfo/p16003coll11/{p}/json", headers=UA), timeout=60)); n += 1
        print(p, '|', d.get('title'), '|', str(d.get('date')), '|', str(d.get('transc') or d.get('descri'))[:1500].replace('\n', ' / '), flush=True)
        time.sleep(3.3)
    print('requests', n); sys.exit()
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!date/nosort/50/1/0/0/1/0/json"
    d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(f"{r.get('pointer')}({str(r.get('date'))[:10]})" for r in recs[:50]), flush=True)
    time.sleep(3.3)
print('requests', n)
