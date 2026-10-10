#!/usr/bin/env python3
"""FV-N2e G3: Google Books API phrase search (key from GOOGLE_BOOKS_KEY, country=US) on decoded phrases of N2-IA..IH; prints id, title, date, viewability, snippet."""
import json, os, time, urllib.parse, urllib.request
Q = [("IA", '"detained in Baltimore a few days"'), ("IB", '"vacant major-generalship for Crook"'), ("IB", '"muster out Heintzelman"'),
     ("IC", '"no grading between Monroe and Shreveport"'), ("IC", '"any work has been done upon it since"'), ("IC", '"gauge of the Vicksburg and Monroe"'),
     ("IC", '"seventy-four and a quarter miles"'), ("ID", '"21st street and Pennsylvania avenue" Buyers'), ("ID", '"searched for the man Buyers"'),
     ("IG", '"assembled at Bermuda Hundred instead of"'), ("IG", '"cause General Rucker to be notified"'), ("IH", '"Canby and not Hurlbut"')]
for tag, q in Q:
    u = "https://www.googleapis.com/books/v1/volumes?q=" + urllib.parse.quote(q) + "&country=US&maxResults=5&key=" + os.environ["GOOGLE_BOOKS_KEY"]
    d = json.load(urllib.request.urlopen(u, timeout=40))
    print(f"== {tag} {q} total {d.get('totalItems')}")
    for i in d.get("items", [])[:5]:
        v = i["volumeInfo"]; s = (i.get("searchInfo", {}).get("textSnippet") or "")[:240]
        print(f"  {i['id']} | {v.get('title','')[:60]} | {v.get('publishedDate')} | {i['accessInfo']['viewability']} | {s}")
    time.sleep(2)
