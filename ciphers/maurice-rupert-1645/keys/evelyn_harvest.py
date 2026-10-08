#!/usr/bin/env python3
"""D1A-EVL, 8 Oct 2026: harvest the printed cipher-number / interlinear-gloss line pairs from Bray's Evelyn Memoirs (1819)
vol. II, King Charles I - Nicholas correspondence, out of the Internet Archive OCR word boxes, into the PAIRS.tsv format of
tools/interlinear_align.py (plain_line, plain_raw, cipher_line, cipher_raw; here plain_line/cipher_line = 'page:leaf:y').

usage: evelyn_harvest.py DIR [--pages 82-120] [--out keys/evelyn_harvest_pairs.tsv] [--check]
   DIR holds memoirsillustrat02eveluoft_djvu.xml and _page_numbers.json (fetched once from archive.org; not committed).

A cipher line is an OCR line with >= 3 integer word boxes (colon separators dropped). Its gloss is the line directly above
it when that line is set in the small interlinear type: median word height < 0.8 x the leaf's median line height (prose
~40 px, glosses ~23-28 px on these leaves). A prose line above, or none, gives no pair (e.g. passages printed undeciphered).
cipher_raw keeps only the tokens whose x-span falls within the gloss's x-extent, one code width (MARGIN px) to the left and RMARGIN px to the right (trailing prose words dropped), since the
glosses drift left of their numbers (R15-MREVL) and the OCR word boxes are stretched to fill word spaces, so prose
words and unglossed codes at either end of the line do not enter the alignment; clear words inside that span are kept
(interlinear_align treats them as clear, consuming no gloss letters). --check exits non-zero if the output is stale (rule 7)."""
import json, re, sys, pathlib, statistics as st, xml.etree.ElementTree as ET
a = sys.argv[1:]; d = pathlib.Path(a[0]); HERE = pathlib.Path(__file__).resolve().parent
pr = a[a.index("--pages") + 1] if "--pages" in a else "82-120"; p0, p1 = map(int, pr.split("-"))
out = pathlib.Path(a[a.index("--out") + 1]) if "--out" in a else HERE / "evelyn_harvest_pairs.tsv"
pn = {p["leafNum"]: p["pageNumber"] for p in json.load(open(d / "memoirsillustrat02eveluoft_page_numbers.json"))["pages"]}
NUM = re.compile(r"^[\(\[]?\d{1,3}[\.\-:,;\)\]]*$"); MARGIN = 60; RMARGIN = 400
rows = []
for leaf, obj in enumerate(ET.parse(d / "memoirsillustrat02eveluoft_djvu.xml").getroot().iter("OBJECT"), 1):
    pg = pn.get(leaf, "")
    if not str(pg).isdigit() or not (p0 <= int(pg) <= p1): continue
    lines = []
    for ln in obj.iter("LINE"):
        ws = []
        for w in ln.iter("WORD"):
            tx = (w.text or "").strip()
            if not re.search(r"[A-Za-z0-9]", tx): continue
            l, b, r, t = map(int, w.get("coords").split(",")[:4]); ws.append((l, r, t, b, tx))
        if ws: lines.append(sorted(ws))
    if not lines: continue
    lines.sort(key=lambda ws: min(x[2] for x in ws))
    h = lambda ws: st.median(x[3] - x[2] for x in ws); med = st.median(h(ws) for ws in lines)
    for i, ws in enumerate(lines):
        if sum(1 for w in ws if NUM.match(w[4])) < 3 or i == 0: continue
        g = lines[i - 1]
        if sum(1 for w in g if NUM.match(w[4])) >= 0.5 * len(g) or h(g) >= 0.8 * med: continue
        if min(x[2] for x in ws) - max(x[3] for x in g) > MARGIN: continue
        lo, hi = min(x[0] for x in g) - MARGIN, max(x[1] for x in g) + RMARGIN
        cw = [w[4] for w in ws if w[0] >= lo and w[1] <= hi]
        while cw and not NUM.match(cw[-1]): cw.pop()
        if sum(1 for t in cw if NUM.match(t)) < 1: continue
        y = min(x[2] for x in ws)
        rows.append((f"{pg}:{leaf}:{y}g", " ".join(x[4] for x in g), f"{pg}:{leaf}:{y}", " ".join(cw)))
txt = "plain_line\tplain_raw\tcipher_line\tcipher_raw\n" + "".join("\t".join(r) + "\n" for r in rows)
if "--check" in a:
    ok = out.exists() and out.read_text() == txt; print(f"{out.name} up to date" if ok else "STALE"); sys.exit(0 if ok else 1)
out.write_text(txt); print(f"{len(rows)} gloss/cipher line pairs, pages {p0}-{p1} -> {out}")
