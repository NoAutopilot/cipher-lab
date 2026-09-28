#!/usr/bin/env python3
"""F61-SPLITS-TABLE (campaign step H81, 28 Sept 2026, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only: one table of the
blind tile-sort tests H65-H80 (scripts/f61sbs.py) for the family worker (H52's key rebuild) and the verifier (H66).
Numbers are parsed from the committed result files (so a stale result makes this table stale too); the descriptive
columns (glyph per letter group, the f.61 atlas class, the table cell) are the runner's summary of each step's NOTES.md
section, written here once. Not a reading.
  python3 scripts/f61splits.py [--check]   -> scripts/f61_glyph_splits.tsv
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [  # step, result file, family reader class, letter sets, leaves, glyph per set (summary), f.61 atlas equivalent, table cell(s), kind
    ("H65", "f61sbs_result.txt", "PHI", "o | e", "f.101r f.188r", "o: two loops side by side on a stem | e: trefoil / phi", "SBS | PHI", "b/o | e/r", "split"),
    ("H67", "f61sbs_b_result.txt", "PHI", "b | e (o anchor)", "f.101r f.188r", "b: with o, side by side on a stem | e: trefoil / head loop", "SBS | PHI", "b/o | e/r", "split"),
    ("H69", "f61pair_h69_result.txt", "4TRI", "a,n | c,p", "f.101r f.188r", "a/n: 4 with hook or stroke beside (hand-specific) | c/p: 4 over a closed triangle on the stem", "C43/4STEM | 4TRI", "a/n | c/p", "split"),
    ("H70", "f61pair_h70_result.txt", "VBAR_A", "s | t", "f.101r", "s: triangle with a second stroke at the point | t: triangle with top bar only", "VBAR_B | VBAR_A", "f/s | g/t", "split (thin)"),
    ("H71", "f61pair_h71_result.txt", "PHI", "e | r", "f.101r f.188r", "no letter split (reader grouped by hand / third loop)", "PHI", "e/r (table: two drawn symbols; Tomokiyo prose: one)", "within-cell"),
    ("H73", "f61pair_h73_result.txt", "C43", "a | n", "f.101r f.188r", "no letter split under the 43 glyph", "C43", "a/n (table: two drawn symbols)", "within-cell"),
    ("H75", "f61pair_h75_result.txt", "HASH4", "d | q", "f.101r f.188r", "no letter split", "4PI / HASH4", "d/q (one shared symbol)", "control"),
    ("H77", "f61pair_h77_result.txt", "LOOPS", "o | u", "f.101r", "o: stemmed side-by-side loops (SBS) | u: barred stemless pair (INF)", "SBS | INF", "b/o | h/u", "split"),
    ("H79", "f61pair_h79_result.txt", "EBR_A", "l,y | f,s", "f.101r", "leans f/s -> diagonal/triangle form, l/y -> forms without a diagonal; not significant", "EBR_B | EBR_A/VBAR_B", "l/y | f/s", "split (near miss)"),
    ("H89P", "f61pair_h89_result.txt", "PHI", "o | e", "f.274", "o: flat row of loops, stem hanging from below (SBS) | e: trefoil, stem through the centre", "SBS | PHI", "b/o | e/r", "split (third hand)"),
    ("H89V", "f61pair_h89_result.txt", "VBAR_A", "s | t", "f.274", "s: triangle with a long second stroke at the point | t: top bar only", "VBAR_B | VBAR_A", "f/s | g/t", "split (second hand)"),
    ("H98", "f61pair_h98_result.txt", "HASH4", "i | d,q", "f.101r f.188r", "i: bare hash / H-like cluster, no 4 | d/q: a 4 joined above the hash", "H24 | HASH4 (4PI on f.61)", "i/x | d/q", "split"),
    ("H80", "f61pair_h80_result.txt", "VBAR_A", "g | t", "f.101r f.188r", "no letter split", "VBAR_A", "g/t (one shared symbol)", "control"),
]
rows = ["step\tfamily_class\tletter_sets\tleaves\tscored\tobserved\tp95\tP\tgate\tglyph_per_set\tf61_class\ttable_cell\tkind"]
for st, f, cls, sets, lv, gl, f61, cell, kind in STEPS:
    t = open(f"{HERE}/{f}").read()
    m = re.search(r"scored (\d+) .*?observed (\d+)/\d+; (?:permutation |exact )?P(?:\(>=obs\))? = ([\d.]+).*?p95 (\d+)/", t)
    g = re.search(r"GATE[^:]*: (\w+)", t)
    if st.startswith("H89"):
        blk = t.split(f"family {st[-1]} ")[1]; m = re.search(r"scored (\d+) .*?observed (\d+)/\d+; exact P = ([\d.]+).*?p95 (\d+)/", blk, re.S); g = re.search(r"GATE H89" + st[-1] + r": (\w+)", t)
    if st == "H67":
        m2 = re.search(r"Fisher one-sided b vs e P = ([\d.e-]+)", t); sc = re.search(r"(\d+) tiles", t)
        rows.append("\t".join([st, cls, sets, lv, "41", "b 11/14 vs e 3/13 in the SBS group", "-", m2.group(1), g.group(1), gl, f61, cell, kind])); continue
    rows.append("\t".join([st, cls, sets, lv, m.group(1), m.group(2), m.group(4), m.group(3), g.group(1), gl, f61, cell, kind]))
txt = "\n".join(rows) + "\n"; res = f"{HERE}/f61_glyph_splits.tsv"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")
