#!/usr/bin/env python3
"""FM-PRE stage 3 (8 Oct 2026): rule-3 controls for fm_prefilter.py.
 (1) KNOWN-ANSWER: seven ledger entries found in print independently of the filter -- located from the printed side (OR I/36-2, I/36-3 signature
     lines 'G. D. SHELDON' with a 'Fort Monroe' dateline, matched to the ledger by date and by reading both texts) -- must be flagged print-likely.
 (2) NULL: every entry's tokens shuffled (seed fixed); the share of shuffled entries reaching the print-likely cover is the false-flag rate of
     the cover statistic at these entry lengths.
  fm_control.py --scratch DIR"""
import argparse, collections, csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT); sys.path.insert(0, HERE)
import entries_mssEC19 as m, prefilter_ls4 as pl, fm_entries as fe, fm_prefilter as fp

# pointer, entry_on_page, printed place (checked by eye against the ledger text, 8 Oct 2026)
KNOWN = [(5652, 0, "OR I/36-2 (6 May 1864, Sheldon to Eckert: Butler thinks it unsafe to run the line south side of the river from Jamestown)"),
         (5706, 1, "OR I/36-3 (28 May 1864, Sheldon to Eckert: Gen. Carr, a telegraph from Gloucester to West Point)"),
         (5708, 2, "OR I/36-3 (28 May 1864, Sheldon to Butler: two routes in view, Williamsburg to White House or Yorktown)"),
         (5709, 2, "OR I/36-3 (28 May 1864, Sheldon to Butler: Halleck's opinion, north side of York River best route)"),
         (5716, 1, "OR I/36-3 (29 May 1864, Sheldon to Eckert: Bickford and party arrived, six teams, left at sundown)"),
         (5722, 1, "OR I/36-3 (31 May 1864, Sheldon to Eckert: will communicate with Bickford; Palmer's party met rebel pickets)"),
         (5739, 1, "OR I/36-3 (11 June 1864, Sheldon to Butler: material ready for the line Jamestown Island, Swan's Point, Cabin Point, Garysville)")]

if fe.S == "ms18":    # MS18-PRE: the known answers are the clear ledger entries with an exact 8-word run in the print volumes (ms18_known.py), found without the cover statistic
    KNOWN = [(int(r[0]), int(r[1]), "%s, %s exact 8-word run(s) in %s" % (r[2], r[4], r[5])) for r in
             (l.rstrip("\n").split("\t") for l in open(os.path.join(fe.OUTDIR, "known-ms18.tsv")) if not l.startswith("#") and not l.startswith("pointer"))]

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--scratch", required=True); ap.add_argument("--seed", type=int, default=20261008)
    a = ap.parse_args(argv)
    rows = {(r["pointer"], r["entry"]): r for r in csv.DictReader((l for l in open(os.path.join(fe.OUTDIR, "prefilter-%s.tsv" % fe.S)) if not l.startswith("#")), delimiter="\t")}
    print("KNOWN-ANSWER")
    hit = 0
    for p, n, where in KNOWN:
        r = rows[(str(p), str(n))]; ok = "print-likely" in r["verdict"]; hit += ok
        print(f"  {p}/{n} cover {r['or_cov']} ({r['or_vol']}) verdict {r['verdict']} -- {where}")
    print(f"  recall {hit}/{len(KNOWN)}")
    pl.NEWVOLS = {k: v for k, v in fp.VOLS.items() if os.path.exists(os.path.join(a.scratch, "or", k + ".txt"))}
    pl.CACHE = os.path.join(fp.ROOT, "sources", "ia-fulltext", "print-check", fe.CFG["cache"])
    codes, fm = fe.build(); rnd = random.Random(a.seed)
    for e in fm:
        t = list(e["tokens"]); rnd.shuffle(t); e["tokens"] = t
    freq, cov, wc = pl.scan_new(fm, codes, a.scratch, os.path.join(pl.CACHE, "scan_%s_shuffled_seed%d.json" % (fe.S, a.seed)))
    real = [int(r["or_cov"]) for r in rows.values()]
    sh = [cov[i][0] for i in range(len(fm))]
    for lab, vals in (("real", real), ("shuffled", sh)):
        print(f"NULL {lab}: n={len(vals)} cover>=7 {sum(v >= 7 for v in vals)} ({sum(v >= 7 for v in vals)/len(vals):.3f}); cover 5-6 {sum(5 <= v <= 6 for v in vals)}; cover>=10 {sum(v >= 10 for v in vals)}; max {max(vals)}")
    long_ = [i for i, e in enumerate(fm) if e["words"] >= 60]
    print(f"NULL shuffled, entries >= 60 words (n={len(long_)}): cover>=7 {sum(sh[i] >= 7 for i in long_)}; real same entries cover>=7 {sum(real[i] >= 7 for i in long_)}")

if __name__ == "__main__":
    main()
