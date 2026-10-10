#!/usr/bin/env python3
"""FM-UND (10 Oct 2026): Huntington CONTENTdm full-text (p16003coll11, CISOSEARCHALL, all pointers), two rare PLAIN-word queries per undated tail + control 9678. 3.3 s apart. A miss is a search result."""
import json, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [('control','Inspector Inquiry evidence'),
 ('5568/0a','conveyance intelligence cause want success'),('5568/0b','examination papers conveyance intelligence'),
 ('5575/0a','disaster receive prisoners cover'),('5575/0b','receive prisoners cover approved signs'),
 ('5616/0a','Hutchins Delany Palmer Tempest Ajax Freeman'),('5616/0b','Vatterland Bishop steamers Escort tows Bay'),
 ('5656/0a','Wilsons Wharf Fort Powhattan Kautz flag of truce'),('5656/0b','Shore Davenport oakumed evidence Corresp'),
 ('5658/0a','Harrisons landing Jamestown Bermuda landing Eckert'),('5658/0b','Ingalls reserves programme apprise condition gratifying'),
 ('5689/0a','Clingman Hoke Walker Hunton Ransom Kemper'),('5689/0b','Shelby Weitzell Rucker Briggs Barnard defensive'),
 ('5759/0a','Pickett Catawba Weldon Columbia Hampton canal'),('5759/0b','Canby White House waylay dismounted'),
 ('5842/0a','picket line shells safely off Copy'),('5842/0b','shells picket line near our loss'),
 ('5902/0a','Edisto opposition Kitchen wished press'),('5902/0b','opposition Edisto possible honor obedient'),
 ('5914/0a','Town Creek propose make a stand'),('5914/0b','exhausted Town Creek short plunge')]
n = 0
for tag, q in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/50/1/0/0/1/0/json"
    try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
    except Exception as e:
        n += 1; print(tag, q, 'ERR', str(e)[:80], flush=True); time.sleep(25)
        try: d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60)); n += 1
        except Exception as e2: print('stop', e2); break
    print(f'{tag} {q!r}: {d.get("pager", {}).get("total")} hits:', ' '.join(str(r.get('pointer')) for r in d.get('records', [])[:60]), flush=True)
    time.sleep(3.3)
print('requests', n)
