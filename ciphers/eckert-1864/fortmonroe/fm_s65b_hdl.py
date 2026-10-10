#!/usr/bin/env python3
"""FM-S65B (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare PLAIN words of each of the eleven rows
(not key-dependent words), plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'),
     ('5892/1a','Monohansett Taunton Beckwith'), ('5892/1b','Monohansett steamer Fort Monroe leave 1 AM'), ('5892/1c','Monohansett Eckert meet arrival City Point'),
     ('5893/1','Bruno Bolivia Bates answer quick'),
     ('5896/0a','letter referred to dispatch staff officer retained no copy'), ('5896/0b','staff officer delivered retained copy Beckwith Seward'), ('5896/0c','Seward letter Grant staff officer Hampton Roads'),
     ('5896/1','Anderson despatches Sherman Annapolis Friday Schofield'),
     ('5908/0a','Radford New Ironsides torpedoes Lynch'), ('5908/0b','Lynch Bureau of Ordnance torpedoes Radford forward receipt'), ('5908/0c','Ironsides torpedoes Norfolk Beckwith Radford'),
     ('5910/1a','Camman Company gold Cooper naval officer'), ('5910/1b','Cammann gold sell fall Cooper'), ('5910/1c','sell gold fall approval Eckert Cooper'),
     ('5914/2a','Gordon commission adjourned cashier National Bank'), ('5914/2b','Meredith Gordon commission cashier bank Norfolk'), ('5914/2c','Webster Beckwith Gordon commission cashier'),
     ('5928/2','change of operators Hamlet'),
     ('5936/2a','ponchos not on hand Canby Ingalls'), ('5936/2b','ponchos Sheridan arrival Ingalls Beckwith'), ('5936/2c','ponchos Canby Sausage Ingalls Shoed'),
     ('5941/2a','Sherman John Sherman Goldsboro Newbern Old Point Wednesday'), ('5941/2b','going to see Grant City Point Goldsboro Newbern Wednesday'), ('5941/2c','Sherman Honorable John Sherman Monroe Wednesday'),
     ('5942/1','furlough Adams hampered Beckwith')]
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
