#!/usr/bin/env python3
"""H29: append (or replace) the 'REAL WE028 usage erving-monroe_1806-02-05' row in design/stats_real.tsv from
design/real_extra.tsv, using design_stats.stats() so the columns are the same as the target's and the THE=972 rows'.
design_stats.py's own main now reads real_extra.tsv too, so a full re-run reproduces the row."""
import os, sys, random
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(HERE, "..", "design")
sys.path.insert(0, D)
import design_stats as ds
name, toks = open(os.path.join(D, "real_extra.tsv")).read().splitlines()[1].split("\t")
st = ds.stats([int(x) for x in toks.split()], random.Random(7), 1600)
lines = open(os.path.join(D, "stats_real.tsv")).read().splitlines()
hdr = lines[0].split("\t")
row = [name] + [ds.fmt(st.get(k, "")) for k in hdr[1:]]
missing = [k for k in hdr[1:] if k not in st]
lines = [l for l in lines if not l.startswith(name)]
lines.append("\t".join(row))
open(os.path.join(D, "stats_real.tsv"), "w").write("\n".join(lines) + "\n")
print("row written:", name, "N", st["N"], "D", st["D"], "units_top1", ds.fmt(st["units_top1"]), "columns missing from stats():", missing)
