#!/usr/bin/env python3
"""AUD2-LEDGER-16 (9 Oct 2026, account 4): second audit of E260, E262, E263 -- Huntington CONTENTdm full text (p16003coll11,
CISOSEARCHALL, suppressfulltext=1, all pointers) on clear-word pairs NOT used by FV-FM7b (its pairs are logged in AUDIT (FV-FM7b) s.2),
plus recipient-side/staff/same-week traffic terms. >= 3.2 s apart. Prints each hit's pointer, title and the transcription window.
A miss is a search result, not a statement about print (rule 10)."""
import json, re, time, urllib.parse, urllib.request
HB = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
UA = {'User-Agent': 'cipher-lab research script (contact via repository)'}
Q = [  # (entry, query terms ANDed, regex to show)
 ('E260', 'hudson ingalls', r'hudson'), ('E260', 'hudson steamer', r'hudson'), ('E260', 'such orders were received', r'such orders'),
 ('E260', 'webster comply', r'comply'), ('E260', 'water transportation destitute', r'destitute'), ('E260', 'obrien ingalls', r'ingalls'),
 ('E262', 'homan cable', r'cable'), ('E262', 'short notice material', r'short notice'), ('E262', 'cable appomattox', r'appomattox'),
 ('E262', 'arriving considerable', r'considerable'), ('E262', 'none on hand cable', r'none on hand'), ('E262', 'side of the james', r'side of'),
 ('E263', 'empty steamers', r'empty'), ('E263', 'estimates buildings', r'estimates'), ('E263', 'fast as they arrive', r'fast as'),
 ('E263', 'howell ingalls', r'howell'), ('E263', 'bradley steamers washington', r'bradley'), ('E263', 'bring down troops', r'bring down'),
]
n = 0
for e, q, rx in Q:
    url = HB + "dmQuery/p16003coll11/CISOSEARCHALL%5E" + urllib.parse.quote(q) + "%5Eall%5Eand/title!transc/nosort/200/1/0/0/1/0/json"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60))
    except Exception as ex:
        print(e, q, 'ERR', str(ex)[:80]); n += 1; time.sleep(3.2); continue
    n += 1
    recs = d.get('records', [])
    print(f'== {e} {q!r}: {d.get("pager", {}).get("total")} hits')
    for r in recs[:40]:
        t = str(r.get('transc') or '')
        ms = list(re.finditer(rx, t, re.I))[:1]
        for m in ms:
            print(f'  {r.get("pointer")} | {str(r.get("title"))[:40]} | ...{t[max(0, m.start()-200):m.end()+200]}...'.replace('\n', ' '))
        if not ms:
            print(f'  {r.get("pointer")} | {str(r.get("title"))[:40]} | (term not in transc window)')
    time.sleep(3.2)
print('requests', n)
