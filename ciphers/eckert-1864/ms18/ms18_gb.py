#!/usr/bin/env python3
"""MS18-PRE stage 4b (8 Oct 2026): Google Books phrase check (Papers of U. S. Grant, Basler, Lincoln Collected Works and the rest of Google's snippet index) on
the 1864 rows left clean by the offline + be-api + Huntington checks. One quoted 4-word plain phrase per row (the phrase fm_net.py's ia phase chose,
net-ms18-ia.tsv), www.googleapis.com/books/v1/volumes with country=US and GOOGLE_BOOKS_KEY (read from the environment, never printed), 2 s apart.
A volume counts as a printed copy only when its textSnippet contains the whole phrase (normalised) and the title or snippet is not the row's own
transcription; 'gb_print' lists up to three such volumes. A positive control (a Grant telegram of 4 May 1864 printed in the Official Records) runs first.
  ms18_gb.py [--budget 200]  -> ms18/net-ms18-gb.tsv (resumable). A ranking input, not a verdict (rule 10)."""
import argparse, csv, json, os, re, sys, time, urllib.parse, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
UA = "cipher-lab research script (contact via repository)"
def norm(s): return " ".join(re.findall(r"[a-z]+", re.sub(r"<[^>]+>", "", s).lower()))
def tsv(p): return list(csv.DictReader((l for l in open(p, encoding="utf-8") if not l.startswith("#")), delimiter="\t")) if os.path.exists(p) else []
def query(phrase):
    url = "https://www.googleapis.com/books/v1/volumes?" + urllib.parse.urlencode({"q": '"%s"' % phrase, "country": "US", "maxResults": 8, "key": os.environ["GOOGLE_BOOKS_KEY"]})
    for attempt in (0, 1):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=40))
        except Exception as ex:
            if attempt: return {"error": str(ex)[:60]}
            time.sleep(6)
def run(phrase):
    j = query(phrase)
    if "error" in j and "totalItems" not in j: return None, []
    hits = []
    for it in j.get("items", []):
        sn = norm(it.get("searchInfo", {}).get("textSnippet", ""))
        if norm(phrase) in sn: hits.append("%s (%s)" % (it["volumeInfo"].get("title", "")[:50], it["volumeInfo"].get("publishedDate", "")))
    return j.get("totalItems", 0), hits
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--budget", type=int, default=200); a = ap.parse_args()
    if not os.environ.get("GOOGLE_BOOKS_KEY"): sys.exit("GOOGLE_BOOKS_KEY not set")
    out = os.path.join(HERE, "net-ms18-gb.tsv"); done = {(r["pointer"], r["entry"]): r for r in tsv(out)}
    ctl_tot, ctl_hits = run("crossing of the Rapidan effected"); print("positive control: total", ctl_tot, "snippet hits", len(ctl_hits), file=sys.stderr)
    if not ctl_hits: sys.exit("positive control missed: Google Books check is not a test today")
    pre = {(r["pointer"], r["entry"]): r for r in tsv(os.path.join(HERE, "prefilter-ms18-final.tsv"))}
    ia = {(r["pointer"], r["entry"]): r for r in tsv(os.path.join(HERE, "net-ms18-ia.tsv"))}
    n = 0
    for k, r in pre.items():
        if r["final_verdict"] != "clean" or not r["date"].startswith("1864") or k in done: continue
        ph = (ia.get(k) or {}).get("phrase", "")
        if not ph or ph == "no-4-run": done[k] = {"pointer": k[0], "entry": k[1], "phrase": ph or "", "gb_total": "", "gb_print": "", "gb_note": "no phrase"}; continue
        if n >= a.budget: break
        tot, hits = run(ph); n += 1
        done[k] = {"pointer": k[0], "entry": k[1], "phrase": ph, "gb_total": "?" if tot is None else tot, "gb_print": " | ".join(hits[:3]), "gb_note": "query failed" if tot is None else ""}
        time.sleep(2)
        if n % 20 == 0: save(out, done)
    save(out, done); print("queries this run", n, file=sys.stderr)
def save(out, done):
    cols = ["pointer", "entry", "phrase", "gb_total", "gb_print", "gb_note"]
    with open(out, "w") as f:
        f.write("# MS18-PRE (8 Oct 2026): Google Books quoted-phrase check on the 1864 clean rows (ms18_gb.py, country=US); gb_print = volumes whose snippet contains the whole phrase. A ranking input, not a verdict.\n")
        f.write("\t".join(cols) + "\n")
        for r in done.values(): f.write("\t".join(str(r.get(c, "")).replace("\t", " ") for c in cols) + "\n")
if __name__ == "__main__": main()
