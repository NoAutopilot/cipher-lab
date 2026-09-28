#!/usr/bin/env python3
"""F61-QO2 (campaign step H51, 28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): scripts/f61joint.py with the loop family
split by H26's blind groups, on top of H27's bracket split.

Pre-registered. Relabels, before the fit: on both leaves every sign the H26 call put in group G2 (two loops side by side at
the stem head) -> SBS, and every pass-A DBL on f.61 -> SBS (the three DBL signs the call reconciled were all G2; L03/14,
on the one sheet whose count did not reconcile, follows its class); G1 (trefoil) and G3 (stacked figure-8) stay PHI. The
(line, pos) -> group pairing is scripts/f61qo.py's own (per sheet in reading order, unreconciled sheets skipped). Then
H27's relabel (EBR_A/EBR_B/ISH). Same folds, permutations (seed 1) and gate as H20/H27; gated cells: PHI, C43, 4TRI, INF,
VBAR_A, VBAR_B, SBS, EBR_A, EBR_B, ZHOOK. Gate: both leaf folds above every permutation AND the ten cells identical in
every fold (absence counts as unstable, as before).

  python3 scripts/f61qo2.py [--check]   -> scripts/f61joint_h51_result.txt, f61joint_h51_map.tsv
"""
import csv, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import f61joint, f61joint2, f61qo
def groups():
    """(line, pos) -> group from read_call_QO.tsv, paired as f61qo.score pairs them."""
    exp = f61qo.expected(); by_sheet = defaultdict(list)
    for e in exp: by_sheet[e[0]].append(e)
    got = defaultdict(list)
    for r in csv.DictReader((l for l in open(f"{HERE}/read_call_QO.tsv") if not l.startswith("#")), delimiter="\t"): got[r["sheet"].replace(".jpg", "")].append(r)
    g = {}
    for sheet in f61qo.SHEETS:
        rows = sorted(got.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"]))); e = by_sheet.get(sheet, [])
        if len(rows) != len(e): continue
        line = ("F108_" if sheet.startswith("f108") else "") + sheet.split("_")[1]
        for r, ex in zip(rows, e): g[(line, ex[1])] = r["group"]
    return g
G = groups()
def relabel(lines):
    for line, seq in lines.items():
        for j, c in enumerate(seq):
            if c in ("PHI", "DBL"):
                grp = G.get((line, j + 1))
                if grp == "G2" or (c == "DBL" and not line.startswith("F108")): seq[j] = "SBS"
                elif grp in ("G1", "G3"): seq[j] = "PHI"
    f61joint2.relabel(lines)
if __name__ == "__main__":
    f61joint.main(relabel=relabel, tag="_h51", nine=["PHI", "C43", "4TRI", "INF", "VBAR_A", "VBAR_B", "SBS", "EBR_A", "EBR_B", "ZHOOK"])
