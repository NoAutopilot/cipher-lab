"""AUD2-LEDGERN2-5 (10 Oct 2026, account 4): holder CONTENTdm all-pointer queries (clear copies and incoming sides) for O9-DC/DE/DH/DI on words FV-O9a did not
query, plus item info of 4491 (re-read of the request FV-O9a quotes) and of any new hit. >= 3.3 s apart. Usage: aud2_ledgern2_5_hdl.py. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
n = 0
def get(u):
    global n
    n += 1
    try: return json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60))
    except Exception as e: return {'_err': str(e)[:80]}
    finally: time.sleep(3.3)
Q = ['victualling', 'reimbursed expedition', 'Van Vliet Day', 'Billings', 'Avache', 'Navy operation', 'Brady Lafayette', 'Stover consultation',
     'Olcott Fox', 'Dix Brady']
for q in Q:
    d = get(HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json")
    print(repr(q), d.get('_err') or (d.get('pager', {}).get('total')), ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:50]), flush=True)
for p in sys.argv[1:] or ['4491']:
    d = get(HB + f"dmGetItemInfo/p16003coll11/{p}/json")
    print('INFO', p, d.get('_err') or ('title=' + str(d.get('title'))[:120] + ' | transc=' + str(d.get('transc'))[:1500].replace('\n', ' ')), flush=True)
print('requests', n)
