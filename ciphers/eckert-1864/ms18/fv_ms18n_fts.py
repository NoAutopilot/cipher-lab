"""FV-MS18n: IA be-api full-text queries (E371, E374, E375). Usage: fv_ms18n_fts.py 'QUERY' [...]; prints id, title, first highlight. A miss is a search result (rule 10)."""
import json, sys, time, urllib.parse, urllib.request
UA = "cipher-lab research script (contact via repository)"
for q in sys.argv[1:]:
    url = "https://be-api.us.archive.org/fts/v1/search?" + urllib.parse.urlencode({"q": q, "size": 15})
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
        d = json.load(r)
    hits = d.get("hits", {}).get("hits", [])
    print(f"## {q!r}: {d.get('hits', {}).get('total')} hits")
    for h in hits:
        f = h.get("fields", {}); hl = h.get("highlight", {})
        snip = " ... ".join(sum(hl.values(), []))[:300].replace("\n", " ")
        print(f"  {f.get('identifier', [''])[0]} | {str(f.get('title', [''])[0])[:70]} | {snip}")
    time.sleep(1.6)
