"""FV-N2f (10 Oct 2026, account 1, for LANE LEDGER-10): holder CONTENTdm all-pointer clear-copy / received-copy queries for N2-JG JH JI (mssEC collection
p16003coll11). Usage: fv_n2f_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]; n = 0
def get(url, t=60):
    global n
    try:
        r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t).read(); n += 1; return r
    except Exception as e:
        n += 1; print('ERR', e, flush=True); time.sleep(25)
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t).read(); n += 1; return r
        except Exception as e2:
            n += 1; print('ERR2', e2, flush=True); return None
Q = ['steamers New Orleans', 'Hampton Roads steamers', 'ocean steamers', 'Urbana Early', 'Parkersburg Hunter', 'return immediately', 'liberal construction', 'Meigs Barnard']
for q in Q:
    r = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json")
    if r:
        d = json.loads(r); recs = d.get('records', [])
        print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(x.get('pointer')) for x in recs[:50]), flush=True)
        json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
print('requests', n)
