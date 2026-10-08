#!/usr/bin/env python3
"""MS18-PRE stage 3a (8 Oct 2026): print-side-independent known-answer list for the mssEC 18 pre-filter.
Not the cover statistic: for every ledger entry that is clear in the ledger (code fraction < 0.12, >= 20 words) take its every 8-word run
(lower case, letters only) and look for it exactly in the normalised text of the print volumes in --scratch. An exact 8-word run in print is a located
printed copy (OCR slips and the clerk's spelling make this a recall-limited list: it finds copies, it cannot exclude them). Writes ms18/known-ms18.tsv with each
located entry, its printed volume, and the pre-filter verdict. Usage: ms18_known.py --scratch DIR"""
import argparse, csv, os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__)); PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT); sys.path.insert(0, os.path.join(PARENT, "fortmonroe"))
os.environ["FM_LEDGER"] = "ms18"
import entries_mssEC19 as m, fm_entries as fe, fm_prefilter as fp

def norm(s): return re.findall(r"[a-z]+", s.lower())

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--scratch", required=True); a = ap.parse_args()
    codes, ents = fe.build()
    pre = {(r["pointer"], r["entry"]): r for r in csv.DictReader((l for l in open(os.path.join(HERE, "prefilter-ms18.tsv")) if not l.startswith("#")), delimiter="\t")}
    cand = [e for e in ents if e["codefrac"] < 0.12 and e["words"] >= 20]
    want = {}
    for ci, e in enumerate(cand):
        t = e["tokens"]
        for i in range(len(t) - 7):
            want.setdefault(tuple(t[i:i + 8]), set()).add(ci)
    hits = collections.defaultdict(lambda: collections.defaultdict(int))
    for vol, label in fp.VOLS.items():
        fn = os.path.join(a.scratch, "or", vol + ".txt")
        if not os.path.exists(fn): continue
        t = norm(open(fn, encoding="utf-8", errors="replace").read())
        for i in range(len(t) - 7):
            g = tuple(t[i:i + 8])
            if g in want:
                for ci in want[g]: hits[ci][label] += 1
    rows = []
    for ci, h in hits.items():
        e = cand[ci]; r = pre[(str(e["pointer"]), str(e["entry_on_page"]))]
        rows.append((e["pointer"], e["entry_on_page"], e["date"], e["words"], sum(h.values()), max(h, key=h.get), r["or_cov"], r["verdict"]))
    rows.sort()
    with open(os.path.join(HERE, "known-ms18.tsv"), "w") as f:
        f.write("# MS18-PRE (8 Oct 2026): clear ledger entries whose exact 8-word plain runs occur in the print volumes (ms18_known.py); located independently of the cover statistic. a ranking input, not a verdict.\n")
        f.write("pointer\tentry\tdate\twords\texact_8gram_hits\ttop_volume\tor_cov\tprefilter_verdict\n")
        for r in rows: f.write("\t".join(map(str, r)) + "\n")
    flagged = sum("print-likely" in r[7] for r in rows)
    print(f"clear entries >=20 words: {len(cand)}; located in print by exact 8-gram: {len(rows)}; pre-filter print-likely among them: {flagged}", file=sys.stderr)
if __name__ == "__main__": main()
