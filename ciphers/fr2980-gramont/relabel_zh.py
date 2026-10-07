#!/usr/bin/env python3
"""DA1-GRA (7 Oct 2026): relabel the fr.3040 no.6 barred z as its own reader code `zh` in n8gra2/n8gra3 recon.tsv.

R12D-GRAZB2 (6 Oct 2026) found the f.30 `zb` and the fr.3040 barred z are different shapes, so the fr.3040 reader
label `zb` (and the barred tokens the passes wrote as `z`) collide with f.30's codes. Rule, fixed before any re-score:
  - a `zb` token -> `zh` (the readers' own barred label; R12D-GRAZB2 put 10 of 11 in the barred class C1, 1 OFF);
  - a `z` token -> `zh` if R12D-GRAZB2's per-sign-box sort put it in C1 (barred), or, where that sort has no class
    for it (OFF / not sampled), N9-GRAZ's sort put it in K2 (barred);
  - every other `z` stays `z`: K1 (plain), OFF in both sorts, or the two sorts disagree (K2 in N9-GRAZ but C2/C3 in
    R12D-GRAZB2) -- listed by --list, not settled here.
Input: <dir>/recon_prezh.tsv (the reconciled files as committed before this job); output <dir>/recon.tsv.
--check exits 1 if a committed recon.tsv differs from what this rule writes. key.tsv is not read or changed:
`zh` is not in key.tsv, so the registered scorers treat it as an unkeyed wildcard.
"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
DIRS = ["n8gra2", "n8gra3"]


def rd(p):
    return list(csv.DictReader(open(HERE / p), delimiter="\t"))


def classes():
    zo = {r["id"]: r for r in rd("n9graz/z_occ.tsv")}
    zs = {r["id"]: r["class"] for r in rd("n9graz/sort_sonnet.tsv")}
    oc = {r["id"]: r for r in rd("r12zb/occ.tsv")}
    s2 = {r["id"]: r["class"] for r in rd("r12zb2/sort_sonnet.tsv")}
    n9 = {r["line_pos"]: zs.get(i) for i, r in zo.items() if r["src"] == "fr3040"}
    r12 = {r["line_pos"]: s2.get(i) for i, r in oc.items() if r["src"] == "fr3040"}
    return n9, r12


def relabel(d, n9, r12, log):
    src = (HERE / d / "recon_prezh.tsv").read_text().splitlines()
    out = [src[0]]
    for ln in src[1:]:
        row, codes = ln.split("\t")
        t = codes.split()
        for k, x in enumerate(t):
            lp = f"{row} {k}"
            a, b = n9.get(lp), r12.get(lp)
            if x == "zb":
                t[k] = "zh"; why = "reader zb"
            elif x == "z" and (b == "C1" or (b in (None, "OFF") and a == "K2")):
                t[k] = "zh"; why = "sort barred"
            elif x == "z":
                why = "kept z"
            else:
                continue
            log.append((d, lp, x, t[k], a or "-", b or "-", why))
        out.append(row + "\t" + " ".join(t))
    return "\n".join(out) + "\n"


def main():
    n9, r12 = classes()
    log, stale = [], False
    for d in DIRS:
        new = relabel(d, n9, r12, log)
        p = HERE / d / "recon.tsv"
        if "--check" in sys.argv:
            if p.read_text() != new:
                print(f"STALE {p}"); stale = True
        else:
            p.write_text(new)
    if "--list" in sys.argv or "--check" not in sys.argv:
        print("dir\tline_pos\twas\tnow\tn9graz\tr12zb2\twhy")
        for r in log:
            print("\t".join(r))
    if "--check" in sys.argv:
        print("recon.tsv up to date" if not stale else "recon.tsv STALE")
        sys.exit(1 if stale else 0)


if __name__ == "__main__":
    main()
