"""AUD2-LEDGERN2-2 (10 Oct 2026, account 4): second-verifier holder CONTENTdm all-pointer queries for N2-FA/FB/FE that FV-N2a (fv_n2a_hdl.py) did not run:
spelling variants of McCloskey, the Warren side of 30-31 Oct 1864, Meigs/Ingalls June 1864 clear words, the Sixth Corps shipping of 2-5 Dec 1864; then
item info for any hit not yet opened. Usage: aud2_ledgern2_2_hdl.py OUT_DIR [ptr ...]. >= 3.3 s apart. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out = sys.argv[1]; ptrs = sys.argv[2:]; n = 0
Q = [] if ptrs else ['McClosky', 'Felix', 'ballots Fifth Corps', 'Warren ballots', 'Seymour commissioner', 'sea going steamers', 'New Orleans service',
                     'Medical Department steamers', 'Sixth Corps Bradley', 'river steamers', 'Third Division Sixth Corps', 'Getty division']
for q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as e:
        n += 1; print(q, 'ERR', e); time.sleep(3.3); continue
    n += 1
    recs = d.get('records', [])
    print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in recs[:60]), flush=True)
    json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
for p in ptrs:
    url = HB + f"dmGetItemInfo/p16003coll11/{p}/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
        t = d.get('transc') or d.get('fullte') or ''
        print(f'== {p} | {d.get("title")} | {d.get("date")}\n{(t if isinstance(t, str) else json.dumps(t))[:3000]}', flush=True)
    except Exception as e:
        n += 1; print(p, 'ERR', e)
    time.sleep(3.3)
print('requests', n)
