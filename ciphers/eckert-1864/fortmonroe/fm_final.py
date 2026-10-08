#!/usr/bin/env python3
"""FM-PRE stage 5 (8 Oct 2026): merge prefilter-fm.tsv (offline) with net-fm-ia.tsv / net-fm-hdl.tsv (network) into prefilter-fm-final.tsv, and write
clean-fm.tsv, the rows still clean after every check, ordered for a reader: book guess (No. 1 first), then lowest print cover first (PF4's order),
then longest first. A ranking, not a verdict (rule 10). No arguments."""
import collections, csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import fm_entries as fe
sys.path.insert(0, os.path.dirname(HERE)); import prefilter_ls4 as pl
OUT = fe.OUTDIR; S = fe.S

def tsv(name):
    p = os.path.join(OUT, name)
    if not os.path.exists(p): return []
    return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))

def filed_ms18():
    """MS18-PRE: entries of mssEC 18 already filed (ls3_r18_readings.md headers '**E78 | mssEC 18 p.48, pointer 9714 | 21 Apr 1864 ...'): {(pointer, yyyy-mm-dd): id}."""
    import re
    mon = {m_: i + 1 for i, m_ in enumerate("jan feb mar apr may jun jul aug sep oct nov dec".split())}
    out = {}
    for l in open(os.path.join(os.path.dirname(HERE), "ls3_r18_readings.md"), encoding="utf-8"):
        mm = re.match(r"\*\*(\S+) \| mssEC 18 p\.\d+, pointer (\d+) \| (\d+) (\w{3})\w* (\d{4})", l)
        if mm: out.setdefault((mm.group(2), "%s-%02d-%02d" % (mm.group(5), mon[mm.group(4).lower()], int(mm.group(3)))), []).append(mm.group(1))
    return out

def main():
    pre = tsv("prefilter-%s.tsv" % S)
    ia = {(r["pointer"], r["entry"]): r for r in tsv("net-%s-ia.tsv" % S)}
    hd = {(r["pointer"], r["entry"]): r for r in tsv("net-%s-hdl.tsv" % S)}
    gb = {(r["pointer"], r["entry"]): r for r in tsv("net-%s-gb.tsv" % S)}    # MS18-PRE only (ms18/ms18_gb.py)
    cols = list(pre[0].keys()) + ["ia_phrase", "ia_result", "ia_print", "hunt_best", "hunt_hits", "gb_total", "gb_print", "net", "final_verdict"]
    out = []
    filed = filed_ms18() if S == "ms18" else {}
    for r in pre:
        k = (r["pointer"], r["entry"]); i = ia.get(k); h = hd.get(k)
        r["ia_phrase"] = (i or {}).get("phrase", ""); r["ia_result"] = (i or {}).get("ia_result", ""); r["ia_print"] = (i or {}).get("ia_print", "")
        r["hunt_best"] = (h or {}).get("hunt_best", ""); r["hunt_hits"] = (h or {}).get("hunt_hits", "")
        g = gb.get(k) or {}; r["gb_total"] = g.get("gb_total", ""); r["gb_print"] = g.get("gb_print", "")
        r["net"] = ("ia" if i and i.get("ia_result") not in (None, "", "?") else "") + ("+hdl" if h and h.get("hunt_hits") not in (None, "", "query=?") else "")
        if r["verdict"] != "clean": fv = r["verdict"]
        else:
            v = []
            if r["ia_print"]: v.append("print-likely")
            if r["hunt_best"] in ("y", "y+copy", "copy"): v.append("clear-sibling")
            # PF4's phrase rule: at most 20 volumes in the whole index and one of them a war-records / correspondent work; a generic phrase in unrelated books is not a hit
            if r["gb_print"] and str(r["gb_total"]).isdigit() and int(r["gb_total"]) <= 20 and pl.REL.search(r["gb_print"]): v.append("print-likely(gb)")
            fv = "+".join(v) if v else ("clean" if "hdl" in r["net"] else "clean-offline")
        if S == "ms18" and "1865-01-01" <= r["date"] <= "1865-04-30":    # LS3-K: the book for Jan-Apr 1865 is not in hand; listed, not scored
            fv = "book-not-in-hand" + ("" if fv.startswith("clean") else "+" + fv)
        fid = filed.get((r["pointer"], r["date"]))
        if fid: fv = "filed:" + "/".join(fid) + ("" if fv.startswith("clean") else "+" + fv)    # same leaf and day as an entry already filed: the reader checks it is the same telegram
        r["final_verdict"] = fv; out.append(r)
    with open(os.path.join(OUT, "prefilter-%s-final.tsv" % S), "w") as f:
        f.write("# " + fe.LAB + " (8 Oct 2026): prefilter-" + fe.S + ".tsv + network checks (fm_final.py). final_verdict clean = offline clean AND the Huntington full-text check run and silent (the be-api phrase layer failed its own control, 1 of 7, and was stopped after 30 rows; a hit there still counts); "
                "clean-offline = the Huntington check not run for that row (< 40 words). A ranking, not a verdict.\n")
        f.write("\t".join(cols) + "\n")
        for r in out: f.write("\t".join(str(r.get(c, "")).replace("\t", " ") for c in cols) + "\n")
    book = {"1": 0, "9": 1, "2": 2}
    clean = [r for r in out if r["final_verdict"] == "clean"]
    clean.sort(key=lambda r: (book.get(r["best_book"], 3), int(r["or_cov"]), -int(r["words"]), r["date"]))
    ccols = ["best_book", "pointer", "page", "entry", "date", "direction", "words", "or_cov", "s1", "s2", "s9", "hunt_best", "ia_result"]
    with open(os.path.join(OUT, "clean-%s.tsv" % S), "w") as f:
        f.write("# " + fe.LAB + " (8 Oct 2026): rows clean after offline + network checks, ordered for a reader (book guess, lowest print cover, longest). Not a verdict; a clean row can still be in print.\n")
        f.write("\t".join(ccols) + "\n")
        for r in clean: f.write("\t".join(str(r[c]) for c in ccols) + "\n")
    c = collections.Counter(r["final_verdict"] for r in out)
    print(sorted(c.items(), key=lambda x: -x[1]), "reader rows", len(clean), collections.Counter(r["best_book"] for r in clean), file=sys.stderr)

if __name__ == "__main__":
    main()
