#!/usr/bin/env python3
"""FM65-B (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare plain words of each of the ten rows,
plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'), ('5856/0','Eliza Hancox winants'), ('5856/1','collector draper friend Eckert'), ('5857/1','Binney Brice paymaster mustered December'),
     ('5858/0','Blackstone Leary special'), ('5858/1','Sampson Ariel Victor Illinois Sedgwick'), ('5860/1','overcoat package papers theatre Phillips'),
     ('5860/2','Desey Townsend Mill supt'), ('5861/1','Sampson hasbin ordered Baltic'), ('5861/2','Ellen Stanton arrived safely'),
     ('5864/1','Elias Smith Tribune correspondent permission'), ('5866/0','Sampson Annapolis Coal docks'), ('5866/2','Ariel Sedgwick Victor Illinois ordered')]
n = 0
for tag, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    except Exception as e:
        n += 1; print(tag, q, 'ERR', str(e)[:80], flush=True); time.sleep(25)
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    print(f'{tag} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
