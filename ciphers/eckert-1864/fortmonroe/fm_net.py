#!/usr/bin/env python3
"""FM-PRE stage 4 (8 Oct 2026): the two network checks of PF4, run only on the rows fm_prefilter.py left clean (>= 40 words).
  fm_net.py --scratch DIR --phase ia  [--budget 250]    one quoted 4-word plain phrase per row through be-api full-text search (no identifier)
  fm_net.py --scratch DIR --phase hdl [--budget 215]    two rare plain words per row through Huntington dmQuery CISOSEARCHALL (transcription in the result);
                                                         hits scored by cover of the row's rare 3-grams (y >= 7, u 3-6) and share of all 3-grams (copy >= 0.5)
Reuses prefilter_ls4.py (Net, phrases, fts, hunt_terms, hunt, hit_scores). Responses are cached (small gz JSON under sources/ia-fulltext/print-check/fm/),
so a re-run is offline. Results go to net-fm-ia.tsv / net-fm-hdl.tsv (merged by fm_final.py). A ranking, not a verdict (rule 10)."""
import argparse, csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT); sys.path.insert(0, HERE)
import entries_mssEC19 as m, prefilter_ls4 as pl, fm_entries as fe, fm_prefilter as fp

OUT = os.path.join(HERE, "net-fm-ia.tsv")      # set per phase in main(): net-fm-ia.tsv / net-fm-hdl.tsv (two phases may run at once)
COLS = ["pointer", "entry", "phrase", "ia_result", "ia_print", "hunt_terms", "hunt_hits", "hunt_best"]

def load_out():
    if not os.path.exists(OUT): return {}
    return {(r["pointer"], r["entry"]): r for r in csv.DictReader((l for l in open(OUT) if not l.startswith("#")), delimiter="\t")}

def save(d):
    with open(OUT, "w") as f:
        f.write("# FM-PRE (8 Oct 2026): network checks on the clean rows (fm_net.py); hunt hit = pointer@parentobject:label:cover:share-of-3-grams; a ranking, not a verdict.\n")
        f.write("\t".join(COLS) + "\n")
        for k in sorted(d, key=lambda k: (int(k[0]), int(k[1]))): f.write("\t".join(str(d[k].get(c, "")).replace("\t", " ") for c in COLS) + "\n")

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--scratch", required=True); ap.add_argument("--phase", choices=["ia", "hdl"], required=True)
    ap.add_argument("--budget", type=int, default=215); ap.add_argument("--min-words", type=int, default=40); ap.add_argument("--offline", action="store_true")
    ap.add_argument("--only", help="comma list pointer/entry (the known-answer control rows of fm_control.py); output net-fm-<phase>-control.tsv, no clean-row filter")
    a = ap.parse_args(argv)
    global OUT
    OUT = os.path.join(HERE, "net-fm-%s%s.tsv" % (a.phase, "-control" if a.only else ""))
    pl.NEWVOLS = {k: v for k, v in fp.VOLS.items() if os.path.exists(os.path.join(a.scratch, "or", k + ".txt"))}
    pl.CACHE = os.path.join(fp.ROOT, "sources", "ia-fulltext", "print-check", "fm"); os.makedirs(pl.CACHE, exist_ok=True)
    codes, fm = fe.build()
    freq, cov, wc = pl.scan_new(fm, codes, a.scratch, os.path.join(pl.CACHE, "scan_fm.json"))
    pre = {(r["pointer"], r["entry"]): r for r in csv.DictReader((l for l in open(os.path.join(HERE, "prefilter-fm.tsv")) if not l.startswith("#")), delimiter="\t")}
    todo = [e for e in fm if pre[(str(e["pointer"]), str(e["entry_on_page"]))]["verdict"] == "clean" and e["words"] >= a.min_words]
    if a.only:
        want = {tuple(x.split("/")) for x in a.only.split(",")}
        todo = [e for e in fm if (str(e["pointer"]), str(e["entry_on_page"])) in want]
    print("rows: %d" % len(todo), file=sys.stderr)
    out = load_out()
    net = pl.Net(a.offline, a.budget if a.phase == "hdl" else 0, a.budget if a.phase == "ia" else 0)
    net.countfile = os.path.join(pl.CACHE, "requests_%s.json" % a.phase); net.prior = json.load(open(net.countfile)) if os.path.exists(net.countfile) else {}
    done = 0
    for e in todo:
        k = (str(e["pointer"]), str(e["entry_on_page"])); row = out.setdefault(k, {"pointer": k[0], "entry": k[1]})
        try:
            if a.phase == "ia" and "phrase" not in row:
                ph = pl.phrases(e, wc, codes, 4, 1)
                row["phrase"] = ph[0] if ph else "no-4-run"
                if ph:
                    x = pl.fts(net, ph[0])
                    if x is None: row["ia_result"] = "?"
                    else:
                        tot, ids = x; rel = [i for i, t in ids if pl.REL.search(t) or pl.REL.search(i)]
                        row["ia_result"] = str(tot); row["ia_print"] = ",".join(rel[:3]) if (rel and tot <= 20) else ""
                done += 1
            if a.phase == "hdl" and "hunt_terms" not in row:
                terms = pl.hunt_terms(e, wc, codes, 2); row["hunt_terms"] = " ".join(terms); hh = []; best = "none"
                if terms:
                    x = pl.hunt(net, terms)
                    if x is None: hh.append("query=?")
                    else:
                        for rec in x[1]:
                            if int(rec["pointer"]) == e["pointer"]: continue
                            c, full = pl.hit_scores(e, rec.get("transc") or "", codes, freq)
                            lab = "y" if c >= 7 else "u" if c >= 3 else "n"
                            if full >= 0.5: lab = "copy" if lab != "y" else "y+copy"
                            if lab != "n":
                                hh.append(f"{rec['pointer']}@{rec['parentobject']}:{lab}:cov{c}:full{full:.2f}")
                                order = ["none", "n", "u", "copy", "y", "y+copy"]
                                if order.index(lab) > order.index(best): best = lab
                row["hunt_hits"] = " ".join(hh) if hh else "none"; row["hunt_best"] = best
                done += 1
        except pl.BudgetStop as b:
            print("budget stop", b, file=sys.stderr); break
        if done and done % 15 == 0: save(out); net.save_counts(); print(done, dict(net.n), file=sys.stderr)
    save(out); net.save_counts()
    print("done", done, "requests this run", dict(net.n), file=sys.stderr)

if __name__ == "__main__":
    main()
