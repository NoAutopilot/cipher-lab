#!/usr/bin/env python3
"""VIV-105: fetch native-resolution page regions of the clerk's copy (fr.16107, ark btv1b9009661v) from openapi.bnf.fr.
Re-run to regenerate images/v105/*.jpg (untracked); appends url/date/bytes/sha1 to v105/fetch_log.jsonl.
Usage: python3 v105/fetch.py [info|pages]   (run from the target folder)"""
import hashlib, json, sys, time, urllib.request, os
UA = "cipher-lab research script (contact via repository)"
BASE = "https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9009661v"
# (name, canvas, region) -- pixel regions (c110 as VIV-T; c111 is 8060x6210). A first pct: try returned HTTP 500.
PAGES = [("c110_f105r", 110, "5250,650,3150,5550"), ("c111_f105v", 111, "250,250,3850,5800"),
         ("c111_f106r", 111, "4050,250,3850,5800"), ("c112_f106v", 112, "250,250,3850,5800")]
def get(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read(); code = r.status
    open(out, "wb").write(data)
    rec = {"url": url, "date": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()), "status": code,
           "bytes": len(data), "sha1": hashlib.sha1(data).hexdigest(), "file": out}
    open("v105/fetch_log.jsonl", "a").write(json.dumps(rec) + "\n"); print(rec)
os.makedirs("images/v105", exist_ok=True)
what = sys.argv[1] if len(sys.argv) > 1 else "pages"
if what == "info":
    get(f"{BASE}/f111/info.json", "v105/c111_info.json")
else:
    names = sys.argv[2:] or [p[0] for p in PAGES]
    for n, c, reg in PAGES:
        if n in names:
            get(f"{BASE}/f{c}/{reg}/max/0/default.jpg", f"images/v105/{n}.jpg"); time.sleep(3.2)
