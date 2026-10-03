#!/usr/bin/env python3
"""H70: walk Founders Online 'More between these correspondents' Preceding/Next chain (Armstrong<->Madison)
from a seed doc, both directions, until the date leaves [LO, HI]. One headless fetch at a time, 2 s apart,
one retry after a 20 s pause, logged to requests.log. Pages saved as docs/<id>.html (fetch once)."""
import os, re, subprocess, sys, time, html
LO, HI = os.environ.get("LO", "1807-11-15"), os.environ.get("HI", "1808-06-15")
MON = {m: i+1 for i, m in enumerate("January February March April May June July August September October November December".split())}
os.makedirs("docs", exist_ok=True)
def fetch(did):
    out = f"docs/{did.replace('/','_')}.html"
    if os.path.exists(out) and os.path.getsize(out) > 5000: return out
    url = f"https://founders.archives.gov/documents/{did}"
    for attempt in (1, 2):
        env = dict(os.environ, NODE_PATH=subprocess.run(["npm","root","-g"],capture_output=True,text=True).stdout.strip())
        subprocess.run(["timeout","120","node","../../../tools/browser_fetch.js",url,out],env=env,capture_output=True)
        sz = os.path.getsize(out) if os.path.exists(out) else 0
        with open("requests.log","a") as f: f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())}\tbrowser\t{sz}\t{url}\n")
        time.sleep(2)
        if sz > 5000 and "Founders Online" in open(out,errors="ignore").read(): return out
        if attempt == 1: time.sleep(20)
    return None
def meta(path):
    t = open(path, errors="ignore").read()
    title = html.unescape(re.search(r"<title>(.*?)</title>", t, re.S).group(1)).strip()
    m = re.search(r"(\d{1,2}) (\w+) (\d{4})", title)
    date = f"{m.group(3)}-{MON.get(m.group(2),0):02d}-{int(m.group(1)):02d}" if m else "?"
    prev = re.search(r"Preceding.*?href=\"/documents/([^\"]+)\"", t, re.S)
    nxt = re.search(r"Next\s*</[^>]+>.*?href=\"/documents/([^\"]+)\"", t, re.S)
    return title, date, prev.group(1) if prev else None, nxt.group(1) if nxt else None
seed = sys.argv[1] if len(sys.argv) > 1 else "Madison/99-01-02-2703"
seen = {}
for direction in ("prev", "next"):
    did, first = seed, True
    while did and (first or did not in seen):
        p = fetch(did)
        if not p: print("FAIL", did, flush=True); break
        title, date, prev, nxt = meta(p); seen[did] = (date, title)
        if first or True: print(date, did, title, flush=True)
        if not first and date != "?" and (date < LO or date > HI): break
        first = False
        did = prev if direction == "prev" else nxt
with open("chain.tsv", "w") as f:
    for did, (d, t) in sorted(seen.items(), key=lambda x: x[1][0]): f.write(f"{d}\t{did}\t{t}\n")
