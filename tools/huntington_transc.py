#!/usr/bin/env python3
"""Fetch Huntington CONTENTdm volunteer transcriptions (dmGetItemInfo) for a pointer range.

Usage:
  huntington_transc.py --alias p16003coll11 --compound 9302 --out DIR     # page pointers from dmGetCompoundObjectInfo
  huntington_transc.py --alias p16003coll11 --range 8893 8900 --out DIR   # explicit inclusive range
  huntington_transc.py --summarize DIR                                    # list pointer, title, transc length (offline)

One request every --delay seconds (default 1.6) with a browser UA; pointers already cached
as DIR/p<pointer>.json are skipped; stops on 429/403 after one retry. Stores title, transc and
page-level fields only (no images). Route: ciphers/eckert-1864/NOTES.md D4-E5.
"""
import argparse, http.client, json, os, sys, time, urllib.request, urllib.error

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
BASE = "https://hdl.huntington.org/digital/bl/dmwebservices/index.php?q="
KEEP = ("title", "callid", "transc", "date", "dateh")

def get(path):
    req = urllib.request.Request(BASE + path, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def slim(d):
    return {k: d.get(k) for k in KEEP}

def fetch_one(alias, ptr):
    for attempt in (0, 1):
        try:
            return slim(get(f"dmGetItemInfo/{alias}/{ptr}/json"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 403):
                if attempt: raise SystemExit(f"HTTP {e.code} twice at {ptr}: stopping host")
            elif attempt: raise
        except (urllib.error.URLError, http.client.HTTPException, OSError, ValueError):
            if attempt: raise
        time.sleep(5)

def pointers_from_compound(alias, obj):
    return [int(p["pageptr"]) for p in get(f"dmGetCompoundObjectInfo/{alias}/{obj}/json")["page"]]

def summarize(d):
    for f in sorted(os.listdir(d)):
        if f.startswith("p") and f.endswith(".json"):
            j = json.load(open(os.path.join(d, f)))
            print(f[1:-5], j.get("title"), len(j.get("transc") or ""), sep="\t")

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--alias"); ap.add_argument("--compound", type=int)
    ap.add_argument("--range", nargs=2, type=int); ap.add_argument("--out")
    ap.add_argument("--delay", type=float, default=1.6); ap.add_argument("--summarize")
    a = ap.parse_args(argv)
    if a.summarize: return summarize(a.summarize)
    if not (a.alias and a.out and (a.compound or a.range)): ap.error("need --alias, --out and --compound or --range")
    os.makedirs(a.out, exist_ok=True)
    ptrs = pointers_from_compound(a.alias, a.compound) if a.compound else list(range(a.range[0], a.range[1] + 1))
    n = 0
    for p in ptrs:
        fn = os.path.join(a.out, f"p{p}.json")
        if os.path.exists(fn): continue
        time.sleep(a.delay)
        json.dump(fetch_one(a.alias, p), open(fn, "w"), ensure_ascii=False)
        n += 1
    print(f"fetched {n}, cached {len(ptrs)-n}, total {len(ptrs)}")

if __name__ == "__main__":
    main()
