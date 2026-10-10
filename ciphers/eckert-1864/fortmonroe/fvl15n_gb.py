#!/usr/bin/env python3
"""FV-L15n (10 Oct 2026): Google Books snippet queries for the E537/E565 N1 confirms (Grant Papers 13/14).
Key from GOOGLE_BOOKS_KEY (never printed), country=US, 1.6 s apart. Output fvl15n_gb.out."""
import json, os, time, urllib.parse, urllib.request
IDS = {"mnRjmhe3QLoC": "v13", "ij8fAQAAMAAJ": "v13", "DVLPEPsH1_oC": "v14", "1D8fAQAAMAAJ": "v14"}
Q = [("E537", '"remain at Varina until Mr. Blair arrives" intitle:Grant'),
     ("E537", '"January 20, 1865" Ord Mulford "Steamer New York" intitle:Grant'),
     ("E565", '"Shall I go without him" intitle:Grant'),
     ("E565", '"March 5, 1865" Roberts scout Bowers intitle:Grant'),
     ("E544", '"All asked for by you has been ordered" intitle:Grant')]
key = os.environ["GOOGLE_BOOKS_KEY"]
out = []
for ent, q in Q:
    url = "https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode({"q": q, "country": "US", "maxResults": 20, "key": key})
    req = urllib.request.Request(url, headers={"User-Agent": "cipher-lab research script (contact via repository)"})
    try:
        d = json.load(urllib.request.urlopen(req, timeout=30))
    except Exception as e:
        out.append(f"{ent}\t{q}\tERROR {type(e).__name__}"); time.sleep(1.6); continue
    hits = [(IDS[i["id"]], i["id"], i.get("searchInfo", {}).get("textSnippet", "")) for i in d.get("items", []) if i["id"] in IDS]
    if not hits:
        out.append(f"{ent}\t{q}\tNO HIT (total {d.get('totalItems', 0)})")
    for v, i, s in hits:
        out.append(f"{ent}\t{q}\t{v} {i}\t{s}")
    time.sleep(1.6)
open("fvl15n_gb.out", "w").write("\n".join(out) + "\n")
print("\n".join(out))
