#!/usr/bin/env python3
"""F61-SUBSYM (campaign step H23, 27 Sept 2026): do the a/n and e/r cells split into the table's two symbols each?

Pre-registered. The Mayenne table draws two symbols for a/n (rows a, n) and two for e/r (rows e, r); the map reads each
cell through one class. Material: the two-leaf alignment of scripts/f61joint.py (tools/interlinear_align.py, wildcard
dashes, null-cost -1; f.61 spans + f.108 T1/T2), whose per-class letter counts are read here. Test 1: among the classes
assigned a/n (C43, 4STEM, C6, LOOPBAR, 4PI when so assigned), the a versus n counts per class. Test 2: e versus r under
PHI, split on f.61 by the reader's own note in read_call_A.tsv ('triple loop' versus other 'phi' notes; the f.108
passes give no such note, so f.61 only), and under HASH4/INF/any class assigned e/r. Gate (H23): some pair of classes
splits a from n, or e from r, with each side at 3+ counts and at most 1 crossing.

  python3 scripts/f61subsym.py [--check]
"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from f61crib import load_read, load_spans, fit
from f61crib3 import OPTS
from f61crib4 import split_lines
from f61joint import f108_lines
def main():
    lines = split_lines(load_read()); lines.update(f108_lines())
    spans = load_spans() + [(s, "F108_" + ("L02" if s == "T1" else "L03"), m) for s, _, m, _ in (l.rstrip("\n").split("\t") for l in open(f"{HERE}/tomokiyo_spans_3983.tsv") if l[0] == "T")]
    # PHI subtypes on f.61 from the reader's note; f.108 PHI stays one class
    marks = {(r["line"], int(r["pos"])): r["marks"] for r in csv.DictReader(open(f"{HERE}/read_call_A.tsv"), delimiter="\t")}
    sub = {}
    for (line, pos), mk in marks.items():
        if lines[line][pos - 1] == "PHI":
            lines[line][pos - 1] = "PHI_triple" if "triple" in mk else "PHI_plain"
    counts = fit(spans, lines, "subsym", OPTS, keep_dashes=True)
    out = []; ok = False
    def show(label, classes, x, y):
        nonlocal ok
        rows = []
        for c in classes:
            cnt = counts.get(c, Counter()); rows.append((c, cnt.get(x, 0), cnt.get(y, 0), sum(cnt.values())))
            out.append(f"  {c}\t{x}:{cnt.get(x,0)}\t{y}:{cnt.get(y,0)}\tall letters {sum(cnt.values())}: " + " ".join(f"{k}:{v}" for k, v in cnt.most_common()))
        for i in range(len(rows)):
            for j in range(len(rows)):
                if i != j:
                    a, b = rows[i], rows[j]
                    if a[1] >= 3 and b[2] >= 3 and a[2] <= 1 and b[1] <= 1:
                        out.append(f"  SPLIT: {a[0]} = {x} ({a[1]} vs {a[2]}), {b[0]} = {y} ({b[2]} vs {b[1]})"); ok = True
    out.append("test 1: a versus n under the classes the joint fit assigns a/n")
    show("a/n", ["C43", "4STEM", "C6", "LOOPBAR", "4PI"], "a", "n")
    out.append("test 2: e versus r under the phi subtypes (f.61 reader notes; f.108 PHI unsplit) and other e/r-assigned classes")
    show("e/r", ["PHI_triple", "PHI_plain", "PHI", "HASH4"], "e", "r")
    out.append(f"GATE H23 (a pair of classes splits a/n or e/r, 3+ each side, at most 1 crossing): {'PASS' if ok else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61subsym_result.txt"
    if "--check" in sys.argv:
        okc = os.path.exists(res) and open(res).read() == txt
        print("fresh" if okc else "STALE"); sys.exit(0 if okc else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()
