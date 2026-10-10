"""FV-O9a (10 Oct 2026, account 1, for LANE LEDGER-N2): holder CONTENTdm all-pointer clear-copy queries for O9-DC/DE/DH/DI plus the two IIIF leaves (2400 px, to a scratch dir). Usage: fv_n2a_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out=sys.argv[1]; n=0
Q=['Stover','Brady Olcott','Brady arrested','Maria Day','Marcia Day','Van Vliet expedition','Vache','Stover books papers','Olcott Lafayette','separate distinct account']
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        n+=1; print(q,'ERR',e); time.sleep(3.3); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs[:60]), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
for p in [9673,9684]:
    url = f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg'
    fp = os.path.join(out, f'p{p}.jpg')
    try:
        open(fp, 'wb').write(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120).read()); n+=1; print('img',p)
    except Exception as e:
        n+=1; print('img',p,'ERR',e)
    time.sleep(3.3)
print('requests',n)
