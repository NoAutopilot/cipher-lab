#!/usr/bin/env python3
"""Fetch every Page: of Index:The Master of Mysteries (1912).djvu from the MediaWiki API, once.
Polite: descriptive User-Agent, maxlag=5, 50 titles per call, >=2 s between calls, stop on 429/403/5xx."""
import json, sys, time, urllib.parse, urllib.request, pathlib, datetime
UA = "cipher-lab research script (contact via repository)"
API = "https://en.wikisource.org/w/api.php"
OUT = pathlib.Path(__file__).parent / "text" / "wikisource"
N = 552
log = []
def call(params):
    params = dict(params, format="json", formatversion="2", maxlag="5")
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
        log.append({"url": url, "status": r.status, "bytes": len(body)})
        return json.loads(body)
pages = {}
for start in range(1, N + 1, 50):
    titles = [f"Page:The Master of Mysteries (1912).djvu/{i}" for i in range(start, min(start + 50, N + 1))]
    try:
        d = call({"action": "query", "prop": "revisions", "rvprop": "content|ids|timestamp",
                  "rvslots": "main", "titles": "|".join(titles)})
    except Exception as e:
        log.append({"error": str(e), "start": start}); print("STOP", e); break
    if "error" in d:
        log.append({"api_error": d["error"], "start": start}); print("STOP", d["error"]); break
    for p in d["query"]["pages"]:
        n = int(p["title"].rsplit("/", 1)[1])
        if p.get("missing"):
            pages[n] = None; continue
        rv = p["revisions"][0]
        pages[n] = {"revid": rv["revid"], "timestamp": rv["timestamp"], "content": rv["slots"]["main"]["content"]}
    print(start, len(pages), flush=True)
    time.sleep(2)
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "pages.json").write_text(json.dumps({str(k): pages[k] for k in sorted(pages)}, ensure_ascii=False, indent=0))
(OUT / "fetch_log.json").write_text(json.dumps({"date": datetime.date.today().isoformat(), "user_agent": UA, "calls": log}, indent=1))
print("pages", len(pages), "missing", sum(1 for v in pages.values() if v is None))
