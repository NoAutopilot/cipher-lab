#!/usr/bin/env python3
"""FM65-A (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare plain words of each of the twelve rows,
plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector difficulty Evidence Nashville'), ('5847/2','anchor chain Baltic Sampson'), ('5849/0','Leary Ariel Victor Newport'),
     ('5849/1','Morgan commissary coaling watering Rawlins'), ('5850/1','Berrien Navy Yard'), ('5851/0','Euterpe Livingston Varuna Prometheus'),
     ('5851/1','Webster Howell coaled loaded'), ('5852/1','Jamestown dispatch steamers Rawlins'), ('5852/2','Russia flag ship'),
     ('5853/1','Leary Montauk'), ('5854/0','Bendford Ainsworth Alliance'), ('5854/1','Cuyahoga Draper Sedgwick Baltic'), ('5855/2','Hancox Winants')]
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
