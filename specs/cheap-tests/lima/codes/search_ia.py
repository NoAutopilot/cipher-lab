#!/usr/bin/env python3
"""Search archive.org advancedsearch.php for four telegraph codebooks (lima-1916 test 1).
One request at a time, >=1.5s apart, descriptive UA. Writes candidates JSON."""
import json
import sys
import time
import urllib.parse
import urllib.request

UA = "cipher-lab research script (contact via repository)"
BOOKS = [
    ("abc_code", 'title:("A B C" OR "ABC") AND title:(code OR telegraphic) AND title:(universal OR commercial)'),
    ("western_union", 'title:("Western Union Telegraphic Code")'),
    ("lieber", 'title:("Standard Telegraphic Code") AND creator:(Lieber)'),
    ("bentley", 'title:("Bentley\'s Complete Phrase Code")'),
]

REQS = 0

def fetch(url):
    global REQS
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = r.read()
    REQS += 1
    time.sleep(1.6)
    return data

def search(query):
    params = {
        "q": query,
        "fl[]": ["identifier", "title", "date", "year"],
        "rows": "5",
        "output": "json",
    }
    url = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode(params, doseq=True)
    data = fetch(url)
    return json.loads(data)

def main():
    out = {}
    only = sys.argv[1:] if len(sys.argv) > 1 else None
    for key, q in BOOKS:
        if only and key not in only:
            continue
        try:
            res = search(q)
            docs = res.get("response", {}).get("docs", [])
        except Exception as e:
            docs = []
            print(f"{key}: search error {e}", file=sys.stderr)
        out[key] = docs
        print(key, "->", [(d.get("identifier"), d.get("title"), d.get("year")) for d in docs])
    path = "specs/cheap-tests/lima/codes/search_results.json"
    try:
        with open(path) as f:
            merged = json.load(f)
    except FileNotFoundError:
        merged = {}
    merged.update(out)
    with open(path, "w") as f:
        json.dump(merged, f, indent=1)
    print("requests:", REQS)

if __name__ == "__main__":
    main()
