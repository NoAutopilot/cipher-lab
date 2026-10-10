"""FV-O9b (10 Oct 2026, account 1, for LANE LEDGER-10): holder CONTENTdm all-pointer clear-copy and incoming-side queries for O9-DA/DD/DF, item info for 4551 (FV-O9a lead), and four IIIF leaves (2400 px, to a scratch dir). Usage: fv_o9b_hdl.py SCRATCH_DIR. A miss is a search result (rule 10)."""
import json, os, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
out=sys.argv[1]; n=0
def get(url, t=60):
    global n
    for k in range(2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t).read(); n += 1; return r
        except Exception as e:
            n += 1; print('ERR', e, flush=True)
            if k == 0: time.sleep(25)
    return None
r = get(HB + "dmGetItemInfo/p16003coll11/4551/json")
if r: d = json.loads(r); json.dump(d, open(os.path.join(out, 'info_4551.json'), 'w')); print('4551:', d.get('title'), '|', d.get('transc'), flush=True)
time.sleep(3.3)
Q=['Simpson Barlow','master Painter','Painter absconded','Olcott Morgan','Fulton Dix','Fulton state rooms','Van Vliet Fulton','Brown forage','Brown hay','hay sailing vessels','large propeller','Muss']
for q in Q:
    r = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json")
    if r:
        d = json.loads(r); recs = d.get('records', [])
        print(f'{q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(x.get('pointer')) for x in recs[:60]), flush=True)
        json.dump(d, open(os.path.join(out, 'q_' + q.replace(' ', '_') + '.json'), 'w'))
    time.sleep(3.3)
for p in [9709, 9687, 9699, 9700]:
    r = get(f'https://hdl.huntington.org/digital/iiif/p16003coll11/{p}/full/2400,/0/default.jpg', 120)
    if r: open(os.path.join(out, f'p{p}.jpg'), 'wb').write(r); print('img', p, len(r), flush=True)
    time.sleep(3.3)
print('requests', n)
