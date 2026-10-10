#!/usr/bin/env python3
"""AUD2-LEDGER14-1 (10 Oct 2026): in-volume and targeted Google Books queries, second round (keyed, country=US, 1.6 s apart)."""
import json, os, time, urllib.parse, urllib.request
KEY = os.environ.get("GOOGLE_BOOKS_KEY", "")
Q = [
 ("E600", '"First Delaware Cavalry" "coming election" furlough', None),
 ("E600", '"Delaware Cavalry" "vote" furlough', "VeE7BgAAQBAJ"),
 ("E600", '"Delaware Cavalry" "vote" furlough', "ZM8wAQAAMAAJ"),
 ("E600", '"Delaware Cavalry" vote furlough Stanton Wallace intitle:Delaware', None),
 ("E600", '"Wallace" "Delaware" "furlough" "vote" October 27 1864', None),
 ("E600", '"Delaware" cavalry furlough vote intitle:"Lew Wallace"', None),
 ("E600", 'Wallace furlough "Delaware cavalry" vote 1864 Scharf', None),
 ("E602", '"Locust Point" Ricketts July 1864 quartermaster Thomas', None),
 ("E602", 'Meigs Ricketts "Locust Point" "Harper\'s Ferry" quartermaster', None),
 ("E602", '"Ricketts" "about 8,000 men" Baltimore', None),
]
out = []
for lab, q, vol in Q:
    if vol:
        url = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote(q)}+id:{vol}&country=US&key={KEY}"
    else:
        url = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote(q)}&maxResults=6&country=US&key={KEY}"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=30))
    except Exception as e:
        out.append(f"{lab} | {q} | {vol} | ERROR {type(e).__name__}"); time.sleep(1.6); continue
    out.append(f"{lab} | {q} | {vol} | {d.get('totalItems',0)}")
    for it in d.get("items", [])[:6]:
        v = it.get("volumeInfo", {}); s = it.get("searchInfo", {}).get("textSnippet", "")
        out.append(f"    {v.get('title','')[:60]} {v.get('publishedDate','')} [{it.get('id')}] | {s[:300]}")
    time.sleep(1.6)
print("\n".join(out))
