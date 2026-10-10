#!/usr/bin/env python3
"""AUD2-LEDGER10-4 (second audit N2-IC): Google Books API (GOOGLE_BOOKS_KEY, country=US) -- control, decoded phrases, context telegrams, railroad mileage."""
import json, os, time, urllib.parse, urllib.request
Q = [("control", '"I have telegraphed you twice to inform me of the gauge"'),
     ("IC", '"gauge of the Vicksburg and Monroe railroad"'), ("IC", '"no grading between Monroe"'), ("IC", '"not likely that any work has been done upon it"'),
     ("IC", '"74 1/4 miles" Vicksburg Monroe'), ("IC", '"seventy-four and a quarter" Vicksburg Monroe'), ("IC", 'Meigs Canby gauge Vicksburg Monroe railroad June 1864'),
     ("ctx", '"expediency of the expense is so much doubted"'), ("ctx", '"repair of the railroad from Vicksburg to Monroe"'),
     ("rr", '"Vicksburg, Shreveport and Texas" railroad annual report directors 1861'), ("rr", '"Vicksburg, Shreveport and Texas" Monroe miles gauge'),
     ("rr", '"Vicksburg, Shreveport" "31st January, 1861"')]
for tag, q in Q:
    u = "https://www.googleapis.com/books/v1/volumes?q=" + urllib.parse.quote(q) + "&country=US&maxResults=6&key=" + os.environ["GOOGLE_BOOKS_KEY"]
    try:
        d = json.load(urllib.request.urlopen(u, timeout=40))
    except Exception as e:
        print(f"== {tag} {q} ERROR {type(e).__name__}"); time.sleep(3); continue
    print(f"== {tag} {q} total {d.get('totalItems')}")
    for i in d.get("items", [])[:6]:
        v = i["volumeInfo"]; s = (i.get("searchInfo", {}).get("textSnippet") or "")[:260]
        print(f"  {i['id']} | {v.get('title','')[:60]} | {v.get('publishedDate')} | {i['accessInfo']['viewability']} | {s}")
    time.sleep(2)
