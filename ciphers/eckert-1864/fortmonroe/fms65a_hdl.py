#!/usr/bin/env python3
"""FM-S65A (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers) on rare plain words of each of the twelve rows,
plus the positive control (9678). >= 3.3 s apart, no images. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector difficulty Evidence Nashville'),
 ('5845/2 q1','Webster Sheldon ready OBrien'), ('5845/2 q2','Butler headquarters Webb Vinton ready'), ('5845/2 q3','Sheldon Webster Knox Monroe ready'),
 ('5857/2 q1','Stanton Sheridan instructions Savannah'), ('5857/2 q2','Collector Draper Savannah Monroe Stanton'), ('5857/2 q3','Draper Sheridan expect leave afternoon'),
 ('5858/2 q1','steamer Martin Grant Monroe'), ('5858/2 q2','Martin Beckwith Sheldon Grant left'), ('5858/2 q3','Martin steamer City Point Grant Monroe'),
 ('5862/0 q1','River Queen Butler James Beckwith'), ('5862/0 q2','River Queen Sheldon himself same way'), ('5862/0 q3','Queen left Butler on board gone up James'),
 ('5862/2 q1','Ord Foster relieve Grant Beckwith'), ('5862/2 q2','relieve Foster Ord Sheldon either good'), ('5862/2 q3','Ord Gillmore Foster relieve Hilton'),
 ('5872/0 q1','Illinois Morgan Rawlins 1200'), ('5872/0 q2','Illinois sea Rawlins Beckwith Sheldon'), ('5872/0 q3','Illinois eighty-seven men Morgan'),
 ('5872/1 q1','nothing arrived Rawlins Morgan Beckwith'), ('5872/1 q2','Morgan Rawlins end not yet'), ('5872/1 q3','Morgan Sheldon Beckwith arrived Lieut'),
 ('5872/2 q1','Grover rounds ammunition Rawlins'), ('5872/2 q2','Grover forty rounds Beckwith Sheldon'), ('5872/2 q3','Grover Brevet more rounds take'),
 ('5874/1 q1','Grover rounds answer Rawlins wait'), ('5874/1 q2','Grover needn\'t wait more Beckwith'), ('5874/1 q3','Grover forty rounds will answer'),
 ('5883/2 q1','Palmer wait Monroe until I get there Eckert'), ('5883/2 q2','Palmer Eckert Sheldon Grant Monroe'), ('5883/2 q3','Eckert wait Monroe Palmer tomorrow'),
 ('5892/0 q1','Seward Richmond party not here'), ('5892/0 q2','Eckert Seward arrived evening Richmond party'), ('5892/0 q3','Sheldon Eckert Seward remain here Monroe')]
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
