#!/usr/bin/env python3
"""MS18-PRE stage 3b (8 Oct 2026): power of the print-likely cover (>= 7) on cipher-like entries. The 12 known-answer entries of ms18_known.py are CLEAR in the
ledger; the rows the reader will get are keyed, so only their plain tokens can reach the cover. Each known entry has a fraction p of its tokens replaced by a
non-word placeholder (a code word breaks the plain run), 5 seeds per p; recall = share still at cover >= 7. A recall that falls with p is the filter's honest
power at the plain-token share of a keyed entry (the median plain share of the ledger's keyed rows is printed beside it). Usage: ms18_power.py --scratch DIR"""
import argparse, os, random, statistics, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); PARENT = os.path.dirname(HERE)
sys.path.insert(0, PARENT); sys.path.insert(0, os.path.join(PARENT, "fortmonroe"))
os.environ["FM_LEDGER"] = "ms18"
import entries_mssEC19 as m, prefilter_ls4 as pl, fm_entries as fe, fm_prefilter as fp
def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--scratch", required=True); a = ap.parse_args()
    codes, ents = fe.build()
    known = {(int(l.split("\t")[0]), int(l.split("\t")[1])) for l in open(os.path.join(HERE, "known-ms18.tsv")) if not l.startswith("#") and not l.startswith("pointer")}
    kn = [e for e in ents if (e["pointer"], e["entry_on_page"]) in known]
    pl.NEWVOLS = {k: v for k, v in fp.VOLS.items() if os.path.exists(os.path.join(a.scratch, "or", k + ".txt"))}
    pl.CACHE = tempfile.mkdtemp(prefix="ms18power_")
    keyed = [1 - e["codefrac"] for e in ents if e["codefrac"] >= 0.12 and e["words"] >= 40]
    print(f"known entries {len(kn)}; median plain share of keyed ledger rows (>= 40 words) {statistics.median(keyed):.2f}")
    for p in (0.0, 0.3, 0.5, 0.7):
        hit = tot = 0
        for seed in range(5 if p else 1):
            rnd = random.Random(1000 + seed); es = []
            for e in kn:
                c = dict(e); c["tokens"] = [("zq" if rnd.random() < p else t) for t in e["tokens"]]; es.append(c)
            freq, cov, wc = pl.scan_new(es, codes, a.scratch, os.path.join(pl.CACHE, "s_%s_%d.json" % (p, seed)))
            hit += sum(cov[i][0] >= m.MINCOV for i in range(len(es))); tot += len(es)
        print(f"p(replaced)={p}: recall {hit}/{tot} = {hit/tot:.2f}")
if __name__ == "__main__": main()
