#!/usr/bin/env python3
"""AUD2-LEDGER10-4 pass 2: Canby's 28 May letter in print (52 vs 72 miles to Monroe); the VS&T directors' report of January 1861; ser. III / Grant Papers vol. 11 context."""
import json, os, time, urllib.parse, urllib.request
Q = [("10383", '"one hundred and forty-eight miles" Vicksburg Shreveport'), ("10383", '"road to Monroe" Canby Vicksburg 1864 "has been in operation"'),
     ("rr", '"Vicksburg, Shreveport and Texas" "annual report" January 1861 directors'), ("rr", '"Vicksburg, Shreveport & Texas Railroad" "January 31, 1861"'),
     ("rr", '"Vicksburg, Shreveport and Texas" "seventy-four" Monroe'),
     ("ctx", 'Meigs Canby "Vicksburg and Monroe" 1864 gauge "Papers of Ulysses S. Grant"'), ("ctx", '"Vicksburg and Shreveport Railroad" Meigs Canby 1864 gauge repair Grant')]
for tag, q in Q:
    u = "https://www.googleapis.com/books/v1/volumes?q=" + urllib.parse.quote(q) + "&country=US&maxResults=6&key=" + os.environ["GOOGLE_BOOKS_KEY"]
    try:
        d = json.load(urllib.request.urlopen(u, timeout=40))
    except Exception as e:
        print(f"== {tag} {q} ERROR {type(e).__name__}"); time.sleep(3); continue
    print(f"== {tag} {q} total {d.get('totalItems')}")
    for i in d.get("items", [])[:6]:
        v = i["volumeInfo"]; s = (i.get("searchInfo", {}).get("textSnippet") or "")[:300]
        print(f"  {i['id']} | {v.get('title','')[:60]} | {v.get('publishedDate')} | {i['accessInfo']['viewability']} | {s}")
    time.sleep(2)
