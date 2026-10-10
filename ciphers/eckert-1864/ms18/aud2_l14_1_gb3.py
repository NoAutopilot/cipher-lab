#!/usr/bin/env python3
"""AUD2-LEDGER14-1 (10 Oct 2026): in-volume snippet queries on three Delaware leads (keyed, country=US, 1.6 s apart)."""
import json, os, time, urllib.parse, urllib.request
KEY = os.environ.get("GOOGLE_BOOKS_KEY", "")
Q = [
 ('"mouth of the Monocacy"', "VeE7BgAAQBAJ"),
 ('"cannot carry the state without them"', "VeE7BgAAQBAJ"),
 ('"First Delaware Cavalry"', "VeE7BgAAQBAJ"),
 ('furlough', "VeE7BgAAQBAJ"),
 ('"cannot carry the state without them"', "-QlQAQAAIAAJ"),
 ('"Delaware Cavalry"', "-QlQAQAAIAAJ"),
 ('furlough', "-QlQAQAAIAAJ"),
 ('"October 28"', "-QlQAQAAIAAJ"),
 ('Stanton furlough', "-QlQAQAAIAAJ"),
 ('"cannot carry the state without them"', "7hIRAAAAIAAJ"),
 ('"Delaware Cavalry"', "7hIRAAAAIAAJ"),
 ('furlough', "7hIRAAAAIAAJ"),
]
out = []
for q, vol in Q:
    url = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote(q)}+id:{vol}&country=US&key={KEY}"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=30))
    except Exception as e:
        out.append(f"{q} | {vol} | ERROR {type(e).__name__}"); time.sleep(1.6); continue
    out.append(f"{q} | {vol} | {d.get('totalItems',0)}")
    for it in d.get("items", [])[:3]:
        v = it.get("volumeInfo", {}); s = it.get("searchInfo", {}).get("textSnippet", "")
        out.append(f"    {v.get('title','')[:50]} {v.get('publishedDate','')} {v.get('authors')} | {s}")
    time.sleep(1.6)
print("\n".join(out))
