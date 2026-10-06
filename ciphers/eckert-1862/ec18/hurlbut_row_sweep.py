#!/usr/bin/env python3
"""Date-aligned sweep of one Hurlbut-row code word (Leghorn, Legend, Leopard, Lehigh) in the sent ledgers mssEC 18-19.

Usage: hurlbut_row_sweep.py DATA_DIR OR_DIR WORD [WORD ...] [--out candidates.tsv]

  DATA_DIR/vol18.json, vol19.json: the CONTENTdm dmQuery pages (URLs and sha256 in ../pilot1864/manifest.tsv).
  OR_DIR/<vol>.txt: the OR ser. I `_djvu.txt` files listed in or_volumes.tsv (URLs and sha256 there). Neither is committed.

For every case-insensitive occurrence of WORD (with -s / -'s) in the volunteer text, the script writes the telegram
header nearest above it on the page (date line), the ledger context, and the best OR location: the OR offset where the
most 3-word clear-context shingles from the 14 words either side of the hit fall within 600 characters, with the OR text
around that cluster. It does not decide anything: the slot word in the print is read by eye from the snippet and the row
goes into <word>_uses.tsv by hand (R12A-ECKLEG, 6 Oct 2026; the same method D1-ECK62S used for lehigh_uses.tsv by eye).
No score, no gate.
"""
import json, re, sys, collections
from pathlib import Path

MONTHS = "jan|feb|mch|mar|apr|may|jun|jul|aug|sep|oct|nov|dec"
DATE = re.compile(r"(?i)\b(%s)\w*\.?\s*(\d{1,2})(?:st|nd|rd|th)?\.?,?\s*(?:18)?(6[2-7])\b" % MONTHS)

def norm(s):
    return re.sub(r"[^a-z ]+", " ", s.lower()).split()

def main(a):
    out = a[a.index("--out") + 1] if "--out" in a else None
    pos_args = [x for i, x in enumerate(a) if x != "--out" and (i == 0 or a[i-1] != "--out")]
    data, ordir, words = Path(pos_args[0]), Path(pos_args[1]), [w.lower() for w in pos_args[2:]]
    hits = []
    for v in ("18", "19"):
        recs = json.load(open(data / ("vol%s.json" % v)))["records"]
        for r in recs:
            t = r.get("transc") or ""
            if not isinstance(t, str):
                continue
            for word in words:
                for m in re.finditer(r"(?i)\b%s(?:'?s)?\b" % re.escape(word), t):
                    dates = list(DATE.finditer(t[:m.start()]))
                    date = dates[-1].group(0) if dates else "(none above on page)"
                    header = ""
                    if dates:
                        hl = t.rfind("\n", 0, dates[-1].start())
                        he = t.find("\n", dates[-1].end())
                        header = " ".join(t[hl+1:he if he > 0 else len(t)].split())
                    before = norm(t[:m.start()])[-14:]
                    after = norm(t[m.end():])[:14]
                    sh = [tuple(before[i:i+3]) for i in range(len(before) - 2)] + \
                         [tuple(after[i:i+3]) for i in range(len(after) - 2)]
                    ctx = " ".join(t[max(0, m.start()-120):m.end()+120].split())
                    hits.append(dict(row=["mssEC " + v, str(r["pointer"]), r["title"].replace("Page ", ""), date,
                                          header[:90], m.group(0), ctx], sh=set(sh), best=(0, None, None)))
    need = set().union(*[h["sh"] for h in hits]) if hits else set()
    snips = {}
    for f in sorted(Path(ordir).glob("*.txt")):
        ot = f.read_text(errors="replace")
        w = [(m.group(0).lower(), m.start()) for m in re.finditer(r"[A-Za-z]+", ot)]
        idx = collections.defaultdict(list)
        for i in range(len(w) - 2):
            k = (w[i][0], w[i+1][0], w[i+2][0])
            if k in need:
                idx[k].append(w[i][1])
        for h in hits:
            pos = sorted(p for s in h["sh"] for p in idx.get(s, []))
            for i, p in enumerate(pos):
                n = sum(1 for q in pos[i:] if q - p <= 600)
                if n > h["best"][0]:
                    heads = re.findall(r"\n\s*(\d{1,4})\s*\n|\n\s*(\d{1,4}) [A-Z]{3,}|[A-Z]{3,}\.?\s+(\d{1,4})\s*\n", ot[max(0, p-9000):p])
                    nums = [x for hh in heads for x in hh if x]
                    h["best"] = (n, f.stem, p)
                    h["snip"] = " ".join(ot[max(0, p-250):p+450].split())
                    h["pg"] = nums[-1] if nums else ""
        del ot, w, idx
    rows = []
    for h in hits:
        n, vol, p = h["best"]
        ok = vol and n >= 2
        rows.append(h["row"] + [str(n), vol if ok else "", h.get("pg", "") if ok else "", h.get("snip", "") if ok else ""])
    hdr = ["ledger", "pointer", "page", "date_ocr", "header", "form", "ledger_context", "shingles", "or_vol",
           "or_page_ocr_approx", "or_snippet"]
    lines = ["\t".join(hdr)] + ["\t".join(x) for x in rows]
    txt = "\n".join(lines) + "\n"
    if out:
        Path(out).write_text(txt)
    else:
        sys.stdout.write(txt)

if __name__ == "__main__":
    main(sys.argv[1:])
