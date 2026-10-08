#!/usr/bin/env python3
"""FM-PRE stage 5 (8 Oct 2026): merge prefilter-fm.tsv (offline) with net-fm-ia.tsv / net-fm-hdl.tsv (network) into prefilter-fm-final.tsv, and write
clean-fm.tsv, the rows still clean after every check, ordered for a reader: book guess (No. 1 first), then lowest print cover first (PF4's order),
then longest first. A ranking, not a verdict (rule 10). No arguments."""
import collections, csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def tsv(name):
    p = os.path.join(HERE, name)
    if not os.path.exists(p): return []
    return list(csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t"))

def main():
    pre = tsv("prefilter-fm.tsv")
    ia = {(r["pointer"], r["entry"]): r for r in tsv("net-fm-ia.tsv")}
    hd = {(r["pointer"], r["entry"]): r for r in tsv("net-fm-hdl.tsv")}
    cols = list(pre[0].keys()) + ["ia_phrase", "ia_result", "ia_print", "hunt_best", "hunt_hits", "net", "final_verdict"]
    out = []
    for r in pre:
        k = (r["pointer"], r["entry"]); i = ia.get(k); h = hd.get(k)
        r["ia_phrase"] = (i or {}).get("phrase", ""); r["ia_result"] = (i or {}).get("ia_result", ""); r["ia_print"] = (i or {}).get("ia_print", "")
        r["hunt_best"] = (h or {}).get("hunt_best", ""); r["hunt_hits"] = (h or {}).get("hunt_hits", "")
        r["net"] = ("ia" if i and i.get("ia_result") not in (None, "", "?") else "") + ("+hdl" if h and h.get("hunt_hits") not in (None, "", "query=?") else "")
        if r["verdict"] != "clean": fv = r["verdict"]
        else:
            v = []
            if r["ia_print"]: v.append("print-likely")
            if r["hunt_best"] in ("y", "y+copy", "copy"): v.append("clear-sibling")
            fv = "+".join(v) if v else ("clean" if r["net"] == "ia+hdl" else "clean-offline" if not r["net"] else "clean-" + r["net"].strip("+"))
        r["final_verdict"] = fv; out.append(r)
    with open(os.path.join(HERE, "prefilter-fm-final.tsv"), "w") as f:
        f.write("# FM-PRE (8 Oct 2026): prefilter-fm.tsv + network checks (fm_final.py). final_verdict clean = offline clean AND be-api phrase and Huntington full text both run and silent; "
                "clean-offline / clean-ia / clean-hdl = a network check not run for that row (budget or < 40 words). A ranking, not a verdict.\n")
        f.write("\t".join(cols) + "\n")
        for r in out: f.write("\t".join(str(r.get(c, "")).replace("\t", " ") for c in cols) + "\n")
    book = {"1": 0, "9": 1, "2": 2}
    clean = [r for r in out if r["final_verdict"] == "clean"]
    clean.sort(key=lambda r: (book.get(r["best_book"], 3), int(r["or_cov"]), -int(r["words"]), r["date"]))
    ccols = ["best_book", "pointer", "page", "entry", "date", "direction", "words", "or_cov", "s1", "s2", "s9", "hunt_best", "ia_result"]
    with open(os.path.join(HERE, "clean-fm.tsv"), "w") as f:
        f.write("# FM-PRE (8 Oct 2026): rows clean after offline + network checks, ordered for a reader (book guess, lowest print cover, longest). Not a verdict; a clean row can still be in print.\n")
        f.write("\t".join(ccols) + "\n")
        for r in clean: f.write("\t".join(str(r[c]) for c in ccols) + "\n")
    c = collections.Counter(r["final_verdict"] for r in out)
    print(sorted(c.items(), key=lambda x: -x[1]), "reader rows", len(clean), collections.Counter(r["best_book"] for r in clean), file=sys.stderr)

if __name__ == "__main__":
    main()
