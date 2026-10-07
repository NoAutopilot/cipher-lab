#!/usr/bin/env python3
"""BKLOG-0507 (7 Oct 2026): merge the four per-page reconciliation outputs (out_{r36,v36top,v36mid,r37}.tsv) of the kept
f.36-37 rows' 193 splits, per PREREG.md (RUN6-BIR3637 + BKLOG-0507 addendum).

  python3 merge_bypage.py          # writes summary.tsv and, if any page passes item 4, ../passD_v3.tsv (v2 + that page's H/M)
  python3 merge_bypage.py --check  # exit 1 if the committed outputs are stale (rule 7)

Item 4 per page: more than half of a page's rows '?' or conf L -> non-discriminating, nothing from it is spliced.
Only H/M choices that name a sign id (not '?', not NONE) are applied. E before = (40 + 193) / 700; E after = (40 + 193 - applied) / 700.
"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
V2 = HERE.parents[1] / "f36r" / "passD_v2.tsv"; V3 = HERE.parent / "passD_v3.tsv"
PAGES = ["r36", "v36top", "v36mid", "r37"]

def build():
    v2 = list(csv.DictReader(open(V2), delimiter="\t"))
    summ = ["page\trows\tH\tM\tL\tq\tpasses_item4\tapplied"]; apply = {}
    for p in PAGES:
        rows = list(csv.DictReader(open(HERE / f"out_{p}.tsv"), delimiter="\t"))
        n = len(rows); c = {k: sum(r["conf"] == k for r in rows) for k in "HML"}
        q = sum(r["choice"] == "?" for r in rows)
        weak = sum(r["choice"] == "?" or r["conf"] == "L" for r in rows)
        ok = weak * 2 <= n; a = 0
        if ok:
            for r in rows:
                if r["conf"] in "HM" and r["choice"] not in ("?", "NONE", ""):
                    apply[(r["line"], r["pos"])] = r["choice"]; a += 1
        summ.append(f"{p}\t{n}\t{c['H']}\t{c['M']}\t{c['L']}\t{q}\t{'yes' if ok else 'no'}\t{a}")
    na = len(apply)
    summ.append(f"total\t193\t\t\t\t\t\t{na}")
    summ.append(f"E_before\t{(40 + 193) / 700:.3f}"); summ.append(f"E_after\t{(40 + 193 - na) / 700:.3f}")
    out = {"summary.tsv": "\n".join(summ) + "\n"}
    if na:
        lines = ["passage\tpos\tsign_id"]
        for r in v2:
            s = apply.get((r["passage"], r["pos"]), r["sign_id"])
            lines.append(f"{r['passage']}\t{r['pos']}\t{s}")
        out[str(V3)] = "\n".join(lines) + "\n"
    return out

if __name__ == "__main__":
    out = build(); stale = False
    for name, text in out.items():
        p = Path(name) if name.startswith("/") else HERE / name
        if "--check" in sys.argv:
            if not p.exists() or p.read_text() != text: print("STALE", p); stale = True
        else: p.write_text(text)
    if "--check" in sys.argv: print("OK, not stale" if not stale else "stale"); sys.exit(1 if stale else 0)
    print(out["summary.tsv"])
