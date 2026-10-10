#!/usr/bin/env python3
"""AUD2-LEDGER14-1 (10 Oct 2026): Google Books API queries for E600/E602 second audit.
Keyed (GOOGLE_BOOKS_KEY from env, never printed), country=US, 1.6 s apart, positive control first."""
import json, os, sys, time, urllib.parse, urllib.request
KEY = os.environ.get("GOOGLE_BOOKS_KEY", "")
Q = [
 ("CTRL", '"those who join Mosby are exempt"'),
 ("CTRL2", '"transportation waiting at Locust Point"'),
 ("E600", '"Delaware Cavalry" furlough vote Wallace 1864'),
 ("E600", '"enable them to go home and vote"'),
 ("E600", '"go home and vote" "transportation going and returning"'),
 ("E600", '"furlough of sufficient time to enable them"'),
 ("E600", '"First Delaware Cavalry" "vote" 1864 furlough'),
 ("E600", '"without prejudice to the public service" "go home and vote"'),
 ("E600", '"Delaware" "go home and vote" Stanton October 1864'),
 ("E600", '"such of the" "Delaware" "as are in your command" furlough'),
 ("E602", '"Locust Point" Ricketts Meigs 1864'),
 ("E602", '"Ricketts" "without ambulances" Meigs'),
 ("E602", '"more than enough transportation" Harper\'s Ferry 1864'),
 ("E602", '"too many animals and wagons"'),
 ("E602", '"forage collected at Martinsburg"'),
 ("E602", '"Hunter\'s large train"'),
 ("E602", '"Sigel is reported not to have lost"'),
 ("E602", 'Meigs "Captain Thomas" Baltimore July 1864 Ricketts'),
 ("E602", '"necessities of this campaign" Meigs'),
]
out = []
for lab, q in Q:
    url = ("https://www.googleapis.com/books/v1/volumes?q=" + urllib.parse.quote(q)
           + "&maxResults=6&country=US&key=" + KEY)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "cipher-lab research script (contact via repository)"})
        d = json.load(urllib.request.urlopen(req, timeout=30))
    except Exception as e:
        out.append(f"{lab} | {q} | ERROR {type(e).__name__}"); time.sleep(1.6); continue
    out.append(f"{lab} | {q} | {d.get('totalItems',0)}")
    for it in d.get("items", [])[:6]:
        v = it.get("volumeInfo", {}); s = it.get("searchInfo", {}).get("textSnippet", "")
        out.append(f"    {v.get('title','')[:60]} {v.get('publishedDate','')} [{it.get('id')}] | {s[:260]}")
    time.sleep(1.6)
print("\n".join(out))
