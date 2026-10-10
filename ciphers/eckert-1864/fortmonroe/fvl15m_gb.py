#!/usr/bin/env python3
"""FV-L15m (10 Oct 2026, for LANE LEDGER-15): Google Books API snippets for E571 in Grant Papers vol. 14 (keyed, country=US, 1.6 s apart; key never printed)."""
import json, os, re, time, urllib.parse, urllib.request
K = os.environ["GOOGLE_BOOKS_KEY"]; n = 0
for q in ['"Convoy is now ready"', '"few moments with" Babcock Roberts', '"Glisson says he will send" Rawlins telegraphed']:
    for vid in ["DVLPEPsH1_oC", "1D8fAQAAMAAJ"]:
        u = f"https://www.googleapis.com/books/v1/volumes?q={urllib.parse.quote(q)}&country=US&key={K}"
        u = f"https://www.googleapis.com/books/v1/volumes/{vid}?country=US&key={K}" if False else u
        break
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "cipher-lab research script (contact via repository)"}), timeout=60).read()); n += 1
    print("##", q, "total", d.get("totalItems"))
    for it in d.get("items", [])[:6]:
        s = re.sub("<[^>]+>", "", (it.get("searchInfo") or {}).get("textSnippet", ""))
        print("  ", it["id"], it["volumeInfo"].get("title", "")[:50], "|", s)
    time.sleep(1.6)
print("requests", n)
