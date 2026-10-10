"""AUD2-LEDGERN2-1 (account 4): second-audit print searches for N2-FH and N2-GF.
IA advancedsearch + be-api full text, Chronicling America, Google Books. 1.6 s between requests per host.
Writes one line per request to stdout (redirect to aud2_ledgern2_1_search.out)."""
import json, os, time, urllib.parse, urllib.request, sys
UA = "cipher-lab research script (contact via repository)"
def get(url, headers=None, ua=UA):
    h = {"User-Agent": ua}; h.update(headers or {})
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=60) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except Exception as e:
        return getattr(e, "code", 0), str(e)
def ia_adv(q):
    u = "https://archive.org/advancedsearch.php?" + urllib.parse.urlencode({"q": q, "fl[]": ["identifier", "title", "volume"], "rows": 30, "output": "json"}, doseq=True)
    s, b = get(u); time.sleep(1.6)
    try: docs = json.loads(b)["response"]["docs"]
    except Exception: docs = []
    print(f"IA-ADV\t{s}\t{q}\t" + " | ".join(f"{d['identifier']}:{str(d.get('title',''))[:60]}:{d.get('volume','')}" for d in docs)); sys.stdout.flush()
def be(term, ident):
    u = "https://be-api.us.archive.org/fts/v1/search?" + urllib.parse.urlencode({"q": term, "identifier": ident})
    s, b = get(u); time.sleep(1.6)
    try:
        j = json.loads(b); hits = j.get("hits", {}).get("hits", [])
        snips = []
        for h in hits:
            hl = h.get("highlight", {})
            for v in hl.values(): snips += v
        print(f"BE\t{s}\t{ident}\t{term}\t{len(hits)}\t" + " || ".join(x.replace("\n", " ")[:300] for x in snips[:6]))
    except Exception:
        print(f"BE\t{s}\t{ident}\t{term}\tERR\t{b[:200]}")
    sys.stdout.flush()
def ca(q, d1, d2):
    u = "https://www.loc.gov/collections/chronicling-america/?fo=json&c=20&dates=" + d1 + "/" + d2 + "&q=" + urllib.parse.quote(q)
    s, b = get(u, ua="Mozilla/5.0"); time.sleep(1.6)
    try:
        j = json.loads(b); items = j.get("results", [])
        print(f"CA\t{s}\t{q}\t{d1}/{d2}\t{(j.get('pagination') or {}).get('of')}\t" + " | ".join(f"{str(i.get('partof_title') or i.get('title'))[:40]} {i.get('date')} {i.get('id','')[-50:]}" for i in items[:10]))
    except Exception:
        print(f"CA\t{s}\t{q}\tERR\t{b[:200]}")
    sys.stdout.flush()
def gb(q):
    key = os.environ.get("GOOGLE_BOOKS_KEY", "")
    u = "https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode({"q": q, "country": "US", "maxResults": 15, "key": key})
    s, b = get(u); time.sleep(1.6)
    try:
        items = json.loads(b).get("items", [])
        print(f"GB\t{s}\t{q}\t{len(items)}\t" + " | ".join(f"{i['id']}:{i['volumeInfo'].get('title','')[:50]}({i['volumeInfo'].get('publishedDate','')}): {i.get('searchInfo',{}).get('textSnippet','')[:160]}" for i in items[:10]))
    except Exception:
        print(f"GB\t{s}\t{q}\tERR\t{b[:200]}")
    sys.stdout.flush()
if __name__ == "__main__":
    step = sys.argv[1]
    if step == "ia":
        ia_adv('title:(war of the rebellion) AND (volume:4 OR title:"series III") AND title:(series III)')
        ia_adv('title:("official records" navies) AND title:(series I)')
        ia_adv('title:(papers of ulysses s grant) AND volume:13')
        ia_adv('title:(life and letters of george gordon meade)')
        ia_adv('title:(charles russell lowell)')
    elif step == "be":
        for ident, terms in json.loads(sys.argv[2]).items():
            for t in terms: be(t, ident)
    elif step == "ca":
        for q, d1, d2 in json.loads(sys.argv[2]): ca(q, d1, d2)
    elif step == "gb":
        for q in json.loads(sys.argv[2]): gb(q)
